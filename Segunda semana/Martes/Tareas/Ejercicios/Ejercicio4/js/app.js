function agregarElemento() {
	//Arreglo de la lista
	var lista = document.getElementById('listaDesordenada');

	//Crea literalmente el elemento li de la lista
	var li = document.createElement("li");

	//Crea el nodo en el DOM con el elemento que se ingresó por el cuadro de texto
	var texto = document.getElementById('agregar').value;
	var elemento = document.createTextNode(texto);

	li.appendChild(elemento);

	lista.appendChild(li);
}


function actualizarElemento() {
	//Arreglo de la lista
	var lista = document.getElementById('listaDesordenada');

	var indice = document.getElementById('actualizar').value;
	var nuevo = document.getElementById('actualizado').value;
	var nodo = document.createTextNode(nuevo);
	var li = document.createElement("li");

	//Se le asigna el nuevo elemento
	li.appendChild(nodo);

	//Agrega el nuevo elemento en la misma posición del elemento viejo
	lista.replaceChild(li, lista.childNodes[indice]);
}


function eliminarElemento() {
	//Arreglo de la lista
	var lista = document.getElementById('listaDesordenada');

	//Se asigna el índice a borrar en el arreglo
	var indice = document.getElementById('eliminar').value;

	//Se borra el elemento de la lista
	lista.removeChild(lista.childNodes[indice]);
}

