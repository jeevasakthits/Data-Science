import os
import re
#os.chdir("E:/hindi_and_english_books/Bio_txt_English")
#print(os.listdir())
def read_file(English_Filename,Hindi_Filename):
    os.chdir("E:/hindi_and_english_books/Bio_txt_English")
    File1_Open=open(English_Filename,'r')
    English_Txt_List=[]
    for Line_in_File in File1_Open:
        English_Txt_List.append(Line_in_File)
    #print(len(English_Txt_List))
    #English_Book_Txt= ' '.join(map(str, English_Txt_List))
    os.chdir("E:/hindi_and_english_books/Bio_txt_Hindi")
    File2_Open=open(Hindi_Filename,encoding="utf8")
    Hindi_Txt_List=[]
    for Line_in_File in File2_Open:
        Hindi_Txt_List.append(Line_in_File)
    #print(len(Hindi_Txt_List))
    #Hindi_Book_Txt= ' '.join(map(str, Hindi_Txt_List))
    
    List_of_English_Split=[]
    English_Book_Txt=str(English_Txt_List)
    Hindi_Book_Txt=str(Hindi_Txt_List)
    #print(English_Book_Txt)
    tmp1=re.match('(.*?)\d\.\d',English_Book_Txt)
    #print(tmp1)
    Value_English_Start=tmp1.group(0)
    English_Book_Txt1=English_Book_Txt[len(Value_English_Start)-3:]
    List_of_Hindi_Split=[]
    Value_Hindi_Start=re.match('(.*?)\d\.\d',Hindi_Book_Txt).group(0)
    #List_of_Hindi_Split.append(Value)
    Hindi_Book_Txt1=Hindi_Book_Txt[len(Value_Hindi_Start)-3:]

    i_Num1=0
    while(i_Num1<1):
        English_Chapter_No=English_Book_Txt1[0:English_Book_Txt1.find(" ")]
        English_Book_Txt1=English_Book_Txt1[English_Book_Txt1.find(" "):]
        try:
            English_Content=re.match('(.*?)\d\.\d',English_Book_Txt1).group(0)
        except:
            i_Num1=2
            break
        English_String_Value=English_Chapter_No+" "+English_Content
        #print(English_String_Value)
        List_of_English_Split.append(English_String_Value)
        English_Book_Txt1=English_Book_Txt1[len(re.match('(.*?)\d\.\d',English_Book_Txt1).group(0))-3:]
    
    
    i_Num2=0
    while(i_Num2<1):
        Hindi_Chapter_No=Hindi_Book_Txt1[0:Hindi_Book_Txt1.find(" ")]
        Hindi_Book_Txt1=Hindi_Book_Txt1[Hindi_Book_Txt1.find(" "):]
        try:
            Hindi_Content=re.match('(.*?)\d\.\d',Hindi_Book_Txt1).group(0)
        except:
            i_Num2=2
            break
        Hindi_String_Value=Hindi_Chapter_No+" "+Hindi_Content
        #print(Hindi_String_Value)
        List_of_Hindi_Split.append(Hindi_String_Value)
        Hindi_Book_Txt1=Hindi_Book_Txt1[len(re.match('(.*?)\d\.\d',Hindi_Book_Txt1).group(0))-3:]
    

    English_Chapter_list=sorted(List_of_English_Split)
    Hindi_Chapter_list=sorted(List_of_Hindi_Split)

    English_Chapter_list.append(Value_English_Start)
    Hindi_Chapter_list.append(Value_Hindi_Start)
    English_Chapter_list.append(English_Book_Txt1)
    Hindi_Chapter_list.append(Hindi_Book_Txt1)

    l=[]
    l.append(English_Chapter_list)
    l.append(Hindi_Chapter_list)
    print(len(Hindi_Chapter_list),len(English_Chapter_list))
    return l

def read_file1(English_Filename,Hindi_Filename):
    os.chdir("E:/hindi_and_english_books/Bio_txt_English")
    File1_Open=open(English_Filename,'r')
    English_Txt_List=[]
    for Line_in_File in File1_Open:
        English_Txt_List.append(Line_in_File)
    #print(len(English_Txt_List))
    #English_Book_Txt= ' '.join(map(str, English_Txt_List))
    os.chdir("E:/hindi_and_english_books/Bio_txt_Hindi")
    File2_Open=open(Hindi_Filename,encoding="utf8")
    Hindi_Txt_List=[]
    for Line_in_File in File2_Open:
        Hindi_Txt_List.append(Line_in_File)
    #print(len(Hindi_Txt_List))
    #Hindi_Book_Txt= ' '.join(map(str, Hindi_Txt_List))
    
    List_of_English_Split=[]
    English_Book_Txt=str(English_Txt_List)
    Hindi_Book_Txt=str(Hindi_Txt_List)

    English_Book_txt=re.sub("\d\.\d","",English_Book_txt)
    Hindi_Book_Txt=re.sub("\d\.\d","",Hindi_Book_Txt)

    English_Book_txt=re.sub("\.\d","",English_Book_txt)
    Hindi_Book_Txt=re.sub("\.\d","",Hindi_Book_Txt)

    English_Book_txt=re.sub("\d\.",".",English_Book_txt)
    Hindi_Book_Txt=re.sub("\d\.","।",Hindi_Book_Txt)
    print(English_Book_txt,Hindi_Book_Txt)

    English_Book_txt=English_Book_txt.split(".")
    Hindi_Book_Txt=Hindi_Book_Txt.split("।")
    print(English_Book_txt)
    print(Hindi_Book_Txt)

    print(len(English_Book_txt),len(Hindi_Book_Txt))

    """

    
    l1=list(English_Book_Txt.split('.'))
    l2=list(Hindi_Book_Txt.split('।'))
    print(len(l1),len(l2))
    print(l2)
    print(l1)
    l = []
    for x in l1:
        if not x.isdigit():
           l.append(x)
    print(len(l))
    return [l1,l1]"""
    

l1=read_file1("5156_1_Untitled-2.txt","5401_1.txt")
print(l1)
#print(re.findall(r"[\d.\d\.-].*[\d.\d\.-]+",s))
