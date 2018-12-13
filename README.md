# speech2sql

The most common programming language for managing and interacting with relational databases is Structured Query Language (SQL). Despite its human-readable syntax, it is quite challenging to use for many people, especially those with no prior programming experience. With the ubiquity of data stored in relational databases, building natural language interfaces for relational databases is an important problem to solve, and an ongoing challenge1.


## RESEARCH QUESTION

### Can deep learning networks convert natural language queries in the form of speech?


## DATA

The primary data source for answering this question is a Github repository2 containing data and code for building and evaluating systems that map sentences to SQL. It was developed as part of a meta-analysis of text-to-SQL systems, and contains over 90,000 SQL queries along with corresponding natural language questions, from a variety of sources.
The data includes queries that were automatically generated, along with queries/questions that were created by natural language processing researchers and members of the database community.


## MODELS

**Web Speech API**

The Web Speech API has a controller interface that uses the default speech recognition system available on the device. Most modern OSes have a speech recognition system for issuing voice commands. For example Dictation on Mac OS X, Siri on iOS, Cortana on Windows 10, Android Speech, etc.



## INTERFACE

**Web Application**
The final product is a web application integrated with the Web Speech API and a pre-trained seq2seq model. Through the web application a live demonstration of speech-to-SQL can be performed.


Sources
Finegan-Dollak, Catherine, et al. "Improving text-to-sql evaluation methodology." arXiv preprint arXiv:1806.09029 (2018).
Github: https://github.com/jkkummerfeld/text2sql-data

Dunnhumby Engine Server API - http://docs.dhignite.com/
