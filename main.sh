#!/bin/bash

#assign current date if no date provided
if [ $# -ne 0 ]; then
    thedate=$1
else
    thedate=$(date +%m/%d/%Y)
fi


#run main.py to set up the project
python3 main.py

#generate orders by date
python3 src/generate_orders.py $thedate