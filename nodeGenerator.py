#!/usr/bin/python

import sys, os
import xml.etree.ElementTree as ET

def generateNodeFile(junctionFile):
    tree = ET.parse(junctionFile)
    #fileDir = os.path.realpath(junctionFile)
    outFile = open('sf_downtown.nod.xml','w')
    outFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    outFile.write('<nodes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n xsi:noNamespaceSchemaLocation="http://sumo.sf.net/xsd/nodes_file.xsd">\n')
    root = tree.getroot()
    for child in root:
        id = child.get('id')
        x = child.get('x')
        y = child.get('y')
        type = child.get('type')
        outFile.write('    <node id="' + id +'" x="' + x + '" y="' + y + '" type="' + type + '"/>\n')
    outFile.write('</nodes>')

if __name__ == '__main__':
    generateNodeFile('/home/huajun/Desktop/sf_downtown_maps/junction_sf_downtown_bbox_no_internal_links.net.xml')