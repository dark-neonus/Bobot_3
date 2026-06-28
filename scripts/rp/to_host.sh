#!/bin/bash

# ==============================================================================
# CONFIGURATION: Set your laptop username here
# ==============================================================================
LAPTOP_USER="dark-neonus"   # 👈 Change to your actual laptop user account
TUNNEL_PORT="5022"

if [ "$#" -lt 2 ]; then
    echo "Usage: ./to_host.sh [PI_SOURCE1] [PI_SOURCE2] ... [LAPTOP_DESTINATION_DIR]"
    echo "Example: ./to_host.sh ~/Bobot3/main.cpp ~/Desktop/"
    exit 1
fi

LAPTOP_DEST="${@: -1}"
SOURCES=("${@:1:$#-1}")

echo "🔄 Pushing files through secure tunnel to Laptop..."
echo "📍 Destination: ${LAPTOP_USER}@localhost:${LAPTOP_DEST} (Port $TUNNEL_PORT)"
echo "------------------------------------------------------------"

rsync -avzP -e "ssh -p $TUNNEL_PORT" "${SOURCES[@]}" "${LAPTOP_USER}@localhost:${LAPTOP_DEST}"
