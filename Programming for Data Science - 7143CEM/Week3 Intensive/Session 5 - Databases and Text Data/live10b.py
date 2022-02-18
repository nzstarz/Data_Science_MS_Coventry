
# 7143CEM Programming for Data Science
# Live coding -- Week 3 -- Fun Friday (part two)

# Databases and Text Data

# Next ... play time (Fun Friday)

#---
# 3. SQLite database

# Write a pandas dataframe to a SQLite database
import pandas as pd
animals = pd.DataFrame(
    [['Cheetah', 60],
     ['Marlin',  80],
     ['Falcon', 185]],
    columns = ['name','topspeed'])
print(animals)

import sqlite3
# comes with Anaconda
#conn = sqlite3.connect('fast_animals.db')
#animals.to_sql('ANIMALS', conn, index=False)
#conn.commit()
#conn.close()

# Download SQLiteStudio (free software) from
# https://sqlitestudio.pl/
# Database menu | Add a database | click on folder icon
# navigate to fast_animals.db
# Add: Horsefly 90 mph

# Read from the database

another_conn = sqlite3.connect('fast_animals.db')
AAA = pd.read_sql_query("SELECT * FROM ANIMALS", another_conn)
another_conn.close()

print(AAA)

# Conclusion: we can write to a SQL database
#             we can read from an SQL database

#---
# 4. Jupyter notebook (already done)

#---
# 5. Analysis of text data
# Go to Anaconda Prompt:
#   conda install -c conda-forge textblob
#   python -m textblob.download_corpora
# Consoles menu | Restart kernel

import textblob
print(textblob.__version__)

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'
blob = textblob.TextBlob(text)
print(blob)
print(type(blob))

# Natural Language Processing (NLP)

print(blob.sentences)
print(blob.sentences[0])
print(blob.sentences[1])

print(blob.words)
print(blob.tags) # noun, verb
# https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/

print(blob)
print(blob.sentiment)
# polarity: -1 (negative) to +1 (positive), 0 (neutral)
# subjectivity: 0 (objective/factual) to 1 (subjective/opinion)
print(blob.sentences[0])
print(blob.sentences[0].sentiment)
print(blob.sentences[1])
print(blob.sentences[1].sentiment)

for s in blob.sentences:
    print(s)
    print(s.sentiment)
    
another = textblob.TextBlob('Python programming is horrible.')
print(another)
print(another.sentiment)

# Project Gutenberg
# https://www.gutenberg.org/

filename = 'pg19337.txt' # A Christmas Carol
# filename = 'pg1524.txt'  # Hamlet

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
print(word.synsets) # synonyms (thesaurus)
# Database: WordNet (Princeton University)


#---
# 6. Preview of Week 5
#    Data science overview
#    Big Data
#    Data protection, data security, data ethics


# -- the end --
