# Brief Documentation

## 1. Setup

To get started with the application, follow these steps:

### 1.1 Clone the Repository:
```bash
git clone <repo_url>
```
### 1.2 Setup virtual environment
Setup a virtual environment to isolate project dependencies and 
avoid conflicts with other Python projects or your system's Python environment

Make sure Python 3.x is installed on your machine. You can verify this by running
```bash
python --version
```

If not installed please follow the python docs to install python 
https://www.python.org/downloads/

Run the following command to create a virtual environment
```bash
python python -m venv venv
```

Activate the virtual environment
- Windows
    ```bash
    venv\Scripts\activate 
    ```

- Mac/Linux
    ```bash
    source venv/bin/activate 
    ```

## 2. Install Dependencies:

Make sure you have Python 3.x and pip installed. Then, install the required packages using:
```bash
pip install -r requirements.txt
```

## 3. Setup the Database:
Create a local database to apply migrations on.

Create migrations :
```bash
python manage.py makemigrations
```

Run migrations to set up the database:
```bash
python manage.py migrate
```

## 4. Running the Application

Once the project is set up, you can run the development server:

```bash
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/ in your browser to access the application.

## 5. Testing the Application

### Uploading Images:
Visit the home page to upload an image using the provided form.
After uploading, the center-most pixel color will be extracted and stored in the database.

### Viewing Uploaded Images:
After the image is uploaded, the system will redirect to a list of all uploaded images

Click on any image to view it in full size along with its corresponding color.

If a non-image file is uploaded, the system will reject the file and display an error message.
If the image cannot be processed, the system will notify the user of the failure.
