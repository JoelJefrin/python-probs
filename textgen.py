import numpy as np
from keras.layers import Embedding, LSTM, Dense
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential

text = "Natural Language Prcoessing requires much understanding of lingustics, POS Tagging and NER. NLP Example is CHATGPT."

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
vocab_size = len(tokenizer.word_index) + 1

sequences = tokenizer.texts_to_sequences([text])

sequences = pad_sequences(sequences, maxlen=10, padding='pre')

X = sequences[:, :-1] # Input sequences
y = sequences[:, -1] # Target word (next word in the sequence)

# Define the model
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=9)) # input_length adjusted to match X
model.add(LSTM(16, return_sequences=False)) # Removed input_shape and return_sequences=False
model.add(Dense(vocab_size, activation='softmax'))
# Compile and fit the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy']) # Changed loss function
model.fit(X, y, epochs=100)

# Generate text
seed_text = "Example"
for i in range(10):
    # Encode the seed text as a sequence of word indices
     seed_sequence = tokenizer.texts_to_sequences([seed_text])[0]
     seed_sequence = pad_sequences([seed_sequence], maxlen=9, padding='pre') # Adjusted maxlen to 9
# Generate the next word using the model
     next_word_probs = model.predict(seed_sequence)[0]
     next_word_idx = np.argmax(next_word_probs)
     next_word = tokenizer.index_word[next_word_idx]
     seed_text += " " + next_word
print(seed_text)


