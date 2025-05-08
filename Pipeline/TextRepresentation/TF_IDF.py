from sklearn.feature_extraction.text import TfidfVectorizer

import Logging.Log_to_files


class TF_IDF:
    def __init__(self, n_grams=(1, 1)):
        self.n_grams = n_grams
        self.tf_idf_vectorizer = TfidfVectorizer(ngram_range=self.n_grams)

    def text_to_vector(self, texts):
        tf_idf_matrix = self.tf_idf_vectorizer.fit_transform(texts)
        feature_names = self.tf_idf_vectorizer.get_feature_names_out()
        vectors = tf_idf_matrix.toarray()

        Logging.Log_to_files.logtofile.debug('TF_IDF ile vektör işlemi tamamlandı.')
        return feature_names, vectors
