import cv2
import os
import shutil
import Tkinter as T
import tkMessageBox
from PIL import Image, ImageTk

import config


def show_image(image):
    cv2.imshow('Image',image)
    while(1):
	k = cv2.waitKey(0)
	if k==27: #stopping for escape
	    exit()
	elif k==32:
	    break

def save_snippet():
    global E
    global app
    user_input =  E.get()
    app.destroy()

    snippet_name = user_input + config.cache_img_extension
    if not os.path.isdir(config.train_cache):
        os.mkdir(config.train_cache)
    samples = os.listdir(config.train_cache)
    count = samples.count(snippet_name)
    if count == 0:
        shutil.copy(config.cache_img_name+config.cache_img_extension,os.path.join(config.train_cache,snippet_name)) 
    else:
        #code if the sample name exists.
        i = 1
        newname = os.path.join(config.train_cache,snippet_name,"_",i,config.cache_img_extension)
        if os.path.exists(newname):
            print os.listdir 
    
def dont_save_snippet():
    global app
    app.destroy()
    
def show_face_snippet():
    global app
    global E
    app = T.Tk()
    app.attributes('-topmost', 1)
    #app.attributes('-topmost', 0)

    image = Image.open(config.cache_img_name+config.cache_img_extension)            # Opening the face snippet stored as cache image
    photo = ImageTk.PhotoImage(image)           # Creating a photoImage variable for showing in Tkinter
    
    L_img = T.Label(app, image=photo)
    L_img.image = photo
    L_img.pack()

    L1 = T.Label(app, text="Snippet Name")
    L1.pack()
    
    E = T.Entry(app,justify = T.CENTER)
    E.pack()
    E.focus_set()
    
    BL = T.Button(app, text ="Submit", command = save_snippet)
    BR = T.Button(app, text ="Cancel", command = dont_save_snippet)
    BL.pack(side = T.LEFT)
    BR.pack(side = T.RIGHT)
    
    app.mainloop()

def show_all_faces(face_locations,img):
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
    return img

def show_individual_faces(face_locations,img):
    o_img = img.copy()
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        face_img = img[top: bottom , left: right]       # a snippet for taking user input for that face.
        cv2.imwrite(config.cache_img_name+config.cache_img_extension,face_img)              # writing the face snippet as .cache.jpg initially
                                                        # later if the user inputs a name for this snippet
                                                        #then saving it with that name.
        yield img
        img = o_img.copy()


