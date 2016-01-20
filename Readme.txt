This is a simple python program that will use string matching to fill in your spreadsheet. 
eg. If I have JS as my row value and IE in my column value I can tell my program to fill in whatever into those cells. 
The string matching will pull from anywhere within the cell value. So if I say look for JS and the cell contains 'AS3 Adplayer JS blah blah', I'll get a match. The only hard coded value you need to look out for in this program is it looks by default into the column second most to the left. So if your row values are in the column all the way to the left change the line 'row_is_a_js_row = row_value in row[1]' to 'row_is_a_js_row = row_value in row[0]'. This is line 30.
Instructions: (Really easy to run)
Make sure your spreadsheet is a csv
Make sure this spreadsheet is in the same directory as this python program.
Run the python program (editor.py) and it will walk you through what it does
