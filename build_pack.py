import sys
import logging

if __name__ == '__main__':
	from builder.build import Build
else:
	from .builder.build import Build

def main():
	logging.basicConfig(filename='builder.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
	logging.info('Building pack started...')

	apimSerial = sys.argv[1].upper()
	outName = sys.argv[2]
	magicNum = sys.argv[3]
	externalUnits = sys.argv[4:]

	build = Build(apimSerial)
	build.buildPack(outName, magicNum, externalUnits)
	
	logging.info('Building pack done!')

if __name__ == '__main__':
	main()