import json 
import numpy as np
import os
if not os.path.exists('./similarity_match/WebNLG_star'):
    os.makedirs('./similarity_match/WebNLG_star')
from similarities import Similarity
m = Similarity(model_name_or_path="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
entity1_path='./data_decomposition/WebNLG_star/entity1.json'
entity2_path='./data_decomposition/WebNLG_star/entity2.json'
relation_Message_path='./data_decomposition/WebNLG_star/relation.json'
relation_Message_properity_path='./data_decomposition/WebNLG_star/relation_properity.json'
data_entity1=json.load(open(entity1_path))
data_entity2=json.load(open(entity2_path))
data_relation_Message=json.load(open(relation_Message_path))
data_relation_Messag_properitye=json.load(open(relation_Message_properity_path))

sim_Entity1=[]
sim_Entity2=[]
sim_Relation_Message=[]

for ent1_index_one in range(len(data_entity1)):
    for ent1_index_two in range(ent1_index_one+1,len(data_entity1)):
        dicu_exist={}
        dicv_exist={}
        for u_number in range(len(data_entity1[ent1_index_one])):
            for v_number in range(len(data_entity1[ent1_index_two])):
                if data_entity1[ent1_index_one][u_number] in dicu_exist.keys() and data_entity1[ent1_index_two][v_number] in dicv_exist.keys():
                    continue
                if data_relation_Messag_properitye[ent1_index_one][u_number]!=data_relation_Messag_properitye[ent1_index_two][v_number]:
                    continue
                sim_One_Two=m.similarity(data_entity1[ent1_index_one][u_number],data_entity1[ent1_index_two][v_number])
                dicu_exist[data_entity1[ent1_index_one][u_number]]=1
                dicv_exist[data_entity1[ent1_index_two][v_number]]=1
                if sim_One_Two > float(0.5):
                    dict_Message={}
                    dict_Message['head1_index']=ent1_index_one
                    dict_Message['head1_n_index']=u_number
                    dict_Message['head1']=data_entity1[ent1_index_one][u_number]
                    dict_Message['head2_index']=ent1_index_two
                    dict_Message['head2_n_index']=v_number
                    dict_Message['head2']=data_entity1[ent1_index_two][v_number]
                    dict_Message['similarity']=float(sim_One_Two)
                    sim_Entity1.append(dict_Message)


for ent2_index_one in range(len(data_entity2)):
    for ent2_index_two in range(ent2_index_one+1,len(data_entity2)):
        dicu_exist={}
        dicv_exist={}
        for u_number in range(len(data_entity2[ent2_index_one])):
            for v_number in range(len(data_entity2[ent2_index_two])):
                if data_entity2[ent2_index_one][u_number] in dicu_exist.keys() and data_entity2[ent2_index_two][v_number] in dicv_exist.keys():
                    continue
                if data_relation_Messag_properitye[ent2_index_one][u_number]!=data_relation_Messag_properitye[ent2_index_two][v_number]:
                    continue
                sim_One_Two=m.similarity(data_entity2[ent2_index_one][u_number],data_entity2[ent2_index_two][v_number])
                dicu_exist[data_entity2[ent2_index_one][u_number]]=1
                dicv_exist[data_entity2[ent2_index_two][v_number]]=1
                if sim_One_Two > float(0.5):
                    dict_Message={}
                    dict_Message['tail1_index']=ent2_index_one
                    dict_Message['tail1_n_index']=u_number
                    dict_Message['tail1']=data_entity2[ent2_index_one][u_number]
                    dict_Message['tail2_index']=ent2_index_two
                    dict_Message['tail2_n_index']=v_number
                    dict_Message['tail2']=data_entity2[ent2_index_two][v_number]
                    dict_Message['similarity']=float(sim_One_Two)
                    sim_Entity2.append(dict_Message)


for relation_index_one in range(len(data_relation_Message)):
    for relation_index_two in range(relation_index_one+1,len(data_relation_Message)):
        dicu_exist={}
        dicv_exist={}
        for u_number in range(len(data_relation_Message[relation_index_one])):
            for v_number in range(len(data_relation_Message[relation_index_two])):
                if data_relation_Message[relation_index_one][u_number] in dicu_exist.keys() and data_relation_Message[relation_index_two][v_number] in dicv_exist.keys():
                    continue
                if data_relation_Messag_properitye[relation_index_one][u_number]!=data_relation_Messag_properitye[relation_index_two][v_number]:
                    continue
                sim_One_Two=m.similarity(data_relation_Message[relation_index_one][u_number],data_relation_Message[relation_index_two][v_number])
                dicu_exist[data_relation_Message[relation_index_one][u_number]]=1
                dicv_exist[data_relation_Message[relation_index_two][v_number]]=1
                if sim_One_Two > float(0.5):
                    dict_Message={}
                    dict_Message['relation1_index']=relation_index_one
                    dict_Message['relation1_n_index']=u_number
                    dict_Message['relation1']=data_relation_Message[relation_index_one][u_number]
                    dict_Message['relation2_index']=relation_index_two
                    dict_Message['relation2_n_index']=v_number
                    dict_Message['relation2']=data_relation_Message[relation_index_two][v_number]
                    dict_Message['similarity']=float(sim_One_Two)
                    sim_Relation_Message.append(dict_Message)


with open('./data_decomposition/WebNLG_star/sim_Entity1.json','w') as file_obj:
    json.dump(sim_Entity1,file_obj,ensure_ascii=False)
with open('./data_decomposition/WebNLG_star/sim_Entity2.json','w') as file_obj:
    json.dump(sim_Entity2,file_obj,ensure_ascii=False)
with open('./data_decomposition/WebNLG_star/sim_Relation_Message.json','w') as file_obj:
    json.dump(sim_Relation_Message,file_obj,ensure_ascii=False)