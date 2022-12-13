import json 
import numpy as np
import os
if not os.path.exists('./data_decomposition/NYT'):
    os.makedirs('./data_decomposition/NYT')

file_path='./data/NYT/train_triples.json'
data=json.load(open(file_path))
data=np.array(data)
entity1=[]#entity1-----实体1
relation=[]#relation-----实体之间的关系描述信息
entity2=[]#entity2-----实体2
entity1_Property=[]#entity1_Property-----实体1的属性
relation_Property=[]#relation_Property-----实体之间的关系属性
entity2_Property=[]#entity2_Property-----实体2的属性
relation_Message=[]#relation_Message-----实体之间的关系文本（实体以删除）
entity1_Delete_Position=[]#entity1_Delete_Position-----实体1在文本中的起始位置
entity2_Delete_Position=[]#entity2_Delete_Position-----实体2在文本中的起始位置
entity1_index=0
relation_index=1
entity2_index=2
# print('data',data.shape)
for number in range(data.shape[0]):
    list_entity1=[]
    list_entity2=[]
    list_relation=[]
    list_entity1_Property=[]
    list_entity2_Property=[]
    list_relation_Property=[]
    for list_number in range(len(data[number]['triple_list'])):
        list_entity1.append(data[number]['triple_list'][list_number][entity1_index])
        list_entity2.append(data[number]['triple_list'][list_number][entity2_index])
        list_relation.append(data[number]['triple_list'][list_number][relation_index])
        charactor=""
        now_position=0
        for i in range(len(data[number]['triple_list'][list_number][relation_index])):
            if data[number]['triple_list'][list_number][relation_index][i]=='/':
                if i==0:
                    continue
                else:
                    if now_position==0:
                        list_entity1_Property.append(charactor)
                        now_position=now_position+1
                    elif now_position==1:
                        list_entity2_Property.append(charactor)
                        now_position=now_position+1
                charactor=""
            else:
                charactor=charactor+data[number]['triple_list'][list_number][relation_index][i]
        list_relation_Property.append(charactor)
    entity1.append(list_entity1)
    entity2.append(list_entity2)
    relation.append(list_relation)
    entity1_Property.append(list_entity1_Property)
    entity2_Property.append(list_entity2_Property)
    relation_Property.append(list_relation_Property)

with open('./data_decomposition/NYT/entity1.json','w') as file_obj:
    json.dump(entity1,file_obj,ensure_ascii=False)
with open('./data_decomposition/NYT/entity2.json','w') as file_obj:
    json.dump(entity2,file_obj,ensure_ascii=False)
with open('./data_decomposition/NYT/entity1_properity.json','w') as file_obj:
    json.dump(entity1_Property,file_obj,ensure_ascii=False)
with open('./data_decomposition/NYT/entity2_properity.json','w') as file_obj:
    json.dump(entity2_Property,file_obj,ensure_ascii=False)


for number in range(data.shape[0]):
    now_Text=data[number]['text']
    list_relation_Message=[]
    list_entity1_Delete_Position=[]
    list_entity2_Delete_Position=[]
    for list_number in range(len(data[number]['triple_list'])):
        relation_Text=""
        flag1=0
        flag2=0
        position1_begin=now_Text.find(entity1[number][list_number])
        position2_begin=now_Text.find(entity2[number][list_number])
        list_entity1_Delete_Position.append(position1_begin)
        list_entity2_Delete_Position.append(position2_begin)
        for length_index in range(len(now_Text)):
            if length_index==position1_begin:
                flag1=len(entity1[number][list_number])
            elif length_index==position2_begin:
                flag2=len(entity2[number][list_number])
            if flag1>0:
                flag1=flag1-1
                continue
            if flag2>0:
                flag2=flag2-1
                continue
            relation_Text=relation_Text+now_Text[length_index]
        list_relation_Message.append(relation_Text)
    entity1_Delete_Position.append(list_entity1_Delete_Position)
    entity2_Delete_Position.append(list_entity2_Delete_Position)
    relation_Message.append(list_relation_Message)


with open('./data_decomposition/NYT/relation.json','w') as file_obj:
    json.dump(relation_Message,file_obj,ensure_ascii=False)
with open('./data_decomposition/NYT/relation_properity.json','w') as file_obj:
    json.dump(relation_Property,file_obj,ensure_ascii=False)
# print(entity1[data.shape[0]-1])
# print(entity2[data.shape[0]-1])
# print(relation[data.shape[0]-1])
# print(entity1_Property[data.shape[0]-1])
# print(entity2_Property[data.shape[0]-1])
# print(relation_Property[data.shape[0]-1])
# print(entity1_Delete_Position[data.shape[0]-1])
# print(entity2_Delete_Position[data.shape[0]-1])
# print(relation_Message[data.shape[0]-1])


