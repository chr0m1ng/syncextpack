#!/bin/bash

# Activate virtual environment (if it exists)
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Set default values
apimSerial="YYYYYYYY"
magicNum=0

# Check command line arguments
if [ $# -eq 0 ]; then
    echo "Build mode: Single"
else
    echo "Build mode: Batch"
    apimSerial=$1
    magicNum=$2
fi

echo "APIM Serial: $apimSerial"
echo "Magic Number: $magicNum"

# =================== CORE ======================
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum Navitel Player_EN Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink_EN_NEW Player_EN Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink_EN_NEW Player_EN DDApp Reboot
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum Player_EN DDApp Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum Navitel MirrorLink_EN_NEW Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink_NEW Player Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum DDApp
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum Explorer Reboot
python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum AutoKit MirrorLink_EN_NEW Explorer Reboot

# ===============================================

# =================== UTILS ===================

# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum RemovePack BaseFlash
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum FordNavi
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum PatchEject
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum ForceRestart

# =============================================

# =================== MIRRORLINK ===================

# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink_EN Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink_NEW Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink_EN_NEW Reboot
# python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum MirrorLink_EN_NEW Reboot PatchEject

# ==================================================

# =================== TRANSLATIONS ===================

# ====================================================

# =================== UPDATES ===================

# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdateNavitel
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum RevertNavitel
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdateCityGuideLic
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdateCityGuide
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdateMirrorLink
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdateMirrorLinkEN
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdatePlayer
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdatePlayerEN
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdatePrimo
# python3 build_pack.py $apimSerial SyncExtPack/install.bin $magicNum UpdateNextgen

# ===============================================

# =================== INSTALLER ===================

# Build UpdateService first, then build installer
echo "Building update service pack..."
python3 build_pack.py $apimSerial SyncExtPack/update.bin $magicNum UpdateService


# Check if the build was successful before proceeding
if [ $? -eq 0 ]; then
    echo "Building installer..."
    python3 build_installer.py $apimSerial
    
    # Check if installer build was successful before archiving
    if [ $? -eq 0 ]; then
        echo "Building archive..."
        python3 build_archive.py $apimSerial ./SyncExtPack/
    else
        echo "Installer build failed!"
    fi
else
    echo "Update service build failed!"
fi

# =================================================

# Deactivate virtual environment if it was activated
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
fi

echo "Press any key to continue..."
read -n 1 -s
