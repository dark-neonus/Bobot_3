#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: ./get_from_pi.sh [REMOTE_PI_SOURCE1] [REMOTE_PI_SOURCE2] ... [LOCAL_LAPTOP_DEST_DIR]"
    echo "Example: ./get_from_pi.sh ~/Bobot3/logs/ ./backup/"
    exit 1
fi

LOCAL_DEST="${@: -1}"
REMOTE_SOURCES=()
for ((i=1; i<$#; i++)); do
    REMOTE_SOURCES+=("dark-neonus@raspberrypi.local:${!i}")
done

echo "🔄 Pulling files from Raspberry Pi to Laptop..."
echo "📍 Local Destination: $LOCAL_DEST"
echo "------------------------------------------------------------"

rsync -avzP "${REMOTE_SOURCES[@]}" "$LOCAL_DEST"
