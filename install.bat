@echo off
color 03
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    pause
    exit /b 1
) else (
    echo Python is installed.
    python --version
)
pip uninstall discord.py
pip uninstall websocket
pip install -r requirements.txt