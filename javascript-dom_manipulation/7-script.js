#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const movies = data.results;
      const ul = document.getElementById('list_movies');
      for (let movie of movies) {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(movie.title));
        ul.appendChild(li);
        console.log(movie.title);
      }
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
});
