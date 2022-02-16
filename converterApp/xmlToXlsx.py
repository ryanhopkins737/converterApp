import xml.etree.ElementTree as ET
from lxml import etree
import xlsxwriter




tree = ET.parse(r'C:\Users\ryan.hopkins\Desktop\testPRM0356Params_MaintenanceInfo_20220111.xml')
rootTag = tree.getroot()
print(rootTag)


allTags = set()
# Adds all distinct tag names to a set from the XML file
for x in rootTag.iter("*"):
    allTags.add(x.tag)
allTags = list(allTags)


# Creates a list with ordered tags and removes ones that are used
orderedTags = [rootTag.tag]
parent = [rootTag.tag]
master = [rootTag.tag]
next_parent = []

findingTags = True

# while findingTags:
#     print('hi')
#     for b in parent:
#         for a in allTags:
#             if b.find(a) == 0:
#                 next_parent.append(a)
#                 master.append(a)
#                 print('hihi')
#     if len(master) == len(allTags):
#         findingTags = False
#     print('bye')
#     parent = next_parent
#     next_parent = []

# for y in rootTag.itertext():
#     print(y)

for z in rootTag.iter('*'):
    print(f'{z.text}, {z.tag}')
    text = z.text
    tag = z.tag


print(f'{rootTag.itertext()}')
print(master)
print(parent)
print(next_parent)

a = rootTag.findall('ParameterValueSetList')
print(allTags)