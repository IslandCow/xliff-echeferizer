import xml.etree.ElementTree as ET
import cheferizer as EC 
import re

tree = ET.parse("dt2_sv-US-zyyy.xlf")
root = tree.getroot()

nm = re.search("{.*}", root.tag)
namespace = nm.group(0)

for	neighbor in root.iter(namespace + 'source') :
	e = EC.EChef()
	print e.X(neighbor.text)
