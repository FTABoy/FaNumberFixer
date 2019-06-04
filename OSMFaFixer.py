#!/usr/bin/python
# -*- coding: utf-8 -*-
# Converting some Arabic (Ya, Ka) characters , English digits [1234567890] and also Arabic digits [٤٥٦] into their equivalents in Perisan encoding [۴۵۶].

import re,fileinput,sys,os
import xml.etree.ElementTree as ET
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/modules")
import persian

print("* Loading File")
tree = ET.parse('input.osm')		#Source input file name
root = tree.getroot()
print("* File loaded, Fixing.")

counter = 0
issuecounter = 0
ar_characters = 0
ar_numbers = 0
en_numbers = 0
for node in root.findall('node'):
	for tag in node.findall('tag'):
		k = tag.attrib['k']
		if k=='name':
			name = tag.attrib['v']
			temp = tag.attrib['v']
			v_fixed=persian.convert_ar_characters(name)
			if temp != v_fixed:
				ar_characters = ar_characters+1
				issuecounter = issuecounter+1
				temp = v_fixed
			v_fixed=persian.convert_ar_numbers(v_fixed)
			if temp != v_fixed:
				ar_numbers = ar_numbers+1
				issuecounter = issuecounter+1
				temp = v_fixed
			v_fixed=persian.convert_en_numbers(v_fixed)
			if temp != v_fixed:
				en_numbers = en_numbers+1
				issuecounter = issuecounter+1
				temp = v_fixed
			if v_fixed != name:
				counter=counter+1
				tag.attrib['v'] = v_fixed
				node.set('action', 'modify')
print ("    "+str(counter) + " node With "+str(issuecounter)+" Issue Fixed. \n\t("+str(ar_characters)+" Arabic Chars - "+str(ar_numbers)+" Arabic Numbers - "+str(en_numbers)+" English Numbers)")



counter = 0
issuecounter = 0
ar_characters = 0
ar_numbers = 0
en_numbers = 0
for way in root.findall('way'):
	for tag in way.findall('tag'):
		k = tag.attrib['k']
		if k=='name':
			name = tag.attrib['v']
			temp = tag.attrib['v']
			v_fixed=persian.convert_ar_characters(name)
			if temp != v_fixed:
				ar_characters = ar_characters+1
				issuecounter = issuecounter+1
				temp = v_fixed
			v_fixed=persian.convert_ar_numbers(v_fixed)
			if temp != v_fixed:
				ar_numbers = ar_numbers+1
				issuecounter = issuecounter+1
				temp = v_fixed
			v_fixed=persian.convert_en_numbers(v_fixed)
			if temp != v_fixed:
				en_numbers = en_numbers+1
				issuecounter = issuecounter+1
				temp = v_fixed
			if v_fixed != name:
				counter=counter+1
				tag.attrib['v'] = v_fixed
				way.set('action', 'modify')
print ("    "+str(counter) + " way With "+str(issuecounter)+" Issue Fixed. \n\t("+str(ar_characters)+" Arabic Chars - "+str(ar_numbers)+" Arabic Numbers - "+str(en_numbers)+" English Numbers)")



counter = 0
issuecounter = 0
ar_characters = 0
ar_numbers = 0
en_numbers = 0
for relation in root.findall('relation'):
	for tag in relation.findall('tag'):
		k = tag.attrib['k']
		if k=='name':
			name = tag.attrib['v']
			temp = tag.attrib['v']
			v_fixed=persian.convert_ar_characters(name)
			if temp != v_fixed:
				ar_characters = ar_characters+1
				issuecounter = issuecounter+1
				temp = v_fixed
			v_fixed=persian.convert_ar_numbers(v_fixed)
			if temp != v_fixed:
				ar_numbers = ar_numbers+1
				issuecounter = issuecounter+1
				temp = v_fixed
			v_fixed=persian.convert_en_numbers(v_fixed)
			if temp != v_fixed:
				en_numbers = en_numbers+1
				issuecounter = issuecounter+1
				temp = v_fixed
			if v_fixed != name:
				counter=counter+1
				tag.attrib['v'] = v_fixed
				relation.set('action', 'modify')
print ("    "+str(counter) + " Relation With "+str(issuecounter)+" Issue Fixed. \n\t("+str(ar_characters)+" Arabic Chars - "+str(ar_numbers)+" Arabic Numbers - "+str(en_numbers)+" English Numbers)")

print ("")
print ("* Writing to output file")
tree.write('output.osm',encoding="UTF-8")
print ("* Done.")








# [out:xml][timeout:90];
# {{geocodeArea:iran}}->.searchArea;
# (
  # node["name"!~"[a-z]+"]["name"!~"[A-Z]+"]["name"]["name:fa"](area.searchArea);
  # way["name"!~"[a-z]+"]["name"!~"[A-Z]+"]["name"]["name:fa"](area.searchArea);
  # relation["name"!~"[a-z]+"]["name"!~"[A-Z]+"]["name"]["name:fa"](area.searchArea);
  # node["name"!~"[a-z]+"]["name"!~"[A-Z]+"]["name"~"[0-9]+|ي|ك"](area.searchArea);
  # way["name"!~"[a-z]+"]["name"!~"[A-Z]+"]["name"~"[0-9]+|ي|ك"](area.searchArea);
  # relation["name"!~"[a-z]+"]["name"!~"[A-Z]+"]["name"~"[0-9]+|ي|ك"](area.searchArea);
 # );
# (._;>;);
# out meta;




