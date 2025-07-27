@echo off

call .venv\Scripts\activate.bat

set apimSerial=YYYYYYYY
set magicNum=0

if %1. == . (
	echo Build mode: Single
) else (
	echo Build mode: Batch
	set apimSerial=%1
	set magicNum=%2
)


REM =================== CORE ======================
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% Navitel Player_EN Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink_EN_NEW Player_EN Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink_EN_NEW Player_EN DDApp Reboot
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% Player_EN DDApp Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% Navitel MirrorLink_EN_NEW Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink_NEW Player Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% DDApp
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% Explorer Reboot


REM ===============================================


REM =================== UTILS ===================

REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% RemovePack BaseFlash
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% FordNavi
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% PatchEject
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% ForceRestart

REM =============================================


REM =================== MIRRORLINK ===================

REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink_EN Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink_NEW Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink_EN_NEW Reboot
REM python build_pack.py %apimSerial% SyncExtPack/pack_install.bin %magicNum% MirrorLink_EN_NEW Reboot PatchEject

REM ==================================================


REM =================== TRANSLATIONS ===================


REM ====================================================


REM =================== UPDATES ===================

REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdateNavitel
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% RevertNavitel
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdateCityGuideLic
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdateCityGuide
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdateMirrorLink
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdateMirrorLinkEN
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdatePlayer
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdatePlayerEN
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdatePrimo
REM python build_pack.py %apimSerial% SyncExtPack/install.bin %magicNum% UpdateNextgen

REM ===============================================


REM =================== INSTALLER ===================

python build_pack.py %apimSerial% SyncExtPack/update.bin %magicNum% UpdateService & python build_installer.py %apimSerial%
python build_archive.py %apimSerial% ./SyncExtPack/

REM =================================================

deactivate

pause