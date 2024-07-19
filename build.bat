@echo off
pip install --upgrade nuitka
python -m nuitka --standalone --onefile --follow-imports --windows-icon-from-ico=skid.png --output-dir=dist --output-filename=skid.exe skid.py