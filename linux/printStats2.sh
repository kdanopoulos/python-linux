#! /usr/bin/bash

args=("$@")

numFile=0

for obj in ${args[@]} 
do
	curMax=$(( -999999,01 ))
    curMin=$(( 999999,01 ))
    lines[numFile]=-1
    i=1
    filename[numFile]=$obj
    while read line
    do
    	curNum=$line
        if (( $(echo "$curMax < $curNum" |bc -l) ))
        then
            curMax=$curNum
        fi
        if (( $(echo "$curMin > $curNum" |bc -l) ))
        then
            curMin=$curNum
        fi
    i=$((i+1))    
    done < ${filename[numFile]}
    lines[numFile]=$i
    max[numFile]=$curMax
    min[numFile]=$curMin
    fileName[numFile]=$filename
    numFile=$((numFile+1))



    
    
done

for ((i=0;i<numFile;i++))
do
    echo FILE: ${filename[i]}, lines: ${lines[$i]}, max=${max[$i]}, min=${min[$i]}
done

