#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
      return response.json();
  })
  .then(data => {
    const hello = data;
    console.log(hello);
    document.getElementById('hello').textContent = hello.hello;
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
});