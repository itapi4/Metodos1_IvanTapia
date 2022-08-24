#!/bin/bash
function factorial(){
	local res=1
	for ((i=1;i<=factor;i++))
	do
        	let res=$res*$i
	done
	fact=$res
}
factor=20
factorial
numefact=$fact
factor=17
factorial
denofact=$fact
let division=$numefact/$denofact
echo $division
