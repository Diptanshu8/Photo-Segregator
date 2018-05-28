import sys,os
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


