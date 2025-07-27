from .base_units import BaseAppUnit, AppMeta

class BaseTranslationUnit(BaseAppUnit):

	NAME = 'BaseTranslationUnit'
	FILES = []
	DEPENDS = []
	APP_CONFIG = None
	APP_META = AppMeta(None,
					   None,
					   None,
					   None,
					   True)

	def __init__(self):
		BaseAppUnit.__init__(self)


class TranslationHungarian(BaseTranslationUnit):

	NAME = 'TranslationHungarian'
	FILES = [
		('/Custom_Translations/Hungarian/DataManager/', '/DataManager/'),
		('/Custom_Translations/Hungarian/Nuance/', '/Nuance/'),
	]


class TranslationHungarianTextEN(TranslationHungarian):

	NAME = 'TranslationHungarianTextEN'
	FILES = [
		('/Custom_Translations/Hungarian_Text_EN/DataManager/', '/DataManager/'),
	]


class TranslationHungarianTextDE(TranslationHungarian):

	NAME = 'TranslationHungarianTextDE'
	FILES = [
		('/Custom_Translations/Hungarian_Text_DE/DataManager/', '/DataManager/'),
	]


class TranslationCzech(BaseTranslationUnit):

	NAME = 'TranslationCzech'
	FILES = [
		('/Custom_Translations/Czech/DataManager/', '/DataManager/'),
		('/Custom_Translations/Czech/Nuance/', '/Nuance/'),
	]

class TranslationCzech2(BaseTranslationUnit):

	NAME = 'TranslationCzech2'
	FILES = [
		('/Custom_Translations/Czech_2/DataManager/', '/DataManager/'),
		('/Custom_Translations/Czech_2/Nuance/', '/Nuance/'),
	]

class TranslationCzechTest(BaseTranslationUnit):

	NAME = 'TranslationCzechTest'
	FILES = [
		('/Custom_Translations/Czech_Test/DataManager/', '/DataManager/'),
		('/Custom_Translations/Czech_Test/Nuance/', '/Nuance/'),
	]


class TranslationDefault(BaseTranslationUnit):

	NAME = 'TranslationDefault'
	FILES = [
		('/Custom_Translations/Default/DataManager/', '/DataManager/'),
		('/Custom_Translations/Default/Nuance/', '/Nuance/'),
	]