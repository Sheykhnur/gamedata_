import os
import io
import re

input = open("unique_items.ltx", "r")
output = open("list", "w")
for line in input.readlines() :
	m = re.search('(?<=\[)\w+(?=\])', line) 
	if m <> None:
		output.write(m.group(0) + ' = true\n')
output.close()	
input.close()
os.system("PAUSE")