#!/bin/bash
function help(){
	echo Debe incluir tres parametros: Posicion Inicial, Velocidad y tiempo total
}
if ! [ $# -eq 3 ]; then
	help
	exit 1
else
	echo Corriendo Programa
fi
