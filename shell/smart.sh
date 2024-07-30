#!/bin/bash

# Start a loop to iterate through possible disk drives from 'a' to 'z'
for disk in {a..z}; do

    # Formulate the path for the disk drive
    drive="/dev/sd${disk}"

    # Check if the drive exists
    if [ -e "$drive" ]; then

        # Get the current date and time in the specified format
        current_time=$(date +'%Y-%m-%d %H:%M:%S')

        # Retrieve SMART data for the drive and filter specific parameters using awk
        smartctl -a "$drive" | awk '/^  5/ || $1=="187" || $1=="188" || $1=="197" || $1=="198" {print "'"$current_time"'", "'"$drive"'", $2, $4, $5, $10}'
        echo "------------------------------------------------------------------"
    fi
done