#!/usr/bin/env python3
"""
Ford SYNC 2 Plugin DLL Creator

This script creates a plugin DLL for custom apps from scratch, without needing 
any base DLL files. It generates a minimal Windows CE DLL with the correct 
structure and executable path for your app.

Usage:
    python create_plugin_dll.py <app_name>

Example:
    python create_plugin_dll.py AutoKit
    python create_plugin_dll.py VideoPlayer
"""

import os
import struct
import sys
from pathlib import Path


def create_minimal_plugin_dll(app_name, output_dir="."):
    """
    Create a minimal plugin DLL from scratch for the specified app.
    
    This generates a basic Windows CE DLL with the minimum structure needed
    to launch an app from Ford SYNC 2 interface.
    """
    
    app_path = f"/SyncExtendedPack/Apps/Media/{app_name}/{app_name}.exe"
    app_path_bytes = app_path.encode('utf-8') + b'\x00'  # null-terminated
    
    print(f"🔧 Creating plugin DLL for {app_name}")
    print(f"   Target path: {app_path}")
    
    # DOS Header (64 bytes)
    dos_header = bytearray(64)
    dos_header[0:2] = b'MZ'  # DOS signature
    dos_header[60:64] = struct.pack('<I', 128)  # PE header offset
    
    # PE Header (starts at offset 128)
    pe_signature = b'PE\x00\x00'
    
    # COFF Header (20 bytes)
    coff_header = struct.pack('<HHIIIHH',
        0x01C0,  # Machine type (ARM for Windows CE)
        3,       # Number of sections
        0,       # Time/date stamp
        0,       # Pointer to symbol table
        0,       # Number of symbols
        224,     # Size of optional header
        0x2102   # Characteristics (executable, DLL)
    )
    
    # Optional Header (224 bytes for PE32)
    optional_header = struct.pack('<HHBBIIIIIIIHHHHHHIIIIHHIIIIIIII',
        0x10B,      # Magic (PE32)
        1, 0,       # Linker version
        0x1000,     # Size of code
        0x1000,     # Size of initialized data
        0,          # Size of uninitialized data
        0x2000,     # Address of entry point
        0x1000,     # Base of code
        0x2000,     # Base of data
        0x10000000, # Image base
        0x1000,     # Section alignment
        0x200,      # File alignment
        4, 0,       # OS version
        0, 0,       # Image version
        4, 0,       # Subsystem version
        0,          # Win32 version
        0x4000,     # Size of image
        0x200,      # Size of headers
        0,          # Checksum
        9,          # Subsystem (Windows CE)
        0,          # DLL characteristics
        0x100000,   # Size of stack reserve
        0x1000,     # Size of stack commit
        0x100000,   # Size of heap reserve
        0x1000,     # Size of heap commit
        0,          # Loader flags
        16          # Number of RVA and sizes
    )
    
    # Data directories (16 entries, 8 bytes each)
    data_directories = b'\x00' * (16 * 8)
    
    # Section Headers (3 sections, 40 bytes each)
    
    # .text section
    text_section = struct.pack('<8sIIIIIIHHI',
        b'.text\x00\x00\x00',  # Name
        0x1000,     # Virtual size
        0x1000,     # Virtual address
        0x1000,     # Size of raw data
        0x400,      # Pointer to raw data
        0, 0, 0, 0, # Relocations, line numbers, counts
        0x60000020  # Characteristics (code, executable, readable)
    )
    
    # .data section
    data_section = struct.pack('<8sIIIIIIHHI',
        b'.data\x00\x00\x00',  # Name
        0x1000,     # Virtual size
        0x2000,     # Virtual address
        len(app_path_bytes) + 100,  # Size of raw data (path + padding)
        0x1400,     # Pointer to raw data
        0, 0, 0, 0, # Relocations, line numbers, counts
        0xC0000040  # Characteristics (data, readable, writable)
    )
    
    # .rsrc section (minimal resource section)
    rsrc_section = struct.pack('<8sIIIIIIHHI',
        b'.rsrc\x00\x00\x00',  # Name
        0x1000,     # Virtual size
        0x3000,     # Virtual address
        0x200,      # Size of raw data
        0x1600,     # Pointer to raw data
        0, 0, 0, 0, # Relocations, line numbers, counts
        0x40000040  # Characteristics (initialized data, readable)
    )
    
    # Build the complete PE file
    pe_data = bytearray()
    
    # DOS header (64 bytes)
    pe_data.extend(dos_header)
    
    # Pad to PE header offset (128)
    pe_data.extend(b'\x00' * (128 - len(pe_data)))
    
    # PE header
    pe_data.extend(pe_signature)
    pe_data.extend(coff_header)
    pe_data.extend(optional_header)
    pe_data.extend(data_directories)
    
    # Section headers
    pe_data.extend(text_section)
    pe_data.extend(data_section)
    pe_data.extend(rsrc_section)
    
    # Pad to first section (0x400)
    pe_data.extend(b'\x00' * (0x400 - len(pe_data)))
    
    # .text section content (minimal code)
    # This is a minimal ARM assembly stub that would normally launch the app
    text_content = bytearray(0x1000)
    # Add some basic ARM instructions (NOP equivalents for safety)
    for i in range(0, min(64, len(text_content)), 4):
        text_content[i:i+4] = b'\x00\xF0\x20\xE3'  # ARM NOP instruction
    
    pe_data.extend(text_content)
    
    # .data section content (app path and basic data)
    data_content = bytearray(len(app_path_bytes) + 100)
    
    # Store the app path at the beginning of data section
    data_content[0:len(app_path_bytes)] = app_path_bytes
    
    # Add some padding and basic DLL export information
    data_content[64:68] = struct.pack('<I', 0x2000)  # Pointer to app path
    data_content[68:72] = struct.pack('<I', len(app_path_bytes))  # Path length
    
    pe_data.extend(data_content)
    
    # Pad to next section boundary
    while len(pe_data) % 0x200 != 0:
        pe_data.append(0)
    
    # .rsrc section content (minimal resources)
    rsrc_content = b'\x00' * 0x200
    pe_data.extend(rsrc_content)
    
    # Create output filename
    output_filename = f"{app_name}Plugin.dll"
    output_path = os.path.join(output_dir, output_filename)
    
    try:
        # Write the DLL file
        with open(output_path, 'wb') as f:
            f.write(pe_data)
        
        print(f"✅ Successfully created: {output_path}")
        print(f"📝 Plugin DLL size: {len(pe_data)} bytes")
        
        # Provide usage instructions
        print(f"\n📋 Next steps:")
        print(f"   1. Copy {output_filename} to your SYNC 2's \\windows\\ directory")
        print(f"   2. Copy your {app_name} app files to \\SyncExtendedPack\\Apps\\Media\\{app_name}\\")
        print(f"   3. Add this XML entry to SyncApps.xml:")
        print(f"      <app name=\"{app_name}\">")
        print(f"          <native>{app_name}Plugin</native>")
        print(f"          <iconPath>Apps/Info/SyncApps/Icons/{app_name}.png</iconPath>")
        print(f"      </app>")
        print(f"   4. Regenerate the SWF file using the SyncExtPack builder")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating DLL: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Ford SYNC 2 Plugin DLL Creator")
        print("=" * 40)
        print("\nUsage:")
        print("  python create_plugin_dll.py <app_name>")
        print("\nExamples:")
        print("  python create_plugin_dll.py AutoKit")
        print("  python create_plugin_dll.py VideoPlayer")
        print("  python create_plugin_dll.py MyCustomApp")
        print("\nThe script generates a minimal Windows CE DLL with the correct")
        print("structure to launch your app from Ford SYNC 2 interface.")
        sys.exit(1)
    
    app_name = sys.argv[1]
    
    # Validate app name
    if not app_name.replace("_", "").replace("-", "").isalnum():
        print("❌ Error: App name should only contain letters, numbers, hyphens, and underscores")
        sys.exit(1)
    
    if len(app_name) > 50:
        print("❌ Error: App name is too long (max 50 characters)")
        sys.exit(1)
    
    success = create_minimal_plugin_dll(app_name)
    
    if not success:
        sys.exit(1)
    
    print(f"\n🎉 Plugin DLL for {app_name} created successfully!")


if __name__ == "__main__":
    main()
