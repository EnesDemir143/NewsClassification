import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer
from Logging.Log_to_files import logtofile

class BERT:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
        device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        self.model = AutoModelForMaskedLM.from_pretrained("google-bert/bert-base-uncased").to(device)

    def bert_contextual_embedding(self, text):
        token_vector = self.tokenizer(text, return_tensors='pt')
        output = self.model(**token_vector)
        return output
