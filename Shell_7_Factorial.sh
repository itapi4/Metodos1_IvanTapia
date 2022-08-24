#!/bim/bash
function factorial(){
	res=1
	for ((i=1;i<=$n;i++))
	do
        	let res=$res*$i
	done
	echo El factorial de $n es $res
}
for ((aumento=0;aumento<=20;aumento++)) 
do
  n=$aumento
  factorial
done 
