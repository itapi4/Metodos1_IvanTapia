#!/bim/bash
if [ -d data ]; then
	echo Ya existe la carpeta data
	echo Desea borrarla [Y/N]
	read conditional
	if [ "$conditional" = "Y" ]; then
		rm -r data
		echo Se ha borrado exitosamente la carpeta data
	else
		echo Seleciono NO o una opcion no valida
	fi
else
	mkdir data
	echo Se ha creado la carpeta data
fi
