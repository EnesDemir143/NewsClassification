import re
import string
import spacy
from Logging.Log_to_files import logtofile

from nltk.corpus import stopwords

class ManuelTextPreprocessing:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def _remove_htmls(self, text):
        return re.sub(r'<.*?>', '', text)

    def _remove_special_chracters(self, text):
        text = re.sub('[^a-zA-Z0-9\\s]', '', text)
        text = re.sub('\\s+', ' ', text)
        return text

    def _remove_stop_words(self, text):
        STOPWORDS = set(stopwords.words('english'))
        return " ".join([word for word in text.split() if word not in STOPWORDS])

    def _remove_punct(self, text):
        punctuations = string.punctuation
        return text.translate(str.maketrans('', '', punctuations))

    def _remove_url(self, text):
        return re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    def _lowercase(self, text):
        return text.lower()

    def text_preprocess(self, text):
        text = self._lowercase(text)
        text = self._remove_url(text)
        text = self._remove_htmls(text)
        text = self._remove_special_chracters(text)
        text = self._remove_punct(text)
        text = self._remove_stop_words(text)

        doc = self.nlp(text)
        filtered_text = [token.lemma_ for token in doc]
        logtofile.debug('Manuel textpreprocessing tamamlandı.')
        return " ".join(filtered_text)
