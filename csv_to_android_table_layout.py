import csv
import sys
import os
import pdb

print """<?xml version="1.0" encoding="utf-8"?>
<TableLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:shrinkColumns="*"
    android:stretchColumns="*">"""

#extract table id prefix from csv file name
table_name = os.path.splitext(os.path.basename(sys.argv[1]))[0] 
with open(sys.argv[1], 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    rownum = 0
    for row in csvreader:
        print """
    <TableRow
        android:id="@+id/{0}_row_{1}"
        android:layout_height="wrap_content"
        android:layout_width="match_parent">""".format(table_name, rownum)
        colnum = 0
        for field in row:
            if rownum == 0:
                print """
            <TextView
                android:textStyle="bold"
                android:id="@+id/{0}_row_{1}_col_{2}"
                android:text="{3}" />""".format(table_name, rownum, colnum, field.strip())
            else:
                print """
            <TextView                
                android:id="@+id/{0}_row_{1}_col_{2}"
                android:text="{3}" />""".format(table_name, rownum, colnum, field.strip())
            colnum = colnum+1
        print """
    </TableRow>"""
        rownum = rownum+1
        
print """
</TableLayout>"""
