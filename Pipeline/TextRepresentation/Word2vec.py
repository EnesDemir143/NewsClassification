import gensim

class Word2vec:
    def __init__(self):
        self.word2vec = gensim.models.Word2Vec(
            window=10,
            min_count=2,
            workers=6
        )

