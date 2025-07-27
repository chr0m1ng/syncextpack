import logging

from .units_map import PROGRAM_UNITS
from .packer import Packer
from .utils import getValidThruDate, validateSerial


class Build(object):

	def __init__(self, serialNum):
		self.__serialNum = serialNum.upper()

	def buildPack(self, outName, magicNum, externalUnits):
		if validateSerial(self.__serialNum):
			units = self.__parseUnits(externalUnits)

			if units:
				packer = Packer()
				packer.start(self.__serialNum, units)
				packer.compile(outName, magicNum)
				packer.cleanup()

				validThruDate = getValidThruDate()
				logging.info('This package will be valid till: %s' % validThruDate)
				return validThruDate
		else:
			logging.error('Serial number is not valid!')

	def __parseUnits(self, units):
		result = []
		for unitName in units:
			if self.__isDummyUnit(unitName):
				isDummy = True
				unitName = unitName[2:]
			else:
				isDummy = False

			if unitName not in PROGRAM_UNITS:
				logging.error('Cannot find unit: %s' % unitName)
				return []
			unitClass = PROGRAM_UNITS.get(unitName)
			unitClass.DUMMY = isDummy
			result.append(unitClass)
		return result

	def __isDummyUnit(self, unitName):
		return unitName.startswith('D_')