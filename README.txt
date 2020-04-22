Plagiarism Checker

Description: This program takes a list of files and cross-checks them for long phrase matches. In the same
             folder as this file, place several short-medium sized text passages (Nothing long like Anna Karenina).
             Then, create another text file that lists all of the other text files on new lines (See CheckList.txt).
             Once the program is run, it will ask the user for the Checklist, Matches per Report, and Words per Match.
             The algorithm will take two files and find phrase matches between them. If a phrase match is too small, 
             then it will not be reported. If there are not enough matches being reported, then the file pair will
             also not be reported.  Repeat this with every possible file pair until a table of values are revealed,
             displaying the most number of similarities and the top and the least amount of similarities at the bottom.
             
Known Error: There is a small off-by-one error when reporting the longest phrase. Every time I try to fix it, 
             another off-by-one error occurs, so this current program is the one with the least error. It still
             shouldn't be too much of an issue. 
