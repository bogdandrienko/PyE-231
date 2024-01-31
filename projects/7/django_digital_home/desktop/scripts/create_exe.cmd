cd ..
call env/scripts/activate
pip install pyinstaller



rmdir /Q /S output
pyinstaller main.py --noconfirm --onedir --windowed --name=desktop --icon=icon.ico --distpath ./output/dist --workpath ./output/build
mkdir output\dist\desktop\src
xcopy src output\dist\desktop\src /E /I



cmd
