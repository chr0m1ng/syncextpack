# SyncExtPack Installation Guide

Steps to install custom apps on your Ford SYNC 2.

> **⚠️ Recommendation**: It's recommended to upgrade your Ford SYNC 2 to firmware version 3.10 before installing SyncExtPack. See the [Firmware Installation Guide](FIRMWARE_INSTALLATION.md) for upgrade instructions.

## RequirementscExtPack Installation Guide

Steps to install on your Ford SYNC 2.

## Requirements

- **USB Drive**: 2.0 compatible, maximum 32GB, formatted as FAT32 MBR partition
- **Your APIM Serial Number**: Find it in your car

## Step 1: Get Your APIM Serial Number

Go to: **Menu → Settings → General → About SYNC** and write down your APIM serial number (example: `XV31M13H`)

## Step 2: Choose Build Script

Based on your operating system:

- **Windows**: Use `build_pack.bat`
- **macOS/Linux**: Use `build_pack.sh`

## Step 3: Configure Apps to Install

1. Open the build script file in a text editor
2. Find the main build line (around line 33):

   ```bash
   python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum AutoKit MirrorLink_EN_NEW Explorer Reboot
   ```

3. **Uncomment** the line you want, or **create your own** using this format:

   ```bash
   python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum {APPS_LIST_SEPARATED_BY_SPACE}
   ```

**Available apps**: AutoKit, MirrorLink_EN_NEW, Explorer, Player_EN, Navitel, DDApp, Reboot

## Step 4: Build the Package

Run the build script with your APIM serial:

**Windows**:

```batch
build_pack.bat XV31M13H 0
```

**macOS/Linux**:

```bash
./build_pack.sh XV31M13H 0
```

This will generate a ZIP file like: `SyncExtPack_XV31M13H_AutoKit_MirrorLink_EN_NEW_Explorer.zip`

## Step 5: Prepare USB Drive

1. **Format USB drive** as FAT32 MBR partition
2. **Extract the ZIP file contents** directly to the USB drive root
3. **Verify structure**:

   ```text
   USB Drive (E:)
   └── SyncExtPack/
       ├── update.bin
       ├── UpdateInstaller.dll
       ├── Installer.jpg
       └── pack_install.bin
   ```

## Step 6: Install in Vehicle

1. **Turn car on** (recommended - process takes time and can drain battery) and wait for SYNC 2 to completely boot
2. **Insert USB stick**
3. **Go to wallpaper settings**: Menu → Settings → Display → Wallpaper → Add → usbX
4. **Select Installer.jpg** - press once and be patient
5. **SYNC 2 will reboot** - wait for it to fully restart

## Step 7: Complete Installation

1. **Remove USB stick** and connect to PC
2. **Rename file**: Change `pack_install.bin` to `install.bin`
3. **Reinsert USB** into vehicle
4. **Wait a few seconds** - installation will start automatically
5. **Be patient** - wait for installation to complete
6. **SYNC 2 might reboot** when finished (if not, that's fine - proceed to step 8)

## Step 8: Verify Installation

1. Wait for SYNC 2 to fully boot
2. Remove USB stick
3. Press **i button → Apps**
4. Check that your new apps are there

## Complete

Your Ford SYNC 2 now has the custom apps installed.
