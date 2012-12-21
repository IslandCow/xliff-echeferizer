import xml.dom as DOM

def translate(s) :
	return s + "Bork Bork Bork!"




tree = ET.parse("dt2_sv-US-zyyy.xlf")
root = tree.getroot()
print root.tag
print root.attrib

for	n in root.iter() :
	print n.tag
	if n.tag == "trans-unit":
		for neighbor in n.findall("source"):
			print neighbor.text
