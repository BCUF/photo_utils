FOR /R %%a IN (*.tif) DO python resizer.py -s 2000 -i "%%~a" -o "c:\tmp\img\%%~na_2k.jpg"
pause