#!/bin/bash

#assign current date if no date provided
if [ $# -ne 0 ]; then
    thedate=$1
else
    thedate=$(date +%m/%d/%Y)
fi

#the folder to store the orders
folder="data/raw/orders"

if [ ! -d "$folder" ]; then
    mkdir "$folder"
fi

for i in {1..3}; do
    echo "Generating orders for $thedate..."
    python3 src/generate_orders.py "$thedate"
    thedate=$(date -j -v-1d -f "%m/%d/%Y" "$thedate" +%m/%d/%Y)
done