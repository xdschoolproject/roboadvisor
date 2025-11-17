## Setting Up the Virtual Environment (Windows)
   **Note:** This step is needed after cloning the repository because the virtual environment contains all the necessary dependencies that the project requires.
   
### 1. Create a Virtual Environment
   Open **Command Prompt** or **PowerShell**, and navigate to your cloned project folder:
   ```bash
   cd path\to\your\cloned\repo\test
````

Then, create a new virtual environment in your project directory:

```bash
py -3.13 -m venv venv
```
After entering the command a venv folder should be created inside the project folder, like this:

```
project_folder/
│
├── venv/                         # Virtual environment folder Should be Here
│
├── roboadvisor/         
│
├── db.sqlite3                  
│
└── requirements.txt            
│
└──home_page/                     
│
└── stock_analysis_back_end/  
│
└── stock_analysis_front_end/ 
│
└── docs/                   

```
This structure places the `venv` (virtual environment) in the root of the project folder, alongside your application folder (`roboadvisor`), the database file (`db.sqlite3`), and the `requirements.txt` file.

### 2. Activate the Virtual Environment

Activate the environment by running the following command:

```bash
venv\Scripts\Activate.ps1
```

After activation, you should see `(venv)` in the command prompt, indicating that the virtual environment is active.

### 3. Install Dependencies

Install all the required dependencies from the `requirements.txt` file by running:

```bash
pip install -r requirements.txt
```

This will install all the necessary Python packages listed in `requirements.txt` to your virtual environment.

### 4. Verify the Installed Dependencies

To ensure that all dependencies were successfully installed, run the following command:

```bash
pip freeze
```

<br>

## Running the Django Web Application

### 1. Activate the Virtual Environment ()
   Open **terminal** in **vscode**, and navigate to your project folder:
   ```bash
   cd path\to\your\cloned\repo\
````
   Then activate the venv:
   ```bash
   venv\Scripts\Activate.ps1
````
### 2. Apply Database Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```
Note: You don't need to run migrate every time you start the server—just when there are changes to your models or new migrations.

### 3. Run the Django Development Server

Start the server with:

```bash
python manage.py runserver
```

By default, it will be accessible at `http://127.0.0.1:8000/`.

**Note:** This will only run code written in **django** and will not include **streamlit** code. You need to run both servers in order to run both applications together.

<br>

## Running the Streamlit and Django Web Application Together
### 1. Activate the Virtual Environment
   Open **terminal** in **vscode**, and navigate to your project folder:
   ```bash
   cd path\to\your\cloned\repo\test
````
   Then activate the venv:
   ```bash
   venv\Scripts\Activate.ps1
````
### 2. Apply Database Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```
**Note:** We need to run both **django** and **streamlit** server in the terminal. You need to run both servers in order to run both web applications together.

### 3. Run the Streamlit Server First

Navigate to the stock_analysis_front_end folder:
```bash
cd path\to\your\cloned\repo\roboadvisor\stock_analysis_front_end\ 
```
Start the server with: 
```bash
streamlit run stock_analysis_app.py 
```
This should open the stock analysis page in your browser. You can close the browser after openning but don't exit the server in the terminal.

### 4. Open a new tab in the terminal in vscode and activate the Virtual Environment in the new tab
   Open a new tab in the **terminal** in **vscode**, and navigate to your project folder (in vscode terminal click the "+" button):
   ```bash
   cd path\to\your\cloned\repo\test
````
   Then activate the venv:
   ```bash
   venv\Scripts\Activate.ps1
````
After activation, you should have two terminal tabs in vscode. The `(venv)` in the command prompt, indicates that the virtual environment is active.

### 5. Run the Django Development Server Second
Navigate to the main roboadvisor folder (make sure you are in the folder that has manage.py file):
```bash
cd path\to\your\cloned\repo\
```
Start the server with:
```bash
python manage.py runserver
```
By default, it will be accessible at `http://127.0.0.1:8000/`. Open the browser and enter `http://127.0.0.1:8000/` in the URL
