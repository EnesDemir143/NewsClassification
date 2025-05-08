import gensim
import numpy as np
from gensim.models import KeyedVectors


class Word2vec:
    def __init__(self):
        self.word2vec = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

    def word_to_vector(self, text):
        vectors = [self.word2vec[token] if token in self.word2vec.key_to_index else np.zeros(self.word2vec.vector_size)
                   for token in text.split()]
        return vectors