# Import Datasets
Before training the model, the training set and test set need to be added to today's file. Go to the path: `<./PRGC/data/>` ， and execute the following command:<br>
```
python get_data.py
```
Download BERT-Base-Cased which contains pytroch_model.bin, vocab.txt and config.json. Put these under `<./PRGC/pretrain_models>`.

# Commands for Training The Model
### NYT
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=NYT --ensure_corres --ensure_rel
```

### NYT*
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=NYT_star --ensure_corres --ensure_rel
```

### WebNLG
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=WebNLG --ensure_corres --ensure_rel
```

### WebNLG*
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=WebNLG_star --ensure_corres --ensure_rel
```

### NYT_generate
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=NYT_generate --ensure_corres --ensure_rel
```

### NYT*_generate
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=NYT_star_generate --ensure_corres --ensure_rel
```

### WebNLG_generate
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=WebNLG_generate --ensure_corres --ensure_rel
```

### WebNLG*_generate
```
python train.py --ex_index=1 --epoch_num=100 --device_id=0 --corpus_type=WebNLG_star_generate --ensure_corres --ensure_rel
```

# Commands for Testing Process
### NYT
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=NYT --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```

### NYT*
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=NYT_star --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```

## WebNLG
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=WebNLG --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```

## WebNLG*
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=WebNLG_star --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```

### NYT_generate
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=NYT_generate --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```

### NYT*_generate
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=NYT_star_generate --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```

## WebNLG_generate
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=WebNLG_generate --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```

## WebNLG*_generate
```
python ../evaluate.py --ex_index=1 --device_id=0 --mode=test --corpus_type=WebNLG_star_generate --ensure_corres --ensure_rel --corres_threshold=0.5 --rel_threshold=0.1
```


# Environment Configuration
To configure the environment for OneRel, perform the following steps

1. conda create -n PRGC_env python=3.7
2. conda activate PRGC_env
3. pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
4. pip install transformers==3.2.0
5. pip install tqdm

After the configuration is complete, you will get the following configuration information:

certifi            2022.9.14<br>
charset-normalizer 2.1.1<br>
click              8.1.3<br>
filelock           3.8.0<br>
idna               3.4<br>
importlib-metadata 5.0.0<br>
joblib             1.2.0<br>
numpy              1.21.6<br>
packaging          21.3<br>
Pillow             9.2.0<br>
pip                22.2.2<br>
pyparsing          3.0.9<br>
regex              2022.9.13<br>
requests           2.28.1<br>
sacremoses         0.0.53<br>
sentencepiece      0.1.97<br>
setuptools         63.4.1<br>
six                1.16.0<br>
tokenizers         0.8.1rc2<br>
torch              1.10.1+cu111<br>
torchaudio         0.10.1+rocm4.1<br>
torchvision        0.11.2+cu111<br>
tqdm               4.64.1<br>
transformers       3.2.0<br>
typing_extensions  4.3.0<br>
urllib3            1.26.12<br>
wheel              0.37.1<br>
zipp               3.8.1<br>
