import cv2
import os
import config
import image_handlers as ih

def show_train_snippets():
    snips = [os.path.join(config.train_cache,item) for item in os.listdir(config.train_cache)]
    for snip in snips:
        img = cv2.imread(snip)
        print "Image: {}".format(snip)
        ih.show_image(img)

if __name__=="__main__":
    show_train_snippets()
