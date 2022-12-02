import requests


# CALL FOR SEARCHING RECIPES BY INGREDIENTS
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"apples,flour,sugar","number":"2","ignorePantry":"true","ranking":"1"}

headers = {
	"X-RapidAPI-Key": "07f5ddb891msh21c512d703b7bd5p1cb69cjsnc2ae67f8953b",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print("RECIPES API CALL")

print(response.json())


# CALL FOR RANDOM FOOD JOKE
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/jokes/random"

headers = {
	"X-RapidAPI-Key": "07f5ddb891msh21c512d703b7bd5p1cb69cjsnc2ae67f8953b",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print("JOKES API CALL")

print(response.json())