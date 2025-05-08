import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer

class BERT:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
        device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        self.model = AutoModelForMaskedLM.from_pretrained("google-bert/bert-base-uncased").to(device)

    def bert_