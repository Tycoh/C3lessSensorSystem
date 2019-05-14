# -*- coding: utf-8 -*-

import yaml

def readYaml(yamlPath):
    print('reading Yaml file from '+yamlPath)
    with open(yamlPath,'r',encoding="utf-8") as file:
        yml=yaml.load(file)
    return yml