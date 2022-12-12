import flask
from flask import Flask, Response, request, render_template, redirect, url_for
import requests, json, unicodedata
from flaskext.mysql import MySQL
import flask_login
from wtforms import Form, validators, TextField, PasswordField
import hashlib

#for image uploading
import os, base64

app = Flask(__name__)


'''
A new page looks like this:
@app.route('new_page_name')
def new_page_function():
	return new_page_html
'''


url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
	"X-RapidAPI-Key": "hidden",
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


#default page
@app.route("/", methods=['GET'])
def hello():
	return render_template('home.html')

@app.route("/left.html", methods=['GET'])
def left_page():
	return render_template('left.html')


@app.route("/no-sidebar.html", methods=['GET'])
def no_page():
	return render_template('left.html')

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


