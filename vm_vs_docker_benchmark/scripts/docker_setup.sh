#!/bin/bash
echo "🐳 Setting up Docker environment for Pacman benchmark..."

sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io x11-utils

sudo usermod -aG docker $USER

echo "🐙 Building Docker image..."
docker build -t pacman-benchmark .

echo "✅ Setup complete!"
echo "➡️ To run the benchmark:"
echo "   docker run --rm pacman-benchmark"
