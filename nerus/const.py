
from os import getenv

from .path import (
    get_dir,
    join_path,
    norm_path,
    expand_user
)


#########
#
#   NERUS
#
########


NERUS = 'nerus'
NERUS_DIR = norm_path(join_path(get_dir(__file__), '..'))


##########
#
#   WORKER
#
#########


LOCALHOST = 'localhost'

WORKER_NAME = getenv('WORKER_NAME', NERUS)
WORKER_HOST = getenv('WORKER_HOST', LOCALHOST)
WORKER_ANNOTATOR = getenv('WORKER_ANNOTATOR')
WORKER_QUEUE = getenv('WORKER_QUEUE')


#######
#
#   MARKUP
#
########


PER = 'PER'
ORG = 'ORG'
LOC = 'LOC'


#######
#
#   BIO
#
######


B = 'B'
I = 'I'
O = 'O'


#######
#
#   FACTRU
#
########


FACTRU = 'factru'
FACTRU_DIR = 'factRuEval-2016-master'
FACTRU_TESTSET = 'testset'
FACTRU_DEVSET = 'devset'


#######
#
#   NE5
#
#######


NE5 = 'ne5'
NE5_DIR = 'Collection5'


#######
#
#   GAREEV
#
#######


GAREEV = 'gareev'
GAREEV_DIR = 'rus-ner-news-corpus.iob'


#########
#
#   WIKINER
#
#########


WIKINER = 'wikiner'
WIKINER_URL = 'https://github.com/dice-group/FOX/blob/master/input/Wikiner/aij-wikiner-ru-wp3.bz2'
WIKINER_FILENAME = 'aij-wikiner-ru-wp3.bz2'


#######
#
#   LENTA
#
#######


LENTA = 'lenta'
LENTA_URL = 'https://github.com/yutkin/Lenta.Ru-News-Dataset/releases/download/v1.0/lenta-ru-news.csv.gz'
LENTA_FILENAME = 'lenta-ru-news.csv.gz'


#######
#
#   BSNLP
#
#######


BSNLP = 'bsnlp'
BSNLP_DIR = 'bsnlp'


##########
#
#  SOURCES
#
#########


SOURCES = [FACTRU, NE5, LENTA, WIKINER, GAREEV, BSNLP]
SOURCES_DIR = getenv('SOURCES_DIR', join_path(NERUS_DIR, 'data', 'sources'))


########
#
#  ANNOTATORS
#
#######


ANNOTATORS_HOST = WORKER_HOST
ANNOTATORS_BASE_PORT = 8080


#######
#
#   DEEPPAVLOV
#
########


DEEPPAVLOV = 'deeppavlov'
DEEPPAVLOV_HOST = getenv('DEEPPAVLOV_HOST', ANNOTATORS_HOST)
DEEPPAVLOV_PORT = int(getenv('DEEPPAVLOV_PORT', 8081))

DEEPPAVLOV_IMAGE = getenv('DEEPPAVLOV_IMAGE', 'natasha/deeppavlov-ner-ru')
DEEPPAVLOV_CONTAINER_PORT = 5000

DEEPPAVLOV_SECTION = int(getenv('DEEPPAVLOV_TOKENS', 1000))
DEEPPAVLOV_BATCH = int(getenv('DEEPPAVLOV_BATCH', 100))

DEEPPAVLOV_URL = 'http://{host}:{port}/ner'


#######
#
#   DEEPPAVLOV BERT
#
########


DEEPPAVLOV_BERT = 'deeppavlov_bert'
DEEPPAVLOV_BERT_HOST = getenv('DEEPPAVLOV_BERT_HOST', ANNOTATORS_HOST)
DEEPPAVLOV_BERT_PORT = int(getenv('DEEPPAVLOV_BERT_PORT', 8086))

DEEPPAVLOV_BERT_IMAGE = getenv('DEEPPAVLOV_IMAGE', 'natasha/deeppavlov-ner-ru-bert')
DEEPPAVLOV_BERT_CONTAINER_PORT = 5000

# assume 200 tokens split by whitespace < 512 bert tokens
DEEPPAVLOV_BERT_SECTION = int(getenv('DEEPPAVLOV_BERT_TOKENS', 200))
DEEPPAVLOV_BERT_BATCH = int(getenv('DEEPPAVLOV_BERT_BATCH', 100))

DEEPPAVLOV_BERT_URL = 'http://{host}:{port}/ner'


#########
#
#  MITIE
#
#########


MITIE = 'mitie'
MITIE_HOST = getenv('MITIE_HOST', ANNOTATORS_HOST)
MITIE_PORT = int(getenv('MITIE_PORT', 8083))

MITIE_IMAGE = 'natasha/mitie-ner-ru'
MITIE_CONTAINER_PORT = 8080

MITIE_URL = 'http://{host}:{port}/'


#########
#
#   NATASHA
#
#########


NATASHA = 'natasha'
NATASHA_HOST = getenv('NATASHA_HOST', ANNOTATORS_HOST)
NATASHA_PORT = int(getenv('NATASHA_PORT', 8085))

NATASHA_IMAGE = 'natasha/natasha:0.10.0'
NATASHA_CONTAINER_PORT = 8080

NATASHA_URL = 'http://{host}:{port}/'


#######
#
#   PULLENTI
#
#####


PULLENTI = 'pullenti'
PULLENTI_HOST = getenv('PULLENTI_HOST', ANNOTATORS_HOST)
PULLENTI_PORT = int(getenv('PULLENTI_PORT', 8080))

PULLENTI_IMAGE = 'pullenti/pullenti-server:3.17'
PULLENTI_CONTAINER_PORT = 8080


########
#
#   TEXTERRA
#
###########


TEXTERRA = 'texterra'
TEXTERRA_HOST = getenv('TEXTERRA_HOST', ANNOTATORS_HOST)
TEXTERRA_PORT = int(getenv('TEXTERRA_PORT', 8082))

TEXTERRA_IMAGE = 'natasha/texterra-russian'
TEXTERRA_CONTAINER_PORT = 8080

TEXTERRA_CHUNK = int(getenv('TEXTERRA_CHUNK', 30000))
# if lang is undefined may try to load eng model and fail
TEXTERRA_URL = 'http://{host}:{port}/texterra/nlp?targetType=named-entity&language=ru'


#########
#
#  TOMITA
#
########


TOMITA = 'tomita'
TOMITA_HOST = getenv('TOMITA_HOST', ANNOTATORS_HOST)
TOMITA_PORT = int(getenv('TOMITA_PORT', 8084))

TOMITA_IMAGE = 'natasha/tomita-algfio'
TOMITA_CONTAINER_PORT = 8080

TOMITA_URL = 'http://{host}:{port}/'


########
#
#  ANNOTATORS
#
#########


ANNOTATORS = [DEEPPAVLOV, DEEPPAVLOV_BERT, PULLENTI, TEXTERRA, TOMITA, NATASHA, MITIE]


########
#
#   QUEUE
#
########


FAILED = 'failed'
QUEUE_HOST = getenv('QUEUE_HOST', WORKER_HOST)
QUEUE_PORT = int(getenv('QUEUE_PORT', 6379))
QUEUE_PASSWORD = getenv('QUEUE_PASSWORD', 'ENvHwwFLhiKe7hE')


########
#
#   DB
#
##########


SOURCE = 'source'
LABEL = 'label'
TEXT = 'text'
_ID = '_id'

DB_HOST = getenv('DB_HOST', WORKER_HOST)
DB_PORT = int(getenv('DB_PORT', 27017))
DB_NAME = 'db'
DB_USERNAME = getenv('DB_USERNAME', 'root')
DB_PASSWORD = getenv('DB_PASSWORD', 'Yax6mUVzdXzsCCo')


########
#
#   YC
#
#########


YC_TOKEN = getenv('YC_TOKEN')
YC_CLOUD = getenv('YC_CLOUD')
YC_FOLDER = getenv('YC_FOLDER', 'default')
YC_SUBNET = getenv('YC_SUBNET', 'default')

YC_UBUNTU_1604 = 'standard-images/ubuntu-1604-lts'
YC_HDD = 'network-hdd'
YC_PLATFORM = 'standard-v1'


#######
#
#  SSH
#
########


SSH_USER = NERUS
SSH_KEY = getenv('SSH_KEY', expand_user('~/.ssh/id_rsa.pub'))
SSH_PRIVATE_KEY = getenv('SSH_PRIVATE_KEY', expand_user('~/.ssh/id_rsa'))
SSH_CONFIG = getenv('SSH_CONFIG', expand_user('~/.ssh/nerus.conf'))


######
#
#   DUMP
#
#######


DUMPS_DIR = join_path(NERUS_DIR, 'data', 'dumps')
NERUS_ = 'nerus_'
NORM = 'norm'
RAW = '.raw'
JSONL = '.jsonl'
GZ = '.gz'


#########
#
#   GPU
#
#########


GPU_LABEL = NERUS
GPU_USER = 'root'
GPU_IMAGE = DEEPPAVLOV_BERT_IMAGE
GPU_CONTAINER_PORT = DEEPPAVLOV_BERT_CONTAINER_PORT
