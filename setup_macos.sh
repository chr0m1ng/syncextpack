#!/bin/bash

# macOS Setup Script - Created by Claude 3.5 Sonnet
# Automates the setup of SyncExtPack Builder on macOS

echo "=== SyncExtPack Builder - macOS Setup ==="

# Check if we're on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "This setup script is designed for macOS. Exiting."
    exit 1
fi

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew is not installed. Please install it first:"
    echo "/bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi

echo "✓ Homebrew found"

# Install swfmill if not already installed
if ! command -v swfmill &> /dev/null; then
    echo "Installing swfmill..."
    brew install swfmill
else
    echo "✓ swfmill already installed"
fi

# Setup swfmill symlink
if [ -L "FlashTools/swfmill" ]; then
    echo "✓ swfmill symlink already exists"
elif [ -f "FlashTools/swfmill" ]; then
    echo "Backing up original swfmill and creating symlink..."
    mv FlashTools/swfmill FlashTools/swfmill.linux.bak
    ln -s /opt/homebrew/bin/swfmill FlashTools/swfmill
    echo "✓ swfmill symlink created"
else
    echo "Creating swfmill symlink..."
    ln -s /opt/homebrew/bin/swfmill FlashTools/swfmill
    echo "✓ swfmill symlink created"
fi

# Make crypto_pack executable
if [ -f "crypto_pack" ]; then
    chmod +x crypto_pack
    echo "✓ crypto_pack made executable"
fi

# Check if Docker is available
if command -v docker &> /dev/null; then
    echo "✓ Docker found - crypto_pack will work via Docker wrapper"
    echo "  You can use crypto_pack_docker.sh to run the Linux binary"
else
    echo "⚠️  Docker not found. Installing Docker Desktop is recommended for full functionality."
    echo "   Download from: https://www.docker.com/products/docker-desktop"
    echo "   Alternative: Use Lima/Colima for lightweight containerization"
fi

# Make shell scripts executable
chmod +x build_pack.sh unpack_pack.sh crypto_pack_docker.sh

echo ""
echo "=== Setup Summary ==="
echo "✓ swfmill: $(swfmill --version 2>/dev/null || echo 'Not working')"
echo "✓ Shell scripts: build_pack.sh, unpack_pack.sh created and made executable"
echo "✓ Docker wrapper: crypto_pack_docker.sh created"

# Check Python environment
if command -v python3 &> /dev/null; then
    echo "✓ Python3: $(python3 --version)"
    
    # Check if virtual environment exists
    if [ -d ".venv" ]; then
        echo "✓ Virtual environment found at .venv"
    else
        echo "ℹ️  No virtual environment found. You may want to create one:"
        echo "   python3 -m venv .venv"
        echo "   source .venv/bin/activate"
        echo "   pip install -r requirements.txt  # if requirements.txt exists"
    fi
else
    echo "⚠️  Python3 not found. Please install Python 3.x"
fi

# Check and setup Java
if command -v java &> /dev/null; then
    echo "✓ Java: $(java -version 2>&1 | head -n1)"
else
    echo "ℹ️  Java not found in PATH. Adding Homebrew OpenJDK to shell profile..."
    
    # Add Java to shell profile
    JAVA_PATH='export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"'
    
    if [[ "$SHELL" == *"zsh"* ]]; then
        if ! grep -q "openjdk" ~/.zshrc 2>/dev/null; then
            echo "$JAVA_PATH" >> ~/.zshrc
            echo "   Added Java to ~/.zshrc"
        fi
    elif [[ "$SHELL" == *"bash"* ]]; then
        if ! grep -q "openjdk" ~/.bash_profile 2>/dev/null; then
            echo "$JAVA_PATH" >> ~/.bash_profile
            echo "   Added Java to ~/.bash_profile"
        fi
    fi
    
    echo "   Please restart your terminal or run: source ~/.zshrc"
fi

echo ""
echo "=== Usage ==="
echo "1. For full functionality, install Docker Desktop"
echo "2. Use ./build_pack.sh instead of build_pack.bat"
echo "3. Use ./unpack_pack.sh instead of unpack_pack.bat"
echo "4. The project should now work on macOS with crypto_pack via Docker"

echo ""
echo "Setup complete! 🎉"
