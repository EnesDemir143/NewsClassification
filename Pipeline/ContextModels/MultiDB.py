from sklearn.naive_bayes import MultinomialNB

from Logging.Log_to_files import logtofile

class MultinominalNBmodel:
    def __init__(self):
        self.model = MultinomialNB()

    def model_train(self, x_train, y_train):
        logtofile.debug('Model train başladı')
        self.model.fit(x_train, y_train)
        logtofile.debug('Model train tamamlandı.')
        return self.model

