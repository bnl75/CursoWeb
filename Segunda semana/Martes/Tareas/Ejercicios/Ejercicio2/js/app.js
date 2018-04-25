function cambiaEstilo() {
	var cadena = document.getElementById('letras');

	document.getElementById("estilo").innerHTML = cadena.value;

	var color = prompt("Color en inglés")

	document.getElementById("estilo").style.color = color;

}