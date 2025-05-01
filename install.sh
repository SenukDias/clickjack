#!/bin/bash

# Stop on errors
set -e

# Ensure script is run as root
if [[ "$EUID" -ne 0 ]]; then
  echo "❌ Please run as root (e.g., sudo ./install_clickjack.sh)"
  exit 1
fi

# Define paths
TOOL_DIR="/usr/local/bin"
TOOL_PATH="$TOOL_DIR/clickjack_tool"
WRAPPER_PATH="/usr/bin/clickjack"

# Copy main Python script
echo "📁 Installing clickjack tool..."
cp ./clickjack.py "$TOOL_PATH"
chmod +x "$TOOL_PATH"

# Create wrapper script
echo "🔧 Creating /usr/bin/clickjack..."
echo -e "#!/bin/bash\npython3 $TOOL_PATH \"\$@\"" > "$WRAPPER_PATH"
chmod +x "$WRAPPER_PATH"

echo "✅ Installation complete!"
echo "👉 You can now run: clickjack https://example.com"

