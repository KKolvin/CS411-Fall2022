######################################
# author ben lawson <balawson@bu.edu>
# Edited by: Craig Einstein <einstein@bu.edu>
######################################
# Some code adapted from
# CodeHandBook at http://codehandbook.org/python-web-application-development-using-flask-and-mysql/
# and MaxCountryMan at https://github.com/maxcountryman/flask-login/
# and Flask Offical Tutorial at  http://flask.pocoo.org/docs/0.10/patterns/fileuploads/
# see links for further understanding
###################################################

import flask
from flask import Flask, Response, request, render_template, redirect, url_for
import requests, json, unicodedata

#for image uploading
import os, base64

app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!


'''
A new page looks like this:
@app.route('new_page_name')
def new_page_function():
	return new_page_html
'''


url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "07f5ddb891msh21c512d703b7bd5p1cb69cjsnc2ae67f8953b",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

find = "recipes/findByIngredients"
randomFind = "recipes/random"
	

@app.route('/recipes')
def get_recipes():
	search_content = str(request.args['ingridients'])
	if (search_content.strip() != ""):
		# If there is a list of ingridients -> list
		querystring = {"number":5,"ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
		response = requests.request("GET", url + find, headers=headers, params=querystring).json()
		return render_template('recipes.html', recipes=response, ingredients = search_content)
	else:
		# Random recipes
		querystring = {"number":"5"}
		response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
		print(response)
		return render_template('recipes.html', recipes=response['recipes'])


#default page
@app.route("/", methods=['GET'])
def home():
	return render_template('home.html')

@app.route("/left.html", methods=['GET'])
def left_page():
	return render_template('left.html')

@app.route("/right-sidebar.html", methods=['GET'])
def right_page():
	return render_template('left.html')

@app.route("/no-sidebar.html", methods=['GET'])
def no_page():
	return render_template('left.html')

if __name__ == "__main__":
	#this is invoked when in the shell  you run
	#$ python app.py
	app.run(port=5000, debug=True, threaded=True)

