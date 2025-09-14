#!/bin/bash
APP_DIR="/path/to/your/django/project"
VENV_DIR="$APP_DIR/venv"
PORT=8009

echo "🔍 Checking for processes on port $PORT..."
PID=$(lsof -ti:$PORT)

if [ -n "$PID" ]; then
    echo "⚠️ Killing process $PID on port $PORT..."
    kill -9 $PID
else
    echo "✅ No process running on port $PORT"
fi

echo "📂 Changing to app directory: $APP_DIR"
cd "$APP_DIR" || exit 1

echo "⚡ Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "🚀 Starting Django app on port $PORT..."
python manage.py runserver 0.0.0.0:$PORT
