import pandas as pd
from summarizer import Summarizer,TransformerSummarizer

table = pd.read_csv("D:/GenAI/data/test_NBA.csv")
table = table.iloc[1]
print(table)
csv_as_str = table.to_csv()

bert_model = Summarizer()
bert_summary = ''.join(bert_model(csv_as_str, min_length=200))
print(bert_summary)