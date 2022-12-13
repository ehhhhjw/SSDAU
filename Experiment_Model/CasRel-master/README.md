# Import Datasets
Before training the model, the training set and test set need to be added to today's file. Go to the path: `<./CasRel/data/>` ， and execute the following command:<br>
```
python get_data.py
```
# Commands for Training The Model
### NYT
```
python run.py ---train=True --dataset=NYT
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/NYT/>`

### NYT*
```
python run.py ---train=True --dataset=NYT_star
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/NYT_star/>`

### WebNLG
```
python run.py ---train=True --dataset=WebNLG
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/WebNLG/>`

### WebNLG*
```
python run.py ---train=True --dataset=WebNLG_star
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/WebNLG_star/>`

### NYT_generate
```
python run.py ---train=True --dataset=NYT_generate
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/NYT_generate/>`

### NYT*_generate
```
python run.py ---train=True --dataset=NYT_star_generate
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/NYT_star_generate/>`

### WebNLG_generate
```
python run.py ---train=True --dataset=WebNLG_generate
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/WebNLG_generate/>`

### WebNLG*_generate
```
python run.py ---train=True --dataset=WebNLG_star_generate
```
After that, the trained model will be stored under path: `<./CasRel/saved_weights/WebNLG_star_generate/>`


# Commands for Testing Process
### NYT
```
python run.py --dataset=NYT
```

### NYT*
```
python run.py --dataset=NYT_star
```

## WebNLG
```
python run.py --dataset=WebNLG
```

## WebNLG*
```
python run.py --dataset=WebNLG_star
```

### NYT_generate
```
python run.py --dataset=NYT_generate
```

### NYT*_generate
```
python run.py --dataset=NYT_star_generate
```

## WebNLG_generate
```
python run.py --dataset=WebNLG_generate
```

## WebNLG*_generate
```
python run.py --dataset=WebNLG_star_generate
```

# Environment Configuration
To configure the environment for OneRel, perform the following steps

1. conda create -n CasRel_env python=3.7
2. conda activate CasRel_env
3. pip install tqdm
4. pip install codecs
5. pip install keras-bert==0.80.0
6. pip install tensorflow==2.5.0

After the configuration is complete, you will get the following configuration information:
absl-py                          1.2.0<br>
astor                            0.8.1<br>
cached-property                  1.5.2<br>
cachetools                       4.2.4<br>
certifi                          2021.5.30<br>
charset-normalizer               2.0.12<br>
dataclasses                      0.8<br>
gast                             0.2.2<br>
google-auth                      1.35.0<br>
google-auth-oauthlib             0.4.6<br>
google-pasta                     0.2.0<br>
grpcio                           1.48.1<br>
h5py                             3.1.0<br>
idna                             3.4<br>
importlib-metadata               4.8.3<br>
importlib-resources              5.4.0<br>
Keras                            2.3.1<br>
Keras-Applications               1.0.8<br>
keras-bert                       0.80.0<br>
keras-embed-sim                  0.10.0<br>
keras-layer-normalization        0.16.0<br>
keras-multi-head                 0.29.0<br>
keras-pos-embd                   0.13.0<br>
keras-position-wise-feed-forward 0.8.0<br>
Keras-Preprocessing              1.1.2<br>
keras-self-attention             0.51.0<br>
keras-transformer                0.40.0<br>
Markdown                         3.3.7<br>
mock                             4.0.3<br>
numpy                            1.19.5<br>
oauthlib                         3.2.1<br>
opt-einsum                       3.3.0<br>
pip                              21.2.2<br>
protobuf                         3.19.5<br>
pyasn1                           0.4.8<br>
pyasn1-modules                   0.2.8<br>
PyYAML                           6.0<br>
requests                         2.27.1<br>
requests-oauthlib                1.3.1<br>
rsa                              4.9<br>
scipy                            1.4.1<br>
setuptools                       58.0.4<br>
six                              1.16.0<br>
tensorboard                      2.1.1<br>
tensorflow                       2.5.0<br>
tensorflow-estimator             2.5.0<br>
termcolor                        1.1.0<br>
tqdm                             4.64.1<br>
typing_extensions                4.1.1<br>
urllib3                          1.26.12<br>
Werkzeug                         2.0.3<br>
wheel                            0.37.1<br>
wrapt                            1.14.1<br>
zipp                             3.6.0<br>
