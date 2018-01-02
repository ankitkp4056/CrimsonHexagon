# CrimsonHexagon
Code to retrieve posts from a Crimson Hexagon monitor(for a specified period of time)

## Introduction

This module allows you to pull post data from a Crimson Hexagon monitor by specifying the "monitor_id", "start_date" and "end_date".

`\monitor_id\` = 10-digit unique ID corresponding to the Crimson Hexagon Monitor (also present in the URL of Monitor page).

`\start_date\` = the date from which monitoring starts(inclusive).

`\end_date\` = the date befor which monitoring stops(exclusive).

It uses the POST endpoint of the MONITOR API of Crimson Hexagon.


## TO RUN:

`\ python CH_script.py --monitor_id=1234567890 \`

The end_date and start_date need to be speciofied in CH_script.py 

