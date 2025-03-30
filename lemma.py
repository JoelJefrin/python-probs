import nltk
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('punkt')


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

text = 'the cats are running faster than the dogs '

words = word_tokenize(text)

stemmed_words = [stemmer.stem(word) for word in words]
lematized_words = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in words]

print("the original words: ",words)
print("stemmed words: ", stemmed_words)
print("lemmatized_words: ", lematized_words)
