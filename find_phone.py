from train_phone_finder import findCentroid
import sys
def main():
    path = sys.argv[1]
    x,y = findCentroid(path)
    print('{:0.4} {:0.4}'.format(x,y))
if __name__ == '__main__':
    main()
