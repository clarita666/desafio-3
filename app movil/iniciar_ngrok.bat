@echo off
echo 🚀 Iniciando servidor y ngrok...
echo.

REM Iniciar el servidor Python en segundo plano
start "Servidor Python" python servidor.py

REM Esperar un momento para que el servidor se inicie
timeout /t 3 /nobreak >nul

REM Iniciar ngrok
echo 📱 Iniciando ngrok...
ngrok http 8000

pause