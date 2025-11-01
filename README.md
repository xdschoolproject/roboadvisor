## Setting Up the Virtual Environment (Windows)

### 1. Create a Virtual Environment
   Open **Command Prompt** or **PowerShell**, and navigate to your cloned project folder:
   ```bash
   cd path\to\your\cloned\repo\test
````

Then, create a new virtual environment in your project directory:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

Activate the environment by running the following command:

```bash
venv\Scripts\activate
```

After activation, you should see `(venv)` in the command prompt, indicating that the virtual environment is active.

### 3. Install Dependencies

Install all the required dependencies from the `requirements.txt` file by running:

```bash
pip install -r requirements.txt
```

This will install all the necessary Python packages listed in `requirements.txt` to your virtual environment.

````
