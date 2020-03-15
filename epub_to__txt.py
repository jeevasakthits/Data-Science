#Epub File Reading and store as a txt file pyhton
from epub_conversion.utils import open_book, convert_epub_to_lines
from inscriptis import get_text
import re
import os
# -*- coding: utf-8 -*-
import sys
import re
import nltk 
import pandas as pd
"""dict = []
krutidev = []
dict.append(krutidev)
walkmanchanakya = [
    "-", "$",
    "I+ks", "पे़",
    "ks±", "ोर्ं",
    "k±", "kZ±",
    "¢", "ः",
    "ñ", "॰",
    # "Q+Z" , "QZ+" ,
    "sas", "sa",
    "aa", "a",
    "¼Z", "र्द्ध",
    "ZZ", "Z",
    "+\n", "+",
    "\n+", "+",
     
    "å", "०",
    "ƒ", "१",
    # "\„" , "२" ,
    "„", "२",
    "…", "३",
    "†", "४",
    "‡", "५",
    # "\ˆ" , "६" ,
    "ˆ", "६",
    "‰", "७",
    "Š", "८",
    # "\‹" , "९" ,
    "‹", "९",

    "d+", "क़",
    "[+k", "ख़",
    "[+", "ख़्",
    "x+", "ग़",
    "T+", "ज़्",
    "t+", "ज़",
    "M+", "ड़",
    # "\<+" , "ढ़" ,
    "<+", "ढ़",
    # "Q+" , "फ़" , # commented in original file
    # "\;+" , "य़" ,
    ";+", "य़",
    "j+", "ऱ",
    "u+", "ऩ",
    "Ùk", "त्त",
    "Ù", "त्त्",
    "ä", "क्त",
    "–", "दृ",
    "—", "कृ",
    "é", "न्न",
    # added by ahbi
    "Â", "न्न",
    # till here
    "™", "न्न्",
    # "\=kk" , "\=k" ,
    # "=kk" , "=k" ,
    # "f\=k" , "f\=" ,
    "f=k", "f=",
    "à", "ह्न",
    "á", "ह्य",
    "â", "हृ",
    "ã", "ह्म",
    "ºz", "ह्र",
    "º", "ह्",
    "í", "द्द",
    # "\{k" , "क्ष" ,
    "{k", "क्ष",
    # "\{" , "क्ष्" ,
    "{", "क्ष्",
    # "f\=" , "त्रि" ,
    "f=", "त्रि",
    # "\=k" , "त्र" ,
    "=k", "त्र",
    # "\«" , "त्र्" ,
    "«", "त्र्",
    "Nî", "छ्य",
    "Vî", "ट्य",
    "Bî", "ठ्य",
    "Mî", "ड्य",
    # "\<î" , "ढ्य" ,
    "<î", "ढ्य",
    "|", "द्य",
    "K", "ज्ञ",
    "}", "द्व",
    "J", "श्र",
    "ª", "्र",
    # "Vª" , "ट्र" ,
    # "Mª" , "ड्र" ,
    # "\>ª" , "ढ्र" ,
    # ">ª" , "ढ्र" ,
    # "Nª" , "छ्र" ,
    "Ø", "क्र",
    "Ý", "फ्",
    "nzZ", "र्द्र",
    "æ", "द्र",
    "ç", "प्र",
    "Á", "प्र",
    "xz", "ग्र",
    "#", "रु",
    ":", "रू",
    "v‚", "ऑ",
    "vks", "ओ",
    "vkS", "औ",
    "vk", "आ",
    "v", "अ",
    "b±", "ईं",
    "Ã", "ई",
    "bZ", "ई",
    "baZ", "ईं",
    "b", "इ",
    "mQ", "ऊ",
    "m", "उ",
    "Å", "ऊ",
    # "\,s" , "ऐ" ,
    ",s", "ऐ",
    # "\," , "ए" ,
    ",", "ए",
    "½", "ऋ",
    "ô", "क्क",
    "d", "क",
    "Dk", "क",
    "D", "क्",
    "£", "र्f",
    "[k", "ख",
    "[", "ख्",
    "x", "ग",
    "Xk", "ग",
    "X", "ग्",
    "Ä", "घ",
    "?k", "घ",
    "?", "घ्",
    "³", "ङ",
    "p", "च",
    "Pk", "च",
    "P", "च्",

    "N", "छ",

    # "\”k" , "ज" ,
    "”k", "ज",
    # "\”" , "ज्" ,
    "”", "ज्",

    "t", "ज",
    "Tk", "ज",
    "T", "ज्",
    # "\>" , "झ" ,
    ">", "झ",
    "÷", "झ्",
    "¥", "ञ",
    "ê", "ट्ट",
    # added by abhi ex for mitti
    # "^" , "ट्ट" ,
    # till here
    "ë", "ट्ठ",
    "V", "ट",
    "B", "ठ",
    "ì", "ड्ड",
    "ï", "ड्ढ",
    "M+", "ड़",
    # "\<+" , "ढ़" ,
    "<+", "ढ़",
    "M", "ड",
    # "\<" , "ढ" ,
    "<", "ढ",
    # "\.k" , "ण" ,
    ".k", "ण",
    # "\." , "ण्" ,
    ".", "ण्",
    "r", "त",
    "Rk", "त",
    "R", "त्",
    "Fk", "थ",
    "F", "थ्",
    "n", "द",
    # "\/" , "ध" ,
    "/", "ध",
    "èk", "ध",
    "è", "ध्",
    "Ë  ", "ध्",
    "u", "न",
    "Uk", "न",
    "U", "न्",
    # "i\+ Q" , "फ़" ,
    "i+ Q", "फ़",
    # "i\+Q" , "फ़" ,
    "i+Q", "फ़",

    "iQ", "फ",
    "i", "प",
    "I+k Q", "फ़",
    "I+kQ", "फ़",
    "IkQ", "फ",
    "Ik", "प",
    "I", "प्",
    "¶", "ζ",
    "¸", "Δ",
    "c", "ब",
    "Ck", "ब",
    "C", "ब्",
    "Hk", "भ",
    "H", "भ्",
    "e", "म",
    "Ek", "म",
    "E", "म्",
    # "\;" , "य" ,
    ";", "य",
    "Õk", "य",
    "Õ", "य्",
    # "\¸" , "य्" ,
    # "¸" , "य्" ,
    "jQ", "रू",
    "j", "र",
    "y", "ल",
    "Yk", "ल",
    "Y", "ल्",
    "G", "ळ",
    "o+Q", "क़",
    "oQ", "क",
    # added by Rakshak
    "osQ", "के",
    "oSQ", "कै",
    "oqQ", "कु",
    "owQ", "कू",
    "oZQ", "कZ",
    # till here
    "o", "व",
    "OkQ", "क",
    "Ok", "व",
    "O", "व्",

    # "\'k" , "श" ,
    "'k", "श",
    # "\'" , "श्" ,
    "'", "श्",

    "Ük", "श",
    "Ü", "श्",

    # "\"k" , "ष" ,
    '"k', "ष",
    # "\"" , "ष्" ,
    '"', "ष्",
    "l", "स",
    "Lk", "स",
    "L", "स्",
    "g", "ह",
    "È", "ीं",
    "z", "्र",
    "Ì", "द्द",
    "Í", "ऋ",  # 21-9-2012
    "Î", "ट्ठ",
    "Ï", "ड्ड",
    "Ñ", "कृ",
    "Ò", "भ",
    "Ó", "्य",
    "Ô", "ड्ढ",
    "Ö", "झ्",
    "Ø", "क्र",
    "Ù", "त्त्",
    "¼", "द्ध",
    "Ú", "फ्र",
    "É", "ह्न",
    "Q", "फ़",
    # following block added on 19-3-2011
    "Ů", "त्त्",
    "Ľ", "द्ध",
    "˝", "ऋ",
    "Ř", "क्र",
    "Ń", "कृ",
    # "Q" , "फ़" ,
    "č", "ध्",
    "Ş", "्र",

    # "\‚" , "ॉ" ,
    "‚", "ॉ",
    "¨", "ो",
    # added by abhi
    # for fixing ;ksa and ;kas
    "kas", "ksa",
    "sak", "ksa",
    # till here
    "ks", "ो",
    "©", "ौ",
    "kS", "ौ",
    "k", "ा",
    "h", "ी",
    "q", "ु",
    "w", "ू",
    # "\`" , "ृ" ,
    "`", "ृ",
    "s", "े",
    "¢", "े",
    "S", "ै",
    "±", "Γ",
    "a", "ं",
    "Γ", "ं",
    "¡", "ँ",
    "ˇ", "ँ",
    "%", ":",
    "W", "ॅ",
    "·", "*",
    "+", "़",
    # "\\" , "?" ,
    "\\", "?",  # needs to be unescaped

    # "\‘" , "\"" ,
    "‘", '"',
    # "\’" , "\"" ,
    "’", '"',
    # "\“" , "\'" ,
    "“", "'",
    # "\”" , "\'" ,
    "”", "'",

    # "^" , "\‘" ,
    "^", "‘",
    # "*" , "\’" ,
    "*", "’",
    # "Þ" , "\“" ,
    "Þ", "“",
    # "ß" , "\”" ,
    "ß", "”",
    "¾", "=",
    "&", "-",
    "μ", "-",
    "¿", "{",
    "À", "}",
    "A", "।",
    # "-" , "." ,
    "Œ", "॰",
    # "]" , "\," ,
    "]", ",",
    # "@" , "\/" ,
    "@", "/",

    "~", "्",
    "्ा", "",
    "ाे", "ो",
    "ाॅ", "ॉ",

    "अौ", "औ",
    "अो", "ओ",
    "आॅ", "ऑ",

    # addded by Rakshak
    "ंे", "ें",
    # by abhi
    "े़े", "े़",
    "ंै", "ैं",
    "ैै", "ै",
    # till here
    # "chr(0x191)","ऽ",
    # 21-9-2012
    "ाो", "ो",
    "ुु", "ु",
    "ेे", "े",
    "ोे", "ो",
    "ंं", "ं",
    # added by @bhi
    "$", ".",
    "f", "α",
    # "f" , "ि" ,
    # "Ç" , "β" ,
    "¯", "β",
    "Z", "γ",
    # "Z" , "र्"
    # Added By Akshay
    "ð", "",
    "", ""
    # upto this only
]

dict.append(walkmanchanakya)
dict34 = [
"﻿a","a",
"ãñ´U","हैं",
"Ú÷U","र्",
"·ð¤","के",
"ãñU","है",
"¥","अ",
"¥æ","आ",
"§ü","ई",
"§","इ",
"©U","उ",
"ª¤","ऊ",
"«¤","ऋ",
"°","ए",
"°ð","ऐ",
"¥ô","ओ",
"¥õ","औ",
"€","क्",
"·¤","क",
"","ख्",
"¹","ख",
"‚","ग्",
"»","ग",
"l","द्य",
"ƒæ","घ",
"ƒ","घ्",
"¾¤","ङ",
"¾÷","ङ्",
"‘","च्",
"¿","च",
"“","च्च्",
"ÀU","छ",
"À÷","छ्",
"’","ज्",
"Á","ज",
"Ûæ","झ",
"Û","झ्",
"†æ","ञ",
"†","ञ्",
"ÅU","ट",
"ÅU÷","ट्",
"ÆU","ठ",
"Æ÷","ठ्",
"ÇU","ड",
"Ç¸U","ड़",
"ÉU","ढ",
"É¸U","ढ़",
"‡æ","ण",
"‡","ण्",
"ˆ","त्",
"Ì","त",
"ž","त्त्",
"‰","थ्",
"Í","थ",
"Î","द",
"¼","द",
"m","द्व",
"Ï","ध",
"Š","ध्",
"‹","न्",
"Ù","न",
"Œ","प्",
"Â","प",
"È¤","फ",
"Õ","ब",
"Ž","ब्",
"Ö÷","भ्",
"Ö","भ",
"×","म",
"×÷","म्",
"Ø","य",
"ÚU","र",
"ü","γ",
"M¤","रू",
"L¤","रू",
"Ë","ल्",
"Ü","ल",
"ß","व",
"Ã","व्",
"o","श",
"àæ","श",
"à","श्",
"á","ष",
"c","ष्",
"S","स्",
"â","स",
"ãU","ह",
"ã","ह",
"±","ह्",
"q","ह्न",
"t","ह्ल",
"ÿ","क्ष्",
"ÿæ","क्ष",
"˜æ","त्र",
"™æ","ज्ञ",
"Ÿæ","श्र",
"æ","ा",
"ç","α",
"Z","γं",
"è","ी",
"é","ु",
"ê","ू",
"ð","े",
"Ô","े",
"ñ","ै",
"ô","ो",
"õ","ौ",
"æò","ॉ",
"¡","ँ",
"¢","ं",
"´","ं",
"¸U","़",
"ò","ॅ",
"^U","ट्ट",
"”","ज्ज्",
"¥æò","ऑ",
"NU","हृ",
"h","द्ध",
"Ý","ळ",
"Ø¸","य़",
"Ú¸","ऱ",
"Ñ",":",
"÷","्",
"ë","ृ",
"ý","्र",
"þ","्र",
"Ò","`",
"Ó","'",
"v","1",
"w","2",
"x","3",
"y","4",
"z","5",
"{","6",
"|","7",
"}","8",
"~","9",
"®","0",
"Ð","।"
]

dict.append(dict34)


def replaceSymbols(modifiedString, font):
    if modifiedString != "":
        outputStr = ""

        for inputSymbolIdx in range(0, len(dict[font]), 2):
            idx = modifiedString.find(dict[font][inputSymbolIdx])

            while idx != -1:
                modifiedString = re.sub(re.escape(dict[font][inputSymbolIdx]), dict[font][inputSymbolIdx + 1],
                                        modifiedString)
                idx = modifiedString.find(dict[font][inputSymbolIdx])

        outputStr = outputStr + modifiedString
    return modifiedString


def readFile(s):
    input = open(s)  # input file name
    modifiedString = input.read()
    # print modifiedString
    input.close()
    return modifiedString


def convertToUni(modifiedString, font):
    textSize = len(modifiedString)
    processedText = ''

    track1 = 0
    track2 = 0
    continu = 1

    chunkSize = 6000

    while continu == 1:
        track1 = track2

        if track2 < textSize - chunkSize:
            track2 = track2 + chunkSize
        else:
            track2 = textSize
            continu = 0
        modifiedString = modifiedString[track1:track2]

        modifiedString = replaceSymbols(modifiedString, font)

        processedText = processedText + modifiedString

        processedText = re.sub(
            r'(α|β)(क|ख|ग|घ|ङ|च|छ|ज|झ|ञ|ट|ठ|ड|ढ|ण|त|थ|द|ध|न|प|फ|ब|भ|म|य|र|ल|ळ|व|श|ष|स|ह|क़|ख़|ग़|ज़|ड़|ढ़|फ़|य़|ऱ|ऩ)', r'\2\1',
            processedText)
        processedText = re.sub(
            r'(α|β)((्(क|ख|ग|घ|ङ|च|छ|ज|झ|ञ|ट|ठ|ड|ढ|ण|त|थ|द|ध|न|प|फ|ब|भ|म|य|र|ल|ळ|व|श|ष|स|ह|क़|ख़|ग़|ज़|ड़|ढ़|फ़|य़|ऱ|ऩ))+)',
            r'\2\1', processedText)
        processedText = re.sub(r'α', "ि", processedText)
        processedText = re.sub(r'β', "िं", processedText)

        processedText = re.sub(r'((ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|़)*)(γ)', r'\3\1', processedText)
        processedText = re.sub(
            r'(क|ख|ग|घ|ङ|च|छ|ज|झ|ञ|ट|ठ|ड|ढ|ण|त|थ|द|ध|न|प|फ|ब|भ|म|य|र|ल|ळ|व|श|ष|स|ह|क़|ख़|ग़|ज़|ड़|ढ़|फ़|य़|ऱ|ऩ)(γ)', r'\2\1',
            processedText)
        processedText = re.sub(
            r'(((क|ख|ग|घ|ङ|च|छ|ज|झ|ञ|ट|ठ|ड|ढ|ण|त|थ|द|ध|न|प|फ|ब|भ|म|य|र|ल|ळ|व|श|ष|स|ह|क़|ख़|ग़|ज़|ड़|ढ़|फ़|य़|ऱ|ऩ)्)+)(γ)',
            r'\4\1', processedText)
        processedText = re.sub(r'γ', "र्", processedText)
        processedText = re.sub(r'µ', '-', processedText)
        processedText = re.sub(r'_', ';', processedText)
        processedText = re.sub(r'(्)((ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|़)*)(ा)', r'\2', processedText)
        processedText = re.sub(r'(व)((ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|्र)*)(Q)', r'क\2', processedText)
        processedText = re.sub(r'ζ', r'“', processedText)
        processedText = re.sub(r'Δ', r'”', processedText)
        processedText = re.sub(r'(ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|्र)(्र)', r'\2\1', processedText)
        processedText = re.sub(r'(प)((ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|़|्र)*)(Q)', r'फ\2', processedText)
        processedText = re.sub(r'(उ)((ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|़|्र)*)(Q)', r'ऊ\2', processedText)
        processedText = re.sub(r' ः ', r' : ', processedText)
        processedText = re.sub(
            r'(क|ख|ग|घ|ङ|च|छ|ज|झ|ञ|ट|ठ|ड|ढ|ण|त|थ|द|ध|न|प|फ|ब|भ|म|य|र|ल|ळ|व|श|ष|स|ह|क़|ख़|ग़|ज़|ड़|ढ़|फ़|य़|ऱ|ऩ)(asd|ँ|ं|़)+(ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|़|्र)',
            r'\1\3\2', processedText)
        processedText = re.sub(
            r'(क|ख|ग|घ|ङ|च|छ|ज|झ|ञ|ट|ठ|ड|ढ|ण|त|थ|द|ध|न|प|फ|ब|भ|म|य|र|ल|ळ|व|श|ष|स|ह|क़|ख़|ग़|ज़|ड़|ढ़|फ़|य़|ऱ|ऩ)((ा|ि|ी|ु|ू|ृ|े|ै|ो|ौ|ं|ँ|़|्र)+)(asd|़)+',
            r'\1\4\2', processedText)
        return processedText"""
def book_read(book_name):
    book = open_book(str(book_name))
    lines = convert_epub_to_lines(book)
    print(len(lines))
    s=("\n".join(lines))
    print(s)
    #text=re.sub("<[^>]*>","",s
    text = get_text(s)
    text=re.sub("[ ]+"," ",text)
    text=re.sub("[\n]+","\n",text)
    return text
choice=int(input('Enter choice \n 1. English \n 2.Hindi \n Enter Input: '))
if choice==1:
    dir0='F:/hindi_english_downloaded_split/ont_to_five/english'
else:
    dir0='F:/hindi_english_downloaded_split/ont_to_five/hindi'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
for io in range(len(list_dir0)):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for i in range(len(list_dir)):
        dir2=dir1+'/'+str(list_dir[i])
        os.chdir(dir2)
        listdir_2=os.listdir()
        listdir_3=listdir_2
        listdir_3= list(filter(lambda x: x[-5:] == '.epub', listdir_3))
        for k in range(len(listdir_3)):
            total_file=total_file+1
            try:
                text=book_read(listdir_3[k])
                if len(text)>1:
                    with open(str(listdir_3[k])+".txt", "w", encoding="utf-8") as f:
                        f.write(text)
                else:
                    file_low_list.append(dir3+"/"+listdir_3[k])
            except:
                file_low_list.append(dir2+"/"+listdir_3[k])
                print(dir2+str(listdir_3[k]))
print('Total file',total_file)

