import face_recognition
import cv2
import os,sys
import param_process_functions as pp
def show_image(image):
    cv2.imshow('Image',image)
    while(1):
	k = cv2.waitKey(0)
	if k==27: #stopping for escape
	    exit()
	elif k==32:
	    break

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


def main():
    test_image = pp.check_params()
    print "Done compiling params and total number of images to be processed is: " + str(len(test_image))
    for test in test_image:
    	print "Processing image:\t"+test

	# The inbuilt load_image_file function messes up with the color scale of the image.
	# Since face detection is done on gray image, the original image is read using opencv.
	# In the built in function, PIL is used to read the image.
        #image = face_recognition.load_image_file(test)

        img = cv2.imread(test)
        face_locations = face_recognition.face_locations(img)
        
        if len(face_locations)>0:
            print "Detected {} faces in this image.".format(len(face_locations))
            show_image(img)
            # uncomment the following line to mark all the faces.
            #img = show_all_faces(face_locations,img) 
            #show_image(img)

            # Generator implementation for individual faces
            for faces,face_snip in show_individual_faces(face_locations, img):
                show_image(face_snip)       #FW: Save this snippet as a temporary test data.
                #show_image(faces)
            cv2.destroyAllWindows()
        else:
            print "No face detected in this image."

if __name__ == "__main__":
    main()
