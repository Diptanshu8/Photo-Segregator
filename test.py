import face_recognition
import cv2
import os,sys
def print_usage():
    print "Usage:\tpython test.py <directory of test images or a single test_image>"

def check_params():
    if len(sys.argv) < 2:
        print_usage()
        exit()
    if os.path.isdir(sys.argv[1]):
        test_dir = sys.argv[1]
        test_image = [os.path.join(test_dir,item) for item in os.listdir("test_images") if item.endswith(".jpg")]
    else:
        test_image = [sys.argv[1]]
    return test_image 

def show_image(image):
    cv2.imshow('Image',image)
    while(1):
	k = cv2.waitKey(0)
	if k==27: #stopping for escape
	    exit()
	elif k==32:
	    break

def main():
    test_image = check_params()
    print "Done compiling params and total number of images to be processed is: " + str(len(test_image))
    for test in test_image:
    	print "Processing image:\t"+test
	# The inbuilt load_image_file function messes up with the color scale of the image.
	# Since face detection is done on gray image, the original image is read using opencv.
	# In the built in function, PIL is used to read the image.
        #image = face_recognition.load_image_file(test)

        img = cv2.imread(test)
        face_locations = face_recognition.face_locations(img)
	show_image(img)
	print "Drawing rectangles around detected faces if any."
	face_count = 0
	for (top, right, bottom, left) in face_locations:
	    # Draw a box around the face
	    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
	    face_count+=1
	print "Drew {} faces.".format(face_count)
	show_image(img)
	cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
