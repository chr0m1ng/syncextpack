import os
import shutil
from collections import namedtuple
from xml.dom.minidom import parseString
import logging

try:
	from lxml import etree
except:
	import xml.etree.ElementTree as etree

SCRIPT_FOLDER = os.path.dirname(__file__)
SOURCE_PATH = os.path.join(SCRIPT_FOLDER, '../../FullPack')
AppConfig = namedtuple('AppConfig', ['app_name', 'plugin_name', 'icon_name', 'index'])
AppConfig.__new__.__defaults__ = (None,) * len(AppConfig._fields)

AppMeta = namedtuple('AppMeta', ['pre_app', 'pre_cmd', 'post_app', 'post_cmd', 'need_reboot'])
AppMeta.__new__.__defaults__ = (None,) * len(AppMeta._fields)

def mkdir_recursive(path):
	sub_path = os.path.dirname(path)
	if not os.path.exists(sub_path):
		mkdir_recursive(sub_path)
	if not os.path.exists(path):
		os.mkdir(path)

class ProgramUnit(object):

	NAME = ''
	FILES = []
	DEPENDS = []
	APP_CONFIG = None
	APP_META = None
	DUMMY = False

	def __init__(self):
		self._dest = None
		self._appConfigs = None

	def process(self, dest, appConfigs):
		logging.info('Processing unit: %s, is dummy: %s' % (self.NAME, self.DUMMY))

		self._dest = dest
		self._appConfigs = appConfigs
		if not self.DUMMY:
			self.__copy()

	def __copy(self):
		for path in self.FILES:
			if isinstance(path, tuple):
				srcPath = path[0]
				dstPath = path[1]
			else:
				srcPath = dstPath = path
			fullSrcPath = SOURCE_PATH + srcPath
			fullDestPath = self._dest + dstPath
			if dstPath.endswith('/'):
				shutil.copytree(fullSrcPath, fullDestPath)
			else:
				dirPath = os.path.dirname(dstPath)
				fullDirPath = self._dest + dirPath
				mkdir_recursive(fullDirPath)
				shutil.copy(fullSrcPath, fullDestPath)


class BaseFlashUnit(ProgramUnit):

	NAME = 'BaseFlashUnit'
	FILES = [
		'/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/',
		'/8inchSkins/Ford/Sync/Apps/Info/SyncApps/SyncApps.swf',
		'/8inchSkins/Ford/Sync/Apps/Menu/Display/WallpaperEditor/AddPhotos/AddPhotos.swf',
		'/8inchSkins/Ford/Sync/Apps/Home/Wallpapers/',
		'/8inchSkins/Lincoln/Sync/Apps/Info/SyncApps/Icons/',
		'/8inchSkins/Lincoln/Sync/Apps/Info/SyncApps/SyncApps.swf',
		'/8inchSkins/Lincoln/Sync/Apps/Menu/Display/WallpaperEditor/AddPhotos/AddPhotos.swf',
		'/8inchSkins/Lincoln/Sync/Apps/Home/Wallpapers/',
	]
	DEPENDS = []
	APP_CONFIG = None
	APP_META = None

	APP_LIST_PATH = '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/SyncApps.xml'
	ICON_FORMAT = 'Apps/Info/SyncApps/Icons/%s'

	def __init__(self):
		ProgramUnit.__init__(self)

	def __prettifyXML(self, elem):
		rough_string = etree.tostring(elem)
		reparsed = parseString(rough_string)
		return reparsed.toprettyxml()

	def __generateAppsList(self):
		root = etree.Element('root')
		apps = etree.Element('apps')
		root.append(apps)
		for config in self._appConfigs:
			child = etree.Element('app', name=config.app_name)
			appPlugin = etree.Element('native')
			appPlugin.text = config.plugin_name
			child.append(appPlugin)
			appIcon = etree.Element('iconPath')
			if config.icon_name != '':
				appIcon.text = self.ICON_FORMAT % config.icon_name
			else:
				appIcon.text = ''
			child.append(appIcon)
			apps.append(child)

		s = self.__prettifyXML(root)
		with open(self._dest + self.APP_LIST_PATH, 'w') as f:
			f.write(s)

	def process(self, dest, appConfigs):
		ProgramUnit.process(self, dest, appConfigs)
		self.__generateAppsList()


class BaseGPSUnit(ProgramUnit):

	NAME = 'BaseGPSUnit'
	FILES = [
		'/windows/GPSDriver.dll',
		'/SyncExtendedPack/Apps/Tools/GPSDeactivator.exe',
		'/SyncExtendedPack/Apps/Tools/GPSInstaller.exe',
	]
	DEPENDS = []
	APP_CONFIG = None
	APP_META = AppMeta('/SyncExtendedPack/Apps/Tools/GPSDeactivator.exe',
					   None,
					   '/SyncExtendedPack/Apps/Tools/GPSInstaller.exe',
					   None,
					   True)

	def __init__(self):
		ProgramUnit.__init__(self)


class BaseAppUnit(ProgramUnit):

	NAME = 'BaseAppUnit'
	FILES = [
		'/SyncExtendedPack/Apps/Tools/SyncAppsRunner.exe',
	]
	DEPENDS = []
	APP_CONFIG = None
	APP_META = None

	def __init__(self):
		ProgramUnit.__init__(self)

