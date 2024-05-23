document.getElementById('add_item').onclick = () => {
  const ul = document.getElementsByClassName('my_list')[0];
  const li = document.createElement('li');
  li.appendChild(document.createTextNode("Item"));
  ul.appendChild(li);
}
