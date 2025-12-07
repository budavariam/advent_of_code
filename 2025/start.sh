#!/bin/bash
# $1: shall be the name of the folder to use like: 01_1

if [[ -z "$1" ]]; then 
    usedir=$(find . -maxdepth 1 -iname '[[:digit:]]*' | sort | tail -1)
else
    usedir="./$1"
fi
echo "Start from '${usedir}' ..."
.ve/bin/python3 "${usedir}/solution.py"