from sklearn.naive_bayes import MultinomialNB

class MultinominalNBmodel:
    def __init__(self):
        self.model = MultinomialNB()

    def model_train(self, x_train, y_train):
        self.model.fit(x_train, y_train)
        return self.model

