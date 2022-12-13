# Import Datasets
Before training the model, the training set and test set need to be added to today's file. Go to the path: `<./TPLinker/data/>` ， and execute the following command:<br>
```
python get_data.py
```
Download BERT-Base-Cased which contains pytroch_model.bin, vocab.txt and config.json. Put these under `<./TPLinker/data/>`.

# Commands for Training and Testing The Model
### NYT
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to NYT
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```

### NYT*
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to NYT_star
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```

### WebNLG
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to WebNLG
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```

### WebNLG*
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to WebNLG_star
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```

### NYT_generate
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to NYT_generate
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```

### NYT*_generate
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to NYT_star_generate
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```

### WebNLG_generate
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to WebNLG_generate
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```

### WebNLG*_generate
Modify line B of the code in file `<./TPLinker/tplinker/run_tplinker.py>` to change the data set to WebNLG_star_generate
```
nohup python -m tplinker.run_tplinker --gpus=0 >> train.log 2>&1 &
```


# Environment Configuration
To configure the environment for OneRel, perform the following steps

1. conda create -n TPLinker_env python=3.7
2. conda activate TPLinker_env
3. pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
4. pip install transformers==3.2.0
5. pip install tqdm
6. pip install pytorch-lightning

After the configuration is complete, you will get the following configuration information:

absl-py                 1.2.0<br>
aiohttp                 3.8.3<br>
aiosignal               1.2.0<br>
async-timeout           4.0.2<br>
asynctest               0.13.0<br>
attrs                   22.1.0<br>
cachetools              5.2.0<br>
certifi                 2022.9.14<br>
charset-normalizer      2.1.1<br>
click                   8.1.3<br>
filelock                3.8.0<br>
frozenlist              1.3.1<br>
fsspec                  2022.8.2<br>
google-auth             2.12.0<br>
google-auth-oauthlib    0.4.6<br>
grpcio                  1.49.1<br>
idna                    3.4<br>
importlib-metadata      5.0.0<br>
joblib                  1.2.0<br>
Markdown                3.4.1<br>
MarkupSafe              2.1.1<br>
multidict               6.0.2<br>
numpy                   1.21.6<br>
oauthlib                3.2.1<br>
packaging               21.3<br>
Pillow                  9.2.0<br>
pip                     22.2.2<br>
protobuf                3.19.6<br>
pyasn1                  0.4.8<br>
pyasn1-modules          0.2.8<br>
pyDeprecate             0.3.2<br>
pyparsing               3.0.9<br>
pytorch-lightning       1.7.7<br>
PyYAML                  6.0<br>
regex                   2022.9.13<br>
requests                2.28.1<br>
requests-oauthlib       1.3.1<br>
rsa                     4.9<br>
sacremoses              0.0.53<br>
sentencepiece           0.1.97<br>
setuptools              63.4.1<br>
six                     1.16.0<br>
tensorboard             2.10.1<br>
tensorboard-data-server 0.6.1<br>
tensorboard-plugin-wit  1.8.1<br>
tokenizers              0.8.1rc2<br>
torch                   1.10.1+cu111<br>
torchaudio              0.10.1+rocm4.1<br>
torchmetrics            0.10.0<br>
torchvision             0.11.2+cu111<br>
tqdm                    4.64.1<br>
transformers            3.2.0<br>
typing_extensions       4.3.0<br>
urllib3                 1.26.12<br>
Werkzeug                2.2.2<br>
wheel                   0.37.1<br>
yarl                    1.8.1<br>
zipp                    3.8.1<br>
