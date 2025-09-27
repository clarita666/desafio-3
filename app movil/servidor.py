import http.server
import socketserver
import os

# Cambiar al directorio de la aplicación
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🌐 Servidor iniciado en http://localhost:{PORT}")
    print("📱 Usa ngrok para acceder desde tu celular")
    print("⏹️  Presiona Ctrl+C para detener el servidor")
    httpd.serve_forever()