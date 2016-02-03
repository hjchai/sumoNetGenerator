import sys
import xml.etree.ElementTree as ET

def separateType(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()
    typeFile = open('sf_downtown.typ.xml','w')
    typeFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    typeFile.write('<types>\n')
    for type in root.findall('type'):
        id = type.get('id')
        priority = type.get('priority')
        numLanes = type.get('numLanes')
        speed = type.get('speed')
        allow = type.get('allow')
        disallow = type.get('disallow')
        oneway = type.get('oneway')
        width = type.get('width')
        typeFile.write('    <type id="' + id + '" priority="' + priority + '" numLanes="' + numLanes +'" speed="' + speed +'"')
        if allow!=None:
            typeFile.write(' allow="' + allow +'"')
        if disallow!=None:
            typeFile.write(' disallow="' + disallow + '"')
        typeFile.write(' oneway="' + oneway + '"')
        if width!=None:
            typeFile.write(' width="' + width +'"')
        typeFile.write('/>\n')
    typeFile.write('</types>')
if __name__ == '__main__':
    separateType('/home/huajun/Desktop/sf_downtown_maps/sf_downtown_bbox_no_internal_links.net.xml')
