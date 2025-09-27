from flask import Flask, render_template, request, jsonify
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buckets')
def listar_buckets():
    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response["Buckets"]]
        return jsonify({"success": True, "buckets": buckets})
    except NoCredentialsError:
        return jsonify({"success": False, "error": "No se encontraron credenciales de AWS"})
    except ClientError as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/crear-bucket', methods=['POST'])
def crear_bucket():
    try:
        data = request.get_json()
        nombre = data['nombre']
        region = data['region']
        
        s3 = boto3.client("s3", region_name=region)
        if region != "us-east-1":
            s3.create_bucket(
                Bucket=nombre,
                CreateBucketConfiguration={"LocationConstraint": region}
            )
        else:
            s3.create_bucket(Bucket=nombre)
        return jsonify({"success": True})
    except ClientError as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/crear-instancia', methods=['POST'])
def crear_instancia():
    try:
        ec2 = boto3.client("ec2")
        response = ec2.run_instances(
            ImageId="ami-0c02fb55956c7d316",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro"
        )
        instance_id = response["Instances"][0]["InstanceId"]
        return jsonify({"success": True, "instanceId": instance_id})
    except ClientError as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/instancias')
def listar_instancias():
    try:
        ec2 = boto3.client("ec2")
        response = ec2.describe_instances()
        instancias = []
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                name = "Sin nombre"
                if "Tags" in instance:
                    for tag in instance["Tags"]:
                        if tag["Key"] == "Name":
                            name = tag["Value"]
                instancias.append({
                    "id": instance['InstanceId'],
                    "name": name,
                    "state": instance['State']['Name']
                })
        return jsonify({"success": True, "instancias": instancias})
    except ClientError as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)