function agregarElemento() {
	//Crea literalmente el elemento li de la lista
	var li = document.createElement("li");

	//Crea el nodo en el DOM con el elemento que se ingresó por el cuadro de texto
	var txt = document.getElementById('elemento').value;
	var elemento = document.createTextNode(txt);

	li.appendChild(elemento);

	document.getElementById('listaDesordenada').appendChild(li);
}