from django.apps import AppConfig
import html
import pathlib
from pathlib import Path
import os

from fast_bert.prediction import BertClassificationPredictor

class WebappConfig(AppConfig):
    name = 'videos'
    MODEL_PATH = Path("model")
    BERT_PRETRAINED_PATH = Path("model/uncased_L-12_H-768_A-12/")
    LABEL_PATH = Path("label/")
    predictor = BertClassificationPredictor(#model_path = MODEL_PATH/"pytorch_model.bin", 
                                            model_path = "unitary/toxic-bert",
                                            #pretrained_path = BERT_PRETRAINED_PATH, 
                                            label_path = LABEL_PATH, multi_label=True)