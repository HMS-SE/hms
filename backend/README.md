# HMS Backend 

## Setup Instructions (Developer)
---
**NOTE**

Make sure you have Python 3.10 installed and setup properly on your system. 

---
1. Change current directory to backend.
```cmd 
cd backend
# or 
cd hms/backend
```
1. Create a new virtual environment (first time).
```cmd
python -m venv venv
# or -- depending on system configuration (Python 3.10 should be used)
python3 -m venv venv 
```
2. Activate the virtual environment.
```cmd
source venv/bin/activate
```
3. Install requirements
```cmd
pip install -r requirements/dev.txt
# or -- depending on system configuration
pip3 install -r requirements/dev.txt
``` 
4. Run the development server
```cmd 
uvicorn main:app --reload
```