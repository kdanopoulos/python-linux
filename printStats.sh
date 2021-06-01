#! /usr/bin/bash

args=("$@")


for obj in ${args[@]} 
do
	max=$(( -999999,01 ))
    min=$(( 999999,01 ))
    i=1
    filename=$obj
    while read line
    do
    	curNum=$line
        if (( $(echo "$max < $curNum" |bc -l) ))
        then
            max=$curNum
        fi
        if (( $(echo "$min > $curNum" |bc -l) ))
        then
            min=$curNum
        fi
    i=$((i+1))    
    done < $filename
    echo FILE: $filename, lines: $i, max=$max, min=$min



    
done