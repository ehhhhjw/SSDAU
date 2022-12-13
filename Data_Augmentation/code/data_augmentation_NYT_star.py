import json 
import numpy as np
import os
if not os.path.exists('./data_generate/NYT_star'):
    os.makedirs('./data_generate/NYT_star')

file_path='./data/NYT_star/train_triples.json'
data=json.load(open(file_path))
data_generate_entity1=json.load(open(file_path))
data_generate_entity2=json.load(open(file_path))
data_generate_relation=json.load(open(file_path))
data_generate_all=json.load(open(file_path))
# data=np.array(data)
# print(data.shape)
# print(type(data))
threshold=0.87

sim_entity1_path='./similarity_match/NYT_star/sim_Entity1_1000.json'
sim_entity2_path='./similarity_match/NYT_star/sim_Entity2_1000.json'
sim_relation_Message_path='./similarity_match/NYT_star/sim_Relation_Message_1000.json'

sim_entity1_data=json.load(open(sim_entity1_path))
sim_entity2_data=json.load(open(sim_entity2_path))
sim_relation_Message_data=json.load(open(sim_relation_Message_path))

sim_entity1_data.sort(key=lambda sim_entity1: sim_entity1["similarity"],reverse=True)
sim_entity2_data.sort(key=lambda sim_entity2: sim_entity2["similarity"],reverse=True)
sim_relation_Message_data.sort(key=lambda sim_relation: sim_relation["similarity"],reverse=True)


entity1=[]#entity1-----实体1
relation=[]#relation-----实体之间的关系描述信息
entity2=[]#entity2-----实体2
entity1_Property=[]#entity1_Property-----实体1的属性
relation_Property=[]#relation_Property-----实体之间的关系属性
entity2_Property=[]#entity2_Property-----实体2的属性
relation_Message=[]#relation_Message-----实体之间的关系文本（实体已删除）
entity1_Delete_Position=[]#entity1_Delete_Position-----实体1在文本中的起始位置
entity2_Delete_Position=[]#entity2_Delete_Position-----实体2在文本中的起始位置
entity1_index=0
relation_index=1
entity2_index=2
# print('data',data.shape)
for number in range(len(data)):
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




for number in range(len(data)):
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


for sort_entity1_index in range(len(sim_entity1_data)):
    # print(sort_entity1_index)
    if sim_entity1_data[sort_entity1_index]["head1"]!=sim_entity1_data[sort_entity1_index]["head2"] and sim_entity1_data[sort_entity1_index]["similarity"]>float(threshold) and entity1_Property[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]==entity1_Property[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]:
        # print(sim_entity1_data[sort_entity1_index])
        two_cell={}
        three_cell=[]
        for list_sim_index in range(len(data[sim_entity1_data[sort_entity1_index]['head1_index']]['triple_list'])):
            four_cell=[]
            if entity1[sim_entity1_data[sort_entity1_index]['head1_index']][list_sim_index]==sim_entity1_data[sort_entity1_index]['head1']:
                new_one_generate_relation='/'+entity1_Property[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]+'/'+entity2_Property[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]+'/'+relation_Property[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]
                four_cell.append(entity1[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']])
                four_cell.append(new_one_generate_relation)
                four_cell.append(entity2[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']])
                three_cell.append(four_cell)
            else:
                three_cell.append(data[sim_entity1_data[sort_entity1_index]['head1_index']]['triple_list'][list_sim_index])
        two_cell['text']=data[sim_entity1_data[sort_entity1_index]['head1_index']]['text'][:entity1_Delete_Position[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]]+entity1[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]+data[sim_entity1_data[sort_entity1_index]['head1_index']]['text'][entity1_Delete_Position[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]+len(entity1[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]):]
        two_cell['triple_list']=three_cell
        data_generate_entity1.append(two_cell)
        data_generate_all.append(two_cell)

        # print(data_generate_entity1[sim_entity1_data[sort_entity1_index]['head1_index']])
        # print(data_generate_entity1[sim_entity1_data[sort_entity1_index]['head2_index']])
        # print(two_cell)


        two_cell={}
        three_cell=[]
        for list_sim_index in range(len(data[sim_entity1_data[sort_entity1_index]['head2_index']]['triple_list'])):
            four_cell=[]
            if entity1[sim_entity1_data[sort_entity1_index]['head2_index']][list_sim_index]==sim_entity1_data[sort_entity1_index]['head2']:
                new_one_generate_relation='/'+entity1_Property[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]+'/'+entity2_Property[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]+'/'+relation_Property[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]
                four_cell.append(entity1[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']])
                four_cell.append(new_one_generate_relation)
                four_cell.append(entity2[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']])
                three_cell.append(four_cell)
            else:
                three_cell.append(data[sim_entity1_data[sort_entity1_index]['head2_index']]['triple_list'][list_sim_index])
        two_cell['text']=data[sim_entity1_data[sort_entity1_index]['head2_index']]['text'][:entity1_Delete_Position[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]]+entity1[sim_entity1_data[sort_entity1_index]['head1_index']][sim_entity1_data[sort_entity1_index]['head1_n_index']]+data[sim_entity1_data[sort_entity1_index]['head2_index']]['text'][entity1_Delete_Position[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]+len(entity1[sim_entity1_data[sort_entity1_index]['head2_index']][sim_entity1_data[sort_entity1_index]['head2_n_index']]):]
        two_cell['triple_list']=three_cell
        data_generate_entity1.append(two_cell)
        data_generate_all.append(two_cell)
        # print(two_cell)


for sort_entity2_index in range(len(sim_entity2_data)):
    if sim_entity2_data[sort_entity2_index]["tail1"]!=sim_entity2_data[sort_entity2_index]["tail2"] and sim_entity2_data[sort_entity2_index]["similarity"]>float(threshold) and entity2_Property[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]==entity2_Property[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]:
        # print(sim_entity1_data[sort_entity1_index])
        two_cell={}
        three_cell=[]
        for list_sim_index in range(len(data[sim_entity2_data[sort_entity2_index]['tail1_index']]['triple_list'])):
            four_cell=[]
            if entity2[sim_entity2_data[sort_entity2_index]['tail1_index']][list_sim_index]==sim_entity2_data[sort_entity2_index]['tail1']:
                new_one_generate_relation='/'+entity1_Property[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]+'/'+entity2_Property[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]+'/'+relation_Property[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]
                four_cell.append(entity1[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']])
                four_cell.append(new_one_generate_relation)
                four_cell.append(entity2[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']])
                three_cell.append(four_cell)
            else:
                three_cell.append(data[sim_entity2_data[sort_entity2_index]['tail1_index']]['triple_list'][list_sim_index])
        two_cell['text']=data[sim_entity2_data[sort_entity2_index]['tail1_index']]['text'][:entity2_Delete_Position[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]]+entity2[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]+data[sim_entity2_data[sort_entity2_index]['tail1_index']]['text'][entity2_Delete_Position[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]+len(entity2[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]):]
        two_cell['triple_list']=three_cell
        data_generate_entity2.append(two_cell)
        data_generate_all.append(two_cell)

        # print(data_generate_entity2[sim_entity2_data[sort_entity2_index]['tail1_index']])
        # print(data_generate_entity2[sim_entity2_data[sort_entity2_index]['tail2_index']])
        # print(two_cell)

        two_cell={}
        three_cell=[]
        for list_sim_index in range(len(data[sim_entity2_data[sort_entity2_index]['tail2_index']]['triple_list'])):
            four_cell=[]
            if entity2[sim_entity2_data[sort_entity2_index]['tail2_index']][list_sim_index]==sim_entity2_data[sort_entity2_index]['tail2']:
                new_one_generate_relation='/'+entity1_Property[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]+'/'+entity2_Property[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]+'/'+relation_Property[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]
                four_cell.append(entity1[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']])
                four_cell.append(new_one_generate_relation)
                four_cell.append(entity2[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']])
                three_cell.append(four_cell)
            else:
                three_cell.append(data[sim_entity2_data[sort_entity2_index]['tail2_index']]['triple_list'][list_sim_index])
        two_cell['text']=data[sim_entity2_data[sort_entity2_index]['tail2_index']]['text'][:entity2_Delete_Position[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]]+entity2[sim_entity2_data[sort_entity2_index]['tail1_index']][sim_entity2_data[sort_entity2_index]['tail1_n_index']]+data[sim_entity2_data[sort_entity2_index]['tail2_index']]['text'][entity2_Delete_Position[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]+len(entity2[sim_entity2_data[sort_entity2_index]['tail2_index']][sim_entity2_data[sort_entity2_index]['tail2_n_index']]):]
        two_cell['triple_list']=three_cell
        data_generate_entity2.append(two_cell)
        data_generate_all.append(two_cell)
        # print(two_cell)


for sort_relation_index in range(len(sim_relation_Message_data)):
    # print(sort_relation_index)
    # if sim_relation_Message_data[sort_relation_index]["similarity"]>float(threshold) and relation_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]==entity2_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]:
    if sim_relation_Message_data[sort_relation_index]['relation1']!=sim_relation_Message_data[sort_relation_index]['relation2'] and sim_relation_Message_data[sort_relation_index]["similarity"]>float(0.9) and entity1_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]==entity1_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']] and entity2_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]==entity2_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]:
        two_cell={}
        three_cell=[]
        for list_sim_relation in range(len(data[sim_relation_Message_data[sort_relation_index]['relation1_index']]['triple_list'])):
            four_cell=[]
            if entity1_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]==entity1_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][list_sim_relation] and entity2_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]==entity2_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][list_sim_relation] and entity1[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]==entity1[sim_relation_Message_data[sort_relation_index]['relation1_index']][list_sim_relation] and entity2[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]==entity2[sim_relation_Message_data[sort_relation_index]['relation1_index']][list_sim_relation]:
                new_one_generate_relation='/'+entity1_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]+'/'+entity2_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]+'/'+relation_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]
                four_cell.append(entity1[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']])
                four_cell.append(new_one_generate_relation)
                four_cell.append(entity2[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']])
                three_cell.append(four_cell)
            else:
                continue
        two_cell['text']=data[sim_relation_Message_data[sort_relation_index]['relation1_index']]['text'][:entity1_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]]+entity1[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]+data[sim_relation_Message_data[sort_relation_index]['relation1_index']]['text'][entity1_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]+len(entity1[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]):entity2_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]]+entity2[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]+data[sim_relation_Message_data[sort_relation_index]['relation1_index']]['text'][entity2_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]+len(entity2[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]):]
        two_cell['triple_list']=three_cell
        data_generate_relation.append(two_cell)
        data_generate_all.append(two_cell)
        # print(data_generate_relation[sim_relation_Message_data[sort_relation_index]['relation1_index']])
        # print(data_generate_relation[sim_relation_Message_data[sort_relation_index]['relation2_index']])
        # print(two_cell)


        two_cell={}
        three_cell=[]
        for list_sim_relation in range(len(data[sim_relation_Message_data[sort_relation_index]['relation2_index']]['triple_list'])):
            four_cell=[]
            if entity1_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]==entity1_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][list_sim_relation] and entity2_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]==entity2_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][list_sim_relation] and entity1[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]==entity1[sim_relation_Message_data[sort_relation_index]['relation2_index']][list_sim_relation] and entity2[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]==entity2[sim_relation_Message_data[sort_relation_index]['relation2_index']][list_sim_relation]:
                new_one_generate_relation='/'+entity1_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]+'/'+entity2_Property[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]+'/'+relation_Property[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]
                four_cell.append(entity1[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']])
                four_cell.append(new_one_generate_relation)
                four_cell.append(entity2[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']])
                three_cell.append(four_cell)
            else:
                continue
        two_cell['text']=data[sim_relation_Message_data[sort_relation_index]['relation2_index']]['text'][:entity1_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]]+entity1[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]+data[sim_relation_Message_data[sort_relation_index]['relation2_index']]['text'][entity1_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]+len(entity1[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]):entity2_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]]+entity2[sim_relation_Message_data[sort_relation_index]['relation1_index']][sim_relation_Message_data[sort_relation_index]['relation1_n_index']]+data[sim_relation_Message_data[sort_relation_index]['relation2_index']]['text'][entity2_Delete_Position[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]+len(entity2[sim_relation_Message_data[sort_relation_index]['relation2_index']][sim_relation_Message_data[sort_relation_index]['relation2_n_index']]):]
        two_cell['triple_list']=three_cell
        data_generate_relation.append(two_cell)
        data_generate_all.append(two_cell)
        # print(two_cell)
print(len(data))
print(len(data_generate_entity1))
print(len(data_generate_entity2))
print(len(data_generate_relation)) 
print(len(data_generate_all))
with open('./data_generate/NYT_star/train_entity1_1000.json','w') as file_obj:
    json.dump(data_generate_entity1,file_obj,ensure_ascii=False)
with open('./data_generate/NYT_star/train_entity2_1000.json','w') as file_obj:
    json.dump(data_generate_entity2,file_obj,ensure_ascii=False)
with open('./data_generate/NYT_star/train_relation_1000.json','w') as file_obj:
    json.dump(data_generate_relation,file_obj,ensure_ascii=False)
with open('./data_generate/NYT_star/train_triples_all_1000.json','w') as file_obj:
    json.dump(data_generate_all,file_obj,ensure_ascii=False)
