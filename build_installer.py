import os
import sys
import subprocess
import time
import shutil
import logging

if __name__ == '__main__':
	from builder.utils import validateSerial, mkdir_recursive, PLATFORM_EXEC_FILE_POSTFIX
	from builder.packer import BUILD_FOLDER_FMT
else:
	from .builder.utils import validateSerial, mkdir_recursive, PLATFORM_EXEC_FILE_POSTFIX
	from .builder.packer import BUILD_FOLDER_FMT

SCRIPT_FOLDER = os.path.dirname(__file__)

RESULT_FOLDER = 'SyncExtPack/'
INSTALLER_DLL_PATH = os.path.join(SCRIPT_FOLDER, './FullPack/UpdateInstaller.dll')

INSTALLER_PATH = os.path.join(SCRIPT_FOLDER, './FlashTools/')
SWF_MILL_PATH = INSTALLER_PATH + 'swfmill' + PLATFORM_EXEC_FILE_POSTFIX
XML_BACKUP_PATH = INSTALLER_PATH + 'Installer.xml.bak'
CONFIG_BACKUP_PATH = INSTALLER_PATH + 'SecureSWF.ssp4.bak'

XML_FILENAME = 'Installer.xml'
CONFIG_FILENAME = 'SecureSWF.ssp4'
NORMAL_SWF_FILENAME = 'Installer.swf'
SECURED_SWF_FILENAME = 'secure_Installer.swf'
BUILD_RESULT_FILENAME = 'Installer.jpg'

XML_APIM_FORMAT = 	'<PushData>\n                <items>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="%s"/>\n\
                  <StackInteger value="8"/>\n\
                </items>\n              </PushData>'

class PackCompiler(object):

	def __init__(self):
		self.__serial = None
		self.__garbage = []

	def start(self, serial):
		self.__serial = serial
		self.__buildFolder = BUILD_FOLDER_FMT.format(self.__serial)
		self.__resultFolder = os.path.join(self.__buildFolder, RESULT_FOLDER)
		mkdir_recursive(self.__resultFolder)
		self.__buildInstaller()

	def cleanup(self):
		for filePath in self.__garbage:
			os.remove(filePath)

	def __getEncryptedSerial(self):
		res = []
		i = 0
		for ch in self.__serial:
			factor = 2 if i % 2 == 0 else 3
			res.append(ord(ch) * factor)
			i = i + 1
		return tuple(res[::-1])

	def __prepareInstallerSrc(self):
		with open(XML_BACKUP_PATH, 'r') as f:
			srcFile = f.read()
		encrSerial = XML_APIM_FORMAT % self.__getEncryptedSerial()
		srcFile = srcFile.replace('<<APIM>>', encrSerial)
		resultPath = os.path.join(self.__buildFolder, XML_FILENAME)
		with open(resultPath, 'w') as f:
			f.write(srcFile)
		return resultPath

	def __prepareSecureConfig(self, swfPath):
		with open(CONFIG_BACKUP_PATH, 'r') as f:
			srcFile = f.read()
		swfPath = os.path.abspath(swfPath).replace('\\', '/')
		srcFile = srcFile.replace(NORMAL_SWF_FILENAME, swfPath)
		resultPath = os.path.join(self.__buildFolder, CONFIG_FILENAME)
		with open(resultPath, 'w') as f:
			f.write(srcFile)
		return resultPath

	def __buildInstaller(self):
		xmlPath = self.__prepareInstallerSrc()
		resultPath = os.path.join(self.__buildFolder, NORMAL_SWF_FILENAME)
		subprocess.call([SWF_MILL_PATH, 'xml2swf', xmlPath, resultPath])
		configPath = self.__prepareSecureConfig(resultPath)
		subprocess.call(['java', '-Xmx1024m', '-jar', INSTALLER_PATH + 'secureSWF.jar', 'run', 'secureSWF4', configPath])
		securedPath = os.path.join(self.__buildFolder, SECURED_SWF_FILENAME)
		buildResultPath = os.path.join(self.__resultFolder, BUILD_RESULT_FILENAME)
		shutil.move(securedPath, buildResultPath)
		shutil.copy(INSTALLER_DLL_PATH, self.__resultFolder)
		self.__garbage.extend([resultPath, configPath, xmlPath])


def main():
	logging.basicConfig(filename='builder.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
	logging.info('Building installer...')

	apimSerial = sys.argv[1].upper()
	if validateSerial(apimSerial):
		packCompiler = PackCompiler()
		packCompiler.start(apimSerial)
		packCompiler.cleanup()
	else:
		logging.error('Installer build failed. APIM serial number is invalid!')

	logging.info('Building installer done!')

if __name__ == '__main__':
	main()