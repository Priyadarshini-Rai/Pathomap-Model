# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:49:55 2022

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:06:51 2022

@author: dell
"""

# In[1]:
# Loading Required Libraries

import pandas as pd
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel
from transformers import BertLMHeadModel
from sklearn.metrics.pairwise import cosine_similarity
from multiprocessing import Process
import numpy as np



# In[2]:
# Loading Model

# For BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = BertLMHeadModel.from_pretrained("/BERT Fine Tuned", output_hidden_states=True) # As per Shivani's code



# In[3]:
# User-defined Function

def get_hidden_states(encoded, model, layers):
    with torch.no_grad():
        output = model(**encoded)

    states = output.hidden_states
    output = torch.stack([states[i] for i in layers]).sum(0).squeeze()

    return output.mean(dim=0)

def get_doc_vector(doc, tokenizer, model, layers=None):
    layers = [-4, -3, -2, -1] if layers is None else layers  # Using last 4 layers for embedding generation

    encoded = tokenizer.encode_plus(doc, return_tensors="pt")

    if encoded['input_ids'].size()[1] > 512:
        new_encoded = {
            'input_ids': torch.empty(1,512),
            'token_type_ids': torch.empty(1,512),
            'attention_mask': torch.empty(1,512)
        }
        new_encoded['input_ids'] = encoded['input_ids'][0][:512].unsqueeze(0)
        new_encoded['token_type_ids'] = encoded['token_type_ids'][0][:512].unsqueeze(0)
        new_encoded['attention_mask'] = encoded['attention_mask'][0][:512].unsqueeze(0)
    else:
        new_encoded = encoded
    doc_vec = get_hidden_states(new_encoded, model, layers)

    return doc_vec
