@echo off
setlocal
cd /d "%~dp0"

if not exist "venv\Scripts\pythonw.exe" (
    echo Virtual environment not found.
    echo Run: python -m venv venv
    echo Then: venv\Scripts\pip.exe install -r requirements.txt
    pause
    exit /b 1
)

start "" "venv\Scripts\pythonw.exe" -m app.gui.native_gui
exit /b 0
