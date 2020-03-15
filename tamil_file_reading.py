Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tika

>>> tika.initVM()
>>> from tika import parser
>>> parsed = parser.from_file('C:/Users/User/Desktop/11_Bio-Zoo_Vol_1_TM.pdf')
2020-01-21 18:27:21,712 [MainThread  ] [WARNI]  Failed to see startup log message; retrying...
2020-01-21 18:27:26,793 [MainThread  ] [WARNI]  Failed to see startup log message; retrying...
>>> print(parsed["metadata"])
{'Content-Type': 'application/pdf', 'Creation-Date': '2018-06-03T12:28:33Z', 'Last-Modified': '2018-06-03T12:28:33Z', 'Last-Save-Date': '2018-06-03T12:28:33Z', 'X-Parsed-By': ['org.apache.tika.parser.DefaultParser', 'org.apache.tika.parser.pdf.PDFParser'], 'X-TIKA:content_handler': 'ToTextContentHandler', 'X-TIKA:embedded_depth': '0', 'X-TIKA:parse_time_millis': '9523', 'access_permission:assemble_document': 'true', 'access_permission:can_modify': 'true', 'access_permission:can_print': 'true', 'access_permission:can_print_degraded': 'true', 'access_permission:extract_content': 'true', 'access_permission:extract_for_accessibility': 'true', 'access_permission:fill_in_form': 'true', 'access_permission:modify_annotations': 'true', 'date': '2018-06-03T12:28:33Z', 'dc:format': 'application/pdf; version=1.6', 'dc:title': '', 'dcterms:created': '2018-06-03T12:28:33Z', 'dcterms:modified': '2018-06-03T12:28:33Z', 'meta:creation-date': '2018-06-03T12:28:33Z', 'meta:save-date': '2018-06-03T12:28:33Z', 'modified': '2018-06-03T12:28:33Z', 'pdf:PDFVersion': '1.6', 'pdf:charsPerPage': ['145', '244', '580', '1153', '3163', '2364', '4906', '0', '1752', '1408', '2426', '1897', '2539', '1356', '1784', '2003', '1434', '1392', '1561', '2083', '2091', '2167', '2318', '501', '735', '1488', '1692', '1429', '2255', '2208', '1494', '1342', '0', '1659', '1655', '2190', '1654', '1743', '1463', '1747', '2107', '2218', '1499', '456', '1751', '1351', '2297', '1953', '593', '1597', '1201', '1433', '1073', '352', '1068', '2322', '460', '708', '1587', '1401', '1466', '1365', '1423', '328', '1313', '1799', '1440', '2036', '1691', '2338', '1035', '0', '2236', '1065', '1114', '640', '1673', '1713', '1382', '951', '1422', '1156', '1739', '1688', '1983', '1560', '629', '1091', '2453', '1392', '2405', '1933', '915', '1611', '1748', '1347', '2266', '2411', '1103', '2463', '1269', '890', '1589', '2315', '521', '1637', '566', '2197', '865', '1303', '0', '836', '1769', '1708', '1355', '1777', '1186', '2407', '1653', '1255', '1241', '1363', '0', '2255', '1197', '2252', '1423', '2869', '2103', '2281', '2278', '2023', '1966', '1858', '744', '768', '423', '1531', '1336', '1427', '709', '1221', '2275', '1245', '353', '2247', '1131', '2119', '1107', '2053', '1690', '1841', '1204', '2480', '2072', '0', '2412', '1161', '878', '688', '451', '1925', '1368', '1646', '2218', '1270', '1878', '2448', '2099', '1319', '2263', '2504', '1395', '1700', '1362', '2307', '2136', '2484', '543', '1347', '2400', '2278', '1248', '1308', '2235', '443', '2422', '2344', '1412', '2277', '1336', '822', '934', '2030', '1816', '1646', '1927', '1814', '1345', '1773', '1860', '1854', '1839', '1756', '1956', '2007', '1884', '1876', '1745', '1789', '1830', '1705', '1835', '1864', '1878', '1795', '1751', '1781', '1798', '1726', '1852', '1773', '1891', '2020', '1761', '1982', '1796', '1674', '1749', '1132', '1917', '1919', '2096', '2065', '3402', '9', '9', '9', '9', '9'], 'pdf:docinfo:created': '2018-06-03T12:28:33Z', 'pdf:docinfo:creator_tool': 'Adobe Acrobat Pro DC 18.11.20038', 'pdf:docinfo:modified': '2018-06-03T12:28:33Z', 'pdf:docinfo:producer': 'Adobe Acrobat Pro DC 18.11.20040', 'pdf:docinfo:title': '', 'pdf:encrypted': 'false', 'pdf:hasXFA': 'false', 'pdf:hasXMP': 'true', 'pdf:unmappedUnicodeCharsPerPage': ['145', '181', '550', '1148', '3154', '2327', '4840', '0', '1408', '0', '2425', '1896', '2537', '1355', '1783', '1984', '1433', '1389', '1559', '2078', '2084', '2164', '2316', '391', '660', '1483', '1276', '1397', '2253', '2206', '1492', '1340', '0', '1394', '1629', '2188', '1652', '1741', '1461', '1745', '2105', '2216', '1425', '34', '1749', '1283', '2295', '1951', '591', '1595', '947', '1431', '1071', '0', '962', '2320', '0', '695', '1571', '1399', '1464', '931', '1395', '326', '1311', '1797', '1426', '2034', '1688', '2336', '1033', '0', '2234', '1063', '1112', '615', '1586', '1711', '1344', '881', '1361', '1154', '1679', '1625', '1918', '1387', '515', '1068', '2368', '1315', '2227', '1777', '840', '1557', '1652', '1171', '2167', '2294', '1086', '2342', '1259', '888', '1514', '2220', '306', '1602', '564', '2102', '766', '1298', '0', '0', '1751', '1690', '1352', '1008', '1153', '2350', '1650', '1252', '1119', '1319', '0', '2252', '984', '2249', '1419', '2849', '2020', '2276', '2275', '2020', '1878', '650', '736', '765', '11', '1517', '1333', '1419', '30', '1188', '2249', '1242', '350', '2238', '1000', '2080', '935', '2025', '1644', '1822', '1168', '2440', '2033', '0', '2406', '1158', '840', '0', '0', '1909', '1365', '1643', '1248', '1235', '1875', '2445', '2095', '1316', '2259', '2487', '1114', '1695', '1065', '2304', '2133', '2481', '540', '1344', '2396', '2275', '1245', '1305', '2231', '246', '2418', '2341', '0', '2274', '1134', '760', '920', '2025', '1799', '1631', '1924', '1811', '659', '1770', '1857', '1851', '1836', '1753', '1953', '2004', '1881', '1873', '1742', '1786', '1827', '1702', '1832', '1861', '1875', '1792', '1748', '1778', '1795', '1723', '1849', '1770', '1888', '2017', '1758', '1979', '1793', '1671', '1746', '1129', '916', '917', '967', '1027', '3402', '6', '6', '6', '6', '6'], 'resourceName': "b'11_Bio-Zoo_Vol_1_TM.pdf'", 'title': '', 'xmp:CreatorTool': 'Adobe Acrobat Pro DC 18.11.20038', 'xmpMM:DocumentID': 'uuid:a2ca0408-41cb-4308-aba0-644bb41e1c01', 'xmpTPg:NPages': '240'}
>>> print(parsed["content"])










































II

© SCERT 2018

www.textbooksonline.tn.nic.in

The wise
possess all

 



III

 I 

01

20

 II

55

71

 III

109

134

158



IV

ICT



V

  

 

  

 

 

 



4
5
 

4
5

9
0

1
8

0

6
0

6
0

6
0

2
0

2
0

0

6
0

6
0

6
0

1
0

1
0

2
0

0
 

VI



VII

A
IIM

S

M
ic

ro
b

io
lo

g
y

JI
PM

ER
SI

D
D

H
A

IV
R

I
N

D
R

I

 

 

 
• 

IA
RI

IIT
 C

he
nn

ai

N
IN

 –
 





1

Chapter  1UNIT I

1.1. Diversity in the Living world

1.2. Need for Classifi cation

1.3. Taxonomy and Systematics

1.4. Th ree Domains of life

1.5. Taxonomic Hierarchy

1.6. Nomenclature

1.7. Concept of Species

1.8. Tools for study of Taxonomy

“Our task must be to…embrace all living 
creatures and the whole of nature and its beauty.”

— Albert Einstein

• 

• 

• 

• 



º¶ªè½ñ¢ðø¢ø¬õ

º¶ªè½ñ¢¹¬ìò¬õ

Ìê¢ê¤è÷¢

ñ¦ù¢è÷¢

î†¬ì ¹¿‚è÷¢

c˜ï¤ô
õ£ö¢õù

è¤óú¢«ìû¤ò£
áó¢õù

ñ¦ù¢è÷¢ º¶ªè½ñ¢ðø¢ø¬õ

ð£Öì¢®è÷¢ ðø¬õè÷¢ áó¢õù Þ¼õ£ö¢õ¤è÷¢

ð£è¢¯ó¤ò£õ¤ôé¢°è÷¢ ¹«ó£®ú¢†è÷¢Ìë¢¬êèœ î£õóé¢è÷¢

40%

13%

2%

1%

31%

13%

Wilson (1992) Mora et al  (2011) Brenden et al  (2017)

73.1

4.9%

17.6% 90.5%
78%

7.3%
7.4%

0.02%

7.3%

5.6%
2.8%

1% 0.1%
4.1%

0.4%

Þï¢î¤ò£õ¤ô¢ ¹î¤î£è èí¢´ð¤®è¢èð¢ðì¢ì
ê¤ø¢ø¤ùé¢è÷¢ (2016): Þï¢î¤ò£õ¤ô¢ èí¢´
ð¤®è¢èð¢ðì¢ì ¹î¤ò ê¤ø¢ø¤ùé¢è÷¤ô¢ º¶ªè½ñ¢ðø¢øù
258 ñø¢Áñ º¶ªè½ñ¢¹¬ìòù 55 Ý°ñ¢.
Ìê¢ê¤ò¤ùé¢è÷¤ô¢ 97, ñ¦ù¢è÷¤ô¢ 27, Þ¼õ£ö¢õ¤è÷¤ô¢ 12,
îì¢¬ìð¢¹¿è¢è÷¤ô¢ 10, è¤óú¢«ìSò£è¢è÷¤ô¢ 9,
áó¢õùõø¢ø¤ô¢ 6 Ýè¤òù Üø¤õ¤òô£÷ó¢è÷£ô¢
Þùñ¢èí¢´ õ¤÷è¢èð¢ðì¾÷¢÷ù. Ìê¢ê¤ò¤ùé¢èÀ÷¢ 61
Üï¢¶ð¢Ìê¢ê¤èÀñ¢ ðì¢ì£ñ¢Ìê¢ê¤èÀñ¢ (ªôð¤ì£ð¢¯ó£ õ¬è)
ñø¢Áñ¢ 38 õí¢´èÀñ¢ («è£ô¤ò£ð¢¯ó£) Üìé¢°ñ¢.

IUCN Ãø¢Áð¢ð® 172 ê¤ø¢ø¤ùé¢è÷¢ Þï¢î¤ò£õ¤ô¢ Üö¤õ¤ù¢
õ¤÷¤ñ¢ð¤ô¢ à÷¢÷ùõ£°ñ¢. Þ¶ àôè Ü÷õ¤ô¢
ð£ó¢è¢°ñ¢«ð£¶ 2.9% Ý°ñ¢. Þ„ê¤ø¢ø¤ùé¢è÷¤ô¢ 53 ð£Öì¢®è÷¢
69 ðø¬õè÷¢, 23 áó¢õù, 3 Þ¼õ£ö¢õ¤è÷¢
2 ñ¦ù¢è÷¢ ñø¢Áñ¢ 22 º¶ªè½ñ¢ðø¢øù Ýè¤òù Üìé¢°ñ¢.

õ¤ô¢êù¢ (1992) «ñ£ó£ ñø¢Áñ¢ °¿õ¤ùó¢
(2011)

ð¤óí¢ìù¢ ñø¢Áñ¢ °¿õ¤ùó¢
(2017)

¹MJ½œ÷ àJKèO¡ ð™õ¬èˆî¡¬ñ
¹î¤ò èí‚W´ (2017) 

ðô¢«õÁ àò¤ó¤ùè¢ °¿è¢è÷¤ù¢
âî¤ó¢ð£ó¢è¢èð¢ðì¢ì õ÷î¢¬î
Ü®ð¢ð¬ìò£è¢è¢ ªè£í¢ì

èíè¢è¦´.

ðô¢«õÁ àò¤ó¤ùè¢
°¿è¢è÷¤ù¢ âî¤ó¢ð£ó¢è¢èð¢ðì¢ì
õ÷î¢¬î Ü®ð¢ð¬ìò£èè¢

ªè£í¢ì èíè¢è¦´

Þï¢î¤ò£õ¤ô¢ ¹î¤î£è èí¢´ð¤®è¢èð¢ðì¢ì
ê¤ø¢ø¤ùé¢è÷¢ (2016)

Þï¢î¤ò£õ¤ô¢ ÜN»‹
G¬ôJ½œ÷ CŸPùƒèœ. 

Þ¶õ¬ó M÷‚èŠð†ì CŸPùƒèO™ 
àœ÷ àJKùƒèO¡ â‡E‚¬è¬ò 

Ü®Šð¬ìò£è‚ ªè£‡´ à¼õ£‚èŠð†ì, 
ð™«õÁ °¿‚è¬÷„ «ê˜‰î àJKù 

õ÷ƒèO¡ åŠd†´‚ èí‚W´.



3



4



55



6



7



8

      

      

      



9



10

 



11



12

 

  



13

•

•

•

•

•



14

•



15



16

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

1

2

3

4



17

DEEP TREE 

http://www.pbs.org/wgbh/nova/labs/lab/evolution/

Deep Tree 

 1

* 

 



18

  

 



19

  
1. Peter H. Raven, George B. Johnson, 

Susan R. Singer, Jonathan B. Losos (2004) 

Biology 7th Edition Published by McGraw-

Hill Science.

2. Janet L. Hopson and John Postlethwait 

(2006) Modern Biology Published by Holt 

Rinehart & Winston Harcourt Education 

Company.

3. Peter H. Raven, George B. Johnson, Kenneth 

A. Mason, Jonathan B. Losos, Susan R. Singer 

(2013) Biology 9th Edition. Published by 

McGraw-Hill Science.



(Basis of classification) 

20

• 

• 



21



22



23



24





26

àôè‹

ªê™ Ü÷Mô£ù¶ ¶¬÷àìLèœ

Ýóêñ„Y˜

Þ¼ð‚è
êñ„Y˜

î†¬ì ¹¿‚èœ

à¼¬÷Š ¹¿‚èœ

õ¬÷î¬ê ¹¿‚èœ
èμ‚è£Lèœ
ªñ™½ìLèœ
º†«î£Lèœ
Ü¬óï£Eèœ
º¶° ï£Eèœ

àìŸ°NòŸø¬õ

°N»ìLèœ
(G«ìKò£)

¯«ù£ç«ð£ó£

«ð£L àìŸ°N
à¬ìò¬õ

à‡¬ñò£ù
àìŸ°N
à¬ìò¬õ

F² / àÁŠ¹ /
àÁŠ¹ ñ‡ìô
Ü÷Mô£ù¶.

Môƒ°ôè‹
(ðô ªê™

à¬ìò¬õ)

êñ„Yó¬ñŠ¹ ªî£°Fè†ì¬ñŠ¹G¬ôèœ àìŸ°N



27

Cordates - Invertebrata)



28



29



30



31



32



33



34



35

 

î¬ê
è‡ìƒèœ º¶°ï£‡

õ£Œªî£‡¬ìŠ
H÷¾èœ

ñôŠ¹¬öî¬êò£ô£ù
ñôŠ¹¬öJ¡
H¡ õ£™

º¶°¹ø
ïó‹¹‚°ö™



36

ª
î
£°

F
:

º
¶
°

ï£
E

è
œ

HK
¾
:-

¹«
ó£
«ì

£è
£˜
«ì

†
ì
£

H
K¾

: 
-

º
¶
ª
è
½
‹
H
è
œ

¶
¬
í

ˆ
 ª

î
£°

F
:

ñ
‡

¬
ì
«ò

£ì
Ÿø

¬
õ

¶
¬
í

ˆ
 ª

î
£°

F
:

î
£¬

ì
è
œ

Ü
Ÿ
ø
¬
õ

¶
¬
í

ˆ
 ª

î
£°

F
:

î
£¬

ì
è
œ

à
¬
ì
ò
¬
õ

Ý
‹
ç
H
ò
£‚

ú
v
,

Ü
C
®
ò
¡

õ
°
Š¹
:

õ
†
ì
õ
£J

¬
ù
 

à
¬
ì
ò
¬
õ
.

C
ø
Š¹
 õ

°
Š¹
:

e
¡
è
œ

C
ø
Š¹
 õ

°
Š¹
 -

ï£
¡
°
 è

£L
è
œ

(â
.è
£.
) 
«ô

‹
Š«

ó
õ
°
Š¹
:

°
¼
ˆ
ª
î
½
‹
¹

e
¡
è
œ

õ
°
Š¹
:

â
½
‹
¹ 
e
¡
è
œ

õ
°
Š¹
:

Þ
¼
 õ

£›
M
è
œ

õ
°
Š¹
:

á
˜õ

ù
õ
°
Š¹
:

ðø
Šð
ù

õ
°
Š¹
:

ð£
Ö

†
®
è
œ

(â
.è
£.
) 
²
ø
£

(â
.è
£.
)

 Ì
¬
ù
, 
e
¡

(â
.è
£.
)

î
õ
¬
÷
, 
«î

¬
ó,

ê
ô
ñ
£‡

ì
˜

(â
.è
£.
) 
æ
í

£¡
,

ð™
L
, 
ð£
‹
¹,

è
ì
™
 Ý

¬
ñ
,

º
î
¬
ô
.

(â
.è
£.
) 

C
†
´
‚
°
¼
M
, 

¹ø
£

(â
.è
£.
) 
â
L
,

º
ò
™
, 
ª
õ
÷
õ
£™

,
F
I
ƒ
è
ô
‹
,

ñ
Q
î
¡
,



37



38

ªî£‡¬ì
ªê¾œ
H÷¾èœ

ã†Kò™
¶¬÷

Í¬÷Š
¬ð ïó‹¹ õì‹

õ£Œ
c†C

õ£Œ Þù
àÁŠ¹èœ

ñôŠ¹¬ö

º¶°
ï£‡



39



40



41



42



43

èì™ Ý¬ñ Gô Ý¬ñ

èì™ Ý¬ñèœ ªð¼‹ð£½‹ õ£›¬õ cK™ 
Ü™ô¶ c¼‚° Ü¼A™ èN‚A¡øù. «ñ™ 
æ´ ð‚èõ£†®™ î†¬ìò£A ðì° õ®õ‹ 
ªðŸÁœ÷¶. ªð¼‹ð£½‹ ¶´Š¹ «ð£¡ø 
è£™è¬÷‚ ªè£‡´œ÷ù.

Gô Ý¬ñèœ ªð¼‹ð£ô£ù õ£›ï£¬÷ 
GôˆF™ èN‚A¡øù. «ñ™ æ´ «è£¹ó 
õ®Mô£ù¶. Mó™èÀ¬ìò CPò 
°†¬ìò£ù õ¬÷‰î è£™è¬÷ 
ªè£‡´œ÷ù.



44



45



46

ð£Ö†®èœ ðø¬õèœ

á˜õù Þ¼õ£›Mèœ

e¡èœ

8%

11%

16%

15%

50%

ªñ™½ìLèœ Aóv«ìSò¡èœ

Üó£‚Q†èœ Hø

Ì„Cèœ

5%
8%

4%

7%

77%

M÷‚èŠð†ì
º¶ªè½‹ðŸø¬õèO¡ ªñ£ˆî

â‡E‚¬è 2014 (IUCN ð®)

18%

3%

75%

4%

àôè CŸPùƒèÀì¡ Þ‰Fò
ð™½J˜ˆ î¡¬ñ åŠ¹«ï£‚°î™

àôè CŸPùƒèœ Þ‰Fò CŸPùƒèœ

6%

94%

M÷‚èŠð†ì CŸPùƒèO¡
ªñ£ˆî â‡E‚¬è

2014 (IUCN ð®)

º¶ªè½‹¹¬ìòù

º¶ªè½‹ðŸøù

î£õóƒèœ

Ì…¬êèœ ñŸÁ‹
¹«ó£®v´èœ

M÷‚èŠð†ì º¶ªè½‹HèO¡
ªñ£ˆî â‡E‚¬è

2014 (IUCN ð®)



47

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 



48



49

M
ô
ƒ
°
ô
è
 õ

¬
è
Šð
£´

î
¬
ô
ï£
‡

 à
J
Kè

œ
õ
£™

ï£
‡

 à
J
Kè

œ
õ
†
ì
 õ

£J
¬
ù

à
¬
ì
ò
¬
õ

°
¼
ˆ
ª
î
½
‹
¹ 
e
¡
è
œ

â
½
‹
¹ 
e
¡
è
œ

Þ
¼
õ
£›

M
è
œ

á
˜õ

ù
ðø

¬
õ
è
œ

î
£¬

ì
ò
Ÿ
ø
¬
õ

ð£
Ö

†
®
è
œ

e
¡
è
œ

î
£¬

ì
è
À

¬
ì
ò
¬
õ

ï£
¡
°
 è

£L
è
œ

º
¶
°
ï£
‡

 à
J
Kè

œ

¶
¬
÷
»
ì
L
è
œ

Ýó„êñ„Y˜G
«ì

Kò
£

¯
«ù

£ç
«ð

£ó
£

î
†
¬
ì
Š

¹¿
‚
è
œ

à
¼
¬
÷
Š

¹¿
‚
è
œ

õ
¬
÷
î
¬
ê
Š

¹¿
‚
è
œ

Ý
˜ˆ

«ó
£«
ð£
ì
£

ª
ñ
™
½
ì
L
è
œ

º
†
«î

£L
è
œ

Ü
¬
óï
£‡

à
J
Kè

œ

ßó£ó êñ„Y˜

àìŸ°NòŸøù

«ð£L 
àìŸ°

N

à¬ìò
¬õ

à‡¬ñ
àìŸ°N
à¬ìòù

¹«
ó£
†
«ì

£v
«ì

£I
ò
£

¬
ê«
û
£Y
«ô

£«
ñ
†
ì
£

è
‡
ìñ

£‚
è
‹

®
Î
®
«ó
£v

«ì
£I

ò
£

â
¡
®
«ó
£Y
«ô

£«
ñ
†
ì
£

Þ
¼
ð‚

è
 ê

ñ
„
Y˜
  
à

¬
ì
ò
ù

(Í
õ
´
‚
°
 à

J
Kè

œ
)

Î
ª
ñ
†
ì
£«
ê
£õ

£

ª
ñ
†
ì
£«
ê
£õ

£

«ó
®
«ò

†
ì
£ 
(ß
ó´
‚
°
 à

J
Kè

œ
)

ð£
ó«
ê£
õ
£

à
ô
è
‹
 M

ô
ƒ
°
ô
è
‹

49



50

Cladogram

* 



51

 
 (Glossary)

  



52



53



54

  
1. Jordan E. L.   and  Verma P.S. (2001) Invertebrate Zoology Revised Edition, Published by S. 

Chand Publications.

2. Darrell S. V and  R Moore (2004)  Biology: Laboratory Manual 7th Edition. McGraw-Hill 

College.

3. Kotpal R. L. (2014) Modern Text Book of Zoology: Vertebrates. Rastogi Publications.

4. Kotpal R.L. (2014) Modern text book of zoology : Invertebrates : animal diversity- I. 11th 

Edition. Meerut : Rastogi Publications.



Learning Objectives:

• 

• 

• 

55



56



57



58



59

ðô Ü´‚°
ªê™èœ



60



61

 



62



63





65



66



67



68

The Online Epithelium

* 



69

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



70



• 

• 

• 

)
(Earthworm- Lampito mauritii)

71



72

Worm 

castings

(Annelida)

(Oligochaeta)

(Haplotaxida)

(Lampito)

(mauritii)



73

(Morphology)

(Peristomium)

(Prostomium) 

(Pygidium)

(Clitellum)



74



75

 
 

 
 

 
 

 

 

 

 
 

3

2

1

(Microchaetus rappi)

(Drawida nilamburansis) 



76

(Buccal cavity)

(Pharynx)

(Oesophagus)

 (Gizzard) 

 

(Intestine)

22



77

(Commissural 

vessels)  (Lateral 

hearts) 

(Typhlosole)

(Vermicasts)



78

(Photo 

receptors)

(Gustatory receptors)

( Olfactory receptors)

 (Tactile 

receptors)  (Chemo receptors) 

 (Thermo receptors) 

(Supra- pharyngeal ganglia)

(Sub - pharyngeal ganglia)



79

 (Meganephridia or septal 

nephridia)

(Pharyngeal or tufted nephridia)

 (Micronephridia or  

Integumentary nephridia)



80

 (Chloragogen cells) 



81

(Protandrous)

 (Ciliary rosettes)

(Vasa deferentia)

(Spermathecae)

 (cocoon)

(Juveniles)



82

Wormery

 (Vermitech) 

 (Vermiculture)

 (Vermicomposting)

 (Vermiwash) 

(wormbin)



83

 
)

(Cursorial)

(Vectors)

(Tergites)

(Sternites)

 (Pleurites)

(Hypognathous)

(Labrum)

(Mandibles)

 (Maxillae),

(Labium) (Hypopharynx

Lingua)

(Prothorax) (Mesothorax) 

(Metathorax)

(Cervicum) 

1



84

(hexapoda) (hexa poda 

 
 

 

 
 

 (brood or genital pouch) 

 (gonopore), 

 (spermathecal pores) 

 (ootheca)

 (genital pouch) 

(Gonapophysis)

(anal styles) 

 (anal cerci)



85

 (gynovalvular plates) 

(anal style)

(brood pouch /genital 

pouch)

 (antenna)



86

(hepatic 

caecae/ enteric caecae)

(Malpighian 

tubules)



87

 (trachea)

 (spiracles) 

 (Stigmata)

(tracheoles)

  

  

 (Haemolymph) 

(Haemocytes) 

 (Ostia)

(Sinuses)



88

 (Pulsatile Vesicle) 

 (Supra 

oesophageal ganglion)

(Sub – oesophageal ganglion)

(circum-

oesophageal ring)

(Ganglionated double ventral nerve cord) 

 (sensory),

 (endocrine centre)



89

(Thigmo receptor)

(Thermo 

receptors)

(Chordotonal receptor) 

(Photo receptor organ)

(ciliated cells)

CO2



90

(Utricular gland)

(Conglobate / phallic 

gland)

 (seminal vesicles)

(vagina)  (Genital 

pouch), 

(Spermatheca)

(Ovipositor)



91

(Parametabolus)



92

 

Oriental Cockroach
Brown-banded Cockroach 

German Cockroach

 
 

American Cockroach)

 

 

Viviparous Cockroach

 
 

• 

• NCICAS

• 

 

 

 
 



93

(Cloaca)



94



95

ï£‚°

«õ£ñ¬ó¡
ðŸèœ

 

«ñ™ î£¬ìŠ
ðŸèœ

 ï£Cˆ¶¬÷
G‚®«ì®ƒ

êš¾
 

ªêMŠð¬ø
êš¾

 

àí¾‚ °ö™

A÷£†®v



96

(Buccal respitation) 

(Pulmonary respiration)

(Aestivation)

(Hibernation)

(Cutaneous respiration)



97

CvìI‚ îñQ

î¬ô îñQ

¸¬ófó™
«î£™îñQ

¸¬ófó™ «î£™
îñQJ¡ FøŠ¹

«è£ùv Ý˜¯K«ò£êv

õô¶ ÝK‚Aœ

H¬ø„ ê‰Fó õ£™¾

ªõ¡®K‚Aœ

Þì¶ ªð¼ˆîñQ

õô¶ ªð¼‰îñQ
¸¬ófó™ C¬óˆ FøŠ¹

¬êÂ ÝK°ô£˜ ¶¬÷

ÝK‚°ô£˜ Þ¬ì„²õ˜

²¼œ õ£™¾ Þì¶ ÝK‚Aœ

ÝK‚°«ô£ ªõ¡†K°«ô£˜
õ£™¾

è£˜«ìªì¡®«ù



98

 (CNS)

(PNS)

(ANS).

(Prosencephalon)



99



100

(Mesencephalon)

(Optic ventricles)

(Rhombencephalon)

(Mesorchium)

(Mesovarium)

(Ostia)

 (tadpole) 



101

ºF˜‰î
îõ¬÷

º†¬ìèœ

è¼

Þ÷‹
îõ¬÷

õ£½œ÷
îõ¬÷

 

º¡ùƒè£™
G¬ô

 

H¡ùƒè£™
G¬ô

 

à†ªê¾œ
G¬ô

 

ªõO„ªê¾œ
G¬ô

 
îõ¬÷J¡ õ÷˜

à¼ñ£Ÿø‹
 



102

  





104

è
¼
ˆ
¶
 õ

¬
óð
ì
‹

«î
£™

 õ
N

²
õ
£ê
‹

«î
£™

²
õ
£ê
‹
, 
õ
£Œ

‚
°
N
 ²

õ
£ê
‹

ñ
Ÿ
Á
‹
 ¸

¬
óf

ó™
 ²

õ
£ê
‹

ª
î
£‡

¬
ì
 «

ñ
™

ïó
‹
¹ 
ª
ê
™

F
óœ

è
œ

ïó
‹
¹ 
õ
¬
÷
ò
‹
,

ïó
‹
¹ 
ª
ê
™

F
ø
¡

ñ
ˆ
F
ò
 ï

ó‹
¹ 
ñ
‡

ì
ô
‹
, 
¹ø

 ï
ó‹

¹
ñ
‡

ì
ô
‹
 ñ

Ÿ
Á
‹
 î

£Q
ò
ƒ
A
 ï

ó‹
¹

ñ
‡

ì
ô
‹

ª
ïç

Šg
®
ò
ƒ
è
œ

ñ
™
H
T
ò
¡

¸
‡

°
ö
™
è
œ

e
«ê

£ª
ïç

ŠK
‚
, 
Î
K«

ò
£ª

ì
L
‚
 õ

¬
è

Þ
¼
ð£
™

à
J
Kˆ

î
¡
¬
ñ

ð£
™
 õ

N
 Þ

¼
«î

£Ÿ
ø
‹

ð£
™
õ
N
 Þ

¼
 «

î
£Ÿ
ø
‹
, 
õ
÷
˜

à
¼
ñ
£Ÿ
ø
‹
 à

œ
÷
¶

 G
‚
®
«ì

®
ƒ
 ê

š
¾
 ñ

Ÿ
Á
‹
 ª

ê
M
Šð
¬
ø

ª
ð£
¶
 è

N
õ
¬
ø
ˆ
¶
¬
÷

Ü
¬
ó¬

õ
Š¬

ð,
®
Š«

÷
£«
ê
£™

b
Q
Š¬

ð,
Ü
¬
ó¬

õ
Š¬

ð

ã
ô
Kˆ

 
î
¬
ê
è
œ

â
½
‹
¹ˆ

î
¬
ê
è
œ
, 
ª
ñ
¡
î
¬
ê
è
œ

ñ
Ÿ
Á
‹
 Þ

î
ò
ˆ
 î

¬
ê
è
œ

ª
ðK
v
«ì

£I
ò
‹

A
¬
÷
ª
ì
™
ô
‹

(¹
í

˜ 
î
®
Š¹
)

à
ì
™
 Y

†
«ì

ñ
ô
Š¹
¬
ö

å
ˆ
î
 Ü

¬
ñ
Š¹
¬
ì
ò

è
‡

ì
ƒ
è
œ

î
¬
ô
, 
ñ
£˜
¹,
 õ

J
Á

Ã
†
´
‚
 è

‡
è
œ

è
®
ˆ
¶
 ª

ñ
™
½
‹
 õ

¬
è

¹ø
„
ê
†
ì
è
‹

²
õ
£ê
 ñ

‡
ì
ô
‹

Þ
¬
í

Š¹
 Þ

î
ò
‹

(Ü
) 
ð‚

è
õ
£†

´
Þ
î
ò
‹

Ý
v
®
ò
‹

ª
ð¼

‰î
ñ
Q
, 
Í
¡
Á
 î

ñ
Q
 õ

¬
÷
¾
è
œ

à
†
è
¼
 ª

è
£‡

ì
 C

õ
Šð
μ

‚
è
œ

²
Ÿ
«ø

£†
ì

ñ
‡

ì
ô
‹

ª
ê
Kñ

£ù
ñ
‡

ì
ô
‹

ïó
‹
¹ 
ñ
‡

ì
ô
‹

è
N
¾
 c

‚
è

ñ
‡

ì
ô
‹

Þ
ù
Šª

ð¼
‚
è
‹

à
œ
À

Á
Š¹
è
œ

à
Á
Š¹
 ñ

Ÿ
Á
‹
 à

Á
Š¹
 ñ

‡
ì
ô
‹

ñ
‡

¹¿
è
óŠ
ð£
¡
Ì
„
C

î
õ
¬
÷

î
¬
ê
ò
¬
ñ
Š¹

cœ
õ
£‚

°
,

õ
†
ì
ˆ
î
¬
ê
è
œ

¹ø
 Ü

¬
ñ
Š¹
 /

¹ø
ˆ
«î

£Ÿ
ø
‹

v
¬
ðó
A
œ

²
õ
£ê
ˆ
¶
¬
÷

 ª
ñ
¡
¬
ñ
ò
£ù

, 
õ
¿
õ
¿
Šð
£ù

 «
î
£™

î
¬
ô
 ñ

Ÿ
Á
‹
 à

ì
™

î
¬
ê
ò
£ô

£ù
 å

†
´
‹
 î

¡
¬
ñ
»
¬
ì
ò

ï£
‚
°
, 
«ñ

™
î
£¬

ì
 ð
Ÿ
è
œ
 ñ

ø
Á
‹

«õ
£ñ

¬
ó¡

 ð
Ÿ
è
œ
, 
è
™
h
ó™

, 
è
¬
í

ò
‹



105

 
-

-

-

-

-
-

-
-

-

-

-

-

-

-



106

-

-
-
-

-

-

-

-

-

-
-

-

-

  



107



108

  
1. Ekambaranatha Ayyar, Anantha 

Krishnan, 5th Edition- (1987); Manual 

of Zoology, Vol I Invertebrata  - 

S.Viswanathan Publishers and 

Printers Pvt. Ltd.,

2. Ekambaranatha Ayyar, Anantha 

Krishnan, 5th Edition- (1987); 

Manual of Zoology, Vol II Chordata 

–S.Viswanathan Publishers and 

Printers Pvt. Ltd.,

3. Jordan E. L, Verman P. S, Revised 

Edition- (2009); Invertebrate Zoology, 

S. Chand & Company Ltd.,

4. Kotpal R. L , (2012), Modern text book 

of Zoology; Vertebrates [Diversity – 

II] – 3rd Edition; Rastogi Publications.

5. John H.  Postlethwait and Janet L. 

Hopson ; Holt, Rinehart and Winston, 

Modern Biology; A Harcourt Education 

Company, Orlando. Austin. NewYork. 

San Diego. Toronto. London.

6. Sultan Ismail, A (1992), The 

Earthworm Book, Other India Press, 

India.



Learning Objectives:

• 

• 

• 

• 

• 

109



110

 
(Digestive system)

(Structure of the alimentary canal)



111



112



113

ãÁ
ªð¼ƒ°ì™

ÞL«ò£
Y‚è™ î¬ê

(õ£™¾)

°ì™
H¶‚è‹

°ì™ õ£™

ñôˆ¶¬÷

H¡CÁ°ì™

ñô‚è£™õ£Œ

ñô‚°ì™

C‚ñ£Œ´ °ì™

ªð¼ƒ°ì™
ñ®Š¹

Þøƒ°
ªð¼ƒ°ì™

கிைடமட்ட ªð¼ƒ°ì™



114

 
(Digestive glands)(Histology of the Gut)





116



117

àí¾‚°ö™

è£˜®ò£‚ ²¼‚°ˆ
î¬ê

¬ð«ô£K‚
²¼‚°ˆ

î¬õ

CÁ°ì™
Þ¬óŠ¬ð ñ®Š¹èœ

Þ¬óŠ¬ð
âHbLò‹

ªðŠR«ù£ü¡ ªðŠRœ

HCI

Cl-
H+

1. ªðŠR«ù£üÂ‹
     HCI ‹ ²ó‚èŠð†ì¶.

2. HCI ªðŠR«ù£ü¬ù
   ªðŠCù£è ñ£ŸPò¶.

3. ªðŠR¡ «ñ½‹
   ªðŠC«ù£ü¬ùˆ É‡´Aø¶.

ºî¡¬ñ ªê™

²õ˜ ªê™

1

2



118



119

 



120

1

4

7

7

8

9

9

1

2

5

8

2

3

4

5

6

6



121

  (Absorption and assimilation of proteins, 

carbohydrates and fats)

 

  

  

1.  

2.  



122

 

)



123



124



125

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



126

Let's Digest

Do you 
know?

ctions called peristalasis.

u know? The liver is also 
portant detoxification 

It helps to filter and 
e harmful toxins from
dy.

ou know? 
intestine is lined

mucosa, a layer of
e that helps to
b nutrients,

uce digestive
mes, and make
s to protect the

ate intestinal wall.

Fun fact:
There are two kinds of fib
both support a healthy co

Soluble 
fibre soaks 
up toxins 
and waste 
in the 
digestive 
system

Insolube fib
(”roughage
bulk throug
intestine to
with  regula
bowel mov

adder stores 
cretion.

Protease
Helps 
digest
protein

Lipase
Helps 
digest
fats

Amy
Helps
carbo

er secrete bile. Bile helps 
mall intestine by breaking 

s fats and making them 
to absorb.

 intestine: 

of the nutrients form 
are digested
bsorbed in the 
intestine.

e intestine (Colon):

of the bacteria living
digestive tract

e found in the large
ine. This is where
gestive process
s to an end.

stomach acid from going
(refluxing) into the oesop

Stomach: 

Gastric juice contain HCl 
gastric enzymes.

Hydrochloric acid (HCl) h
digest proteins and othe
by pepsin enzymes  while
minimizing harmful bact

Pancreas

The pancreas is connecte
duodenum where three  
digestive enzmyes are m

Up to 70% of our natural immun
system support is in the digestive e are more then 

0 trillion

7

8

9

9

5

8

2

3

4

5

6

6

* 



127

.

  

 

 



128



129

è
£˜
®ò

£‚
ð°

F

çð
‡

®‚
ð°

F

¬
ð«

ô
£K
‚

ð°
F

H¡
C
Á
°
ì™

Þ
¬
ì„

C
Á
°
ì™

º
¡

C
Á
°
ì™

ªð
¼
ƒ

°
ì™

ãÁ
 ª

ð¼
ƒ
°
ì™

è
¬
í

ò
‹

è
™
h
ó™

à
I
›
c˜

²ó
ŠH

è
œ

ªê
Kñ

£ù
²ó

ŠH
è
œ

°
ì™

õ
£™

ý
£v

†ó
£

âÂ
‹

¹¬
ìŠ

¹è
œ

ñ
ô
ˆ
¶
¬
÷

ªð
¼
ƒ
°
ì™

C
Á
°
ì™

 H
ó¡

ù
K¡

²ó
ŠH

è
œ
 ñ

ŸÁ
‹

L
ð˜
è
Q
¡
 ñ

®Š
¹è

À
‹

ê‚
è
v

â¡
ªì

Kè
v

²ó
ˆ
î
™

Þ
óŠ
¬
ð

²ó
ŠH

è
œ

Þ
¬
óŠ
¬
ð

à
í

¾
‚
°
ö
™

ªê
Kñ

£ù
ñ
‡

ìô
‹

ªî
£‡

¬
ì

à
í

¾
‚

°
ö
™

õ
£Œ

ï£
¡
°

Ü
´
‚
°
è
œ

õ
£Œ

‚
°
N

à
I
›
c˜

ªï
£F

è
œ

(ì
ò
L
¡
)

«è
£¬

ö
‚
W
›

Ü
´
‚
°

î
¬
êò

´
‚
°

Y«
ó£
ê£

«è
£¬

ö
ò
´
‚
°

ªñ
™
½
î
™

ðŸ
è
œ
,

ï£
‚
°

A
¬
ìñ

†ì
ªð

¼
ƒ
°
ì™

Þ
øƒ

°
ªð

¼
ƒ
°
ì™

C
‚
ñ
£Œ

´
ªð

¼
ƒ
°
ì™

ñ
ô
‚
°
ì™

°
ì™

H¶
‚
è
‹

Þ
ò
‚
è

ªê
Kñ

£ù
‹

By
By

«õ
F

ªê
Kñ

£ù
‹

è
¼
ˆ
¶
 õ

¬
óð
ì‹



130

 (Glossary)



131



132

A

B

CD

E



133

Multiple interactive informational activities 
and resources 

http://www.bbc.co.uk/science/humanbody/ 

Interactive tour of the digestive tract  http://www.medtropolis.com/VBody.asp 

United States Department of Agriculture 
web site on nutrition; resources on dietary 
guidelines; food pyramids; recipes for 
healthy eating 

http://www.usda.gov/cnpp/ 

  

1. Guyton and Hall. J. E, (2006) Textbook 

of Medical Physiology- Eleventh 

 Edition Elsevier saunders. International 

Edition.

2. Brooker et.al. (2008), Biology Volume 

two Plants and Animals, The MacGraw 

Hill companies,inc.

3. Elaine N. and Katja (2010). Human 

Anatomy and Physiology Eighth 

Edition, Benjamin Cummings, 

Pearson. New York.



Learning Objectives:

• 

• 

• 

• 

• 

134



135

(Respiratory functions)



136



137



138

2 2

2 2

2 2



139

è£ŸÁ
àœO¿‚èŠð´î™

è£ŸÁ
ªõO«òŸøŠð´î™

MK‰î G¬ôJ™
Mô£ â½‹¹‚Ã´

²¼ƒAò G¬ôJ™
Mô£ â½‹¹‚Ã´

¸¬ófó™

àîóMî£ù‹

à†²õ£ê‹ ªõO„²õ£ê‹

(Mechanism of breathing)



140

(Respiratory volumes and capacities)



141

°¬ø‰îð†ê ªè£œ÷÷¾
(30&120 IL)

ªè£œ÷÷¾
(I.L)

æŒ¾G¬ô Í„²‚
è£Ÿø÷¾

(VT = 500 ml)

ªõO„²õ£ê
«êIŠ¹‚

ªè£œ÷÷¾
(ERV)

â…Cò
ªè£œ÷÷¾

à†²õ£êˆ
Fø¡

àJ˜Š¹ˆ
Fø¡

ªêò™ð´‹
â…Cò

ªè£œ÷÷¾

à†²õ£ê
«êIŠ¹‚

ªè£œ÷÷¾
(IRV)

•

•

•



142

2

2

•

}
•

 
(Exchange of gases)



143

 
(Respiratory Pigments)

(Transport of gases)



144

CO2 + Hb  Hb CO2



145

CO2 + H2O  H2CO3

H2CO3  HCO3
– + H+



146

(Regulation of respiration)

transport)



147147

(Disorders of Respiratory system)





149149



150



151

Respiratory System’s 

 

Respiration

* 



152

²
õ
£ê
‹
 ï

¬
ì
ª
ðÁ

‹
M
î
‹

ñ
£˜
ð¬

ø
J
™
 «

î
£¡

Á
‹

Ü
¿
ˆ
î
 «

õ
Á
ð£
´
è
÷
£™

à
†
²
õ
£ê
‹
 ñ

Ÿ
Á
‹

ª
õ
O
„
²
õ
£ê
‹

ï¬
ì
ª
ðÁ

A
ø
¶
.

 

à
î
óM

î
£ù

‹
, 
ª
õ
O
M
ô
£

â
½
‹
H
¬
ì
ˆ
 î

¬
êè

œ
ñ
ŸÁ

‹
 à

œ
M
ô
£

â
½
‹
H
¬
ì
ˆ
 î

¬
êè

œ
«ð

£¡
ø¬

õ
 ²

¼
ƒ
A

M
Kî

ô
£™

 ñ
£˜
ð¬

ø‚
ª
è
£œ

÷
÷
¾
 °

¬
øò

«õ
£

Ü
™
ô
¶
 Ã

ì
«õ

£ 
ª
êŒ

A
ø¶

.

ñ
£˜
ð¬

ø
 ²

¼
ƒ
°
î
™

Ü
™
ô
¶
 M

Kõ
¬
ì
î
ô
£™

²
õ
£ê
„
ª
ê
ò
™

ï¬
ì
ª
ðÁ

A
ø
¶
.

à
†
²
õ
£ê
‹

Þ
¶
 å

¼
 ª

ê
ò
™
I
°

G
è
›
„
C
ò
£î

ô
£™

è
£Ÿ
ø
£ù

¶
 ¸

¬
óf

ó™
è
À

œ
ª
ê
™
A
ø
¶
.

ª
õ
O
M
ô
£

â
½
‹
H
¬
ì
ˆ
 î

¬
ê
è
œ

²
¼
ƒ
°
õ
î
£™

 M
ô
£

â
½
‹
¹è

œ
 «

ñ
Ÿ
¹ø

ˆ
F
½
‹
,

ª
õ
O
«ï

£‚
A
»
‹

Ü
¬
ê
A
¡
ø
ù
.

 

à
î
óM

î
£ù

„ 
²
¼
‚
è
ñ
£ù

¶
e
œ
î
¡
¬
ñ
ò
Ÿø

, 
«ñ

Ÿ°
M
‰î

à
î
óM

î
£ù

ˆ
F
¡

¬
ñ
ò
Šð
°
F
 î

†
¬
ì
ò
£A

ø¶
.

ª
õ
O
„
²
õ
£ê
‹

Þ
¶
 å

¼
 ñ

‰î
ñ
£ù

ª
êò

ô
£î

ô
£™

¸
¬
óf

ó™
è
O
½
œ
÷
 è

£Ÿ
Á

ª
õ
O
«ò

Ÿø
Šð
´
A
ø¶

.

à
î
óM

î
£ù

‹
 î

÷
˜‰
¶

e
‡

´
‹
 î

ù
¶
 «

ñ
Ÿ
°
M
‰î

Ü
¬
ñ
Š¬

ð 
Ü
¬
ì
A
ø
¶
.

à
œ
M
ô
£

â
½
‹
H
¬
ì
ˆ
î
¬
êè

œ
²
¼
ƒ
°
õ
î
£™

 M
ô
£

â
½
‹
¹è

œ
 ð
¬
ö
ò

G
¬
ô
‚
°
ˆ
 F

¼
‹
¹A

¡
øù

.

è
¼
ˆ
¶
 õ

¬
óð
ì
‹

Ý
. 
à

î
óM

î
£ù

‹
«ñ

™
«ï

£‚
A

è
£Ÿ
¬
ø

à
œ
O
½
ˆ
î
™

è
£Ÿ
Á

ª
õ
O
M
´
î
™

«ñ
™
«ï

£‚
A
ò

M
ô
£ 
â
¿
‹
¹è

œ

W
N
ø
ƒ
A
ò
 M

ô
£

â
½
‹
¹è

œ

Ü
. 
à

î
óM

î
£ù

‹
W
›
«ï

£‚
A



153

²
õ
£ê

ñ
‡

ì
ô
‹

ï£
C

ï£
C
Šð
œ
÷
‹
,

õ
£Œ

‚
°
N

 
ª
î
£‡

¬
ì

°
ó™

õ
¬
÷

Í
„
²
‚
°
ö
™

Í
„
²
‚

A
¬
÷
‚

°
ö
™
è
œ

 

Þ
ó‡

ì
£‹

 G
¬
ô

Í
„
²
‚

A
¬
÷
‚
°
ö
™
è
œ

Í
¡
ø
£‹

 G
¬
ô

Í
„
²
‚

A
¬
÷
‚
°
ö
™
è
œ

I
è
„
C
P
ò

Í
„
²
‚

A
¬
÷
‚
°
ö
™
è
œ

¸
‡

 Í
„
²
‚

A
¬
÷
‚
°
ö
™
è
œ

º
®
¾
 ¸

‡
Í
„
²
‚

A
¬
÷
‚
°
ö
™ 

²
õ
£ê
 ¸

‡
Í
„
²
‚

A
¬
÷
‚
°
ö
™

è
£Ÿ
Á

¸
‡

í
¬
ø
è
œ

è
£Ÿ
Á
 ¸

‡
í

¬
ø
è
O
¡
 ²

õ
˜ 
: 
æ
ó´

‚
°
 â

O
ò
 î

†
¬
ì

â
H
b
L
ò
‹
 Ü

F
è
ð†

ê
 ¹
ø
Šð
óŠ
¹ 
ñ
Ÿ
Á
‹
 °

¬
ø
‰î

 M
óõ

™
 

ª
î
£¬

ô
¾
.

Í
„
²
‚
°
ö
™

°
¼
ˆ
ª
î
½
‹
¹ 
õ
¬
÷
ò
ƒ
è
œ

°
¼
ˆ
ª
î
½
‹
¹ 
î
†
´
è
œ

Þ
ì
¶
 º

î
Q
¬
ô

Í
„
²
‚
 A

¬
÷
‚
°
ö
™

Þ
ó‡

ì
£‹

 G
¬
ô

Í
„
²
‚
 A

¬
÷
‚
°
ö
™

Í
¡
ø
£‹

 G
¬
ô

Í
„
²
‚
 A

¬
÷
‚
°
ö
™

C
P
ò
 Í

„
²
‚
 A

¬
÷
‚
°
ö
™

Í
„
²
‚
A
¬
÷
 ¸

‡
°
ö
™

º
®
¾
 Í

„
²
‚
A
¬
÷

¸
‡

°
ö
™

²
õ
£ê
 Í

„
²
‚
A
¬
÷

¸
‡

°
ö
™

¸
¬
óf

ó™
 ¸

‡
è
¶
ŠH

™
è
£Ÿ
Á



154

  

 (Glossary)



155



156



157

  
1. Guyton A.C. and Hall. J. E, (2006) Textbook 

of Medical Physiology– Eleventh Edition 

Elsevier Saunders, International Edition 

ISBN 0–8089–2317–X.

2. Mackean D.G. and Hayward D 

(2014). AS and A level biology book, 

Cambridge International, 3rd edition, 

Hodder Education, An Hachette UK 

company, London NWI 3BH.

3. Dee Unglaub Silverthron, Human 

physiology –an integrated approach – 

7th Edition – Pearson Global edition.

4. Elaine N. Marieb and Katja Hoehn 

(2010). Human Anatomy and 

Physiology Eighth Edition, Benjamin 

Cummings, Pearson. New York.

5. Lauralee Sherwood and Robert kell.

(2007). Human physiology from cells 

to systems. First Canadian Edition 

Nelson Education Ltd, Toronto, Ontario  

MIK SG4.

6. Moyes and Schulte, 2016 Principles 

of Animal Physiology– 2 nd edition, 

Pearson

7. Muthayya N.M., 2010 Human 

 physiology– 4th edition, Jaypee brother 

medical publishers.

http://kidshealth.org/kid/closet/movies/

how_the_body_works_interim.html

(Competitive Exam Corner)



Learning Objectives:

• 

• 

• 

• 

• 

• 

158



159



160



161

 



162



163

 



164

+

+

+

+

 A A
B B

AB AB

O



165

àœ÷£˜‰î à¬øî™ ªêò™º¬ø

¹«ó£ˆó£‹H¡ Fó£‹H¡
Ýè ñ£ŸøŠð´î™

F²„«êî‹

É‡ì™

î¬ê Þ¿Š¹
Þóˆîˆî†´è÷£™
Ü¬ìŠ¹ ãŸð´î™

¹«ó£ˆó£‹H¬ù„ ªêò™ðì
¬õ‚°‹ ªð£¼œ àŸðˆF

ç¬ðŠK«ù£ü¡ è¬óò£î
ç¬ðŠK¡ Þ¬öè÷£è ñ£Áî™

Fó£‹H¡ Ýù¶
è¬ó»‹ ç¬ðŠK«ù£ü¡

e¶ ªï£Fò£è
ªêò™ð´î™

è£òñ¬ì‰î ÞìˆF™
ç¬ðŠK¡ Þ¬öèœ à¼õ£A

Þóˆî ªê™è¬÷Š C‚è¬õˆî™
(è£ò‹ Ü¬ìð´î™) 



166

  



167

®ÎQ‚è£ â‚vì˜ù£

®ÎQ‚è£ e®ò£

®ÎQ‚è£ Þ¡®ñ£

â¡«ì£bLò‹

®ÎQ‚è£ â‚vì˜ù£

®ÎQ‚è£ e®ò£

®ÎQ‚è£ Þ¡®ñ£

â¡«ì£bLò‹

®ÎQ‚è£ â‚vì˜ù£

®ÎQ‚è£ e®ò£

®ÎQ‚è£ Þ¡®ñ£

â¡«ì£bLò‹

®ÎQ‚è£ â‚vì˜ù£

®ÎQ‚è£ e®ò£

®ÎQ‚è£ Þ¡®ñ£

â¡«ì£bLò‹

®ÎQ‚è£ â‚vì˜ù£

â¡«ì£bLò‹

®ÎQ‚è£ â‚vì˜ù£

â¡«ì£bLò‹

â¡«ì£bLò‹

ªðKò C¬ó

C¬ó

¸‡C¬ó

Þóˆî ¸‡ ï£÷‹

eœ î¡¬ñˆîñQ

î¬ê„²õ˜ îñQ

¸‡îñQ



168



169



170



171



172



173

 



174



175



176



177

 



178

¸‡ îñQèœ

¸¬ófó™
îñQ

¸¬ófó™
Þóˆî ¸‡
ï£÷ƒèœ

¸¬ófó™ Þóˆî æ†ì‹

Þîò‹

ªð¼…C¬óèœ

C¬óèÀ‹
¸‡ C¬óèÀ‹

õô¶
ÝK‚Aœ

Þì¶
ÝK‚Aœ

àì™ ð°F Þóˆî æ†ì‹

¸‡ C¬óèœ

¸¬ófó™
C¬óèœ

ªð¼‰îñQ

îñQèÀ‹
¸‡ îñQèÀ‹

àì™ ð°F
Þóˆî ¸‡
ï£÷ƒèœ

õô¶
ªõ¡†KAœ

Þì¶
ªõ¡†KAœ



179

 



180



181

Þîò «ï£ò¢è÷¢ (Heart diseases)
Þîòî¢î¤ô¢ ãø¢ð´ñ¢ «è£÷£Á â¶ªõù¤½ñ¢ Þîò«ï£ò¢ âùð¢ð´ñ¢, Þï¢î¤ò ñè¢è÷¤ô¢ 50% ñ£ó¬ìð¢¹ 50 õòî¤½ñ¢ 

25% ñ£ó¬ìð¢¹ 40 õòî¤ùó¤ìºñ¢ è£íð¢ð´è¤ù¢ø¶. Þîò«ï£ò¤ù¢ õ¬èè÷¢:- Types of heart disease.

è«ó£ùó¤ Þîò «ï£ò¢ Coronary heart disease:
Ü¬ìðì¢ì Üô¢ô¶ õ¤óì¢ê¤ ãø¢ðì¢ì

Þóî¢îè¢°öô¢è÷¢ Þîòî¢î¤ø¢°ê¢ ªêô¢½ñ¢
Þóî¢î Ü÷¬õ ñì¢´ð¢ð´î¢¶è¤ù¢ø¶. 
Þîù£ô¢ Ýè¢ú¤üù¢ ñø¢Áñ¢ àí¾
è¤¬ìè¢è£ñô¢ «ê£ó¢õ¬ìè¤ù¢ø¶.

Þóî¢îè¢ °öô¢ «ï£ò¢ (Vascular 
disease): Þîò «ï£ò¢ ªð¼ñ¢ð£½ñ¢ 

Þóî¢î ²ø¢«ø£ì¢ì ñí¢ìôð¢ 
ð°î¤è÷£ù îñù¤è÷¢, ê¤¬óè÷¢, 

ï¤íï¦ó¢è¢ °öô¢è÷¢ ñø¢Áñ¢ 
Þóî¢îî¢î¤ô¢ ãø¢ð´õùõ£°ñ¢.

ªð¼î¢îñí¤ «ï£ò¢ 
(Aorta disease): 

ªð¼î¢îñQ ²õó£ù¶ 
õ½õ¤öï¢¶ ðÖù¢ «ð£ô¢ 

õ¦é¢è¤ õ¤´îô¢ 
(Aneurism)

ªðó¤è£ó¢®ò õ¦è¢è «ï£ò¢ 
(Pericarditis): Þîò «ñô¢ 

ªñô¢½¬øò£ù 
ªðó¤è£ó¢®òî¢î¤ù¢ åù¢Á 

Üô¢ô¶ Þóí¢´ 
à¬øè÷¤½ñ¢ ãø¢ð´ñ¢ 

õ¦è¢èñ¢.

Þîòî¢î¬ê Üöø¢ê¤ 
(Cardiomyopathy): ªðó¤î£ù 
Üô¢ô¶ Þòô¢¹è¢° ñ£ø£è 

õ¤¬øˆî Üô¢ô¶ î®î¢î Þîòñ¢ 
°¬øï¢î Ü÷¾ Þóî¢îî¢¬î 
ñì¢´«ñ àï¢î¤î¢ î÷¢Àõî£ô¢ 
Þîòê¢ ªêòô¤öð¢¹ Üô¢ô¶ 
arrhythmia ãø¢ð´è¤ù¢ø¶.

Þîò õ£ô¢¾ «ï£ò¢ (Heart Value 
disease): Þîòî¢¶è¢° à÷¢Àñ¢, 
ªõ÷¤»ñ¢ èì¢´ð¢ð´î¢¶ñ¢ åù¢Á 
Üô¢ô¶ Üîø¢° «ñø¢ðì¢ì 
õ£ô¢¾è÷¢ ªêòô¢ðì£î 

ï¤¬ôò£°ñ¢.

Þîòê¢ ªêòô¤öð¢¹ (Heart failure):
Þîòñ¢ «î¬õò£ù Ü÷¾ Þóî¢îî¢¬î 

àï¢î¤î¢ î÷¢÷ Þòô£î ï¤¬ôò¤ô¢ 
àì½è¢° àí¾ñ¢ Ýè¢ú¤üÂñ¢ 
õöé¢°õîø¢° Þîòî¢ î¬êè÷¢ 

¶ó¤îñ£èð¢ ªêòô¢ð´õî£ô¢ õ½õ¤öï¢¶ 
õ¤´è¤ù¢ø¶.

Ü˜ó¤î¢î¦ñ¤ò£: 
Þï¢ï¤¬ôò¤ô¢ 
Þîòî¢ ¶®ð¢¹ 

å¿é¢èø¢Á÷¢÷¶.

è£¬ø
ð®î™

°¼Fï£÷Š¬ð

Þîò à¬ø

Þîò ñ¤ù¢
èìˆ¶

Ü¬ñð¢¹

MK‰î ªõù¢ì¢ó¤è¤÷¢
°¬øè¢èð¢ðì¢ì Þóî¢î

èù Ü÷¾

î®ˆî Þîòˆî¬ê„
²õ˜



182



183

Þîò «ï£ŒèO¡ ªð£¶õ£ù «ï£Œõ£ŒŠ¹‚ è£óEèœ

¹¬èH®ˆî™ I¬è Þóˆî
Ü¿ˆî‹

ÜFè
ªè£ôv®ó£™

ê˜‚è¬ó
«ï£Œ

àìŸðJŸC
Þ¡¬ñ

àì™ ð¼ñ¡
(ÜFè ªè£ôv®ó£™)

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _



184

Phases of the Cardiac Cycle’s 

Body fl uids and circulation

* 



185

 

th
e

 
A

V

to

A
V



186

  



187

 

-

-

-

-

-

-

-

-

-

-

-

-

-



188

-

-

-

-

-

-

-
-
-

-

-

-



189



190



191

A 

B 

C 

G 

E 

F

D 

  
1. Christopher D. Moyes and Patricia 

M. Schulte (2016), Principles of 

animal physiology 2nd edition Pearson 

publications.

2. Mary Jones, Richard Fosbery, Jennifer 

Gregory and Dennis Taylor,  Cambridge 

International AS and A level Biology 

Course book 4th  edition,   Cambridge 

University Press.

3. Elaine N. Marieb and Katja Hoehn 

(2011), Anatomy and Physiology 

4th edition Pearson publications.

1. Online and Interactive Resources

a. www.fi.edu/learn/heart/blood/blood.

html for information about blood.

b. www. abpischools.org.uk it 

includes a glossary, questions and 

animations.

c. www.youtube.com/watch? 

v+kcWNjt77uHc for description of 

cardiac cycle. www. brookerbiology.

com



192



193



194



195



196



197



198



199



200



201



202



203



204



205



206



207



208



209



210



211



212



213



214



215



216



217



218



219



220



221



222



223

 1 :  - Living world

Diversity

Systematics

Hierarchy

Nomenclature 

Biodiversity

Autotrophic

Phylogenentic tree

Heterotrophic

Thermoacidophiles

Tautonymy

Bioluminescence

 2  : -  Animal kingdom

Pinacocytes

Diploblastic animals

Asymmetryical

Radial symmetry

Biradial symmetrical

Para zoa

Eumetazoa

Mesoglea

Deutrostomia

Cnidocytes(or) 

cnidoblasts

Polyembryony

Haemocoel

Water vascular system

 Tissue level of organisation

Epithelial tissues 

Connective tissues

Muscular tissues

Neural tissues

Squamous epithelium

Cuboidal epithelium

Columnar epithelium

Ciliated epithelium

Compound epithe-

lium

Simple epithelium

Pseudostratified 

epithelium

Stratified epithelium

Histology

Basic/Primary tissue

  

Organ and organ system in Animals

Worm castings

Epigeics

Anecics

Endogeics

Peristomium

Prostomium

Pygidium

Clitellum

Seta

Coelomic fluid

Sperma theca

Nephridia

Genital opening

Gizzard

Intestinal caeca

Hydrostatic skeleton

Regeneration

Commissural vessels

Ganglion

Photoreceptor

Gustatory receptor

Olfactory receptor

Tactile receptor

Chemoreceptor

Thermo receptor

Cocoon

Vermiwash



224

 Digestion & 

Absorption

Digestive system

Digestive glands 

Salalivary glands 

Liver

Pancreas

Gastro intestinal 

hormones

Digestive enzymes

Absorption

Assimilation

Protein

Carbohydrates

Fats

Egestion

Nutrients

Minerals

Caloric value

Malnutrition

Indigestion

Constipation

Jaundice

Peptic ulcer

Appendicitis

Hiatus hernia

Autotrophs

Electrolytes

Digestive juice

Heterotroph

Foregut

Midgut

Hindgut

Buccal cavity/oral 

cavity

Terminal sulcus

Cardial portion

Fundic portion

Puloric portion

Duodenum

Cardiac sphincter

Pyloric sphincter

Regurgitation

Gastric rugae

Jejunum

Ileum

Chyme

Villi, microirlli

Goblet  cells

Lymphoid tissue

Peyer’s patches

Lymphocytes

Crypts

Succus entericus

Ceacum

Colon

Rectum

Vermiform appendix

Herbivorous animal

Symbiotic bacteria

Anal mucosa

Anal column cells

Piles/haemorrhoids

Serosa 

Muscularis

Sub mucosa

Mucosa

Visceral peritonium

Submucosa plexus

Biological catalysts

Parotid

Subumaxillary gland

Sub lingual gland

Peptic cells

Parietal cells

Falciform ligament

Hepatic lobules

Ampulla of vater

Mastication

Bolus

Peristalsis

lubrication

Churn

Proenzyme



225

Putrifaction

Emulsification

Absorption

Intestinal mucosa

Lumen

Facilitated transpot

Concentration gra-

dient

Active transport

Passive transport

Bartholins duct (or)  

duct of riviris

Cementum

 (Respiration)

Respiratory volume

Respirometer

Spirometer

Surfactants

Bio-molecules

Respiratory  disorder 

Pollutants

nasopharynx

Glottis

Epiglottis

Cartilaginous rings

Alveolus

Chocking

trachea

Bronchus

Bronchioles

Basement substance

Conducting zone

Respiratory zone

Pressure gradients

Intercostal muscles

Thoracic chamber

Inspiration

expiration

Snoring

Residual volume

Total lung capacity

Inspiratrory capacity

Expiratory capacity

Vital capacity

Inspiratory reserve 

volume

Expiratory reserve 

volume

Partial pressure

Partial pressure 

gradient

Dead space

Bronchitis

Emphysema

Reversible manner

Chemosensitive area

Sputum

nasal congestion

Sore throat

fibrosis

Carcinogens

Hypoxia

Heart palpitation

Nausea

Anaemia

Congenital heart 

disease

Hyperbarisim

suffocation

Conjugated protein

Haem  moieties

Respiratory quotient

Cat ions

Electrostatic attrac-

tion

Irritants

Hiccups

Aerobic respiration

Anaerobic respiration

 

– Body fluids and circulation

Cardiac activity

Cardiac cycle

Blood coagulating 

factors

Vasovagal syncope



226

Perfusion

Capillary

Arteriole

Hydrostatic pressure

Osmosis

Arterial end

Venous end

Formed elements

Hepatic portal vein

Hepatic vein

Hepatic artery

erythropoiesis

Granulocytes

Agranulocytes

Phagocytic nature

Pus

Inflammatory reac-

tion

Cell mediated immu-

nity

Macrophages

Sinusoids

Antigen

Antibody

Blood transfusion

Trauma

Meshwork

Lymph nodes

Inguinal

Axillaries

Sub Clarian vein

Lacteals

Vasoconstriction

Vasodilation

Anastomoses

Abdominal cramps

Venules

Uniderectional flow

Ventricular septum

Auricular septum

Double circulation

Pulmonary circuit

Systemic circuit

Papillary muscles

Pericardial space

Pericardial fluid

Auriculo ventricular 

valves

Inferior vena cava

Superior vena cava

Pulmonary veins

Myogenic heart

Depolariation

Tachycardia

Brady cardia

Stroke volume(SV)

Semilunar valves

Heart rate(HR)

Cardiac output (CO)

sphygmomanometer

Pulse rate

Atheroma

Hypertension

Atherosclerosis

Brain haemorrhage

Cerebral infarction

Myocardial infarction

Angina pectoris 

Rheumatoid heart 

disease

Rheumatic fever

Varicose veins

Embolism

Aneurysm

Catheter

Scaffolding

Pump oxygenator

Resuscitation

Cessation of breath





228



229



230



231



232


	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 1
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 2
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 3
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 4
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 5
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 6
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 7
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 8
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 9
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 10
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 11
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 12
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 13
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 14
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 15
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 16
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 17
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 18
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 19
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 20
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 21
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 22
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 23
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 24
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 25
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 26
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 27
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 28
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 29
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 30
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 31
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 32
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 33
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 34
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 35
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 36
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 37
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 38
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 39
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 40
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 41
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 42
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 43
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 44
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 45
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 46
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 47
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 48
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 49
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 50
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 51
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 52
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 53
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 54
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 55
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 56
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 57
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 58
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 59
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 60
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 61
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 62
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 63
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 64
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 65
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 66
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 67
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 68
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 69
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 70
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 71
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 72
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 73
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 74
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 75
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 76
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 77
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 78
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 79
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 80
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 81
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 82
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 83
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 84
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 85
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 86
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 87
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 88
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 89
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 90
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 91
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 92
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 93
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 94
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 95
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 96
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 97
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 98
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 99
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 100
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 101
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 102
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 103
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 104
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 105
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 106
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 107
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 108
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 109
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 110
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 111
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 112
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 113
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 114
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 115
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 116
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 117
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 118
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 119
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 120
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 121
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 122
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 123
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 124
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 125
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 126
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 127
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 128
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 129
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 130
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 131
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 132
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 133
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 134
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 135
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 136
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 137
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 138
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 139
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 140
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 141
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 142
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 143
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 144
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 145
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 146
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 147
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 148
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 149
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 150
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 151
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 152
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 153
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 154
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 155
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 156
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 157
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 158
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 159
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 160
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 161
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 162
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 163
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 164
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 165
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 166
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 167
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 168
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 169
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 170
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 171
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 172
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 173
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 174
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 175
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 176
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 177
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 178
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 179
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 180
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 181
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 182
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 183
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 184
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 185
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 186
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 187
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 188
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 189
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 190
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 191
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 192
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 193
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 194
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 195
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 196
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 197
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 198
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 199
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 200
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 201
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 202
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 203
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 204
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 205
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 206
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 207
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 208
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 209
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 210
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 211
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 212
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 213
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 214
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 215
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 216
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 217
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 218
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 219
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 220
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 221
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 222
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 223
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 224
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 225
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 226
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 227
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 228
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 229
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 230
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 231
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 232
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 233
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 234
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 235
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 236
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 237
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 238
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 239
	XI Std Bio-Zoology Vol-1 Tamil Medium Combined 11-05-2018 240


>>> from tika import language
>>> print(language.from_file('C:/Users/User/Desktop/11_Bio-Zoo_Vol_1_TM.pdf'))
th
>>> 
from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/tamil/tamil_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {}


Warning (from warnings module):
  File "C:\Python36\lib\site-packages\selenium\webdriver\phantomjs\webdriver.py", line 49
    warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead

>>> for ind, i in enumerate(English_word[36000:46000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=ta&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist.append(t)
            tmap[i] = tlist   
        except Exception as e:
            tmap[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap, open('Google_trans_tamil_2_1_trans.pkl', 'wb'))
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist1.append(t)
            tmap1[i] = tlist1
        except Exception as e:
            tmap1[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap1, open('Google_trans_tamil_1_1_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')

        
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:51264","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"096f87b0-3cdb-11ea-b0c3-7bc502da6680\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/096f87b0-3cdb-11ea-b0c3-7bc502da6680/element"}}
Screenshot: available via screen

0
0
10
10
20
20
30
30
40
40
50
50
60
60
70
70
80
80
90
90
100
100
110
110
120
120
130
130
140
140
150
150
160
160
170
170
180
180
190
190
200
200
210
210
220
220
230
230
240
240
250
250
260
260
270
270
280
280
290
290
300
300
310
310
320
320
330
330
340
340
350
350
360
360
370
370
380
380
390
390
400
400
410
410
420
420
430
430
440
440
450
450
460
460
470
470
480
480
490
490
500
500
510
510
520
520
530
530
540
540
550
550

