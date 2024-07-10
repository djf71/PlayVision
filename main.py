import cv2 

def main():

    test_image_path = 'nfl-health-and-safety-helmet-assignment/images/57503_003655_Sideline_frame72.jpg'

    test = cv2.imread(test_image_path)


    cv2.imshow(" ",test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   

main()

 