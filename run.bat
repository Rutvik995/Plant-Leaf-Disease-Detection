@echo off
title FloraScan AI - Plant Leaf Disease Detection Server
echo ========================================================
echo  Starting FloraScan AI - Plant Leaf Disease Detection
echo ========================================================
echo.
echo Starting Python Flask server using Python 3.12...
py -3.12 run.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] Direct launch with py -3.12 failed, trying system python...
    python run.py
)
pause
