#!/bin/bash

# ==============================================================================
# CONFIGURATION: Set your laptop username here
# ==============================================================================
LAPTOP_USER="your_laptop_username"   # 👈 Change to your actual laptop user account
TUNNEL_PORT="5022"

if [ "$#" -lt 2 ]; then
    echo "Usage: ./get_from_host.sh [LAPTOP_SOURCE1] [LAPTOP_SOURCE2] ... [PI_DEST_DIR]"
    echo "Example: ./get_from_host.sh ~/Desktop/firmware.bin ~/Bobot3/build/"
    exit 1
fi

PI_DEST="${@: -1}"
REMOTE_SOURCES=()
for ((i=1; i<$#; i++)); do
    REMOTE_SOURCES+=("${LAPTOP_USER}@localhost:${!i}")
done

echo "📥 Grabbing files from Laptop through secure tunnel..."
echo "📍 Pi Destination: $PI_DEST"
echo "------------------------------------------------------------"

rsync -avzP -e "ssh -p $TUNNEL_PORT" "${REMOTE_SOURCES[@]}" "$PI_DEST"
