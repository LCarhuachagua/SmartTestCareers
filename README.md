# SmartTestCareers

## Steps to run

1. Create virtual env:
    python -m venv stc-env
2. Activate the virtual env:
    a. Windows: stc-env\Scripts\activate.bat
    b. Linux/Mac: source stc-env/Scripts/activate
3. Install dependencies inside requeriments.txt
    pip install -r requeriments.txt
4. Start the server:
    uvicorn main:app --reload