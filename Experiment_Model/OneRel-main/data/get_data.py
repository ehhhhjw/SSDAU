import json 
import os
if not os.path.exists('NYT'):
    os.makedirs('NYT')
if not os.path.exists('NYT_star'):
    os.makedirs('NYT_star')
if not os.path.exists('WebNLG'):
    os.makedirs('WebNLG')
if not os.path.exists('WebNLG_star'):
    os.makedirs('WebNLG_star')
if not os.path.exists('NYT_augmentation'):
    os.makedirs('NYT_augmentation')
if not os.path.exists('NYT_star_augmentation'):
    os.makedirs('NYT_star_augmentation')
if not os.path.exists('WebNLG_augmentation'):
    os.makedirs('WebNLG_augmentation')
if not os.path.exists('WebNLG_star_augmentation'):
    os.makedirs('WebNLG_star_augmentation')


NYT_dev_file_path='../../../Data_Augmentation/data/NYT/dev_triples.json'
NYT_rel_file_path='../../../Data_Augmentation/data/NYT/rel_triples.json'
NYT_test_file_path='../../../Data_Augmentation/data/NYT/test_triples.json'
NYT_train_file_path='../../../Data_Augmentation/data/NYT/train_triples.json'

NYT_star_dev_file_path='../../../Data_Augmentation/data/NYT_star/dev_triples.json'
NYT_star_rel_file_path='../../../Data_Augmentation/data/NYT_star/rel_triples.json'
NYT_star_test_file_path='../../../Data_Augmentation/data/NYT_star/test_triples.json'
NYT_star_train_file_path='../../../Data_Augmentation/data/NYT_star/train_triples.json'

WebNLG_dev_file_path='../../../Data_Augmentation/data/WebNLG/dev_triples.json'
WebNLG_rel_file_path='../../../Data_Augmentation/data/WebNLG/rel_triples.json'
WebNLG_test_file_path='../../../Data_Augmentation/data/WebNLG/test_triples.json'
WebNLG_train_file_path='../../../Data_Augmentation/data/WebNLG/train_triples.json'

WebNLG_star_dev_file_path='../../../Data_Augmentation/data/WebNLG_star/dev_triples.json'
WebNLG_star_rel_file_path='../../../Data_Augmentation/data/WebNLG_star/rel_triples.json'
WebNLG_star_test_file_path='../../../Data_Augmentation/data/WebNLG_star/test_triples.json'
WebNLG_star_train_file_path='../../../Data_Augmentation/data/WebNLG_star/train_triples.json'



NYT_augmentation_dev_file_path='../../../Data_Augmentation/data/NYT_augmentation/dev_triples.json'
NYT_augmentation_rel_file_path='../../../Data_Augmentation/data/NYT_augmentation/rel_triples.json'
NYT_augmentation_test_file_path='../../../Data_Augmentation/data/NYT_augmentation/test_triples.json'
NYT_augmentation_train_file_path='../../../Data_Augmentation/data/NYT_augmentation/train_triples.json'

NYT_star_augmentation_dev_file_path='../../../Data_Augmentation/data/NYT_star_augmentation/dev_triples.json'
NYT_star_augmentation_rel_file_path='../../../Data_Augmentation/data/NYT_star_augmentation/rel_triples.json'
NYT_star_augmentation_test_file_path='../../../Data_Augmentation/data/NYT_star_augmentation/test_triples.json'
NYT_star_augmentation_train_file_path='../../../Data_Augmentation/data/NYT_star_augmentation/train_triples.json'

WebNLG_augmentation_dev_file_path='../../../Data_Augmentation/data/WebNLG_augmentation/dev_triples.json'
WebNLG_augmentation_rel_file_path='../../../Data_Augmentation/data/WebNLG_augmentation/rel_triples.json'
WebNLG_augmentation_test_file_path='../../../Data_Augmentation/data/WebNLG_augmentation/test_triples.json'
WebNLG_augmentation_train_file_path='../../../Data_Augmentation/data/WebNLG_augmentation/train_triples.json'

WebNLG_star_augmentation_dev_file_path='../../../Data_Augmentation/data/WebNLG_star_augmentation/dev_triples.json'
WebNLG_star_augmentation_rel_file_path='../../../Data_Augmentation/data/WebNLG_star_augmentation/rel_triples.json'
WebNLG_star_augmentation_test_file_path='../../../Data_Augmentation/data/WebNLG_star_augmentation/test_triples.json'
WebNLG_star_augmentation_train_file_path='../../../Data_Augmentation/data/WebNLG_star_augmentation/train_triples.json'


NYT_data_dev=json.load(open(NYT_dev_file_path))
NYT_data_rel=json.load(open(NYT_rel_file_path))
NYT_data_test=json.load(open(NYT_test_file_path))
NYT_data_train=json.load(open(NYT_train_file_path))

NYT_star_data_dev=json.load(open(NYT_star_dev_file_path))
NYT_star_data_rel=json.load(open(NYT_star_rel_file_path))
NYT_star_data_test=json.load(open(NYT_star_test_file_path))
NYT_star_data_train=json.load(open(NYT_star_train_file_path))

WebNLG_data_dev=json.load(open(WebNLG_dev_file_path))
WebNLG_data_rel=json.load(open(WebNLG_rel_file_path))
WebNLG_data_test=json.load(open(WebNLG_test_file_path))
WebNLG_data_train=json.load(open(WebNLG_train_file_path))

WebNLG_star_data_dev=json.load(open(WebNLG_star_dev_file_path))
WebNLG_star_data_rel=json.load(open(WebNLG_star_rel_file_path))
WebNLG_star_data_test=json.load(open(WebNLG_star_test_file_path))
WebNLG_star_data_train=json.load(open(WebNLG_star_train_file_path))

NYT_augmentation_data_dev=json.load(open(NYT_augmentation_dev_file_path))
NYT_augmentation_data_rel=json.load(open(NYT_augmentation_rel_file_path))
NYT_augmentation_data_test=json.load(open(NYT_augmentation_test_file_path))
NYT_augmentation_data_train=json.load(open(NYT_augmentation_train_file_path))

NYT_star_augmentation_data_dev=json.load(open(NYT_star_augmentation_dev_file_path))
NYT_star_augmentation_data_rel=json.load(open(NYT_star_augmentation_rel_file_path))
NYT_star_augmentation_data_test=json.load(open(NYT_star_augmentation_test_file_path))
NYT_star_augmentation_data_train=json.load(open(NYT_star_augmentation_train_file_path))

WebNLG_augmentation_data_dev=json.load(open(WebNLG_augmentation_dev_file_path))
WebNLG_augmentation_data_rel=json.load(open(WebNLG_augmentation_rel_file_path))
WebNLG_augmentation_data_test=json.load(open(WebNLG_augmentation_test_file_path))
WebNLG_augmentation_data_train=json.load(open(WebNLG_augmentation_train_file_path))

WebNLG_star_augmentation_data_dev=json.load(open(WebNLG_star_augmentation_dev_file_path))
WebNLG_star_augmentation_data_rel=json.load(open(WebNLG_star_augmentation_rel_file_path))
WebNLG_star_augmentation_data_test=json.load(open(WebNLG_star_augmentation_test_file_path))
WebNLG_star_augmentation_data_train=json.load(open(WebNLG_star_augmentation_train_file_path))

with open('NYT/dev_triples.json','w') as file_obj:
    json.dump(NYT_data_dev,file_obj,ensure_ascii=False)
with open('NYT/rel2id.json','w') as file_obj:
    json.dump(NYT_data_rel,file_obj,ensure_ascii=False)
with open('NYT/test_triples.json','w') as file_obj:
    json.dump(NYT_data_test,file_obj,ensure_ascii=False)
with open('NYT/train_triples.json','w') as file_obj:
    json.dump(NYT_data_train,file_obj,ensure_ascii=False)

with open('NYT_star/dev_triples.json','w') as file_obj:
    json.dump(NYT_star_data_dev,file_obj,ensure_ascii=False)
with open('NYT_star/rel2id.json','w') as file_obj:
    json.dump(NYT_star_data_rel,file_obj,ensure_ascii=False)
with open('NYT_star/test_triples.json','w') as file_obj:
    json.dump(NYT_star_data_test,file_obj,ensure_ascii=False)
with open('NYT_star/train_triples.json','w') as file_obj:
    json.dump(NYT_star_data_train,file_obj,ensure_ascii=False)

with open('WebNLG/dev_triples.json','w') as file_obj:
    json.dump(WebNLG_data_dev,file_obj,ensure_ascii=False)
with open('WebNLG/rel2id.json','w') as file_obj:
    json.dump(WebNLG_data_rel,file_obj,ensure_ascii=False)
with open('WebNLG/test_triples.json','w') as file_obj:
    json.dump(WebNLG_data_test,file_obj,ensure_ascii=False)
with open('WebNLG/train_triples.json','w') as file_obj:
    json.dump(WebNLG_data_train,file_obj,ensure_ascii=False)

with open('WebNLG_star/dev_triples.json','w') as file_obj:
    json.dump(WebNLG_star_data_dev,file_obj,ensure_ascii=False)
with open('WebNLG_star/rel2id.json','w') as file_obj:
    json.dump(WebNLG_star_data_rel,file_obj,ensure_ascii=False)
with open('WebNLG_star/test_triples.json','w') as file_obj:
    json.dump(WebNLG_star_data_test,file_obj,ensure_ascii=False)
with open('WebNLG_star/train_triples.json','w') as file_obj:
    json.dump(WebNLG_star_data_train,file_obj,ensure_ascii=False)


with open('NYT_augmentation/dev_triples.json','w') as file_obj:
    json.dump(NYT_augmentation_data_dev,file_obj,ensure_ascii=False)
with open('NYT_augmentation/rel2id.json','w') as file_obj:
    json.dump(NYT_augmentation_data_rel,file_obj,ensure_ascii=False)
with open('NYT_augmentation/test_triples.json','w') as file_obj:
    json.dump(NYT_augmentation_data_test,file_obj,ensure_ascii=False)
with open('NYT_augmentation/train_triples.json','w') as file_obj:
    json.dump(NYT_augmentation_data_train,file_obj,ensure_ascii=False)

with open('NYT_star_augmentation/dev_triples.json','w') as file_obj:
    json.dump(NYT_star_augmentation_data_dev,file_obj,ensure_ascii=False)
with open('NYT_star_augmentation/rel2id.json','w') as file_obj:
    json.dump(NYT_star_augmentation_data_rel,file_obj,ensure_ascii=False)
with open('NYT_star_augmentation/test_triples.json','w') as file_obj:
    json.dump(NYT_star_augmentation_data_test,file_obj,ensure_ascii=False)
with open('NYT_star_augmentation/train_triples.json','w') as file_obj:
    json.dump(NYT_star_augmentation_data_train,file_obj,ensure_ascii=False)

with open('WebNLG_augmentation/dev_triples.json','w') as file_obj:
    json.dump(WebNLG_augmentation_data_dev,file_obj,ensure_ascii=False)
with open('WebNLG_augmentation/rel2id.json','w') as file_obj:
    json.dump(WebNLG_augmentation_data_rel,file_obj,ensure_ascii=False)
with open('WebNLG_augmentation/test_triples.json','w') as file_obj:
    json.dump(WebNLG_augmentation_data_test,file_obj,ensure_ascii=False)
with open('WebNLG_augmentation/train_triples.json','w') as file_obj:
    json.dump(WebNLG_augmentation_data_train,file_obj,ensure_ascii=False)

with open('WebNLG_star_augmentation/dev_triples.json','w') as file_obj:
    json.dump(WebNLG_star_augmentation_data_dev,file_obj,ensure_ascii=False)
with open('WebNLG_star_augmentation/rel2id.json','w') as file_obj:
    json.dump(WebNLG_star_augmentation_data_rel,file_obj,ensure_ascii=False)
with open('WebNLG_star_augmentation/test_triples.json','w') as file_obj:
    json.dump(WebNLG_star_augmentation_data_test,file_obj,ensure_ascii=False)
with open('WebNLG_star_augmentation/train_triples.json','w') as file_obj:
    json.dump(WebNLG_star_augmentation_data_train,file_obj,ensure_ascii=False)