from train_phone_finder import findCentroid 
import sys
def main():
    path = sys.argv[1]  #getting the path of the test image
    x,y = findCentroid(path)   #computing the normalized centre of the phone location in the image
    print('{:0.4} {:0.4}'.format(x,y)) #displayng the normalized location corect to 4 decimals
if __name__ == '__main__':
    main()
