#!/bin/bash
set -e
sudo apt update
sudo apt install -y docker.io docker-compose nodejs npm python3-pip tor git
echo "Dependencies installed."
