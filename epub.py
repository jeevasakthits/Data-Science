#!/usr/bin/env python
##############################################################################
# File:            epub.py
# Description:     Converts ascii text with basic markup into epub file
# Authors:         Matt Poepping <matt.poepping@gmail.com>
# Date:            2008-09-11
# Copyright:       (c) 2008 Matt Poepping
#
# The contents of this file are subject to the GNU Public License
# Version 2.1 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.gnu.org/licenses/gpl.txt
#
# Software distributed under the License is distributed on an "AS IS"
# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
# License for the specific language governing rights and limitations
# under the License.
##############################################################################/

import sys
import os
import os.path
import shutil
import re
import urllib

# if not enough arguments are given, print the usage.
if not len(sys.argv) == 3:
	print """
./epub.py textfilein.txt outfilename
"""
	sys.exit(0)

sections = []
buffer = ""
currentSection = ""
p = "0"
title = "None"
author = "None"

fileIn = sys.argv[1]
fileOut = sys.argv[2]

# Style sheet to use (todo allow people to pass in their own)
myStyle = """
@page {margin-top: 0.8em;
       margin-bottom: 0.8em;}

body {margin-left: 1em;
      margin-right: 1em;
      padding: 0;}
      
h2 {padding-top:0;
    display:block;}
    
p {margin-top: 0.0em;
   margin-bottom: 0.0em;
   text-indent: 1.0em;}
   
h2 span {height:60px;
         border:1px solid #000;
         display:block;
         margin-bottom:20px;}
	 
span b {float:left;
        font-weight: normal;
        margin-top:38px;
        margin-left: -8px;
        margin-bottom: 0px;
        background-color:#FFF;
        padding-right: 16px;
        padding-left: 5px ;
        padding-bottom: 0px;
        padding-top: 0px;
        font-size:26px;}
	
span em {font-style:normal;
         font-weight: normal;
         text-transform:uppercase;
         font-size:94px;
         margin-right:18px;
         margin-top:-21px;
         margin-bottom: -20px;
         background-color:#FFF;
         float:left;
         padding:0px}
	 
div.body {}

div.book {padding-top: 6.0em;
          page-break-before: right;}
div.chapter {padding-top: 3.0em;}

div.part {padding-top: 3.0em;}

div.sectionx {padding-top: 3.0em;}

div.verse {padding: 1.0em;}

div.verseline {font-style: italic;
               margin-left: 1.0em;
               text-indent: -1.0em;}
	       
h1 {text-align: center;}
"""


# setup all the file directories and default files
if os.path.exists(fileOut):
    shutil.rmtree(fileOut)

os.mkdir(fileOut)
os.mkdir(fileOut + '/META-INF')
os.mkdir(fileOut + '/OEBPS')
os.mkdir(fileOut + '/OEBPS/css')
os.mkdir(fileOut + '/OEBPS/img')

open(fileOut + "/OEBPS/css/main.css", "w").write(myStyle)
open(fileOut + "/mimetype", "w").write("application/epub+zip")

containerXml="""<?xml version="1.0" ?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles>
<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml" />
</rootfiles>
</container>
"""

open(fileOut + "/META-INF/container.xml","w").write(containerXml)


# parse the incoming text document into chapters/sections
for line in open(fileIn).read().split('\n'):
    line = line.strip()

    # process any special characters in the lines Special chars can not span lines
    # process images (only one per line :) )
    if line.find("__img[") > 0:
	    imageName = re.sub(".*__img\[(.[^\]]*)\].*","\\1",line).strip()

	    # handle image with absolute path
	    if imageName[0] == "/":
		    shutil.copy(imageName, fileOut + "/OEBPS/img/")
		    baseName = os.path.basename(imageName)

	    # handle image with relative path
	    if imageName[0:2] == "./":
		    shutil.copy(imageName, fileOut + "/OEBPS/img/")
		    baseName = os.path.basename(imageName)

	    # handle image with web path (download it) (behind proxy? set http_proxy var
	    if imageName[0:4] == "http":
		    baseName = re.sub(".*/(.*\..*)$", "\\1", imageName)
		    open(fileOut + "/OEBPS/img/" + baseName, "w").write(urllib.urlopen(imageName).read())
		    
	    line = re.sub("__img\[.*\]", "<img src=\"img/%s\" />" % baseName , line)
		    
	    
    # if this is a chapter section/start
    if line[0:2] == "__":
        # this is the first chapter
        if currentSection == "":
            currentSection = line[2:]
        else:
            # we have made it to a new section, so write the last section with the
            # last section name, then clear the buffer and start reading some more.
            if p == "1":
                buffer = buffer + "</p>"
            buffer = re.sub("<p></p>","",buffer)
            sections.append( [currentSection, "<h1>" + currentSection + "</h1>" + buffer] )
            currentSection = line[2:]
            buffer = ""
            p = "0"
    elif line[0:6] == "_title":
        title = line[7:]
    elif line[0:7] == "_author":
        author = line[8:]
        
    # if we see a blank line then we should start or end a paragraph
    elif not line:
        if p == "1":
            buffer = buffer + "</p>"
            p = "0"
        if  p == "0":
            buffer = buffer + "<p>"
            p = "1"
        
    else:
        #line = re.sub("\r", "<br />\n", line)
        #line = re.sub("\n", "<br />\n", line)
        line = re.sub("&","&amp;", line)
        buffer = buffer + line + "\n"

# we are at the end of the book, so write that last section out.
if p == "1":
    buffer = buffer + "</p>"
buffer = re.sub("<p></p>","",buffer)
sections.append( [currentSection, buffer] )


# write the TOC and the data files
count = 0
opf1='<opf:item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>'
opf2=""

tocOut="""<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE ncx PUBLIC
"-//NISO//DTD ncx 2005-1//EN"
"http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">

<ncx version="2005-1"
xml:lang="en"
xmlns="http://www.daisy.org/z3986/2005/ncx/">

<head>
<meta name="dtb:uid" content="b0f76506-7763-11dd-83b7-001cc05a7670"/>
<meta name="dtb:depth" content="1"/>
<meta name="dtb:totalPageCount" content="0"/>
<meta name="dtb:maxPageNumber" content="0"/>
</head>
                                  
<docTitle>
<text>%s</text>
</docTitle>
<navMap>
""" % title

contentHeader="""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC
"-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">

<head>
<title>%s</title>
<link rel="stylesheet" href="css/main.css" type="text/css" />
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
</head>

<body>""" % title 



# for each section create an entry in the TOC for it, and then write it to disk
for section in sections:
    tocOut = tocOut + """
    <navPoint id="part%d" playOrder="%d">
    <navLabel>
    <text>%s</text>
    </navLabel>
    <content src="part%d.xml"/>
    </navPoint>
    """ % (count, count, section[0].strip() , count)

    # create some xml indexing
    opf1 = opf1 + "<opf:item id=\"part%d\" href=\"part%d.xml\" media-type=\"application/xhtml+xml\"/>\n" % (count, count)
    opf2 = opf2 + "<opf:itemref idref=\"part%d\"/>\n" % (count)

    # this is where we create a file for each section
    # Every page uses css/main.css for its style sheet
    open(str(fileOut) + "/OEBPS/part" + str(count) + ".xml", "w").write( contentHeader + "" + section[1] + "\n</body>\n</html>")
    count = count + 1

tocOut = tocOut + "</navMap></ncx>"

open(str(fileOut) + "/OEBPS/toc.ncx", "w").write(tocOut)

open(str(fileOut) + "/OEBPS/content.opf","w").write("""<?xml version="1.0" encoding="UTF-8"?>
<opf:package version="2.0" unique-identifier="dcid" xmlns:opf="http://www.idpf.org/2007/opf" xmlns:dc="http://purl.org/dc/elements/1.1/">
<opf:metadata>
<dc:identifier id="dcid" opf:scheme="UUID">urn:uuid:3675ff2a-3059-4102-a2f4-30ab059267ed</dc:identifier>
<dc:title>%s</dc:title>
<dc:creator>%s</dc:creator>
<dc:language>en</dc:language>
<dc:date opf:event="modification">2008-04-07</dc:date>
</opf:metadata>
<opf:manifest>
%s
</opf:manifest>
<opf:spine toc="ncx">
%s
</opf:spine>
</opf:package>""" % (title, author , opf1, opf2))


# now package everything up 
os.system("cd %s ; zip -X %s.zip -n mimetype mimetype  ; zip %s.zip -r META-INF/ OEBPS/ ; mv %s.zip %s.epub; mv %s.epub .." % (fileOut, fileOut, fileOut, fileOut, fileOut, fileOut) )

# clean up the directory we used to make this 
#if os.path.exists(fileOut):
#    shutil.rmtree(fileOut)


# and done
