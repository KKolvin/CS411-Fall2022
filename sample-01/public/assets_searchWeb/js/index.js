// import { createRequire } from 'module';
// const require = createRequire(import.meta.url);

const express = require('express');
const router = express.Router();
const axios = require('axios');
// const async = require('async')

/* GET home page. */
router.get('/', (req, res, next) => {
  res.render('index', { title: 'Express' })
})

const ingredients = 0

const number = 0

// async function spoonacularCall(ingredients, number) {

const options = {
    method: 'GET',
    url: 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients',
    params: {
        ingredients: ingredients,
        number: number,
    },
    headers: {
        'X-RapidAPI-Key': 'SIGN-UP-FOR-KEY',
        'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com'
    }
};

axios.request(options).then(function (response) {
    console.log(response.data);
}).catch(function (error) {
    console.error(error);
});


const optionsJokes = {
    method: 'GET',
    url: 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/jokes/random',
    headers: {
        'X-RapidAPI-Key': 'SIGN-UP-FOR-KEY',
        'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com'
    }
};

axios.request(optionsJokes).then(function (response) {
    console.log(response.data);
}).catch(function (error) {
    console.error(error);
});
// }



module.exports = router;