#!/bin/bsh
res=1
for ((i=1;i<=$1;i++))
do
	let res=$res*$i
done
echo El factorial de $1 es $res

