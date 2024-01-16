import json
import sys
from pathlib import Path
from jsonschema import validate

class Configuration:
    
    def __init__(self, configurationDirectory):
        self.configurationDirectory = configurationDirectory
        
    def loadJsonFile(self, fileName, schema = None):
    
        try:
            jsonFile = open(Path(self.configurationDirectory).joinpath(fileName),"r")
        
        except:
            sys.exit("ERROR: File '" + Path(self.configurationDirectory).joinpath(fileName) + "' does not exist.")
        
        dictionary = json.load(jsonFile)
        
        if schema != None:
            validate(dictionary, schema)
            
        jsonFile.close()
        return dictionary

    def writeJsonFile(self, fileName, dictionary, schema = None):
        if schema != None:
            validate(dictionary, schema)

        file = open(fileName, 'w')            
        json.dump(dictionary, file, indent=2)
        
    def resolveCmd(self, cmd):
        if Path(cmd).is_absolute():
            return cmd
        
        if Path(self.configurationDirectory).joinpath(cmd).exists():
            return str(Path(self.configurationDirectory).joinpath(cmd))
            
        return cmd