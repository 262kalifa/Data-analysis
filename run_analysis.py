import os
import subprocess

# Function to run a Python script
def run_python_script(script_name):
    try:
        print(f"Running {script_name}...")
        subprocess.run(['python', script_name], check=True)
        print(f"{script_name} ran successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

# Function to open a Jupyter notebook
def open_jupyter_notebook(notebook_name):
    try:
        print(f"Opening {notebook_name}...")
        subprocess.run(['jupyter', 'notebook', notebook_name])
    except Exception as e:
        print(f"Error opening {notebook_name}: {e}")

if __name__ == "__main__":
    # Replace these with your actual script and notebook names
    python_script = 'script_name.py'
    jupyter_notebook = 'notebook_name.ipynb'

    run_python_script(python_script)
    open_jupyter_notebook(jupyter_notebook)
