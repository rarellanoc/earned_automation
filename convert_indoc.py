import os, sys
import glob
import codecs

filenames = glob.glob('data_indoc/*.txt')

print " str_data = ["
for fn in filenames:
    with codecs.open(fn,'r','utf-8') as f:
        read_data = f.read()
	read_data = read_data.replace('\n','</br>').replace('#',' ').replace('*','')        

	try:
		print("{ mail: \""+read_data+ " \"}").encode('latin-1') 
	except:
		print("{ mail: \""+read_data+ " \"}").encode('utf-8')    
	print ","
print "]"
