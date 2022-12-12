import flask
from flask import Flask, Response, request, render_template, redirect, url_for
from flaskext.mysql import MySQL
import flask_login
import requests, json, unicodedata
from flaskext.mysql import MySQL
import flask_login
from wtforms import Form, validators, TextField, PasswordField
import hashlib

#for image uploading
import os, base64

# mysql = MySQL()
app = Flask(__name__)
<<<<<<< HEAD
app.secret_key = 'hidden'
=======
# app.secret_key = 'hidden'  # Change this!

# #These will need to be changed according to your creditionals
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '0125'
# app.config['MYSQL_DATABASE_DB'] = 'convenient_recipes'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

# #begin code used for login
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)

# conn = mysql.connect()
# cursor = conn.cursor()
# cursor.execute("SELECT email from Users")
# users = cursor.fetchall()

# def getUserList():
# 	cursor = conn.cursor()
# 	cursor.execute("SELECT email from Users")
# 	return cursor.fetchall()

# class User(flask_login.UserMixin):
# 	pass

# @login_manager.user_loader
# def user_loader(email):
# 	users = getUserList()
# 	if not(email) or email not in str(users):
# 		return
# 	user = User()
# 	user.id = email
# 	return user

# @login_manager.request_loader
# def request_loader(request):
# 	users = getUserList()
# 	email = request.form.get('email')
# 	if not(email) or email not in str(users):
# 		return
# 	user = User()
# 	user.id = email
# 	cursor = mysql.connect().cursor()
# 	cursor.execute("SELECT password FROM Users WHERE email = '{0}'".format(email))
# 	data = cursor.fetchall()
# 	pwd = str(data[0][0] )
# 	user.is_authenticated = request.form['password'] == pwd
# 	return user

# '''
# A new page looks like this:
# @app.route('new_page_name')
# def new_page_function():
# 	return new_page_html
# '''

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	if flask.request.method == 'GET':
# 		return '''
# 			   <form action='login' method='POST'>
# 				<input type='text' name='email' id='email' placeholder='email'></input>
# 				<input type='password' name='password' id='password' placeholder='password'></input>
# 				<input type='submit' name='submit'></input>
# 			   </form></br>
# 		   <a href='/'>Home</a>
# 			   '''
# 	#The request method is POST (page is recieving data)
# 	email = flask.request.form['email']
# 	cursor = conn.cursor()
# 	#check if email is registered
# 	if cursor.execute("SELECT password FROM Users WHERE email = '{0}'".format(email)):
# 		data = cursor.fetchall()
# 		pwd = str(data[0][0] )
# 		if flask.request.form['password'] == pwd:
# 			user = User()
# 			user.id = email
# 			flask_login.login_user(user) #okay login in user
# 			return flask.redirect(flask.url_for('protected')) #protected is a function defined in this file

# 	#information did not match
# 	return "<a href='/login'>Try again</a>\
# 			</br><a href='/register'>or make an account</a>"

# @app.route('/logout')
# def logout():
# 	flask_login.logout_user()
# 	return render_template('hello.html', message='Logged out')

# @login_manager.unauthorized_handler
# def unauthorized_handler():
# 	return render_template('index.html')

# #you can specify specific methods (GET/POST) in function header instead of inside the functions as seen earlier
# @app.route("/register", methods=['GET'])
# def register():
# 	return render_template('register.html', supress='True')

# @app.route("/register", methods=['POST'])
# def register_user():
# 	try:
# 		email=request.form.get('email')
# 		password=request.form.get('password')
# 	except:
# 		print("couldn't find all tokens") #this prints to shell, end users will not see this (all print statements go to shell)
# 		return flask.redirect(flask.url_for('register'))
# 	cursor = conn.cursor()
# 	test =  isEmailUnique(email)
# 	if test:
# 		print(cursor.execute("INSERT INTO Users (email, password) VALUES ('{0}', '{1}')".format(email, password)))
# 		conn.commit()
# 		#log user in
# 		user = User()
# 		user.id = email
# 		flask_login.login_user(user)
# 		return render_template('hello.html', name=email, message='Account Created!')
# 	else:
# 		print("couldn't find all tokens")
# 		return flask.redirect(flask.url_for('register'))

# def getUsersPhotos(uid):
# 	cursor = conn.cursor()
# 	cursor.execute("SELECT imgdata, picture_id, caption FROM Pictures WHERE user_id = '{0}'".format(uid))
# 	return cursor.fetchall() #NOTE return a list of tuples, [(imgdata, pid, caption), ...]

def getUserIdFromEmail(email):
	cursor = conn.cursor()
	cursor.execute("SELECT user_id  FROM Users WHERE email = '{0}'".format(email))
	return cursor.fetchone()[0]

def isEmailUnique(email):
	#use this to check if a email has already been registered
	cursor = conn.cursor()
	if cursor.execute("SELECT email  FROM Users WHERE email = '{0}'".format(email)):
		#this means there are greater than zero entries with that email
		return False
	else:
		return True
#end login code

@app.route('/profile')
@flask_login.login_required
def protected():
	return render_template('hello.html', name=flask_login.current_user.id, message="Here's your profile")

#begin photo uploading code
# photos uploaded using base64 encoding so they can be directly embeded in HTML
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
@flask_login.login_required
def upload_file():
	if request.method == 'POST':
		uid = getUserIdFromEmail(flask_login.current_user.id)
		imgfile = request.files['photo']
		caption = request.form.get('caption')
		photo_data =imgfile.read()
		cursor = conn.cursor()
		cursor.execute('''INSERT INTO Pictures (imgdata, user_id, caption) VALUES (%s, %s, %s )''', (photo_data, uid, caption))
		conn.commit()
		return render_template('hello.html', name=flask_login.current_user.id, message='Photo uploaded!', photos=getUsersPhotos(uid), base64=base64)
	#The method is GET so we return a  HTML form to upload the a photo.
	else:
		return render_template('upload.html')
#end photo uploading code
>>>>>>> 7e7551df7df4192ad3a66cbbdb0e8d514f7c6a05

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '0125'
app.config['MYSQL_DATABASE_DB'] = 'convenient_recipes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# def favourite_post(request, fav_id):
#     video = get_object_or_404(Video, id=fav_id)
#     if request.method == 'POST': #Then add this video to users' favourite
#         video.

#    return render(request, 'foobar/%s' % fav_id)



url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
	"X-RapidAPI-Key": "07f5ddb891msh21c512d703b7bd5p1cb69cjsnc2ae67f8953b",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

find = "recipes/findByIngredients"
randomFind = "recipes/random"

@app.route('/recipes')
def get_recipes():
	if (str(request.args['ingridients']).strip() != ""):
		# If there is a list of ingridients -> list
		querystring = {"number":15,"ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
		response = requests.request("GET", url + find, headers=headers, params=querystring).json()
		return render_template('recipes.html', recipes=response)
	else:
		# Random recipes
		querystring = {"number":"15"}
		response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
		return render_template('recipes.html', recipes=response['recipes'])

# @app.route('/favorites')
# def get_favorites():
# 	return render_template('left.html')





# url2 = "https://dietagram.p.rapidapi.com/apiFood.php"
# headers2 = {
# 	"X-RapidAPI-Key": "2f09010caemsh388058b09814663p16e3bejsn5a3174231729",
# 	"X-RapidAPI-Host": "dietagram.p.rapidapi.com"
# }

# querystring2 = {"name":"Milk"}
# nutrition = requests.request("GET", url2, headers=headers2, params=querystring2)
# print(nutrition.text)



#default page
@app.route("/", methods=['GET'])
def hello():
	return render_template('home.html')

<<<<<<< HEAD
# @app.route("/unauthorized.html", methods=['GET'])
# def no_page():
# 	return render_template('unauth.html')
=======
@app.route("/favorites", methods=['GET', 'POST'])
def new_page_function():
	if request.method == "POST":
		rec = request.form.get("recipe")
	return render_template('left.html', fav=rec)

@app.route("/carousel.html", methods=['GET'])
def carousel():
	return render_template('carousel.html')

# @app.route("/home.html", methods=['GET'])
# def home():
# 	return render_template('home.html')
>>>>>>> 7e7551df7df4192ad3a66cbbdb0e8d514f7c6a05

if __name__ == "__main__":
	#this is invoked when in the shell  you run
	#$ python app.py
	app.run(port=5000, debug=True, threaded=True)



#begin code used for login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("SELECT email from Users")
users = cursor.fetchall()

def getUserList():
	cursor = conn.cursor()
	cursor.execute("SELECT email from Users")
	return cursor.fetchall()

class User(flask_login.UserMixin):
	pass

@login_manager.user_loader
def user_loader(email):
	users = getUserList()
	if not(email) or email not in str(users):
		return
	user = User()
	user.id = email
	return user

@login_manager.request_loader
def request_loader(request):
	users = getUserList()
	email = request.form.get('email')
	if not(email) or email not in str(users):
		return
	user = User()
	user.id = email
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT password FROM Users WHERE email = '{0}'".format(email))
	data = cursor.fetchall()
	pwd = str(data[0][0] )
	user.is_authenticated = request.form['password'] == pwd
	return user


# class Login(Form):
#     login_email = TextField('Email', [validators.Required()])
#     login_pass = PasswordField('Password', [validators.Required()])

# class Register(Form):
#     email = TextField('Email', [validators.Length(min=1, max = 12)])
#     password = PasswordField('Password', [
#         validators.Required(),
#         validators.EqualTo('confirm_password', message='Passwords do not match')
#     ])
#     confirm_password = PasswordField('Confirm Password')


@app.route('/sign_in_up.html', methods=['GET','POST'])
def sign_in_up():
	if request.method == 'GET':
		return render_template('sign_in_up.html')

	button = request.form['submit']
		
	#The request method is POST (page is recieving data)
	if button == 'Log In':
		in_email = request.form.get('loginEmail')
		print("log in", in_email)
		cursor = conn.cursor()
		#check register
		if cursor.execute("SELECT password, username FROM Users WHERE email = '{0}'".format(in_email)):
			data = cursor.fetchall()
			print("show data:", str(data))
			pwd = str(data[0][0])
			user = str(data[0][1])
			print("user in db", in_email, pwd)
			if request.form.get('loginPassword') == pwd:
				user = User()
				user.id = in_email
				flask_login.login_user(user) #okay login in user
				print("login successful")
				return flask.redirect(flask.url_for('protected')) #protected is a function defined in this file
	
	elif  button == 'Sign Up':
	# else:
		up_email = request.form.get('signupEmail')
		cursor = conn.cursor()
		print("signup")
		try:
			up_username=request.form.get('signupUsername')
			up_password=request.form.get('signupPassword')
			confirm = request.form.get('confirm')
			print("signup start", up_password)
		except:
			print("couldn't find all tokens") #this prints to shell, end users will not see this (all print statements go to shell)
			return flask.redirect(flask.url_for('sign_in_up'))
		test =  isEmailUnique(up_email)
		if test:
			if confirm != up_password:
				print("not the same")
				return flask.redirect(flask.url_for('sign_in_up'))
			print("create account")
			cursor.execute("INSERT INTO Users (username, email, password) VALUES ('{0}', '{1}', '{2}')".format(up_username, up_email, up_password))
			conn.commit()
			user = User()
			user.id = up_email
			flask_login.login_user(user)
			print("new user login")
			return flask.redirect(flask.url_for('protected'))
		else:
			message = "Account already existed! Choose another email to register."
			print("email taken")
			return flask.redirect(flask.url_for('sign_in_up', message=message))

 	#information did not match
	# print("redirect")
	return flask.redirect(flask.url_for('logout'))


@app.route('/unauth')
def logout():
	flask_login.logout_user()
	return render_template('unauth.html', message='Logged out')

@login_manager.unauthorized_handler
def unauthorized_handler():
	return render_template('unauth.html')


def isEmailUnique(email):
	#use this to check if a email has already been registered
	cursor = conn.cursor()
	if cursor.execute("SELECT email  FROM Users WHERE email = '{0}'".format(email)):
		#this means there are greater than zero entries with that email
		return False
	else:
		return True
# end login code


@app.route('/profile.html', methods=['GET'])
# @flask_login.login_required
def protected():
	print("user trying to get access")
	return render_template('profile.html', message="Here's your profile")


