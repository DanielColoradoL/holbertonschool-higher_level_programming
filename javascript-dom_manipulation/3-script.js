document.getElementById('toggle_header').onclick = () => {
  const classVal = document.querySelector('header').classList;
  if (classVal.value === 'green') {
    document.querySelector('header').classList.replace('green', 'red');
  } else {
    document.querySelector('header').classList.replace('red', 'green');
  }
}