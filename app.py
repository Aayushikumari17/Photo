from flask import Flask, render_template, request, redirect, url_for
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import uuid

app = Flask(__name__)

# Azure Blob Storage Configuration
azure_storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=newstorageaccav311;AccountKey=7JQsb/ufASY3sg/zPtrtRkSiFk8yRmhZgvzkhfke+8tXD8YVYwbGbWMQFc1tppOKpUWX8E6dvO2b+AStCtfxMA==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
container_name = "image"

@app.route('/')
def index():
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    img_link = list()
    for blob in blobs:
        blob_client = container_client.get_blob_client(blob=blob.name)
        img_link.append(blob_client.url)

    return render_template('index.html', blobs=img_link)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    blob_name = str(uuid.uuid4()) + os.path.splitext(file.filename)[-1]
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(file)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=int("3000"))


  