# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 02:57:20 2017

@author: anand.prakash
"""


from nltk.tag import StanfordPOSTagger

stanford_pos_dir = 'C:\Users\anand.prakash\Downloads\stanford-corenlp-full/'
eng_model_filename= stanford_pos_dir + 'models/english-left3words-distsim.tagger'
my_path_to_jar= stanford_pos_dir + 'stanford-postagger.jar'

st = StanfordPOSTagger(model_filename=eng_model_filename, path_to_jar=my_path_to_jar) 
st.tag('What is the airspeed of an unladen swallow ?'.split())


# NER Tagging:
from nltk.tag import StanfordNERTagger

stanford_ner_dir = 'C:\Users\anand.prakash\Downloads\stanford-corenlp-full'
eng_model_filename= stanford_ner_dir + 'classifiers/english.all.3class.distsim.crf.ser.gz'
my_path_to_jar= stanford_ner_dir + 'stanford-ner.jar'

st = StanfordNERTagger(model_filename=eng_model_filename, path_to_jar=my_path_to_jar) 
st.tag('Rami Eid is studying at Stony Brook University in NY'.split())

# Parsing:
from nltk.parse.stanford import StanfordParser

stanford_parser_dir = 'C:\Users\anand.prakash\Downloads\stanford-corenlp-full'
eng_model_path = stanford_parser_dir  + "edu/stanford/nlp/models/lexparser/englishRNN.ser.gz"
my_path_to_models_jar = stanford_parser_dir  + "stanford-parser-3.5.2-models.jar"
my_path_to_jar = stanford_parser_dir  + "stanford-parser.jar"

parser=StanfordParser(model_path=eng_model_path, path_to_models_jar=my_path_to_models_jar, path_to_jar=my_path_to_jar)
print(parser)
