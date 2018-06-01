import face_recognition
import cv2
import os,sys
import param_process_functions as pp
import image_handlers as ih
import config
 
# this function only deleted the cached image after the execution.
def clear_cache():
    try:
        os.remove(config.cache_img_name+config.cache_img_extension)
    except:
        pass

def main():
    train_images = pp.check_params()
    print "Done compiling params."
    print "Total number of images to be processed is: " + str(len(train_images))
    for sample in train_images:
    	print "Processing image:\t"+sample

	# The inbuilt load_image_file function messes up with the color scale of the image.
	# Since face detection is done on gray image, the original image is read using opencv.
	# In the built in function, PIL is used to read the image.
        #image = face_recognition.load_image_file(sample)

        img = cv2.imread(sample)
        face_locations = face_recognition.face_locations(img)
        
        if len(face_locations)>0:
            print "Detected {} faces in this image.".format(len(face_locations))
            #ih.show_image(sample)

            # uncomment the following line to mark all the faces.
            #img = ih.show_all_faces(face_locations,img) 
            #show_image(sample)

            # Generator implementation for individual faces
            for face in ih.show_individual_faces(face_locations, img):
                ih.show_face_snippet()
            cv2.destroyAllWindows()
        else:
            print "No face detected in this image."
if __name__ =="__main__":
    try:
        main()
    except :
        pass
    clear_cache()
