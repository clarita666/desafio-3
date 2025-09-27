import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def listar_buckets():
    """Lista todos los buckets de S3 en la cuenta"""
    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()
        print("Buckets en tu cuenta:")
        for bucket in response["Buckets"]:
            print(f"  - {bucket['Name']}")
    except NoCredentialsError:
        print("⚠️ No se encontraron credenciales de AWS. Configuralas con 'aws configure'.")
    except ClientError as e:
        print(f"Error: {e}")

def crear_bucket(nombre_bucket, region="us-east-1"):
    """Crea un bucket nuevo en la región indicada"""
    try:
        s3 = boto3.client("s3", region_name=region)
        if region != "us-east-1":
            s3.create_bucket(
                Bucket=nombre_bucket,
                CreateBucketConfiguration={"LocationConstraint": region}
            )
        else:
            s3.create_bucket(Bucket=nombre_bucket)
        print(f"✅ Bucket '{nombre_bucket}' creado en {region}.")
    except ClientError as e:
        print(f"Error al crear el bucket: {e}")

def listar_instancias_ec2():
    """Lista todas las instancias EC2"""
    try:
        ec2 = boto3.client("ec2")
        response = ec2.describe_instances()
        print("\nInstancias EC2:")
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                name = "Sin nombre"
                if "Tags" in instance:
                    for tag in instance["Tags"]:
                        if tag["Key"] == "Name":
                            name = tag["Value"]
                print(f"  - {instance['InstanceId']} ({name}) - {instance['State']['Name']}")
    except ClientError as e:
        print(f"Error: {e}")

def crear_instancia_ec2():
    """Crea una instancia EC2 básica"""
    try:
        ec2 = boto3.client("ec2")
        response = ec2.run_instances(
            ImageId="ami-0c02fb55956c7d316",  # Amazon Linux 2
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName=input("Nombre de tu Key Pair (opcional, Enter para omitir): ").strip() or None
        )
        instance_id = response["Instances"][0]["InstanceId"]
        print(f"✅ Instancia EC2 creada: {instance_id}")
    except ClientError as e:
        print(f"Error al crear instancia: {e}")

def menu():
    """Menú principal"""
    while True:
        print("\n" + "="*50)
        print("🔹 SCRIPT DE AUTOMATIZACIÓN AWS 🔹")
        print("="*50)
        print("1. Listar buckets S3")
        print("2. Crear bucket S3")
        print("3. Listar instancias EC2")
        print("4. Crear instancia EC2")
        print("5. Salir")
        
        opcion = input("\nElige una opción (1-5): ").strip()
        
        if opcion == "1":
            listar_buckets()
        elif opcion == "2":
            nombre = input("Nombre del bucket: ").strip()
            region = input("Región (Enter para us-east-1): ").strip() or "us-east-1"
            crear_bucket(nombre, region)
        elif opcion == "3":
            listar_instancias_ec2()
        elif opcion == "4":
            crear_instancia_ec2()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    menu()