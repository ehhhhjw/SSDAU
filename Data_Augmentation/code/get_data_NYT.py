import json 
import numpy as np
import os

if not os.path.exists('./data/NYT_augmentation'):
    os.makedirs('./data/NYT_augmentation')


dev_file_path='./data/NYT/dev_triples.json'
rel_file_path='./data/NYT/rel2id.json'
test_file_path='./data/NYT/test_triples.json'
train_file_path='./data_generate/NYT/train_triples_all_1000.json'
data_dev=json.load(open(dev_file_path))
data_rel=json.load(open(rel_file_path))
data_test=json.load(open(test_file_path))
data_train=json.load(open(train_file_path))

with open('./data/NYT_augmentation/dev_triples.json','w') as file_obj:
    json.dump(data_dev,file_obj,ensure_ascii=False)
with open('./data/NYT_augmentation/rel2id.json','w') as file_obj:
    json.dump(data_rel,file_obj,ensure_ascii=False)
with open('./data/NYT_augmentation/test_triples.json','w') as file_obj:
    json.dump(data_test,file_obj,ensure_ascii=False)
with open('./data/NYT_augmentation/train_triples.json','w') as file_obj:
    json.dump(data_train,file_obj,ensure_ascii=False)

