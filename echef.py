import xml.etree.ElementTree as ET
import cheferizer as EC 
import re
import sys
import os

ET.register_namespace('', "urn:oasis:names:tc:xliff:document:1.2")

if len(sys.argv) != 2:
	sys.exit("Please provide the name of the file")

fileName = sys.argv[1]
tree = ET.parse(fileName)
root = tree.getroot()

nm = re.search("{.*}", root.tag)
namespace = nm.group(0)

for	neighbor in root.iter(namespace + 'trans-unit') :
	e = EC.EChef()
	source = neighbor.findall(namespace + 'source')[0]
	target = neighbor.findall(namespace + 'target')[0]
	neighbor.set("approved", "yes")
	neighbor.remove(target)
	target.text = e.parse(source.text)
	neighbor.append(target)

fName = os.path.splitext(fileName)[0]

tree.write(fName + "TR" + '.xlf')
