# Import Datasets
Before training the model, the training set and test set need to be added to today's file. Go to the path: `<./OneRel/data/>` ， and execute the following command:<br>
```
python get_data.py
```


# Commands for Training The Model
### NYT
```
python train.py --dataset=NYT --batch_size=8 --rel_num=24
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/NYT/>`

### NYT*
```
python train.py --dataset=NYT_star --batch_size=8 --rel_num=24
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/NYT_star/>`

### WebNLG
```
python train.py --dataset=WebNLG --batch_size=8 --rel_num=171
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/WebNLG/>`

### WebNLG*
```
python train.py --dataset=WebNLG_star --batch_size=8 --rel_num=171
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/WebNLG_star/>`

### NYT_generate
```
python train.py --dataset=NYT_generate --batch_size=8 --rel_num=24
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/NYT_generate/>`

### NYT*_generate
```
python train.py --dataset=NYT_star_generate --batch_size=8 --rel_num=24
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/NYT_star_generate/>`

### WebNLG_generate
```
python train.py --dataset=WebNLG_generate --batch_size=8 --rel_num=171
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/WebNLG_generate/>`

### WebNLG*_generate
```
python train.py --dataset=WebNLG_star_generate --batch_size=8 --rel_num=171
```
After that, the trained model will be stored under path: `<./OneRel/checkpoint/WebNLG_star_generate/>`

# Commands for Testing Process
### NYT
```
python test.py --dataset=NYT --rel_num=24
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"

### NYT*
```
python test.py --dataset=NYT_star --rel_num=24
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"

## WebNLG
```
python test.py --dataset=WebNLG --rel_num=171
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"

## WebNLG*
```
python test.py --dataset=WebNLG_star --rel_num=171
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"
### NYT_generate
```
python test.py --dataset=NYT_generate --rel_num=24
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"

### NYT*_generate
```
python test.py --dataset=NYT_star_generate --rel_num=24
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"

## WebNLG_generate
```
python test.py --dataset=WebNLG_generate --rel_num=171
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"

## WebNLG*_generate
```
python test.py --dataset=WebNLG_star_generate --rel_num=171
```
Before performing the model test, you need to modify line 258 of the code in the `<./OneRel/framework/framework.py>` file to change the path to the corresponding model path: "model.load_state_dict(torch.load(""))"


# Environment Configuration
To configure the environment for OneRel, perform the following steps

1. conda create -n OneRel_env python=3.8
2. conda activate OneRel_env
3. pip install keras_bert==0.88.0
4. pip install matplotlib==3.3.2
5. pip install numpy==1.19.2
6. pip install scikit_learn==1.0.1
7. pip install transformers==4.5.1
8. pip install torch==1.8.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
9. pip install tensorflow==2.5.0
10. pip install keras==2.5.0rc0 -i https://pypi.tuna.tsinghua.edu.cn/simple/
11. conda install sentencepiece

After the configuration is complete, you will get the following configuration information:

absl-py                          0.15.0<br>
astunparse                       1.6.3<br>
cachetools                       5.2.0<br>
certifi                          2022.9.14<br>
charset-normalizer               2.1.1<br>
click                            8.1.3<br>
cycler                           0.11.0<br>
filelock                         3.8.0<br>
flatbuffers                      1.12<br>
gast                             0.4.0<br>
google-auth                      2.12.0<br>
google-auth-oauthlib             0.4.6<br>
google-pasta                     0.2.0<br>
grpcio                           1.34.1<br>
h5py                             3.1.0<br>
idna                             3.4<br>
importlib-metadata               5.0.0<br>
joblib                           1.2.0<br>
keras                            2.5.0rc0<br>
keras-bert                       0.88.0<br>
keras-embed-sim                  0.10.0<br>
keras-layer-normalization        0.16.0<br>
keras-multi-head                 0.29.0<br>
keras-nightly                    2.5.0.dev2021032900<br>
keras-pos-embd                   0.13.0<br>
keras-position-wise-feed-forward 0.8.0<br>
Keras-Preprocessing              1.1.2<br>
keras-self-attention             0.51.0<br>
keras-transformer                0.40.0<br>
kiwisolver                       1.4.4<br>
Markdown                         3.4.1<br>
MarkupSafe                       2.1.1<br>
matplotlib                       3.3.2<br>
numpy                            1.19.2<br>
oauthlib                         3.2.1<br>
opt-einsum                       3.3.0<br>
packaging                        21.3<br>
Pillow                           9.2.0<br>
pip                              22.2.2<br>
protobuf                         3.19.6<br>
pyasn1                           0.4.8<br>
pyasn1-modules                   0.2.8<br>
pyparsing                        3.0.9<br>
python-dateutil                  2.8.2<br>
regex                            2022.9.13<br>
requests                         2.28.1<br>
requests-oauthlib                1.3.1<br>
rsa                              4.9<br>
sacremoses                       0.0.53<br>
scikit-learn                     1.0.1<br>
scipy                            1.9.1<br>
sentencepiece                    0.1.95<br>
setuptools                       63.4.1<br>
six                              1.15.0<br>
tensorboard                      2.10.1<br>
tensorboard-data-server          0.6.1<br>
tensorboard-plugin-wit           1.8.1<br>
tensorflow                       2.5.0<br>
tensorflow-estimator             2.5.0<br>
termcolor                        1.1.0<br>
threadpoolctl                    3.1.0<br>
tokenizers                       0.10.3<br>
torch                            1.8.1+cu111<br>
tqdm                             4.64.1<br>
transformers                     4.5.1<br>
typing-extensions                3.7.4.3<br>
urllib3                          1.26.12<br>
Werkzeug                         2.2.2<br>
wheel                            0.37.1<br>
wrapt                            1.12.1<br>
zipp                             3.8.1<br>

