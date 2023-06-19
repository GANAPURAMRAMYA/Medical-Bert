from bs4 import BeautifulSoup
import requests
import re
!pip install transformers
Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
Collecting transformers
  Downloading transformers-4.29.1-py3-none-any.whl (7.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 51.4 MB/s eta 0:00:00
Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from transformers) (3.12.0)
Collecting huggingface-hub<1.0,>=0.14.1 (from transformers)
  Downloading huggingface_hub-0.14.1-py3-none-any.whl (224 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.5 kB 25.7 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (1.22.4)
Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from transformers) (23.1)
Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (6.0)
Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (2022.10.31)
Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from transformers) (2.27.1)
Collecting tokenizers!=0.11.3,<0.14,>=0.11.1 (from transformers)
  Downloading tokenizers-0.13.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.8/7.8 MB 91.5 MB/s eta 0:00:00
Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.10/dist-packages (from transformers) (4.65.0)
Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.14.1->transformers) (2023.4.0)
Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.14.1->transformers) (4.5.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (1.26.15)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2022.12.7)
Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (3.4)
Installing collected packages: tokenizers, huggingface-hub, transformers
Successfully installed huggingface-hub-0.14.1 tokenizers-0.13.3 transformers-4.29.1
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("ugaray96/biobert_ncbi_disease_ner")
model = AutoModelForTokenClassification.from_pretrained("ugaray96/biobert_ncbi_disease_ner")

pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
Downloading (…)okenizer_config.json: 100%
534/534 [00:00<00:00, 9.52kB/s]
Downloading (…)lve/main/config.json: 100%
780/780 [00:00<00:00, 25.5kB/s]
Downloading (…)solve/main/vocab.txt: 100%
213k/213k [00:00<00:00, 3.93MB/s]
Downloading (…)cial_tokens_map.json: 100%
112/112 [00:00<00:00, 4.15kB/s]
Downloading pytorch_model.bin: 100%
431M/431M [00:07<00:00, 59.9MB/s]
URL="https://www.who.int/health-topics/coronavirus#tab=tab_1"
html_content = requests.get(URL).text
soup = BeautifulSoup(html_content, "lxml")
body=soup.body.text
body= body.replace('\n', ' ')
body= body.replace('\xa0', ' ')
passage=body[2975:4000]
pipe(passage)
[{'entity_group': 'Disease',
  'score': 0.77780175,
  'word': 'Corona',
  'start': 1,
  'end': 7},
 {'entity_group': 'Disease Continuation',
  'score': 0.9994961,
  'word': '##virus disease',
  'start': 7,
  'end': 20},
 {'entity_group': 'No Disease',
  'score': 0.9998833,
  'word': '(',
  'start': 21,
  'end': 22},
 {'entity_group': 'Disease',
  'score': 0.99949193,
  'word': 'CO',
  'start': 22,
  'end': 24},
 {'entity_group': 'Disease Continuation',
  'score': 0.9927835,
  'word': '##VID - 19',
  'start': 24,
  'end': 30},
 {'entity_group': 'No Disease',
  'score': 0.9999471,
  'word': ') is an',
  'start': 30,
  'end': 37},
 {'entity_group': 'Disease',
  'score': 0.5343511,
  'word': 'infectious',
  'start': 38,
  'end': 48},
 {'entity_group': 'Disease Continuation',
  'score': 0.8431151,
  'word': 'disease',
  'start': 49,
  'end': 56},
 {'entity_group': 'No Disease',
  'score': 0.9998767,
  'word': 'caused by the',
  'start': 57,
  'end': 70},
 {'entity_group': 'Disease',
  'score': 0.7147005,
  'word': 'SA',
  'start': 71,
  'end': 73},
 {'entity_group': 'Disease Continuation',
  'score': 0.81189626,
  'word': '##RS - CoV - 2',
  'start': 73,
  'end': 81},
 {'entity_group': 'No Disease',
  'score': 0.99780625,
  'word': 'virus. Most people infected with the virus will experience mild to moderate',
  'start': 82,
  'end': 156},
 {'entity_group': 'Disease',
  'score': 0.98940897,
  'word': 'respiratory',
  'start': 157,
  'end': 168},
 {'entity_group': 'Disease Continuation',
  'score': 0.99763083,
  'word': 'illness',
  'start': 169,
  'end': 176},
 {'entity_group': 'No Disease',
  'score': 0.97332907,
  'word': 'and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like',
  'start': 177,
  'end': 359},
 {'entity_group': 'Disease',
  'score': 0.99897134,
  'word': 'card',
  'start': 360,
  'end': 364},
 {'entity_group': 'Disease Continuation',
  'score': 0.9619364,
  'word': '##iovascular disease',
  'start': 364,
  'end': 382},
 {'entity_group': 'No Disease',
  'score': 0.99815375,
  'word': ',',
  'start': 382,
  'end': 383},
 {'entity_group': 'Disease',
  'score': 0.9737603,
  'word': 'diabetes',
  'start': 384,
  'end': 392},
 {'entity_group': 'No Disease',
  'score': 0.99986374,
  'word': ',',
  'start': 392,
  'end': 393},
 {'entity_group': 'Disease',
  'score': 0.9981515,
  'word': 'chronic',
  'start': 394,
  'end': 401},
 {'entity_group': 'Disease Continuation',
  'score': 0.9989959,
  'word': 'respiratory disease',
  'start': 402,
  'end': 421},
 {'entity_group': 'No Disease',
  'score': 0.9998627,
  'word': ', or',
  'start': 421,
  'end': 425},
 {'entity_group': 'Disease',
  'score': 0.9983329,
  'word': 'cancer',
  'start': 426,
  'end': 432},
 {'entity_group': 'No Disease',
  'score': 0.99956346,
  'word': 'are more likely to develop serious illness. Anyone can get sick with',
  'start': 433,
  'end': 501},
 {'entity_group': 'Disease',
  'score': 0.9992347,
  'word': 'CO',
  'start': 502,
  'end': 504},
 {'entity_group': 'Disease Continuation',
  'score': 0.9916019,
  'word': '##VID - 19',
  'start': 504,
  'end': 510},
 {'entity_group': 'No Disease',
  'score': 0.99994123,
  'word': 'and become seriously ill or die at any age. The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol - based rub frequently. Get vaccinated when it ’ s your turn and follow local guidance. The virus can spread from an infected person ’ s mouth or nose in small liquid particles when they cough,',
  'start': 511,
  'end': 1025}]
