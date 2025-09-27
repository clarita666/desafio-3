#!/bin/bash

echo "🚀 Iniciando servidor y ngrok..."
echo

# Iniciar el servidor Python en segundo plano
python3 servidor.py &
SERVER_PID=$!

# Esperar un momento para que el servidor se inicie
sleep 3

echo "📱 Iniciando ngrok..."
echo "🌐 Servidor corriendo en http://localhost:8000"
echo

# Iniciar ngrok
ngrok http 8000

# Limpiar al salir
kill $SERVER_PID 2>/dev/null