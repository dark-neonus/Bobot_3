#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: ./to_pi.sh [SOURCE1] [SOURCE2] ... [REMOTE_PI_DESTINATION_DIR]"
    echo "Example: ./to_pi.sh main.cpp config.json ~/Bobot3/src/"
    exit 1
fi

DEST_DIR="${@: -1}"
SOURCES=("${@:1:$#-1}")

echo "🚀 Sending ${#SOURCES[@]} items to Raspberry Pi..."
echo "📍 Destination: dark-neonus@raspberrypi.local:$DEST_DIR"
echo "------------------------------------------------------------"

rsync -avzP "${SOURCES[@]}" "dark-neonus@raspberrypi.local:$DEST_DIR"
