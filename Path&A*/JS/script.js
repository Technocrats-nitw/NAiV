

var arr = document.getElementsByTagName("p");

var p = document.createElement("p");
var node = document.createTextNode("Some text node is here");
p.appendChild(node);

var div = document.getElementbyId("demo");
//adding paragraph to the div
div.appendChild(p);

document.write(div);