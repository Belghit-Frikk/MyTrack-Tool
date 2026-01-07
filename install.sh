#!/bin/bash

echo "🚀 Starting MyTrack installation..."

# إعطاء صلاحيات التنفيذ للملفات
chmod +x mytrack.py track-clean.sh

# نقل الملفات إلى مجلد الأوامر في النظام
sudo cp mytrack.py /usr/local/bin/mytrack
sudo cp track-clean.sh /usr/local/bin/track-clean

echo "✅ Installation complete!"
echo "👉 You can now run 'mytrack' or 'track-clean' from anywhere."
