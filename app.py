from flask import Flask, request, render_template, redirect, url_for,session
import pyodbc
from passlib.hash import bcrypt
from flask_session import Session
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import uuid


app = Flask(__name__)

# Azure Blob Storage Configuration
azure_storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=photostor11;AccountKey=vLUut1rGPboRC0v6FV2vKFhK+kwSUiiXR5qufC4TzTXYE+sNXQSs62DxCdFSY7iHq0p406RJzsL0+AStRW6Dxg==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
container_name = "photoo"

# Configure session
app.config['SESSION_TYPE'] = 'filesystem'  # You can choose a different session storage method
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

# Azure SQL Database connection details
server = 'photo.database.windows.net'
database = 'photodb'
username_db = 'aayushidb'
password = 'Aayu@177'
driver = '{ODBC Driver 17 for SQL Server}'

# Establish a connection to the Azure SQL Database
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username_db};PWD={password}')

def authenticate_user(username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT PasswordHash FROM UserLogin WHERE Username = ?", (username,))
    row = cursor.fetchone()
    if row and bcrypt.verify(password, row.PasswordHash):
        return True
    return False




# ... (connection setup code)

def insert_user(first_name,last_name,username,email,password,container_name):
    hashed_password = bcrypt.hash(password)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO UserLogin (first_name,last_name,Username, PasswordHash,email,container_name) VALUES (?, ?,?, ?,?, ?)", (first_name,last_name,username, hashed_password,email,container_name))
    cursor.commit()


@app.route('/loginPage')
def login():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate the user
        if authenticate_user(username, password):
            session['username'] = username  # Create a session variable
            session.modified = True
            print('*'*4 + username)
            return redirect(url_for('dashboard'))  # Redirect to a dashboard or user profile page

        return render_template('login.html', message='Invalid credentials')

    return render_template('login.html')

@app.route('/signupPage')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup1():
    if request.method == 'POST':
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        email = request.form['email'].strip()
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        container_name = f"{first_name}-{username}"   #create contener with the name of this
        container_name = str(container_name.lower())
        #we have to put email and username validation it must be unique
        container_client = blob_service_client.get_container_client(container_name)
        container_client.create_container(public_access="blob")
        if container_client.exists():
            print("message Container created successfully!")
        else:
            print("message Failed to create container")
        insert_user(first_name,last_name,username,email,password,container_name)
        return redirect(url_for('login'))
    return render_template("signup.html")
    
def get_db_data(username1):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM UserLogin WHERE username = ?',str(username1))
    row1 = cursor.fetchone()
    print("#"*8)
    print(row1)
    return row1

def get_container_name(username1):
    if 'username' in session:
        #finding container name in db
        cursor = conn.cursor()
        cursor.execute('SELECT container_name FROM UserLogin WHERE username = ?',str(username1))
        container_name = cursor.fetchone()[0]
        print(container_name,cursor,username1)
        return container_name
    return "default"

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session.get('username')
    user_data = get_db_data(username)
    container_name = user_data.container_name
    #retrieving image from perticular container
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    img_link = list()
    for blob in blobs:
        blob_client = container_client.get_blob_client(blob=blob.name)
        img_link.append(blob_client.url)
    return render_template('dashboard.html', username=session['username'],blobs=img_link,user_data=user_data)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# Base template
@app.route('/base')
def base():
    return render_template('base.html')

# Header template
@app.route('/header')
def header():
    return render_template('header.html')

# Footer template
@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/')
def index():
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    img_link = list()
    for blob in blobs:
        blob_client = container_client.get_blob_client(blob=blob.name)
        img_link.append(blob_client.url)

    return render_template('index.html', blobs=img_link)

#upload process
@app.route('/upload', methods=['POST'])
def upload():
    username = session.get('username')
    container_name = get_container_name(username)
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    blob_name = str(uuid.uuid4()) + os.path.splitext(file.filename)[-1]
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(file)
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        img_url = request.form['img_url']
        print(img_url)
        blob_name = img_url.strip('/')[-1]
        container_name = img_url.strip('/')[-2]
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.delete_blob()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=int("3000"))
