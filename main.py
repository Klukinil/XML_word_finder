import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

items_list2 = root.findall("channel/item/description")
print(len(items_list2))
print(items_list2)

for description in items_list2:
  print(description.text)