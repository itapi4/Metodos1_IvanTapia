#!/bin/bash
pass=0
function checkvalue(){
	if [ $parametro -eq 0 ] || [ $parametro -eq 1 ]; then
		pass=1
	else
		echo intente de nuevo
	fi
}
echo "digite un parametro"
while ! [ $pass -eq 1 ]; do
	read parametro
	checkvalue
done
