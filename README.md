# Pathomap: Literature mining discerns latent disease-gene relationships

Priyadarshini Rai, Atishay Jain, Shivani Kumar, Neha Jha, Divya Sharma, Smriti Chawla, Abhijit Raj, Apoorva Gupta, Sarita Poonia, Angshul Majumdar, Tanmoy Chakraborty, Gaurav Ahuja, and Debarka Sengupta

## Description

Pathomap provides a strategy to obtain an unbiased continuous representation of disease causing genes and their tissue specificity.

## Link to models and data

#### Link to *PathoBERT* model

https://drive.google.com/drive/folders/1GJE6zOrQYkavz0veiW_6SPv6uo6v4-ja?usp=sharing

#### Script and data used for classification

*Classification.ipynb* and *Supplementary File 1.csv*

https://drive.google.com/drive/folders/1GJE6zOrQYkavz0veiW_6SPv6uo6v4-ja?usp=sharing


#### Data for *GeneDisFreq* function

https://drive.google.com/drive/folders/1Hrdw_P2umP81SzrODAvrZhLKu2OwKDC_?usp=sharing

## File description

1. ***Classification.ipynb***: Script used to perform classification.
2. ***Function to Get Embeddings.py***: To get embedding(s) of a word(s) using *PathoBERT*.
3. ***GeneDisFreq.R***: Function to get PMID(s) in which a gene-disease pair is present.
4. ***Supplementary File 1.csv***: Pathological and non-pathological abstracts used as ground truth for the classification task.
5. ***Supplementary File 2.csv***: DisGeNET gene-disease pairs cosine similarity using six different models, namely, *PathoBERT*, Word2vec, BioBERT, BioSentVec, BERT Human, and Word2vec Human.
6. ***Supplementary File 3.csv***: Random gene-disease pairs cosine similarity using six different models, namely, *PathoBERT*, Word2vec, BioBERT, BioSentVec, BERT Human, and Word2vec Human.

## *PathoBERT* and its usage

To get ***PathoBERT*** embeddings of suppose diseases ***cardiac homeostasis*** and ***rhythm disorder***, we will use function ***get_doc_vector*** written inside script ***Function to Get Embeddings.py***.

```
E1 = get_doc_vector('cardiac homeostasis', tokenizer, model)
E2 = get_doc_vector('rhythm disorder', tokenizer, model)
```
To compute the ***cosine similarity*** between the embeddings of diseases ***cardiac homeostasis*** and ***rhythm disorder***, we can use the function ***cosine_similarity***

```
CS = cosine_similarity([E1.numpy()], [E2.numpy()])
```
## Function *GeneDisFreq ( )* usage

```
F = GeneDisFreq('BRCA1', breast cancer')
F = GeneDisFreq('MASP1', 'cardiac homeostasis')
```
