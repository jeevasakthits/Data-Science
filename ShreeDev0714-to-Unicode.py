# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:02:04 2020

@author: User
"""



# -*- coding: utf-8 -*-
import sys
import re

dict = []
krutidev = []
dict.append(krutidev)
array_one = [
    ">" ,	"" , 
"$" ,	"" , 
"›" ,	"ॐ" ,
"@" ,	"ऽ" ,
"&" ,	"।" ,

"[" ,	"p" , 
"{" ,	"p" ,

"“" ,	"\"" ,
"”" ,	"'" ,

"‹" , "µ" ,  
"µH" ,	"क़" ,
"™" ,	"ख़्" ,
"˜" ,	"ख़" ,
"µJ" ,	"ग़" ,
"µO" ,	"ज़" ,
"µÁ" ,	"ज़्" ,
"µS" ,	"ड़" ,
"µT" ,	"ढ़" ,
"µ\\" ,	"फ़" ,
"µ" ,	"" , 

"ª" ,	"©ं" ,
"£" ,	"©ै" ,
"¤" ,	"©ैं" ,
"u" ,	"©ी" ,
"v" ,	"©ीं" ,
"}" ,	"©े" ,
"]" ,	"©ें" ,

"ú" ,	"क्ष्" ,
"j" ,	"क्ष" ,
"k" ,	"ज्ञ" ,
"l" ,	"श्र" ,
"Ì" ,	"त्र" ,
"Í" ,	"त्र्" ,
"Î" ,	"त्त्" ,
"®" ,	"्रु" ,
"¯" ,	"्रू" ,
"é" ,	"रु" ,
"ê" ,	"रू" ,
"#" ,	"ञ्च्" ,
"‚" ,	"ज्ज्" ,
"ƒ" ,	"च्च" ,
"„" ,	"ल्ल" ,
"†" ,	"ह्ण" ,
"‡" ,	"ह्ल" ,
"ˆ" ,	"ह्व" ,
"‰" ,	"्व" ,
"‘" ,	"ङ्क" ,
"’" ,	"ङ्ख" ,
"“" ,	"ङ्ग" , 
"”" ,	"ङ्घ" ,
"¬" ,	"ङ्क्ष" ,
"•" ,	"ह्न" ,
"–" ,	"ड्ढ" ,
"œ" ,	"श्व" ,

"³" ,	"्न" ,
"¶" ,	"ङ्म" ,
"¸" ,	"क्क" ,
"¹" ,	"क्व" ,
"º" ,	"क्त" ,
"¼" ,	"ख्र" ,
"Ã" ,	"झ्र" ,
"¾" ,	"ग्न" ,
"Å" ,	"ट्ट" ,
"Æ" ,	"ट्ठ" ,
"Ç" ,	"ठ्ठ" ,
"È" ,	"ड्ड" ,
"É" ,	"ड्ढ" ,
"Ð" ,	"द्र" ,
"Ñ" ,	"दृ" ,
"Ò" ,	"द्ग" ,
"Ó" ,	"द्घ" ,
"Ô" ,	"द्द" ,
"Õ" ,	"द्ध" ,
"Ö" ,	"द्न" ,
"×" ,	"द्ब" ,
"Ø" ,	"द्भ" ,
"Ù" ,	"द्म" ,
"Ú" ,	"द्य" ,
"Û" ,	"द्व" ,
"Þ" ,	"न्न" ,
"à" ,	"प्र" ,
"á" ,	"प्त" ,
"ï" ,	"ष्ट" ,
"ð" ,	"ष्ठ" ,
"ò" ,	"स्र" ,
"ó" ,	"स्त्र" ,
"õ" ,	"ह्र" ,
"ö" ,	"हृ" ,
"÷" ,	"ह्म" ,
"ø" ,	"ह्य" ,
"ü" ,	"श्च" ,
"ý" ,	"श्न" ,

"ç" ,	"्य" ,
"Œ" ,	"्र" ,
"´" ,	"्र" ,
"«" ,	"्र" ,

"Š" ,	"क्" ,
"»" ,	"ख्" ,
"½" ,	"ग्" ,
"¿" ,	"घ्" ,
"H" ,	"क" ,
"I" ,	"ख" ,
"J" ,	"ग" ,
"K" ,	"घ" ,
"L" ,	"ङ" ,
"À" ,	"च्" ,
"Á" ,	"ज्" ,
"Â" ,	"झ्" ,
"Ä" ,	"ञ्" ,
"M" ,	"च" ,
"N" ,	"छ" ,
"O" ,	"ज" ,
"P" ,	"झ" ,
"Q" ,	"ट" ,
"R" ,	"ठ" ,
"S" ,	"ड" ,
"T" ,	"ढ" ,
"Ê" ,	"ण्" ,
"U" ,	"ण" ,
"Ë" ,	"त्" ,
"Ï" ,	"थ्" ,
"Ü" ,	"ध्" ,
"Ý" ,	"न्" ,
"V" ,	"त" ,
"W" ,	"थ" ,
"X" ,	"द" ,
"Y" ,	"ध" ,
"Z" ,	"न" ,
"ß" ,	"प्" ,
"â" ,	"फ्" ,
"ã" ,	"ब्" ,
"ä" ,	"भ्" ,
"å" ,	"म्" ,
"n" ,	"प" ,
"\\" ,	"फ" ,
"~" ,	"ब" ,
"^" ,	"भ" ,
"_" ,	"म" ,
"æ" ,	"य्" ,
"ë" ,	"ल्" ,
"ì" ,	"व्" ,
"í" ,	"श्" ,
"î" ,	"ष्" ,
"ù" ,	"ळ्" ,
"û" ,	"श्" ,
"ñ" ,	"स्" ,
"ô" ,	"ह्" ,
"`" ,	"य" ,
"a" ,	"र" ,
"b" ,	"ल" ,
"c" ,	"ल" ,
"d" ,	"व" ,
"e" ,	"श" ,
"f" ,	"ष" ,
"g" ,	"स" ,
"h" ,	"ह" ,
"i" ,	"ळ" ,

"Am¡" ,	"औ" ,
"Amo" ,	"ओ" ,
"Am°" ,	"ऑ" ,
"Am" ,	"आ" ,
"A" ,	"अ" ,
"B©" ,	"ई" ,
"B" ,	"इ" ,
"C" ,	"उ" ,
"D" ,	"ऊ" ,
"F" ,	"ऋ" ,
"G" ,	"ॠ" ,
"Eo" ,	"ऐ" ,
"E" ,	"ए" ,

"m" ,	"ा" ,
"r" ,	"ी" ,
"s" ,	"ी" ,
"t" ,	"ीं" ,
"w" ,	"ु" ,
"x" ,	"ु" ,
"y" ,	"ू" ,
"z" ,	"ू" ,
"¥" ,	"ृ" ,
"¦" ,	"ॄ" ,
"|" ,	"ें" ,
"o" ,	"े" ,
"¡" ,	"ै" ,
"¢" ,	"ैं" ,
"…" ,	"ः" ,
"§" ,	"ं" ,
"¨" ,	"ं" ,
"µ" ,	"़" ,
"þ" ,	"ु" ,
"ÿ" ,	"ू" ,
"°" ,	"ॅ" ,
"±" ,	"ँ" ,
"²" ,	"्" ,

"्ा" ,	"" ,
"्ो" ,	"े" ,
"्ौ" ,	"ै" ,

"\"" ,	"‘" ,
"\'" ,	"’" ,


"0" ,	"०" ,
"1" ,	"१" ,
"2" ,	"२" ,
"3" ,	"३" ,
"4" ,	"४" ,
"5" ,	"५" ,
"6" ,	"६" ,
"7" ,	"७" ,
"8" ,	"८" ,
"9" ,	"९" ,
"ए\ॅ" ,	"ऍ" , 
"अ\ो" ,	"ओ" ,
"अ\ा" ,	"आ" ,
"आ\ै" ,	"औ" ,
"आ\े" ,	"ओ" ,
"अ\ै" ,	"ऐ" ,
"अ\े" ,	"ए" ,
"आ\ॅ" ,	"ऑ" ,
"अ\ॅ" ,	"अ‍ॅ"
]
def replace_special_char():
    global array_one
    global modified_substring
    global array_one_length
    if modified_substring != "":
        input_symbol_idx = 0
        while(input_symbol_idx < array_one_length-1):
            input_symbol_idx = input_symbol_idx + 2
            idx = 0
            while (idx != -1 ):
                try:
                    #print(array_one[input_symbol_idx])
                    modified_substring = modified_substring.replace(array_one[ input_symbol_idx ] , array_one[input_symbol_idx+1])
                    #print(array_one[input_symbol_idx],array_one[input_symbol_idx+1])
                    idx = modified_substring.index(array_one[input_symbol_idx],1,len(modified_substring))
                    #print(input_symbol_idx)
                except Exception as e:
                    #print(e)
                    #print(modified_substring,'([pq])([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])',array_one[input_symbol_idx])
                    idx=-1
        print(modified_substring)
        modified_substring = modified_substring.replace( r"([pq])([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])" , "\2\1" ) ;

        modified_substring = modified_substring.replace( r"([pq])((्[कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])+)" , "\2\1" ) ;
        
        modified_substring = modified_substring.replace( r"p" , "ि" ) ;
        modified_substring = modified_substring.replace( r"q" , "िं" ) ;
        
        modified_substring = modified_substring.replace( r"([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])([ा\ि\ी\ु\ू\ृ\े\ै\ो\ौ\ं\ँ]*)([©])" , "\3\1\2" ) ;
        
        modified_substring = modified_substring.replace( r"(([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ][्])+)([©])", "\3\1" ) ;

        
        modified_substring = modified_substring.replace( r"©" , "र्" ) ;
        
        modified_substring = modified_substring.replace ( r"([\s]+)([ऽ\्\ा\ी\ु\ू\ृ\े\ै\ो\ौ\ं\ँ])" , "\2" ) ;

        modified_substring = modified_substring.replace ( r"([्\ु\ू\ृ\े\ै]+)" , "\1" ) ;
        modified_substring = modified_substring.replace ( r"([ं\ँ]+)" , "\1" ) ;
        

        modified_substring = modified_substring.replace( r"([ः\ं\ँ\॰]+)([\ा\ि\ी\ु\ू\ृ\े\ै\ो\ौ]+)" , "\2\1" );
        

        modified_substring = modified_substring.replace( r"ा\े" , "ो" );
        modified_substring = modified_substring.replace( r"ा\ै" , "ौ" );
        modified_substring = modified_substring.replace( r"ॅ\ं" , "ँ" );
        modified_substring = modified_substring.replace( r"ं\ॅ" , "ँ" );
        
        modified_substring = modified_substring.replace( r"ा\ॅ" , "ॉ" );
        modified_substring = modified_substring.replace( r"ॅ\ा" , "ॉ" );
        
        modified_substring = modified_substring.replace( r"ा\ो" , "ो" );
        modified_substring = modified_substring.replace( r"ै\ा" , "ौ" );
        
        modified_substring = modified_substring.replace( r"े\ा" , "ो" );
        
        modified_substring = modified_substring.replace( r"([\s])ः" , "\1:" );

array_one_length = 0
inp_text = ""
text_size = 0
processed_text = ''
sthiti1 = 0
sthiti2 = 0
chale_chalo = 1
modified_substring= ''
chunk_size = 6000

def char_to_unicode(input_1):
    global processed_text
    global array_one_length
    global inp_text
    global text_size
    global array_one
    global processed_text
    global sthiti1
    global sthiti2
    global chale_chalo
    global chunk_size
    global modified_substring
    array_one_length = len(array_one)
    inp_text = input_1
    text_size = len(inp_text)
    processed_text = ''
    sthiti1 = 0
    sthiti2 = 0
    chale_chalo = 1
    chunk_size = 6000
    while ( chale_chalo == 1 ):
        sthiti1 = sthiti2
        if sthiti2 < ( text_size - chunk_size ):
            sthiti2 +=  chunk_size
            while ( chr(inp_text[sthiti2]) != '\n') and (chr(inp_text[sthiti2]) != '\t') and (chr(inp_text[sthiti2]) != ' '):
                sthiti2=sthiti2-1
        else:
            sthiti2 = text_size
            chale_chalo=0
            
        modified_substring = inp_text[sthiti1:sthiti2]
        #print(modified_substring)
        replace_special_char()
        print(modified_substring)
        processed_text = processed_text + modified_substring 
        return processed_text
	  

vl=char_to_unicode('8c2O6udqCHavVpSP3vu0fv7+3d2tm/cunnp/MUbV64d7B0wIqIoDlkUhXGvt/L0U0+9/OJTh7fWUr2oZAEAunTx8te//odrg82arDxUcRQ4b1qNxqyQeVFWVYUQPHR4zQEZRLDfGwDIZ4s5wLK3EmpVBXHQ7PREwAFwEJeYYG1yY402UuvKA8dZ4GzlrHK+tC531jAmrJXD0SwIgqKYOz9pt4kQgBJj2+TQocNaK60X1gDrTLfbCUNunY5jobQvyuxgdHs4vN1ut1utbqPVzqvF6iq2dpsCEogmgWC+mDszb9bx2qBPGZ3P58bbvf37ECIAAISw1W40Gk2tpVNzD+RwPrHGBCGdKUWo7bRwLaHeQmCUM95oMy/')





















