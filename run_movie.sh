#!/bin/bash
pip freeze | grep 'colorama'
# python3 main2.py
echo 'Do you want to print the help file? (y/n)'
read helpfilereq
if [[ $helpfilereq == "y" ]]; 
    then
            cat helpfile.md \n
            python3 main2.py
    else
        python3 main2.py
fi