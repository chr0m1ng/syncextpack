# macOS Support for SyncExtPack Builder

## 🤖 AI-Generated macOS Compatibility

**This macOS compatibility layer was entirely designed and implemented by Claude 3.5 Sonnet** in collaboration with the project maintainer. The AI analyzed the original Windows-only codebase, identified compatibility issues, and created a complete cross-platform solution including:

- Platform detection bug fixes
- Docker integration for Linux binaries
- Homebrew tool integration  
- Shell script equivalents
- Automated setup scripts
- Comprehensive documentation

This demonstrates how AI can effectively modernize and extend existing codebases to support new platforms while maintaining backward compatibility.

---

## Overview

The SyncExtPack Builder now works natively on macOS thanks to:
- Fixed platform detection bug in `builder/utils.py`
- Docker wrapper for the Linux `crypto_pack` binary
- Homebrew installation of `swfmill`
- Shell script equivalents of Windows batch files

## Quick Setup

1. **Install dependencies**:
   ```bash
   # Install Homebrew if not already installed
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install swfmill and Java
   brew install swfmill
   brew install openjdk
   
   # Install Docker Desktop
   # Download from: https://www.docker.com/products/docker-desktop
   ```

2. **Run the automated setup**:
   ```bash
   ./setup_macos.sh
   ```

## Usage

### Building Packs

Use the shell script instead of the Windows batch file:

```bash
# Instead of build_pack.bat
./build_pack.sh YOUR_APIM_SERIAL MAGIC_NUMBER

# Example:
./build_pack.sh ABC12345 0
```

### Direct Python Usage

The Python scripts work the same on macOS:

```bash
python3 build_pack.py YOUR_APIM_SERIAL output.bin 0 UpdateService Player_EN Reboot
```

## Technical Details

### Platform Detection Fix

Fixed the critical bug in `builder/utils.py` where `'win' in sys.platform` incorrectly matched `'darwin'` (macOS), causing it to look for `.exe` files on Unix systems.

**Before** (broken):
```python
if 'win' in sys.platform:  # 'win' matches 'darwin'!
    PLATFORM_EXEC_FILE_POSTFIX = '.exe'
```

**After** (fixed):
```python
if sys.platform.startswith('win'):  # Correctly identifies Windows
    PLATFORM_EXEC_FILE_POSTFIX = '.exe'
```

### Docker Integration

The `crypto_pack_docker.sh` wrapper automatically runs the Linux `crypto_pack` binary in a Docker container with x86_64 emulation:

```bash
docker run --rm \
  --platform=linux/amd64 \
  -v "$PWD:/workspace" \
  -w /workspace \
  -u "$(id -u):$(id -g)" \
  ubuntu:20.04 \
  ./crypto_pack "$@"
```

The Python code automatically detects and uses this wrapper when available.

### Native Tools

- **swfmill**: Installed via Homebrew, symlinked to `FlashTools/swfmill`
- **Java**: OpenJDK via Homebrew for `secureSWF.jar`

## Files Added

- `build_pack.sh` - Shell script equivalent of `build_pack.bat`
- `unpack_pack.sh` - Shell script equivalent of `unpack_pack.bat`
- `crypto_pack_docker.sh` - Docker wrapper for `crypto_pack`
- `setup_macos.sh` - Automated setup script
- `README_MACOS.md` - This documentation

## Compatibility

- **macOS**: ✅ Full support (Apple Silicon and Intel)
- **Linux**: ✅ Should work (untested but designed for compatibility)  
- **Windows**: ✅ Original functionality preserved

## Troubleshooting

### Docker Issues
If you get "Docker not found" errors:
1. Install Docker Desktop
2. Make sure Docker is running
3. Test with: `docker --version`

### Java Issues
If you get "Java Runtime not found" errors:
1. Install OpenJDK: `brew install openjdk`
2. Add to PATH: `export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"`

### Permission Issues
If you get permission errors:
1. Make scripts executable: `chmod +x *.sh`
2. Check Docker permissions in Docker Desktop settings

## Contributing

When contributing to macOS support:
1. Test on both Apple Silicon and Intel Macs if possible
2. Ensure Windows compatibility is preserved
3. Update this README for any new features or requirements
