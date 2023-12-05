import os, io, sys
import xml.etree.ElementTree as etree

tree = etree.parse(sys.argv[1])
root = tree.getroot()

def edit_attrib(child, name, op, adj):
	try:
		val = int(child.attrib[name])
		if op == '+':
			child.attrib[name] = str(val + adj)
		elif op == '*':
			child.attrib[name] = str(int(val * adj))
	except KeyError:
		pass

for child in root:
	#edit_attrib(child, 'x', '+', 15)
	edit_attrib(child, 'x', '+', 15)
	edit_attrib(child, 'x', '*', 1.25)
	edit_attrib(child, 'width', '*', 1.25)

tree.write(sys.argv[1])
