# speech2sql

The most common programming language for managing and interacting with relational databases is Structured Query Language (SQL). Despite its human-readable syntax, it is quite challenging to use for many people, especially those with no prior programming experience. With the ubiquity of data stored in relational databases, building natural language interfaces for relational databases is an important problem to solve, and an ongoing challenge1.


##RESEARCH QUESTION

### Can deep learning networks convert natural language queries in the form of speech, into SQL queries with at least 75% accuracy?


## DATA

The primary data source for answering this question is a Github repository2 containing data and code for building and evaluating systems that map sentences to SQL. It was developed as part of a meta-analysis of text-to-SQL systems1, and contains over 90,000 SQL queries along with corresponding natural language questions, from a variety of sources.
The data includes queries that were automatically generated, along with queries/questions that were created by natural language processing researchers and members of the database community.


## MODELS

**Google Speech-to-Text (API)**
Google Cloud enables developers to convert audio to text through access to its powerful and robust neural network models through its API. It is capable of processing real-time streaming or prerecorded audio. The API has a Python client library, which can be integrated within web  applications, for making audio transcription requests and receiving text transcriptions.
Sequence-to-Sequence model (Keras)

Translating a natural language question into an SQL query is a sequence modelling problem. Understanding the sequence of input words is necessary to make an accurate prediction around it, plus the output query must follow a correct sequence to achieve flawless execution.
A recurrent neural network (RNN) consisting of two long short-term memory (LSTM) units; an encoder and a decoder, will be used for the text to SQL conversion. The encoder unit processes the input sequence (text), and forwards the representations it creates to the decoder unit, which then generates a sequence of its own that represents the prediction (SQL query).

*Mechanisms for Improving Model Performance:*
- Attention will be used to help the network pay attention to specific words in the input sequence, such as table column names.
- Beam Search will enable the decoder to predict the most probable next word, by taking into account the probability each word at every step in the sequence.
- Copying allows the model to generate words by simply copying them from the input sequence.


## INTERFACE

**Web Application**
The final product is a web application integrated with the Google Speech-to-Text API, a trained seq2seq model, and an SQLite database containing some data. Through the web application a live demonstration of speech-to-SQL can be performed.


Sources
Finegan-Dollak, Catherine, et al. "Improving text-to-sql evaluation methodology." arXiv preprint arXiv:1806.09029 (2018).
Github: https://github.com/jkkummerfeld/text2sql-data
