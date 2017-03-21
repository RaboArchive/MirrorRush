import json;
from io import StringIO;

def loadJsonFile(path):
    # Opening json file given by the path
    # Returning a python dictionnary
    f = open(path,'r');
    fileLoaded = json.load(f);
    f.close();
    return fileLoaded;

def saveOptions(path, options):
    # With à given path and a Python dictionnary
    # Saving it in a Json file
    f = open(path,'w');
    f.write(json.JSONEncoder().encode(options));
    f.close();
