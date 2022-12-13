import json 
import os
if not os.path.exists('NYT'):
    os.makedirs('NYT')
if not os.path.exists('NYT_augmentation'):
    os.makedirs('NYT_augmentation')
if not os.path.exists('WebNLG'):
    os.makedirs('WebNLG')
if not os.path.exists('WebNLG_augmentation'):
    os.makedirs('WebNLG_augmentation')

if not os.path.exists('NYT/casrel_data'):
    os.makedirs('NYT/casrel_data')
if not os.path.exists('NYT/exact_data'):
    os.makedirs('NYT/exact_data')
if not os.path.exists('NYT_augmentation/casrel_data'):
    os.makedirs('NYT_augmentation/casrel_data')
if not os.path.exists('NYT_augmentation/exact_data'):
    os.makedirs('NYT_augmentation/exact_data')

if not os.path.exists('WebNLG/clean_WebNLG'):
    os.makedirs('WebNLG/clean_WebNLG')
if not os.path.exists('WebNLG_augmentation/clean_WebNLG'):
    os.makedirs('WebNLG_augmentation/clean_WebNLG')









NYT_casrel_dev_file_path='../../../Data_Augmentation/data/NYT_star/dev_triples.json'
NYT_casrel_test_file_path='../../../Data_Augmentation/data/NYT_star/test_triples.json'
NYT_casrel_train_file_path='../../../Data_Augmentation/data/NYT_star/train_triples.json'

NYT_casrel_dev_triples=json.load(open(NYT_casrel_dev_file_path))
NYT_casrel_test_triples=json.load(open(NYT_casrel_test_file_path))
NYT_casrel_train_triples=json.load(open(NYT_casrel_train_file_path))

NYT_casrel_new_dev_triples=[]
NYT_casrel_new_test_triples=[]
NYT_casrel_new_train_triples=[]

for one_index in range(len(NYT_casrel_dev_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_casrel_dev_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_casrel_dev_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_casrel_dev_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_casrel_dev_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_casrel_dev_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_casrel_new_dev_triples.append(one_layer)

for one_index in range(len(NYT_casrel_test_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_casrel_test_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_casrel_test_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_casrel_test_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_casrel_test_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_casrel_test_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_casrel_new_test_triples.append(one_layer)

for one_index in range(len(NYT_casrel_train_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_casrel_train_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_casrel_train_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_casrel_train_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_casrel_train_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_casrel_train_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_casrel_new_train_triples.append(one_layer)

f=open('NYT/casrel_data/valid.json','a')
for index in range(len(NYT_casrel_new_dev_triples)):
    js = json.dumps(NYT_casrel_new_dev_triples[index])
    f.write(js)
    f.write('\n')
f.close()

f=open('NYT/casrel_data/test.json','a')
for index in range(len(NYT_casrel_new_test_triples)):
    js = json.dumps(NYT_casrel_new_test_triples[index])
    f.write(js)
    f.write('\n')
f.close()



f=open('NYT/casrel_data/train.json','a')
for index in range(len(NYT_casrel_new_train_triples)):
    js = json.dumps(NYT_casrel_new_train_triples[index])
    f.write(js)
    f.write('\n')
f.close()


NYT_exact_dev_file_path='../../../Data_Augmentation/data/NYT/dev_triples.json'
NYT_exact_test_file_path='../../../Data_Augmentation/data/NYT/test_triples.json'
NYT_exact_train_file_path='../../../Data_Augmentation/data/NYT/train_triples.json'

NYT_exact_dev_triples=json.load(open(NYT_exact_dev_file_path))
NYT_exact_test_triples=json.load(open(NYT_exact_test_file_path))
NYT_exact_train_triples=json.load(open(NYT_exact_train_file_path))

NYT_exact_new_dev_triples=[]
NYT_exact_new_test_triples=[]
NYT_exact_new_train_triples=[]

for one_index in range(len(NYT_exact_dev_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_exact_dev_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_exact_dev_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_exact_dev_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_exact_dev_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_exact_dev_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_exact_new_dev_triples.append(one_layer)

for one_index in range(len(NYT_exact_test_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_exact_test_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_exact_test_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_exact_test_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_exact_test_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_exact_test_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_exact_new_test_triples.append(one_layer)

for one_index in range(len(NYT_exact_train_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_exact_train_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_exact_train_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_exact_train_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_exact_train_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_exact_train_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_exact_new_train_triples.append(one_layer)

f=open('NYT/exact_data/valid.json','a')
for index in range(len(NYT_exact_new_dev_triples)):
    js = json.dumps(NYT_exact_new_dev_triples[index])
    f.write(js)
    f.write('\n')
f.close()

f=open('NYT/exact_data/test.json','a')
for index in range(len(NYT_exact_new_test_triples)):
    js = json.dumps(NYT_exact_new_test_triples[index])
    f.write(js)
    f.write('\n')
f.close()



f=open('NYT/exact_data/train.json','a')
for index in range(len(NYT_exact_new_train_triples)):
    js = json.dumps(NYT_exact_new_train_triples[index])
    f.write(js)
    f.write('\n')
f.close()



NYT_augmentation_casrel_dev_file_path='../../../Data_Augmentation/data/NYT_star_augmentation/dev_triples.json'
NYT_augmentation_casrel_test_file_path='../../../Data_Augmentation/data/NYT_star_augmentation/test_triples.json'
NYT_augmentation_casrel_train_file_path='../../../Data_Augmentation/data/NYT_star_augmentation/train_triples.json'

NYT_augmentation_casrel_dev_triples=json.load(open(NYT_augmentation_casrel_dev_file_path))
NYT_augmentation_casrel_test_triples=json.load(open(NYT_augmentation_casrel_test_file_path))
NYT_augmentation_casrel_train_triples=json.load(open(NYT_augmentation_casrel_train_file_path))

NYT_augmentation_casrel_new_dev_triples=[]
NYT_augmentation_casrel_new_test_triples=[]
NYT_augmentation_casrel_new_train_triples=[]

for one_index in range(len(NYT_augmentation_casrel_dev_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_augmentation_casrel_dev_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_augmentation_casrel_dev_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_augmentation_casrel_dev_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_augmentation_casrel_dev_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_augmentation_casrel_dev_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_augmentation_casrel_new_dev_triples.append(one_layer)

for one_index in range(len(NYT_augmentation_casrel_test_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_augmentation_casrel_test_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_augmentation_casrel_test_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_augmentation_casrel_test_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_augmentation_casrel_test_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_augmentation_casrel_test_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_augmentation_casrel_new_test_triples.append(one_layer)

for one_index in range(len(NYT_augmentation_casrel_train_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_augmentation_casrel_train_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_augmentation_casrel_train_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_augmentation_casrel_train_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_augmentation_casrel_train_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_augmentation_casrel_train_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_augmentation_casrel_new_train_triples.append(one_layer)

f=open('NYT_augmentation/casrel_data/valid.json','a')
for index in range(len(NYT_augmentation_casrel_new_dev_triples)):
    js = json.dumps(NYT_augmentation_casrel_new_dev_triples[index])
    f.write(js)
    f.write('\n')
f.close()

f=open('NYT_augmentation/casrel_data/test.json','a')
for index in range(len(NYT_augmentation_casrel_new_test_triples)):
    js = json.dumps(NYT_augmentation_casrel_new_test_triples[index])
    f.write(js)
    f.write('\n')
f.close()



f=open('NYT_augmentation/casrel_data/train.json','a')
for index in range(len(NYT_augmentation_casrel_new_train_triples)):
    js = json.dumps(NYT_augmentation_casrel_new_train_triples[index])
    f.write(js)
    f.write('\n')
f.close()




NYT_augmentation_exact_dev_file_path='../../../Data_Augmentation/data/NYT_augmentation/dev_triples.json'
NYT_augmentation_exact_test_file_path='../../../Data_Augmentation/data/NYT_augmentation/test_triples.json'
NYT_augmentation_exact_train_file_path='../../../Data_Augmentation/data/NYT_augmentation/train_triples.json'

NYT_augmentation_exact_dev_triples=json.load(open(NYT_augmentation_exact_dev_file_path))
NYT_augmentation_exact_test_triples=json.load(open(NYT_augmentation_exact_test_file_path))
NYT_augmentation_exact_train_triples=json.load(open(NYT_augmentation_exact_train_file_path))

NYT_augmentation_exact_new_dev_triples=[]
NYT_augmentation_exact_new_test_triples=[]
NYT_augmentation_exact_new_train_triples=[]

for one_index in range(len(NYT_augmentation_exact_dev_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_augmentation_exact_dev_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_augmentation_exact_dev_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_augmentation_exact_dev_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_augmentation_exact_dev_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_augmentation_exact_dev_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_augmentation_exact_new_dev_triples.append(one_layer)

for one_index in range(len(NYT_augmentation_exact_test_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_augmentation_exact_test_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_augmentation_exact_test_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_augmentation_exact_test_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_augmentation_exact_test_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_augmentation_exact_test_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_augmentation_exact_new_test_triples.append(one_layer)

for one_index in range(len(NYT_augmentation_exact_train_triples)):
    one_layer={}
    one_layer["sentText"]=NYT_augmentation_exact_train_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(NYT_augmentation_exact_train_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=NYT_augmentation_exact_train_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=NYT_augmentation_exact_train_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=NYT_augmentation_exact_train_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    NYT_augmentation_exact_new_train_triples.append(one_layer)

f=open('NYT_augmentation/exact_data/valid.json','a')
for index in range(len(NYT_augmentation_exact_new_dev_triples)):
    js = json.dumps(NYT_augmentation_exact_new_dev_triples[index])
    f.write(js)
    f.write('\n')
f.close()

f=open('NYT_augmentation/exact_data/test.json','a')
for index in range(len(NYT_augmentation_exact_new_test_triples)):
    js = json.dumps(NYT_augmentation_exact_new_test_triples[index])
    f.write(js)
    f.write('\n')
f.close()



f=open('NYT_augmentation/exact_data/train.json','a')
for index in range(len(NYT_augmentation_exact_new_train_triples)):
    js = json.dumps(NYT_augmentation_exact_new_train_triples[index])
    f.write(js)
    f.write('\n')
f.close()




WebNLG_clean_dev_file_path='../../../Data_Augmentation/data/WebNLG_star/dev_triples.json'
WebNLG_clean_test_file_path='../../../Data_Augmentation/data/WebNLG_star/test_triples.json'
WebNLG_clean_train_file_path='../../../Data_Augmentation/data/WebNLG_star/train_triples.json'

WebNLG_clean_dev_triples=json.load(open(WebNLG_clean_dev_file_path))
WebNLG_clean_test_triples=json.load(open(WebNLG_clean_test_file_path))
WebNLG_clean_train_triples=json.load(open(WebNLG_clean_train_file_path))

WebNLG_clean_new_dev_triples=[]
WebNLG_clean_new_test_triples=[]
WebNLG_clean_new_train_triples=[]

for one_index in range(len(WebNLG_clean_dev_triples)):
    one_layer={}
    one_layer["sentText"]=WebNLG_clean_dev_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(WebNLG_clean_dev_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=WebNLG_clean_dev_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=WebNLG_clean_dev_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=WebNLG_clean_dev_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    WebNLG_clean_new_dev_triples.append(one_layer)

for one_index in range(len(WebNLG_clean_test_triples)):
    one_layer={}
    one_layer["sentText"]=WebNLG_clean_test_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(WebNLG_clean_test_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=WebNLG_clean_test_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=WebNLG_clean_test_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=WebNLG_clean_test_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    WebNLG_clean_new_test_triples.append(one_layer)

for one_index in range(len(WebNLG_clean_train_triples)):
    one_layer={}
    one_layer["sentText"]=WebNLG_clean_train_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(WebNLG_clean_train_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=WebNLG_clean_train_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=WebNLG_clean_train_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=WebNLG_clean_train_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    WebNLG_clean_new_train_triples.append(one_layer)

f=open('WebNLG/clean_WebNLG/valid.json','a')
for index in range(len(WebNLG_clean_new_dev_triples)):
    js = json.dumps(WebNLG_clean_new_dev_triples[index])
    f.write(js)
    f.write('\n')
f.close()

f=open('WebNLG/clean_WebNLG/test.json','a')
for index in range(len(WebNLG_clean_new_test_triples)):
    js = json.dumps(WebNLG_clean_new_test_triples[index])
    f.write(js)
    f.write('\n')
f.close()



f=open('WebNLG/clean_WebNLG/train.json','a')
for index in range(len(WebNLG_clean_new_train_triples)):
    js = json.dumps(WebNLG_clean_new_train_triples[index])
    f.write(js)
    f.write('\n')
f.close()




WebNLG_augmentation_clean_dev_file_path='../../../Data_Augmentation/data/WebNLG_star_augmentation/dev_triples.json'
WebNLG_augmentation_clean_test_file_path='../../../Data_Augmentation/data/WebNLG_star_augmentation/test_triples.json'
WebNLG_augmentation_clean_train_file_path='../../../Data_Augmentation/data/WebNLG_star_augmentation/train_triples.json'

WebNLG_augmentation_clean_dev_triples=json.load(open(WebNLG_augmentation_clean_dev_file_path))
WebNLG_augmentation_clean_test_triples=json.load(open(WebNLG_augmentation_clean_test_file_path))
WebNLG_augmentation_clean_train_triples=json.load(open(WebNLG_augmentation_clean_train_file_path))

WebNLG_augmentation_clean_new_dev_triples=[]
WebNLG_augmentation_clean_new_test_triples=[]
WebNLG_augmentation_clean_new_train_triples=[]

for one_index in range(len(WebNLG_augmentation_clean_dev_triples)):
    one_layer={}
    one_layer["sentText"]=WebNLG_augmentation_clean_dev_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(WebNLG_augmentation_clean_dev_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=WebNLG_augmentation_clean_dev_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=WebNLG_augmentation_clean_dev_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=WebNLG_augmentation_clean_dev_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    WebNLG_augmentation_clean_new_dev_triples.append(one_layer)

for one_index in range(len(WebNLG_augmentation_clean_test_triples)):
    one_layer={}
    one_layer["sentText"]=WebNLG_augmentation_clean_test_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(WebNLG_augmentation_clean_test_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=WebNLG_augmentation_clean_test_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=WebNLG_augmentation_clean_test_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=WebNLG_augmentation_clean_test_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    WebNLG_augmentation_clean_new_test_triples.append(one_layer)

for one_index in range(len(WebNLG_augmentation_clean_train_triples)):
    one_layer={}
    one_layer["sentText"]=WebNLG_augmentation_clean_train_triples[one_index]["text"]
    two_layer=[]
    for two_index in range(len(WebNLG_augmentation_clean_train_triples[one_index]["triple_list"])):
        three_layer={}
        three_layer["em1Text"]=WebNLG_augmentation_clean_train_triples[one_index]["triple_list"][two_index][0]
        three_layer["em2Text"]=WebNLG_augmentation_clean_train_triples[one_index]["triple_list"][two_index][2]
        three_layer["label"]=WebNLG_augmentation_clean_train_triples[one_index]["triple_list"][two_index][1]
        two_layer.append(three_layer)
    one_layer["relationMentions"]=two_layer
    WebNLG_augmentation_clean_new_train_triples.append(one_layer)

f=open('WebNLG_augmentation/clean_WebNLG/valid.json','a')
for index in range(len(WebNLG_augmentation_clean_new_dev_triples)):
    js = json.dumps(WebNLG_augmentation_clean_new_dev_triples[index])
    f.write(js)
    f.write('\n')
f.close()

f=open('WebNLG_augmentation/clean_WebNLG/test.json','a')
for index in range(len(WebNLG_augmentation_clean_new_test_triples)):
    js = json.dumps(WebNLG_augmentation_clean_new_test_triples[index])
    f.write(js)
    f.write('\n')
f.close()



f=open('WebNLG_augmentation/clean_WebNLG/train.json','a')
for index in range(len(WebNLG_augmentation_clean_new_train_triples)):
    js = json.dumps(WebNLG_augmentation_clean_new_train_triples[index])
    f.write(js)
    f.write('\n')
f.close()