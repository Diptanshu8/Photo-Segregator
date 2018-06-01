import cv2
import os
import shutil
import config
import argparse
import image_handlers as ih

def show_train_snippets():
    if not os.path.isdir(config.train_cache) or not os.listdir(config.train_cache):
        print "Error: There are no trainned snippets as cache."
        return 
    snips = [os.path.join(config.train_cache,item) for item in os.listdir(config.train_cache)]
    for i,snip in enumerate(snips):
        print "Image<{}>: {}".format(i+1,snip)
        ih.show_image(snip)

def delete_train_snippets():
    if not os.path.isdir(config.train_cache) or not os.listdir(config.train_cache):
        print "Error: There are no trainned snippets as cache."
        return 
    user_choice = raw_input("Are you sure you want to delete the trained snippets?")
    valid = {"yes": True, "y": True, "Y": True, "YES" : True, "Yes": True,
            "no": False, "n": False, "NO": False, "No": False, "N": False}
    if not valid.has_key(user_choice):
        print "Valid user_choices are:"
        print valid.keys()
        delete_train_snippets()
    else:
        if valid[user_choice]:
            try:
                shutil.rmtree(config.train_cache)
                print "Removed the trained snippets that were cached."
            except Exception as e:
                print e
        else:
            print "Exiting without removing the trained cache."

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='This is a Photo Segregator Application.')
    group = parser.add_argument_group('utility')
    group.add_argument('-s', action="store_true",
            help="Pass this argument to see all the saved snippets identified by the user.")

    group.add_argument('-d', action="store_true",
            help="Pass this argument to delete all the saved snippets identified by the user.")
    
    results = parser.parse_args()
    if not any(vars(results).values()):
        parser.error("No arguments provided. Either of -s or -d to be provided.")
    if results.s:
        show_train_snippets()
    if results.d:
        delete_train_snippets()
