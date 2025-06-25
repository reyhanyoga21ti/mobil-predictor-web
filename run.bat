@echo off
echo Membuat virtual environment...
python -m venv venv

echo.
echo Mengaktifkan virtual environment...
call venv\Scripts\activate.bat

echo.
echo Menginstal dependensi dari requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Menjalankan Flask App...
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

pause