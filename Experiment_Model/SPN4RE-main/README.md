# Import Datasets
Before training the model, the training set and test set need to be added to today's file. Go to the path: `<./SPN4RE/data/>` ， and execute the following command:<br>
```
python get_data.py
```

Download bert-base-cased to path  `<SPN4RE/datasets/bert/>`
```
git clone https://huggingface.co/bert-base-cased
```
remove the bert-base-cased file to `<SPN4RE/datasets/bert/>`

# Commands for Training and Testing The Model

NYT, NYT_generate Exact Match
```
python -m main --bert_directory BERT_DIR --num_generated_triples 15 --max_grad_norm 2.5 --na_rel_coef 0.25 --max_epoch 100 --max_span_length 10
```
or NYT_star, NYT_star_generate Partial Match
```
python -m main --bert_directory BERT_DIR --num_generated_triples 15 --max_grad_norm 1 --na_rel_coef 0.5 --max_epoch 100 --max_span_length 10
```
WebNLG, WebNLG_generate Partial Match
```
python -m main --bert_directory BERT_DIR --batch_size 4 --num_generated_triples 10 --na_rel_coef 0.25 --max_grad_norm 20  --max_epoch 100 --encoder_lr 0.00002 --decoder_lr 0.00005 --num_decoder_layers 4 --max_span_length 10 --weight_decay 0.000001 --lr_decay 0.02
```

# Environment Configuration
To configure the environment for OneRel, perform the following steps

1. conda create -n SPN4RE_env python=3.7
2. conda activate SPN4RE_env
3. pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
4. pip install transformers==2.6.0
5. pip install scipy

After the configuration is complete, you will get the following configuration information:

boto3              1.24.87<br>
botocore           1.27.87<br>
certifi            2022.9.14<br>
charset-normalizer 2.1.1<br>
click              8.1.3<br>
filelock           3.8.0<br>
idna               3.4<br>
importlib-metadata 5.0.0<br>
jmespath           1.0.1<br>
joblib             1.2.0<br>
numpy              1.21.6<br>
Pillow             9.2.0<br>
pip                22.2.2<br>
python-dateutil    2.8.2<br>
regex              2022.9.13<br>
requests           2.28.1<br>
s3transfer         0.6.0<br>
sacremoses         0.0.53<br>
scipy              1.7.3<br>
sentencepiece      0.1.97<br>
setuptools         63.4.1<br>
six                1.16.0<br>
tokenizers         0.5.2<br>
torch              1.10.1+cu111<br>
torchaudio         0.10.1+rocm4.1<br>
torchvision        0.11.2+cu111<br>
tqdm               4.64.1<br>
transformers       2.6.0<br>
typing_extensions  4.3.0<br>
urllib3            1.26.12<br>
wheel              0.37.1<br>
zipp               3.8.1<br>
