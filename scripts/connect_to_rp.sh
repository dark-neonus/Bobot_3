#!/bin/bash

# ==============================================================================
# CONFIGURATION
# ==============================================================================
PI_USER="dark-neonus"
PI_HOST="raspberrypi.local"
TUNNEL_PORT="5022"

echo "🔍 Searching for Raspberry Pi on the local network..."

# 1. Ping the Pi quickly to ensure it's reachable before initiating SSH
if ! ping -c 1 -W 2 "$PI_HOST" > /dev/null 2>&1; then
    echo "❌ Error: Cannot reach $PI_HOST."
    echo "👉 Make sure your Pi is powered on and connected to the same network."
    exit 1
fi

echo "🚀 Pi found! Securing network tunnel..."
echo "🔒 Reverse tunnel mapped: Pi Port $TUNNEL_PORT ➡️ Laptop Port 22"
echo "------------------------------------------------------------"

# 2. Establish the SSH Connection with Reverse Port Forwarding
# -R 5022:localhost:22 maps the Pi's local port 5022 back to your laptop's SSH server
# -t forces pseudo-terminal allocation (required for interactive apps like Zellij/Micro)
# "clear && bash" flushes the screen buffer instantly and hands you a clean bash shell
ssh -R ${TUNNEL_PORT}:localhost:22 -t "${PI_USER}@${PI_HOST}" "clear && bash"
