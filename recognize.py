import os
import face_recognition as fr
import recognize_utility as util
import param_process_functions as pp
import image_handlers as ih
import config

def load_train_cache_encodings():
    print "\n"
    snippets_list = util.print_train_snippets()
    snippets_count = len(snippets_list)
    
    user_choice = map(int,raw_input("Please enter the number of trained cached images you want to use for recognition.\nEnter space-seperated values for multiple images, 0 for all the images.\n").split(" "))
    
    encodings = {}
    for n,item in enumerate(snippets_list):
        if 0 in user_choice or n+1 in user_choice:
            path = os.path.join(config.train_cache,item)
            sample = fr.load_image_file(path)
            sample_encoding = fr.face_encodings(sample)
            # in some case encodings are not being generated.
            if sample_encoding and not encodings.has_key(item):
                encodings[item] = sample_encoding[0]
            else:
                print "Cannot use {} as known sample. Encoding failure. Check the docs.".format(item)
    return encodings

if __name__ == "__main__":
    if not util.check_train_snippets():
        exit()
    test_images = pp.check_params()
    print "Done compiling params."
    print "Total number of images to be processed is: " + str(len(test_images))
    
    # load known face_encodings.
    print "Loading encodings of the trained cache by the user."
    trained_encodings = load_train_cache_encodings()
    print "Successfully loaded {} encodings.".format(len(trained_encodings))
    
    for sample_no,sample in enumerate(test_images):
    	print "Processing image number {}:\t{}".format(sample_no,sample)
        ih.show_image(sample)
        # detect and generate test image face_encodings
        image = fr.load_image_file(sample)
        sample_encoding = fr.face_encodings(image)
        # in some case encodings are not being generated.
        if sample_encoding:
            sample_encoding = sample_encoding[0]
            results = fr.compare_faces(trained_encodings.values(), sample_encoding)
            # make changes so that the code prints for all the encodings mathced and not just the first
            if True in results:
                for i,r in enumerate(results):
                    if r:
                        name = os.path.splitext(trained_encodings.keys()[i])[0]     # removed the .jpg part
                        if "_" in name:
                            name = "".join(name.split("_")[:-1])                    # removed the _ and joined.
                        print "Identified {} in {}".format(name,sample)
        # print matching image names and matched id from train cache
        # also show the matched images.



