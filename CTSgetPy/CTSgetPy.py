# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:11:14 2019

@author: hcji
"""

import re
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def CTS_options(url="http://cts.fiehnlab.ucdavis.edu/service/conversion/toValues"): 
    response = requests.get(url, timeout=60)
    strings = str(response.content)
    output = re.findall(r'\"(.+?)\"', strings)
    return output


def CTS_translate(source, target, identifier, top_only=True, timeout=60, server="http://cts.fiehnlab.ucdavis.edu/service/convert"):
    url = server
    url += '/' + str(source)
    url += '/' + str(target)
    url += '/' + str(identifier)
    response = requests.get(url, timeout=timeout)
    soup = BeautifulSoup(response.content, "html.parser")
    output = json.loads(str(soup))
    try:
        if top_only:
            return output[0]['result'][0]
        else:
            return output[0]['result']
    except:
        return ''
    
    
def CTS_translate_multi(source, target, identifiers, top_only=True, timeout=60, server="http://cts.fiehnlab.ucdavis.edu/service/convert"):
    result = {}
    if type(identifiers) is str:
        result[identifiers] = CTS_translate(source, target, identifiers, top_only, timeout, server)
    elif type(identifiers) is list:
        for i in tqdm(range(len(identifiers))):
            identifier = str(identifiers[i])
            result[identifier] = CTS_translate(source, target, identifier, top_only, timeout, server)
    else:
        raise IOError('Input identifiers should be string or a list of strings')
    return result
    

def CTSget(source, targets, identifiers, top_only=True, timeout=60, server="http://cts.fiehnlab.ucdavis.edu/service/convert"):
    result = {}
    if type(targets) is str:
        result[targets] = CTS_translate_multi(source, targets, identifiers, top_only, timeout, server)
    elif type(targets) is list:
        for i in range(len(targets)):
            target = targets[i]
            print ('translating from ' + source + ' to ' + target)
            result[target] = CTS_translate_multi(source, target, identifiers, top_only, timeout, server)
    else:
        raise IOError('Input targets should be string or a list of strings')   
    return result
