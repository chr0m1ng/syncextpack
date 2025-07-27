#!/bin/bash

# Docker wrapper for crypto_pack - Created by Claude 3.5 Sonnet
# Wrapper script to run crypto_pack via Docker
# This allows running the Linux binary on macOS with x86_64 emulation

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Use x86-64 Ubuntu image since crypto_pack is a x86-64 Linux binary
IMAGE_NAME="--platform=linux/amd64 ubuntu:20.04"

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker to use this wrapper."
    echo "Alternatively, you can install Docker Desktop from: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Get current user ID and group ID for proper file permissions
USER_ID=$(id -u)
GROUP_ID=$(id -g)

# Create a temporary container and run crypto_pack with proper permissions
docker run --rm \
  --platform=linux/amd64 \
  -v "$SCRIPT_DIR:/workspace" \
  -w /workspace \
  -u "$USER_ID:$GROUP_ID" \
  ubuntu:20.04 \
  bash -c "chmod +x /workspace/crypto_pack && /workspace/crypto_pack $*"
