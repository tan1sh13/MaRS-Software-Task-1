#!/bin/bash

#1)Create directory and navigate
mkdir -p  rover_mission
cd rover_mission

#2)Create empty files
touch log1.txt log2.txt log3.txt

#3)Rename file
mv log1.txt mission_log.txt

#4)Find all .log files
echo Files with .log extension:
find . -type f -name "*.log"

#5)Display Contents
echo Contents of mission_log.txt:
cat mission_log.txt

#6)Find lines with error
echo Lines with errors:
grep ERROR mission_log.txt

#7)Count number of lines
echo Number of lines:
wc -l  mission_log.txt

#8)Current date and time
echo Current date and time
date

#9)CPU usage
echo CPU usage
top

#10)Schedule Shutdown
echo Shutdown in 10 minutes
shutdown +10

