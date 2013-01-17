import xml.etree.ElementTree as ET
import cheferizer as EC 
import re

tree = ET.parse("dt2_sv-US-zyyy.xlf")
root = tree.getroot()

nm = re.search("{.*}", root.tag)
namespace = nm.group(0)

for	neighbor in root.iter(namespace + 'trans-unit') :
	e = EC.EChef()
	source = neighbor.findall(namespace + 'source')[0]
	target = neighbor.findall(namespace + 'target')[0]
	target.text = e.X(neighbor.text)

tree.write('output.xml')
