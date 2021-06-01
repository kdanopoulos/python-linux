#! /usr/bin/bash

args=("$@")

sum=$(( -999999 ))
col=$(( -1 ))
file=test



for obj in ${args[@]} 
do
    filename=$obj
    i=1
    while read line
    do
        num1=$( echo "$line" | cut -d':' -f1 )
        num2=$( echo "$line" | cut -d':' -f2 )
        if (( $sum < $num1 + $num2 ))
        then
            sum=$(( num1 + num2 ))
            col=$((i))
            file=$filename
        fi
        i=$(( i + 1 ))
    done < $filename

    
done

echo FILE: $file, COLUMN: $col, sum=$sum