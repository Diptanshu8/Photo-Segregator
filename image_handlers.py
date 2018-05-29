import cv2
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
    print "Submit Button Clicked!"
def dont_save_snippet():
    print "Cancel Button Clicked!"
    
def show_face_snippet():
    app = T.Tk()

    image = Image.open(config.cache)            # Opening the face snippet stored as cache image
    photo = ImageTk.PhotoImage(image)           # Creating a photoImage variable for showing in Tkinter
    print "Created PhotoImage."
    L_img = T.Label(app, image=photo)
    L_img.image = photo
    L_img.pack()

    L1 = T.Label(app, text="Snippet Name")
    L1.pack()
    
    E1 = T.Entry(app)
    E1.pack()
    
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
        cv2.imwrite(config.cache,face_img)              # writing the face snippet as .cache.png initially
                                                        # later if the user inputs a name for this snippet
                                                        #then saving it with that name.
        yield img
        img = o_img.copy()


