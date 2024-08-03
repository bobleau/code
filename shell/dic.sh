#!/bin/bash

# 生成查找表字典

apt install crunch -y

sleep 10
crunch 10 10 -t TK00%%%%%% -o TK.txt

while read -r line
do
    md5=$(echo -n "$line" | md5sum | cut -b 9-24)
    tk="$line"
    echo "${tk} ${md5}" >> key
done < TK.txt

sleep 10
rm TK.txt

