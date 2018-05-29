import cv2
import Tkinter as T
import tkMessageBox
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
    
#def show_face_snippet(face_snippet):
def show_face_snippet():
    app = T.Tk()
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
        yield(img,face_img)
        img = o_img.copy()


