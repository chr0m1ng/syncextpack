# Manual App Installation Guide for Ford SYNC 2

This guide shows how to manually install custom applications on Ford SYNC 2 using Total Commander, without needing to rebuild the entire firmware package. We'll use **AutoKit** (an app that enables CarPlay and Android Auto) as our example, but the same process applies to any custom app.

## Prerequisites

- Ford SYNC 2 system with SyncExtPack already installed
- Total Commander app installed and working
- USB drive formatted as FAT32 with MBR partition scheme
- Basic understanding of file system navigation

## Overview

Ford SYNC 2 apps require three main components:
1. **App files** - The actual application executable and resources
2. **Plugin DLL** - Windows CE plugin that launches the app from SYNC interface
3. **System registration** - XML and SWF files that add the app to the Apps menu

## Step-by-Step Installation

### Step 1: Prepare Your Files

Before starting, ensure you have:
- App folder (e.g., `AutoKit/` with all app files)
- Plugin DLL (e.g., `AutoKitPlugin.dll`) - see below how to create
- App icon PNG file (e.g., `AutoKit.png`)

#### 1.1 Creating the Plugin DLL

Since most apps don't come with a SYNC 2 plugin DLL, you'll need to create one by modifying an existing plugin:

**Method A: Automated Python Script (Recommended)**

Use the included `create_plugin_dll.py` script to automatically generate the plugin DLL from scratch:

1. **Run the script:**
   ```bash
   python create_plugin_dll.py AutoKit
   ```

2. **The script will automatically:**
   - Generate a complete Windows CE DLL from scratch
   - Configure the correct executable path for your app
   - Create `AutoKitPlugin.dll` ready for installation
   - Show you the exact XML entry needed
   - **No base DLL required!**

**Method B: Manual Hex-Editing**

If you prefer to do it manually or the script doesn't work:

1. **Choose a base plugin DLL** from your SYNC 2 system:
   - `MirrorLinkPlugin.dll` (recommended - clean and simple)
   - `ExplorerPlugin.dll` (Total Commander plugin)
   - Any other working plugin from `\windows\` directory

2. **Copy the base DLL** to your computer and rename it:
   ```
   MirrorLinkPlugin.dll → AutoKitPlugin.dll
   ```

3. **Hex-edit the executable path** using a hex editor:
   - **Windows**: HxD (free download)
   - **macOS**: Hex Fiend (free from App Store)
   - **Linux**: xxd command or GHex

4. **Find and replace the executable path**:
   - Search for the original path string (e.g., `/SyncExtendedPack/Apps/Media/MirrorLink/`)
   - Replace with your app path: `/SyncExtendedPack/Apps/Media/AutoKit/AutoKit.exe`
   - **Important**: Ensure the new path doesn't exceed the original string length
   - Pad with null bytes (`00`) if the new path is shorter

5. **Save the modified DLL** with your app name (e.g., `AutoKitPlugin.dll`)

**Example path replacement:**
```
Original: /SyncExtendedPack/Apps/Media/MirrorLink/MirrorLink.exe
New:      /SyncExtendedPack/Apps/Media/AutoKit/AutoKit.exe
```

### Step 2: Copy App Files to SYNC 2

Using Total Commander on your SYNC 2 system:

**Setup Total Commander Windows:**
- **Left window**: Navigate to `USB Disk` (your USB drive)
- **Right window**: Navigate to SYNC 2 file system

**Copy App Files:**

1. **Navigate to the Media Apps directory in right window:**
   ```
   \SyncExtendedPack\Apps\Media\
   ```
   Keep this window open on this location.

2. **Copy your app folder from USB:**
   - In the left window (USB), select your app folder (e.g., `AutoKit`)
   - Click the **Copy** icon (3rd icon from right to left in toolbar)
   - Confirm "Copy" when prompted - the destination is already set to the right window location
   - **No need to create folders manually** - Total Commander copies the complete folder structure

3. **Copy the Plugin DLL:**
   - In the right window, navigate to `\windows\`
   - In the left window (USB), select your plugin DLL (e.g., `AutoKitPlugin.dll`)
   - Click the **Copy** icon and confirm

4. **Copy the App Icon:**
   - In the right window, navigate to `\8inchSkins\Ford\Sync\Apps\Info\SyncApps\Icons\`
   - In the left window (USB), select your app icon (e.g., `AutoKit.png`)
   - Click the **Copy** icon and confirm

**Total Commander Tips:**
- The copy operation preserves all file structures automatically
- Always use the Copy icon (not drag & drop) for reliable transfers
- The destination path is automatically set to the currently open right window location

### Step 3: Update System Registration Files

#### 3.1 Backup Original Files

**IMPORTANT**: Always backup these files before modifying:
- `\8inchSkins\Ford\Sync\Apps\Info\SyncApps\SyncApps.xml`
- `\8inchSkins\Ford\Sync\Apps\Info\SyncApps\SyncApps.swf`

**Using Total Commander to backup:**
1. **Setup windows:**
   - **Left window**: Navigate to `USB Disk` (your USB drive)
   - **Right window**: Navigate to `\8inchSkins\Ford\Sync\Apps\Info\SyncApps\`

2. **Backup the files:**
   - In the right window (SYNC 2), select both `SyncApps.xml` and `SyncApps.swf`
   - Click the **Copy** icon (3rd icon from right to left in toolbar)
   - Confirm "Copy" - files will be copied to your USB drive for safe keeping

**Alternative**: You can also create a backup folder on your USB drive (e.g., `Backup/`) and copy the files there for better organization.

#### 3.2 Modify SyncApps.xml

1. **Copy SyncApps.xml to your computer** via USB drive

2. **Edit the XML file** with any text editor:

   **Before (example):**
   ```xml
   <?xml version="1.0" ?>
   <root>
       <apps>
           <app name="MirrorLink">
               <native>MirrorLinkPlugin</native>
               <iconPath>Apps/Info/SyncApps/Icons/MirrorLink.png</iconPath>
           </app>
           <app name="Total Commander">
               <native>ExplorerPlugin</native>
               <iconPath>Apps/Info/SyncApps/Icons/Explorer.png</iconPath>
           </app>
           <app name="">
               <native/>
               <iconPath/>
           </app>
   ```

   **After (adding AutoKit):**
   ```xml
   <?xml version="1.0" ?>
   <root>
       <apps>
           <app name="MirrorLink">
               <native>MirrorLinkPlugin</native>
               <iconPath>Apps/Info/SyncApps/Icons/MirrorLink.png</iconPath>
           </app>
           <app name="Total Commander">
               <native>ExplorerPlugin</native>
               <iconPath>Apps/Info/SyncApps/Icons/Explorer.png</iconPath>
           </app>
           <app name="AutoKit">
               <native>AutoKitPlugin</native>
               <iconPath>Apps/Info/SyncApps/Icons/AutoKit.png</iconPath>
           </app>
           <app name="">
               <native/>
               <iconPath/>
           </app>
   ```

   **XML Structure Explanation:**
   - `name` - Display name in SYNC Apps menu
   - `native` - Plugin DLL name (without .dll extension)
   - `iconPath` - Path to app icon (relative to SYNC root)

3. **Save the modified XML file**

#### 3.3 Generate Compatible SWF File

The SWF (Flash) file contains the compiled UI elements and must match your XML configuration.

**Use SyncExtPack Builder to generate the SWF:**

1. **Update your FullPack configuration:**
   - Edit `FullPack/8inchSkins/Ford/Sync/Apps/Info/SyncApps/SyncApps.xml` to match your desired configuration
   - Ensure all app files are in the correct FullPack directories

2. **Build a new package:**
   ```bash
   ./build_pack.sh YOUR_APIM_SERIAL 0
   ```

3. **Extract the generated SWF:**
   - The build process creates an updated `SyncApps.swf` in `FullPack/8inchSkins/Ford/Sync/Apps/Info/SyncApps/`
   - This SWF file will be perfectly synchronized with your XML

### Step 4: Install Updated Registration Files

1. **Copy your modified files back to SYNC 2 using Total Commander:**

   **Setup Total Commander Windows:**
   - **Left window**: Navigate to `USB Disk` (your USB drive where your modified files are)
   - **Right window**: Navigate to `\8inchSkins\Ford\Sync\Apps\Info\SyncApps\`

   **Copy the modified XML file:**
   - In the left window (USB), select your modified `SyncApps.xml`
   - Click the **Copy** icon (3rd icon from right to left in toolbar)
   - Since the file already exists, you'll be prompted with overwrite options
   - Click **"Overwrite All"** to replace the original file

   **Copy the generated SWF file:**
   - In the left window (USB), select the new `SyncApps.swf` (from your build process)
   - Click the **Copy** icon
   - Click **"Overwrite All"** when prompted to replace the original file

   **Total Commander Overwrite Behavior:**
   - When copying files that already exist, Total Commander will ask what to do
   - Always choose **"Overwrite All"** to replace the original files with your modified versions
   - This ensures your new app configuration is properly installed

2. **Reboot your SYNC 2 system**

   **Easy Method: Use the Reboot App**
   - Close Total Commander
   - Press the **i** button (information) on your SYNC 2
   - Navigate to **Apps**
   - Select **Reboot** app
   - Your system will restart automatically

   **Alternative**: You can also turn your car off and on again to restart SYNC 2.

3. **Verify installation:**
   - Navigate to Apps menu
   - Your new app should appear in the list

## Directory Structure Reference

```
SYNC 2 File System:
├── \SyncExtendedPack\Apps\Media\
│   └── [YourApp]\                          # App files location
│       ├── [YourApp].exe
│       └── [other app files...]
├── \windows\
│   └── [YourApp]Plugin.dll                 # Plugin DLL
└── \8inchSkins\Ford\Sync\Apps\Info\SyncApps\
    ├── SyncApps.xml                        # App registration
    ├── SyncApps.swf                        # UI definitions
    └── Icons\
        └── [YourApp].png                   # App icon
```

## Troubleshooting

### AutoKit Doesn't Appear in Menu
- Verify `AutoKitPlugin.dll` is in `\windows\` directory
- Check XML syntax in `SyncApps.xml`
- Ensure SWF and XML files are synchronized
- Reboot SYNC 2 system

### AutoKit Won't Launch
- Verify plugin DLL has correct path to `AutoKit.exe`
- Check that AutoKit files are in `\SyncExtendedPack\Apps\Media\AutoKit\`
- Ensure plugin DLL was properly hex-edited with AutoKit paths


### General App Issues
- **Display issues**: Verify app is designed for 800x480 resolution (Ford SYNC 2 standard)

## Plugin DLL Development

For advanced users wanting to create custom plugins:

### DLL Requirements
- Must be Windows CE compatible
- Should export standard plugin interface functions
- Must handle app launching and lifecycle management

**Note**: The plugin DLL creation process is covered in Step 1.1 above.

## Safety Notes

- **Always backup original files** before making changes
- **Test changes incrementally** - add one app at a time
- **Keep USB recovery tools** available in case of issues
- **Document your changes** for future reference

## Contributing

If you develop new apps or improvements to this process, please contribute back to the community by:
- Sharing working configurations
- Documenting plugin DLL modifications
- Providing troubleshooting solutions
- Creating automated installation scripts

---

**Disclaimer**: Modifying Ford SYNC 2 firmware may void your warranty. Proceed at your own risk and always maintain proper backups.
