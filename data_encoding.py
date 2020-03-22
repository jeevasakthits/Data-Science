#before run this code need to install these libraries
#!pip install bert-serving-server  # server
#!pip install bert-serving-client
#!bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=4 
#!pip install -U sentence-transformers

# it works in GPU

from openpyxl.workbook import Workbook
import pandas as pd

from sentence_transformers import SentenceTransformer
from pandas.api.types import is_numeric_dtype

#we can use Label Encoder but if any case categorical column have full of sentences that will not give better solution.
#so here I used BERT Encoder 
# BERT Encoder
embedder = SentenceTransformer('bert-base-nli-mean-tokens')
def encoding(dataframe,column_no):
  column=dataframe[[column_no]]
  if is_numeric_dtype(column):
    corpus_embeddings = embedder.encode(column)
    # Here It return multi dimention list
    return corpus_embeddings
  else:
    return column
data_1=pd.read_excel("/content/paragraph_section_to_section_combined_trans.xlsx")
for i in range(len(data_1.columns)):
  encoded_data=encoding(dataframe,i)

