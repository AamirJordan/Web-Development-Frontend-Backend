let xhr = new XMLHttpRequest();

xhr.open('GET', 'http://jsonplaceholder.typicode.com/posts');

xhr.responseType = 'json';

xhr.send();


xhr.onload = function() {
  let data = xhr.response;
  console.log(data);
  let showText = document.getElementById('showText');
  for (var i = 0; i < data.length; i++) {
    var node = document.createElement("LI");
    var textnode = document.createTextNode(data[i].userId + " " + data[i].id + " " + data[i].title + " " + data[i].body);
    node.appendChild(textnode);
    showText.appendChild(node);
  }
};
