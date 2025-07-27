from .units.app_units import (
    AutoKitUnit,
    BaseAppUnit,
    BaseFlashUnit,
    BaseGPSUnit,
    DDAppUnit,
    FordNaviUnit,
    MirrorLinkENNewUnit,
    MirrorLinkNewUnit,
    NavitelOldUnit,
    NavitelUnit,
    PrimoUnit,
    RevertNavitelUnit,
    SygicUnit,
    TotalCommanderUnit,
    UpdateMirrorLinkENUnit,
    UpdateMirrorLinkUnit,
    UpdateNavitelUnit,
    UpdatePlayerENUnit,
    UpdatePlayerUnit,
    UpdatePrimoUnit,
    VideoPlayerENUnit,
    VideoPlayerUnit,
)
from .units.service_units import (
    ForceRestartUnit,
    PatchEjectUnit,
    RebootUnit,
    RemovePackUnit,
    UpdateServiceUnit,
)
from .units.translation_units import (
    TranslationCzech,
    TranslationCzech2,
    TranslationCzechTest,
    TranslationDefault,
    TranslationHungarian,
    TranslationHungarianTextDE,
    TranslationHungarianTextEN,
)

PROGRAM_UNITS = {
    # Base
	'BaseApp': BaseAppUnit,
	'BaseFlash': BaseFlashUnit,
	'BaseGPS': BaseGPSUnit,

    # Service
	'Reboot': RebootUnit,
    'UpdateService': UpdateServiceUnit,
    'PatchEject': PatchEjectUnit,
    'RemovePack': RemovePackUnit,
	'ForceRestart': ForceRestartUnit,

    # Other
    'Explorer': TotalCommanderUnit,

    # Navigation
	'Navitel': NavitelUnit,
	'NavitelOld': NavitelOldUnit,
    'FordNavi': FordNaviUnit,
	'Primo': PrimoUnit,
	'Sygic': SygicUnit,

	# Media
	'Player': VideoPlayerUnit,
	'Player_EN': VideoPlayerENUnit,
	'DDApp': DDAppUnit,
	'MirrorLink_NEW': MirrorLinkNewUnit,
	'MirrorLink_EN_NEW': MirrorLinkENNewUnit,
	'AutoKit': AutoKitUnit,

    # Update
	'UpdateNavitel': UpdateNavitelUnit,
	'RevertNavitel': RevertNavitelUnit,
    'UpdateMirrorLink': UpdateMirrorLinkUnit,
    'UpdateMirrorLinkEN': UpdateMirrorLinkENUnit,
	'UpdatePlayer': UpdatePlayerUnit,
	'UpdatePlayerEN': UpdatePlayerENUnit,
	'UpdatePrimo': UpdatePrimoUnit,

	# Translations
	'Translation_Hungarian': TranslationHungarian,
	'Translation_Hungarian_Text_EN': TranslationHungarianTextEN,
	'Translation_Hungarian_Text_DE': TranslationHungarianTextDE,
	'Translation_Czech': TranslationCzech,
	'Translation_Czech_2': TranslationCzech2,
	'Translation_Czech_Test': TranslationCzechTest,
	'Translation_Default': TranslationDefault,
}
SERVICE_UNITS = ['UpdateService', 'Reboot', 'PatchEject', 'BaseApp', 'BaseFlash', 'BaseGPS']
UNIT_CLASS_TO_NAME = {v: k for k, v in PROGRAM_UNITS.items()}