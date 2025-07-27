# SyncExtPack Builder

A tool for building custom firmware packages for Ford SYNC 2 infotainment systems.

## PT-BE docs

Documentação em português disponivel [`README_PT-BR`](README_PT-BR.md).

## Platform Support

- **Windows**: Original platform (use `.bat` files)
- **macOS**: 🤖 **AI-Generated Support** - Full compatibility via Docker integration (use `.sh` files)
- **Linux**: Should work out of the box

## macOS Setup

For macOS users, see [`README_MACOS.md`](README_MACOS.md) for complete setup instructions.

**Note**: The macOS compatibility layer was entirely designed and implemented by **Claude 3.5 Sonnet**, demonstrating how AI can effectively modernize legacy codebases for cross-platform support.

## Quick Start

### Windows
```batch
build_pack.bat YOUR_APIM_SERIAL MAGIC_NUMBER
```

### macOS/Linux
```bash
./setup_macos.sh      # First-time setup
./build_pack.sh YOUR_APIM_SERIAL MAGIC_NUMBER
```

## Documentation

- **[macOS Setup Guide](README_MACOS.md)** - Complete setup instructions for macOS users
- **[Firmware Installation](FIRMWARE_INSTALLATION.md)** - Guide for upgrading to 3.10 or downgrading to 3.08 firmware
- **[SyncExtPack Installation](SYNCEXTPACK_INSTALLATION.md)** - Complete guide for installing the package
- **[Manual App Installation](MANUAL_APP_INSTALLATION.md)** - Step-by-step guide for installing apps using Total Commander without rebuilding firmware (uses AutoKit as example)

## Features

- **Custom App Integration** - Add CarPlay/Android Auto (AutoKit), VideoPlayer, Navigation apps, and more
- **Cross-Platform Support** - Works on Windows, macOS, and Linux
- **Manual Installation Mode** - Install apps directly via Total Commander for quick updates
- **Automated Plugin DLL Creation** - Python script to automatically create plugin DLLs for any app
- **Firmware Preservation** - Keep your existing SYNC 2 setup while adding new functionality

## AutoKit

- You need an adapter to make it work, look for CarlinKit CCPA
