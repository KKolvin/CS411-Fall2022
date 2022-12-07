from flask import Flask, request, render_template
import requests, json, unicodedata

app = Flask(__name__)

# CALL FOR SEARCHING RECIPES BY INGREDIENTS
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

find = "recipes/findByIngredients"
randomFind = "recipes/random"

headers = {
	"X-RapidAPI-Key": "hidden",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

@app.route('/recipes')
def get_recipes():
	
	if (str(request.args['ingridients']).strip() != ""):
		# If there is a list of ingridients -> list
		querystring = {"number":5,"ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
		response = requests.request("GET", url + find, headers=headers, params=querystring).json()
		return render_template('recipes.html', recipes=response)
	else:
		# Random recipes
		querystring = {"number":"5"}
		response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
		print(response)
		return render_template('recipes.html', recipes=response['recipes'])

def get_joke():
	# CALL FOR RANDOM FOOD JOKE
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/jokes/random"

	headers = {
		"X-RapidAPI-Key": "hidden",
		"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers).json()
	print(response)

	return render_template('recipes.html', jokes=response)

if __name__ == '__main__':
  app.run()