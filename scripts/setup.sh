#!/bin/bash
# Install ganache-cli
npm install -g ganache-cli

# Start ganache node in background
echo "Starting ganache node..."
ganache-cli --gasPrice 0 --port 8545 &
sleep 5

# Verify node started
if ! pgrep ganache &>/dev/null; then
    echo "Failed to start ganache node"
    exit 1
fi

echo "Ganache node started successfully"
