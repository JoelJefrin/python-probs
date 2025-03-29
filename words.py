import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = 'my project is based on natural language processing, may name is joel'

words = word_tokenize(text)
print("all words: ", words)

sentence = sent_tokenize(text)
print("the sentance tokenization for this input will be", sentence)