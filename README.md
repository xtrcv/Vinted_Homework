# Simplified MapReduce Framework in Python

This framework tries to follow 'MapReduce' logic as close as possible, with the exception of splitting the initial files and processing them in parallel.

## Prerequisites
Anaconda package and its' dependencies. Scripts were written using VSCodium and were tested on Linux Debian, and should work on any system. To install it on your system, follow the instructions as described here: https://docs.anaconda.com/anaconda/install/index.html

## Task #1
To get results needed for the first task, place the 'map_reduce_task1.py' script in the directory where your CSV file is located, and then change the 'FILE_NAME' in 'data = pd.read_csv("FILE_NAME.csv")' to count how many clicks there were for each date and write the results into a TXT file in the current dirrectory (where you've placed your script).

## Task #2
Scripts used to get the results needed for Task #2 are a bit 'rough around the edges', thus, you will have to run three of them. 

First, run the 'map_reduce_task2.py' to create the 'LT_IDs.txt' file that contains all the Lithuanian ID numbers. IDs are pulled from 'directory = '/home/unserun/Desktop/Vinted Homework/data/users', make sure to specify the right full path to the 'data/users' directory.

Second, run the 'map_reduce_task2.2.py' to create the 'output.txt' file that contains two columns, the date when a particular click was done, and the Lithuanian ID number that did that click on that date. Again, check the full paths of the directories specified in the script so that it iterates over the correct files.

And finally, run the 'map_reduce_task2.3.py' script to create the 'final_results.txt' file that should contain a column of rows that look like this '2017-12-20:1:3'. Here, '2017-12-20' is the date when the click was done, '1' is the Lithuanian ID that did it, and '3' is the number of times that the ID clicked on that date.

## Comments
Unfortunately I forgot to include 'click_target' in the final dataset of the Task #2, but it can pretty easily included later. 

I have to admit that I've spent a lot of time on these tasks and haven't looked into using parallel processing, and although I understand that it's an optional task, I wish I had more time to do it as I believe it's the whole point of MapReduce. 

## FAQ

Q: I have issues executing the code after installing Anaconda.

A: It might be because another Python package already exists on your system. Uninstalling the Python package that you had in your system using 'pip uninstall [package_name]' might help.
