#!/usr/bin/python
#author Tommy Erickson
import csv
from StringIO import StringIO
import re
import sys
from subprocess import call 
import os
import shutil

def cutter(open_csv): #this function is called to cut out a blank row starting the csv
    with open(open_csv,'rb') as fh: 
        with open("updated_test.csv",'w') as f1:
            fh.next()
            for line in fh:
                f1.write(line)
        os.rename("updated_test.csv",open_csv)
        return open_csv

def first_file(open_csv):
    with open(open_csv,'rb') as fh: 
        reader = csv.reader(fh)
        header = next(reader)
        new_file = [] #creates a new file to be written to
        row_value = raw_input('what is the row value you want to look for? Caps matter \n')
        column_value = raw_input('what is the column_value you want to look for? Caps matter \n')
        ie_columns = [i for i, c in enumerate(header) if column_value in c]
        #cell_value = raw_input('what text would you like to put in the cells? \n')
        for row in reader:
        	row_is_a_js_row = row_value in row[1] #this is the only hard coded value in the program that would need to be changed depending on the csv, I may try to add it in such a way that it asks where your value is
        	#new_row = map(lambda (i, c): 'n/a' if i in ie_columns else c, enumerate(row))
         	new_row = []
         	for column_index, cell in enumerate(row):
         		if (column_index in ie_columns and row_is_a_js_row):
         			new_row.append('N/A')
         		else:
         		    new_row.append(cell)
                new_file.append(tuple(new_row))
                orig_stdout = sys.stdout 
        f = file(output_file, 'w')
        sys.stdout = f
        print ",".join(header)
        for row in new_file:
        	print ",".join(row)
        sys.stdout = orig_stdout
        f.close()
        os.rename (output_file, open_csv)
        global start_over
        start_over = raw_input('are there more cells you would like to fill in? Type out yes fully otherwise just hit enter \n')
        if (start_over != 'yes'):
            os.rename(open_csv,output_file)
            return

def main():
    open_csv = raw_input('whats your filename? No need to include the extension, but make sure its a csv file \n') + '.csv'
    shutil.copyfile(open_csv,'whatever.csv')
    cut_out = raw_input('Do you have a blank first line you would like to cut out? Type out yes fully if you do \n')
    if (cut_out == 'yes'):
        cutter(open_csv) # ignore first line of csv
    global output_file
    output_file = raw_input('what would you like the new spreadsheet to be called? You dont need to put the extension on \n') + '.csv' 
    while True: #this loop is to let you edit the sheet repeatedly until you have filled out all the cells you wanted 
        first_file(open_csv)
        if (start_over != 'yes'):
            break #exits the function and the program giving you a newly edited csv!
    os.rename('whatever.csv',open_csv)
main()

