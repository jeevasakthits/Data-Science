import pandas as pd
import os
import xlrd
os.chdir("E:/books_seperate/bio")



df_sentence=pd.read_excel("E:/hindi_and_english_books/final_sentence_level/final_sentence/sentence/parallel_corpora_with_digits.xlsx")
df_sentence1=pd.read_csv("E:/books_seperate/bio/train_sentence_level.csv")

merged_inner = pd.merge(left=df_sentence,right=df_sentence1, left_on='English', right_on='English')
print(merged_inner.head())
print(len(merged_inner))

merged_inner.to_csv("Bio_Sentence_Parallel_corpora.csv")





df_sentence=pd.read_excel("E:/hindi_and_english_books/final_sentence_level/final_sentence/sentence/parallel_corpora_paragraph.xlsx")
df_sentence1=pd.read_csv("E:/books_seperate/bio/train_paragraph_level.csv")

merged_inner = pd.merge(left=df_sentence,right=df_sentence1, left_on='English', right_on='English')
print(merged_inner.head())
print(len(merged_inner))
merged_inner.to_csv("Bio_Sentence_Paragraph_corpora.csv")


df_sentence=pd.read_excel("E:/hindi_and_english_books/final_sentence_level/final_sentence/sentence/train_section_level.xlsx")
df_sentence1=pd.read_excel("E:/books_seperate/bio/train_section_level.xlsx")

merged_inner = pd.merge(left=df_sentence,right=df_sentence1, left_on='English', right_on='English')
print(merged_inner.head())
print(len(merged_inner))
print(os.getcwd())
merged_inner.to_csv("Bio_Sentence_Section_corpora.csv")





