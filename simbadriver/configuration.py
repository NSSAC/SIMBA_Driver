import os
import json
import sys
from jsonschema import validate

class Configuration:
    
    def __init__(self, configurationDirectory):
        self.configurationDirectory = configurationDirectory
        
    def loadJsonFile(self, fileName, schema = None):
    
        try:
            jsonFile = open(os.path.join(self.configurationDirectory, fileName),"r")
        
        except:
            sys.exit("ERROR: File '" + os.path.join(self.configurationDirectory, fileName) + "' does not exist.")
        
        dictionary = json.load(jsonFile)
        
        if schema != None:
            validate(dictionary, schema)
            
        jsonFile.close()
        return dictionary