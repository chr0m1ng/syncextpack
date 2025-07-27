import logging
import os
import shutil
import subprocess
import time

from .units.base_units import AppConfig
from .units_map import SERVICE_UNITS, UNIT_CLASS_TO_NAME
from .utils import PLATFORM_EXEC_FILE_POSTFIX, mkdir_recursive

BUILD_FOLDER_FMT = './SyncExtPack/{0}/'
TEMP_FOLDER = 'TempPack/'
META_PATH = 'META_TEMP.txt'
APP_LIST_PATH = 'APP_LIST.txt'
SCRIPT_FOLDER = os.path.dirname(__file__)
CRYPTO_PACK_PATH = os.path.join(SCRIPT_FOLDER, '../crypto_pack' + PLATFORM_EXEC_FILE_POSTFIX)

# Check for Docker wrapper on non-Windows systems
if PLATFORM_EXEC_FILE_POSTFIX == '':  # Unix-like systems (Linux, macOS)
	docker_wrapper = os.path.join(SCRIPT_FOLDER, '../crypto_pack_docker.sh')
	if os.path.exists(docker_wrapper) and os.access(docker_wrapper, os.X_OK):
		CRYPTO_PACK_PATH = docker_wrapper

class Packer(object):

	DEFAULT_META_DICT = {
		'HEADER': 'Welcome to the SyncExtPack installation!',
		'VERSION': 'v1.0 SyncExtPack for: %s',
		'PRE_APP': None,
		'PRE_CMD': None,
		'POST_APP': None,
		'POST_CMD': None,
		'NEED_REBOOT': None,
	}

	def __init__(self):
		self.__serial = None
		self.__units = []
		self.__processedUnits = []
		self.__appConfigs = []
		self.__appIndex = -1
		self.__meta = dict(self.DEFAULT_META_DICT)

	def start(self, serial, units):
		self.__serial = serial
		self.__units = units
		self.__buildFolder = BUILD_FOLDER_FMT.format(self.__serial)
		self.__tempFolder = os.path.join(self.__buildFolder, TEMP_FOLDER)
		self.__metaPath = os.path.join(self.__buildFolder, META_PATH)
		self.__appList = os.path.join(self.__buildFolder, APP_LIST_PATH)

		logging.info('Building pack for: %s' % serial)
		logging.info('Selected units: %s' % [unit.NAME for unit in units])

		mkdir_recursive(self.__tempFolder)

		self.__getDefaultAppConfigs()
		self.__processUnits()
		self.__generateMetaFile()
		self.__generateAppList()

	def compile(self, outName, magicNum):
		outPath = os.path.join(self.__buildFolder, outName)
		mkdir_recursive(os.path.dirname(outPath))
		args = [CRYPTO_PACK_PATH, '-p', self.__tempFolder, outPath, self.__serial, magicNum, self.__metaPath]
		ret = subprocess.call(args)
		logging.info('compile: args = %s, ret = %s' % (args, ret))

	def cleanup(self):
		if os.path.exists(self.__tempFolder):
			shutil.rmtree(self.__tempFolder)
		os.remove(self.__metaPath)

	def __processUnits(self):
		for unit in self.__units:
			self.__processUnitAppConfig(unit)
		for unit in self.__units:
			self.__processUnit(unit)

	def __getNextIndex(self):
		self.__appIndex = self.__appIndex + 1
		return self.__appIndex

	def __processUnitAppConfig(self, unit):
		if unit.APP_CONFIG is not None:
			index = unit.APP_CONFIG.index
			if index == 0:
				index = self.__getNextIndex()
			self.__appConfigs[index] = unit.APP_CONFIG

	def __processUnitMeta(self, unit):
		if unit.DUMMY:
			return
		meta = unit.APP_META
		if meta is not None:
			if meta.pre_app and self.__meta['PRE_APP'] is None:
				self.__meta['PRE_APP'] = meta.pre_app
				self.__meta['PRE_CMD'] = meta.pre_cmd
			if meta.post_app and self.__meta['POST_APP'] is None:
				self.__meta['POST_APP'] = meta.post_app
				self.__meta['POST_CMD'] = meta.post_cmd
			if meta.need_reboot:
				self.__meta['NEED_REBOOT'] = True

	def __processUnit(self, unit):
		if unit.NAME not in self.__processedUnits:
			if not unit.DUMMY:
				for subUnit in unit.DEPENDS:
					self.__processUnit(subUnit)
			unitInstance = unit()
			unitInstance.process(self.__tempFolder, self.__appConfigs)
			self.__processUnitMeta(unit)
			self.__processedUnits.append(unit.NAME)

	def __generateMetaFile(self):
		self.__meta['VERSION'] = self.__meta['VERSION'] % self.__serial
		result = ''
		for k, v in self.__meta.items():
			if v is not None:
				result += '%s=%s\n' % (k, v)
		with open(self.__metaPath, 'wb') as f:
			f.write(result.encode('utf-16-le'))

	def __generateAppList(self):
		unitNames = []
		for unitClass in self.__units:
			unitName = UNIT_CLASS_TO_NAME[unitClass]
			if not (unitClass.DUMMY or unitName in SERVICE_UNITS):
				unitNames.append(unitName)
		if unitNames:
			with open(self.__appList, 'w') as f:
				for unitName in unitNames:
					f.write(unitName + '\n')

	def __getDefaultAppConfigs(self):
		for i in range(5):
			self.__appConfigs.append(AppConfig('', '', '', None))