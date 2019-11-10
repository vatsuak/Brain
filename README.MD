OBJECTIVE	
The purpose of this code is to determine the normalized coordinates of a cell phone
in a given picture. 

_____________________________File Description______________________________________

There are overall two files that are used to complete the task.

1)train_phone_finder.py 
  This python file is used to validate the method used with the provided dataset. The 
  file takes in the path of the dataset as the command line input and prints out the
  accuracy of the method used to detect the object on the given dataset.
  Here is what a terminal command will look like when running the file:
            $ python train_phone_finder.py ~/find_phone 

 
  The dataset folder provided to the input may contain any number of image files and must 
  contain an annotated .txt file with the name 'labels.txt'. The annotation must be done in
  the following fashion:
      <image_name> <x​ (coordinate of the phone)> ​<y​ (coordinate of the phone)>

2)find_phone.py
  This file is used to find the normalized coordinate of a phone in a random image
  provided as the input. The file takes in a single image with a phone and displays the 
  location of the phone as two space separated float values(<=1).

NOTE: NO EXCEPTION HANDLING HAS BEEN IMPLEMENTED

_______________________________Discussion____________________________________________

The method that has been used to detect the phone in the images is a very simple, crude 
algorithm. In a few words:

Step 1. Convert the image into binary using global thresholding methods,
Step 2. Draw 2D bounding boxes around the areas of interest(the contours separated out through 
        the binary conversion) in the binary image and "hope" that it is the phone,
Step 3. Record the centroid of the bounding box that has been so drawn
Step 4. Normalize the so obtained centroid with the dimension of the image
Step 5. Report the normalized centroid

Preprocessing: A gaussian smoothing filter has been applied to the image before converting it to
       binary so as to remove the noise so that only the dominant gradients can be viewed

Open Source Libraries used:
   Only openCV(cv2), numpy libraries have been used to accomplish the task. The following major
   functions have been used:
    1. cv2.read()
    2. cv2.blur()
    3. cv2.threshold()
    4. cv2.minAreaRect()
    5. cv2.boxPoints()

The detection works best when the phone is easily distinguishable with a significant color difference
from the background. There shouldn't be any dark objects present in the background other than the phone. 
The method essentially detects the black screen of the phone to draw the boundary, so there should not be 
any reflection off the screen. Therefore the testing data would work well if it adhered to the above 
guidelines.

IMPROVEMENTS: 
The proposed method does not use any form of learning or state of the art algorithm 
since the focus was kept to achieving a complete code with the minimum expected requirements. 
However there could be many improvements that could be done over and above the specified method. Some of 
the methods that could be applied are listed as follows:

1) define better feature detection methods. One can focus on gradients and techniques like canny edge detectors
 as a preprocessing step to better distinguish the object from  the background,
2) A foreground-background separation technique that can facilitate the better detection of the phone.
3) Apply techniques inspired form established ml processes, like face-detection and  modify it to something like a
  "phone detection" and be able to reduce the dimension of the area of interest,
4) A particularly interesting technique that could be implemented is something called "CentroidNet", which claim to have 
   better success rate than may state-of-the art methods( link: http://www.ecmlpkdd2018.org/wp-content/uploads/2018/09/116.pdf)
5) The dataset could be extended and better labels could be provided. For example more variations in the illumination of
  the scenes. Also the labels for the angle of rotation of the principle axis of the phone could have been added.
6) Transferred learning through some pre-trained networks 

Overall the simplicity of the implemented algorithm may be utilized in the fact that this method is a skeletal 
framework to build better and complex pipelines. This is definitely a naive or brute-force method achieving just the 
bare-minimum baseline and can be infinitely improved on, using maybe one of the above techniques. 


------------------------------------------------End------------------------------------------------------------------------



