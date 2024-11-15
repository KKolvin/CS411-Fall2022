# Web app project for CS411 - Convenient Recipe

**Frontend:** html, css, js \
**Backend:** Python Flask, MySQL (database) 



To get the skeleton running, open a terminal and do the following: 
1. enter the skeleton folder 'cd path/to/skeleton' 
2. install all necessary packages 'pip install -r requirements.txt' (or use pip3) 
3. export flask (Mac, Linux)'export FLASK_APP=app.py', (Windows)'set FLASK_APP=app.py'

4. run schema.sql using MySQL Workbench
5. open app.py using your favorite editor, change 'cs460' in 'app.config['MYSQL_DATABASE_PASSWORD'] = 'cs460'' to your MySQL root password. You need to keep the quotations around your root password

6. back to the terminal, run the app 'python -m flask run' (or use python3)
7. open your browser, and open the local website 'localhost:5000'


To enable debugger: "export FLASK_APP=app.py" "export FLASK_DEBUG=1" before running flask


If port 5000 is occupied by another program, type "lsof -i tcp:5000" to check what ports there are, and then
"kill PID" to free the program.

---

**Demo Video**

[![Watch the video]()](https://www.youtube.com/watch?v=fa-8Pvreb_g)
