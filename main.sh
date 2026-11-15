#!/bin/bash

thedate=$1


#run main.py to set up the project
python3 main.py

#generate orders by date
python3 src/generate_orders.py $thedate