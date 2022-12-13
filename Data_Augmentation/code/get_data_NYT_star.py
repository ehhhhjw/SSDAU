import json 
import numpy as np
import os


if not os.path.exists('./data/NYT_star_augmentation'):
    os.makedirs('./data/NYT_star_augmentation')

dev_file_path='./data/NYT_star/dev_triples.json'
rel_file_path='./data/NYT_star/rel2id.json'
test_file_path='./data/NYT_star/test_triples.json'
train_file_path='./data_generate/NYT_star/train_triples_all_1000.json'
data_dev=json.load(open(dev_file_path))
data_rel=json.load(open(rel_file_path))
data_test=json.load(open(test_file_path))
data_train=json.load(open(train_file_path))

with open('./data/NYT_star_augmentation/dev_triples.json','w') as file_obj:
    json.dump(data_dev,file_obj,ensure_ascii=False)
with open('./data/NYT_star_augmentation/rel2id.json','w') as file_obj:
    json.dump(data_rel,file_obj,ensure_ascii=False)
with open('./data/NYT_star_augmentation/test_triples.json','w') as file_obj:
    json.dump(data_test,file_obj,ensure_ascii=False)
with open('./data/NYT_star_augmentation/train_triples.json','w') as file_obj:
    json.dump(data_train,file_obj,ensure_ascii=False)

