import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



animals = pd.DataFrame(
    [['Cheetah', 60],
     ['Marlin', 80],
     ['Falcon', 185]],
    columns= ['name', 'topspeed'])
print(animals)  

import sqlite3

conn = sqlite3.connect('fast_animals.db')
# Careful with the fast_animals database location, find manually.
animals.to_sql('ANIMALS', conn, index = False)
conn.commit()
conn.close()

# Download SQLiteStudio

# Read from the database

another_conn = sqlite3.connect('fast_animals.db')
AAA = pd.read_sql_query("SELECT * FROM ANIMALS", another_conn)
another_conn.close()

print(AAA)

# Conclusion: Can Write and Read from SQL Database

# Textblob

import textblob
print(textblob.__version__)

text = 'Today is beautiful da. Tomorrow looks like bad weather.'
blob = textblob.TextBlob(text)
print(blob)
print(type(blob))
print(blob.sentences)
print(blob.sentences[0])
print(blob.sentences[1])

print(blob.words)
print(blob.word_counts)
print(blob.tags)

print(blob)
print(blob.sentiment)


print(blob.sentences[0])
print(blob.sentences[0].sentiment)
print(blob.sentences[1])
print(blob.sentences[1].sentiment)


for s in blob.sentences:
    print(s)
    print(s.sentiment)


another = textblob.TextBlob("Python Programming is horrible.")
print(another)
print(another.sentiment)
                            
# Project Gutenberg(free books website)

filename = 'pg19337.txt'

import pathlib
text = pathlib.Path(filename).read_text()

print(type(text))
print(len(text))

blob = textblob.TextBlob(text)
print(blob.word_counts)
print(len(blob.word_counts))

print(blob.sentiment)

word = textblob.Word('fun')
print(word.definitions)

print(word.synsets)
# Database: Wordnet(Princeton University)



