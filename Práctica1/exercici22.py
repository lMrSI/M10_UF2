import xml.etree.ElementTree as ET 

def exercici22():
    p = ET.Element('students')
    c = ET.SubElement(p, 'student')
    e = ET.SubElement(c, 'name', 'surname', 'email', 'dni')
    tree = ET.ElementTree(p)
    tree.write("archivo.xml")

    return ET.dump(p)

print(exercici22)
