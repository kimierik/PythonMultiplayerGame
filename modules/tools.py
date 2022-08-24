#this file contains useful functions 
#
#
#
#
#
#
import time

def string_to_json(string):
    string=string.replace("\*","\"")
    return json.loads(string)





