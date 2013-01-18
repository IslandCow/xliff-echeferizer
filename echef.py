import xml.etree.ElementTree as ET
import cheferizer as EC 
import re

ET.register_namespace('', "urn:oasis:names:tc:xliff:document:1.2")

tree = ET.parse("sample_sv-US-zyyy.xlf")
root = tree.getroot()

nm = re.search("{.*}", root.tag)
namespace = nm.group(0)

for	neighbor in root.iter(namespace + 'trans-unit') :
	e = EC.EChef()
	source = neighbor.findall(namespace + 'source')[0]
	target = neighbor.findall(namespace + 'target')[0]
	neighbor.remove(target)
	target.text = e.parse(source.text)
	neighbor.append(target)

tree.write('output.xml')
