# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:20:34 2017

@author: anand.prakash
"""

import os
import nltk


exampleArray = ['Anand is a good boy. He is so smart.']



def processContent():
    try:
        for item in exampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print(tagged)
            
            
            
    except Exception as e:
        print(str(e))
    
processContent()
