from .base_units import (
    AppConfig,
    AppMeta,
    BaseAppUnit,
    BaseFlashUnit,
    BaseGPSUnit,
    ProgramUnit,
)
from .service_units import RebootUnit


class NavitelUnit(ProgramUnit):
    NAME = 'NavitelUnit'
    FILES = [
        '/windows/NavitelPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/Navitel.png',
        '/SyncExtendedPack/Apps/Nav/Navitel/',
    ]
    DEPENDS = [
        BaseFlashUnit,
        BaseGPSUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'Navitel',
        'NavitelPlugin',
        'Navitel.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class NavitelOldUnit(ProgramUnit):
    NAME = 'NavitelOldUnit'
    FILES = [
        '/windows/NavitelOldPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/Navitel.png',
        '/SyncExtendedPack/Apps/Nav/NavitelOld/',
    ]
    DEPENDS = [
        BaseFlashUnit,
        BaseGPSUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'Navitel Old',
        'NavitelOldPlugin',
        'Navitel.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)

        
class PrimoUnit(ProgramUnit):
    NAME = 'PrimoUnit'
    FILES = [
        '/windows/PrimoPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/Primo.png',
        '/SyncExtendedPack/Apps/Nav/Primo/',
    ]
    DEPENDS = [
        BaseFlashUnit,
        BaseGPSUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'iGO Primo',
        'PrimoPlugin',
        'Primo.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class SygicUnit(ProgramUnit):
    NAME = 'SygicUnit'
    FILES = [
        '/windows/SygicPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/Sygic.png',
        '/SyncExtendedPack/Apps/Nav/Sygic/',
    ]
    DEPENDS = [
        BaseFlashUnit,
        BaseGPSUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'Sygic',
        'SygicPlugin',
        'Sygic.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class TotalCommanderUnit(ProgramUnit):
    NAME = 'TotalCommanderUnit'
    FILES = [
        '/windows/ExplorerPlugin.dll',
        '/SyncExtendedPack/Apps/Tools/explorer.exe',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/Explorer.png',
    ]
    DEPENDS = [
        BaseFlashUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'Total Commander',
        'ExplorerPlugin',
        'Explorer.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class VideoPlayerUnit(ProgramUnit):
    NAME = 'VideoPlayerUnit'
    FILES = [
        '/windows/VideoPlayer.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/VideoPlayer.png',
        '/SyncExtendedPack/Apps/Media/VideoPlayer/',
    ]
    DEPENDS = [
        BaseFlashUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'Video Player',
        'VideoPlayer',
        'VideoPlayer.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class VideoPlayerENUnit(VideoPlayerUnit):
    NAME = 'VideoPlayerENUnit'
    FILES = [
        '/windows/VideoPlayer.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/VideoPlayer.png',
        ('/SyncExtendedPack/Apps/Media/VideoPlayer_EN/', '/SyncExtendedPack/Apps/Media/VideoPlayer/'),
    ]


class DDAppUnit(ProgramUnit):
    NAME = 'DDAppUnit'
    FILES = [
        '/windows/DDApp.exe',
        '/SyncExtendedPack/Apps/Tools/DDAppInstall.exe',
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/SyncExtendedPack/Apps/Tools/DDAppInstall.exe',
                       None,
                       True)

    def __init__(self):
        ProgramUnit.__init__(self)


class BaseMirrorLinkUnit(ProgramUnit):
    NAME = 'BaseMirrorLinkUnit'
    FILES = []
    DEPENDS = [
        BaseFlashUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'MirrorLink',
        'MirrorLinkPlugin',
        'MirrorLink.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class MirrorLinkNewUnit(BaseMirrorLinkUnit):
    NAME = 'MirrorLinkNewUnit'
    FILES = [
        '/windows/MirrorLinkPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/MirrorLink.png',
        ('/SyncExtendedPack/Apps/Media/EasyConnected_New/', '/SyncExtendedPack/Apps/Media/EasyConnected/'),
    ]


class MirrorLinkENNewUnit(BaseMirrorLinkUnit):
    NAME = 'MirrorLinkENNewUnit'
    FILES = [
        '/windows/MirrorLinkPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/MirrorLink.png',
        ('/SyncExtendedPack/Apps/Media/EasyConnected_EN_New/', '/SyncExtendedPack/Apps/Media/EasyConnected/'),
    ]


class AutoKitUnit(ProgramUnit):
    NAME = 'AutoKitUnit'
    FILES = [
        '/windows/AutoKitPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/AutoKit.png',
        '/SyncExtendedPack/Apps/Media/AutoKit/',
    ]
    DEPENDS = [
        BaseFlashUnit,
        BaseAppUnit,
        RebootUnit
    ]
    APP_CONFIG = AppConfig(
        'AutoKit',
        'AutoKitPlugin',
        'AutoKit.png',
        0
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class FordNaviUnit(BaseAppUnit):
    NAME = 'FordNaviUnit'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/FordNavi/',
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/SyncExtendedPack/Apps/Tools/FordNavi/FordNavi.exe',
                       None,
                       True)

    def __init__(self):
        BaseAppUnit.__init__(self)


class UpdateNavitelUnit(BaseAppUnit):
    NAME = 'UpdateNavitel'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/UpdateNavitel/',
        ('/SyncExtendedPack/Apps/Nav/Navitel/', '/SyncExtendedPack/Apps/Nav/Navitel_new/'),
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/SyncExtendedPack/Apps/Tools/UpdateNavitel/UpdateNavitel.exe',
                       None,
                       True)

    def __init__(self):
        BaseAppUnit.__init__(self)

class RevertNavitelUnit(BaseAppUnit):
    NAME = 'RevertNavitel'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/UpdateNavitel/',
        ('/SyncExtendedPack/Apps/Nav/NavitelOld/', '/SyncExtendedPack/Apps/Nav/Navitel_new/'),
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/SyncExtendedPack/Apps/Tools/UpdateNavitel/UpdateNavitel.exe',
                       None,
                       True)

    def __init__(self):
        BaseAppUnit.__init__(self)


class UpdatePrimoUnit(BaseAppUnit):
    NAME = 'UpdatePrimo'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/UpdatePrimo/',
        ('/SyncExtendedPack/Apps/Nav/Primo/', '/SyncExtendedPack/Apps/Media/Primo_new/'),
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/SyncExtendedPack/Apps/Tools/UpdatePrimo/UpdatePrimo.exe',
                       None,
                       True)

    def __init__(self):
        BaseAppUnit.__init__(self)


class UpdateMirrorLinkUnit(BaseAppUnit):
    NAME = 'UpdateMirrorLink'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/UpdateMirrorLink/',
        ('/SyncExtendedPack/Apps/Media/EasyConnected_New/', '/SyncExtendedPack/Apps/Media/EasyConnected_new/'),
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/SyncExtendedPack/Apps/Tools/UpdateMirrorLink/UpdateMirrorLink.exe',
                       None,
                       True)

    def __init__(self):
        BaseAppUnit.__init__(self)


class UpdateMirrorLinkENUnit(UpdateMirrorLinkUnit):
    NAME = 'UpdateMirrorLinkEN'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/UpdateMirrorLink/',
        ('/SyncExtendedPack/Apps/Media/EasyConnected_EN_New/', '/SyncExtendedPack/Apps/Media/EasyConnected_new/'),
    ]


class UpdatePlayerUnit(BaseAppUnit):
    NAME = 'UpdatePlayer'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/UpdatePlayer/',
        ('/SyncExtendedPack/Apps/Media/VideoPlayer/', '/SyncExtendedPack/Apps/Media/VideoPlayer_new/'),
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/SyncExtendedPack/Apps/Tools/UpdatePlayer/UpdatePlayer.exe',
                       None,
                       True)

    def __init__(self):
        BaseAppUnit.__init__(self)


class UpdatePlayerENUnit(UpdatePlayerUnit):
    NAME = 'UpdatePlayerEN'
    FILES = [
        '/SyncExtendedPack/Apps/Tools/UpdatePlayer/',
        ('/SyncExtendedPack/Apps/Media/VideoPlayer_EN/', '/SyncExtendedPack/Apps/Media/VideoPlayer_new/'),
    ]
