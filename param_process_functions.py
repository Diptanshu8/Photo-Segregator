import sys,os
import argparse
import config

def check_params():
    parser = argparse.ArgumentParser(description='This is a Photo Segregator Application.')
    parser.add_argument('path', action="store", help="Path to an image or a directory of images.")

    results = parser.parse_args()
    if os.path.isdir(results.path):
        test_dir = results.path
        test_image = [os.path.join(test_dir,item) for item in os.listdir(test_dir) if os.path.splitext(item)[1] in config.image_extention_processable]
    else:
        test_image = [results.path]
    return test_image 

   
