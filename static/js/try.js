const countEl = document.getElementById('count');

callApi();

function callApi() {
    fetch('https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients')
        .then(res => res.json())
        .then(res => {
            // countEl.innerHTML = res.value;
            console.log = res.value;
        })
}