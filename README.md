🚀 Script de Automatización con AWS boto3

Este proyecto es un ejemplo de automatización en AWS utilizando el SDK de Python (boto3).
El script permite:

📂 Listar todos los buckets de S3 en la cuenta.
🛠️ Crear un bucket nuevo en la región indicada.

Fue construido con la ayuda de Amazon Q Developer, que generó la base del código y guió los pasos de implementación.

⚙️ Requisitos
Python 3.8 o superior
boto3 instalado:
pip install boto3

AWS CLI configurado con credenciales válidas:
aws configure

▶️ Uso

Ejecuta el script en tu consola:

python script.py

Primero mostrará todos los buckets existentes en tu cuenta AWS.
Luego te preguntará si deseas crear un bucket nuevo.

Ejemplo de ejecución:

🔹 Script de automatización con boto3 🔹

Buckets en tu cuenta:
  - proyecto-datos
  - logs-pruebas
  - backups2025

¿Querés crear un bucket nuevo? (s/n): s
Ingresá el nombre del nuevo bucket: nerdearla-demo
✅ Bucket 'nerdearla-demo' creado en us-east-1.
