#!/bin/bash

#Generate random battery percentage btw (0-100)
battery=$((RANDOM % 101))

echo "Battery Level:$battery%"

#Check Battery Condition
if [ $battery -lt 20  ]
then
	echo "Battery low! Return to base!"
	exit 1
fi

#Check network Connectivity using ping
ping -c 1 google.com > /dev/null 2>&1

#Check if ping failed
if [ $? -ne 0 ]
then
 	echo "Communication failure!"
	exit 1
fi

#If all checks pass
echo "All systems operational!!!"
