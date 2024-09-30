# Backend

After installing Mysql
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

Check config.ini
Replace the database information with the local sql server

Run uvicorn app.main:app --reload
