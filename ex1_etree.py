def extraire_td(filename):
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    for item in root.findall(".//item"):
        title = item.find("title").text
        description = item.find("description").text
        yield title, description
        
import sys
filename = sys.argv[1]
for t, d in extraire_td(filename):
    print(t, d)
