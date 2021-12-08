import csv
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw()

fn = askopenfilename()
print(fn)
fnwrite = fn.split('/')[-1]
print(fnwrite)
fnwrite = fn[:-1*len(fnwrite)]+'READABLE-'+fnwrite.split('.')[0]+'.csv'
print(fnwrite)

#writefile csv configs
writefile = open(fnwrite,'w', encoding = 'cp850',newline='')
writer = csv.writer(writefile)

#readfile configs
readfile = open(fn, 'r',encoding = 'cp850')
Lines = readfile.readlines()
readfile.close()

for line in Lines:

    splitline = line.split("\t")
    count = 0
    for value in splitline:
        splitvalue = value.split(',')
        if len(splitvalue) > 1:
            splitline[count] = splitvalue[0]+'.'+splitvalue[1]
        count += 1

    writer.writerow(splitline)

writefile.close()
