# Ford SYNC 2 Firmware Installation Guide

Steps to upgrade to 3.10 or downgrade to 3.08.

## Requirements

- **USB Drive**: USB 2.0 compatible, max 32GB, formatted as FAT32 MBR partition

## Choose Your Firmware

Download via Mega, [link here](https://mega.nz/folder/Bn5F2SYQ#Hy_hkQNVFQeMD1F_CNWZhg).

- **Upgrade to 3.10**: `Gen2v310build16180updatepackageEULangpack5.zip`
- **Downgrade to 3.08**: `Sync2 Downgrade 3.10 16180 to 3.08 15128EU.zip`

## Step 1: Prepare USB Drive

1. **Format USB drive** as FAT32 MBR partition
2. **Extract firmware ZIP file** directly to the root of USB drive
3. **Verify structure** - files should be in the root, not in a subfolder:

   ```text
   sync_update (USB Drive)
   ├── autoinstall.lst
   ├── SyncMyRide/
   │   ├── update.bin
   │   ├── [other firmware files]
   │   └── ...
   └── [additional firmware files if any]
   ```

## Step 2: Install in Vehicle

1. **Start engine** (recommended - process takes time and may drain battery)
2. **Wait for SYNC 2** to fully initialize
3. **Insert USB drive**
4. **Wait for automatic update** - SYNC 2 should detect and start installation automatically

## Step 3: If Automatic Update Doesn't Start

Try the car's built-in update function:

Go to: **Menu → Settings → General → Install Application**

## Step 4: If Still Not Working

Use wallpaper hack method:

1. **Go to wallpaper settings**: Menu → Settings → Display → Wallpaper → Add → usbX
2. **Select autoinstall.jpg** (if present in firmware files)
3. **Be patient** - installation will start

## Step 5: Wait for Completion

1. **SYNC 2 may reboot multiple times** - this is normal
2. **Be patient** - do not remove USB drive during process
3. **Only remove USB drive** when SYNC 2 displays "Update completed successfully"
4. **System will restart** and show new firmware version

## Step 6: Verify Installation

1. Go to: **Menu → Settings → General → About SYNC**
2. Check firmware version:
   - **3.10**: Should show version 3.10 build 16180
   - **3.08**: Should show version 3.08 build 15128

## Important Notes

- **Never interrupt** the firmware update process
- **Keep engine running** throughout the installation
- **Multiple reboots are normal** - don't panic
- **Wait for completion message** before removing USB drive

## Completed

Your Ford SYNC 2 is now running the new firmware version.
