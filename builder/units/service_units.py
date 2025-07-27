from .base_units import *

class PatchEjectUnit(BaseAppUnit):
    NAME = 'PatchEjectUnit'
    FILES = [
        ('/SyncExtendedPack/Apps/Tools/SyncAppsRunner_Eject.exe', '/SyncExtendedPack/Apps/Tools/SyncAppsRunner.exe')
    ]

    def __init__(self):
        BaseAppUnit.__init__(self)


class RebootUnit(ProgramUnit):
    NAME = 'RebootUnit'
    FILES = [
        '/windows/RebootPlugin.dll',
        '/8inchSkins/Ford/Sync/Apps/Info/SyncApps/Icons/Reboot.png',
    ]
    DEPENDS = []
    APP_CONFIG = AppConfig(
        'Reboot',
        'RebootPlugin',
        'Reboot.png',
        -1
    )
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class UpdateServiceUnit(ProgramUnit):
    NAME = 'UpdateServiceUnit'
    FILES = [
        '/windows/UpdateService.dll',
    ]
    DEPENDS = [
        BaseFlashUnit
    ]
    APP_CONFIG = None
    APP_META = None

    def __init__(self):
        ProgramUnit.__init__(self)


class RemovePackUnit(BaseAppUnit):
    NAME = 'RemovePackUnit'
    FILES = [
        '/RemoveExtPack/',
    ]
    DEPENDS = []
    APP_CONFIG = None
    APP_META = AppMeta(None,
                       None,
                       '/RemoveExtPack/RemoveExtPack.exe',
                       None,
                       True)

    def __init__(self):
        BaseAppUnit.__init__(self)

class ForceRestartUnit(ProgramUnit):
    NAME = 'ForceRestartUnit'
    APP_META = AppMeta(need_reboot=True)

    def __init__(self):
        ProgramUnit.__init__(self)
