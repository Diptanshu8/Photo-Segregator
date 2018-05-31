import os
import config

def check_train_snippets():
    if not os.path.isdir(config.train_cache) or not os.listdir(config.train_cache):
        print "Error: There are no trainned snippets as cache."
        return False 
    return True

def print_train_snippets():
    if check_train_snippets():
        snips = [item for item in os.listdir(config.train_cache)]
        print "The following are the train snippets in random order.\nTo view them simply run train_utility.py with proper parameters."
        for i,snip in enumerate(snips):
            print "Image<{}>: {}".format(i+1,snip)
        return snips
