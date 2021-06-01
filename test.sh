#! /usr/bin/bash

args=("$@")

curOb=$(( 1 ))
maxOb=$(( 2 ))
num=$2
for obj in ${args[@]} 
do
	if (( $(echo "$curOb <= $maxOb" |bc -l) ))
    	then
    		
    fi
    curOb=$((curOb+1))





	zero=$(( 0 ))
	i=$(( 1 ))
    filename=$obj
    while read line
    do
    	city=$( echo "$line" | cut -d':' -f1 )
    	num1=$( echo "$line" | cut -d':' -f2 | cut -d'!' -f1 )
        num2=$( echo "$line" | cut -d':' -f2 | cut -d'!' -f2 )

        if (( $(echo "$num1 >= $zero" |bc -l) ))
        then
            if (( $(echo "$num2 >= $zero" |bc -l) ))
        	then
            	echo $line
        	fi
        fi
    i=$((i+1))  
    done < $filename



    
done


