var jugador1 = prompt("Ingresa tu nombre jugador 1");
var jugador2 = prompt("Ingresa tu nombre jugador 2");

var opcion1 = prompt("¿Piedra, papel o tijeras " + jugador1 + "?");
opcion1 = opcion1.toLowerCase();
var opcion2 = prompt("¿Piedra, papel o tijeras " + jugador2 + "?");
opcion2 = opcion2.toLowerCase();

if (opcion1 == opcion2) {
	alert(jugador1 + " y " + jugador2 + " han EMPATADO");
} else if (opcion1 == "piedra" && opcion2 == "tijeras") {
	alert(jugador1 + " ha GANADO");
} else if (opcion1 == "tijeras" && opcion2 == "papel") {
	alert(jugador1 + " ha GANADO");
} else if (opcion1 == "papel" && opcion2 == "piedra") {
	alert(jugador1 + " ha GANADO");
} else if (opcion2 == "piedra" && opcion1 == "tijeras") {
	alert(jugador2 + " ha GANADO");
} else if (opcion2 == "tijeras" && opcion1 == "papel") {
	alert(jugador2 + " ha GANADO");
} else if (opcion2 == "papel" && opcion1 == "piedra") {
	alert(jugador2 + " ha GANADO");
} else {
	alert("Opción inválida!!!");
}