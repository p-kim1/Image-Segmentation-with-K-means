import sys
from PIL import Image
import kmeans
import numpy as np
import matplotlib.pyplot as plt

def main():
    imageFile = sys.argv[1]
    k = int(sys.argv[2])
    save = sys.argv[3]
    image = Image.open(imageFile)
    image = image.convert("RGB")
    width = image.width
    height = image.height

    #Obtain pixel RGB values
    train = []
    for x in range(0,width):
        for y in range(0,height):
            RGB = image.getpixel((x,y))
            train.append(RGB)
            
    #Run K-means
    train = np.array(train)
    km = kmeans.kmeans(k,train)
    centers = km.kmeanstrain(train).astype(int)
    clusters = km.kmeansfwd(train)

    #Create new image based on RBG values given by centers
    #Replaces original pixel with RGB corresponding to cluster
    newImage = Image.new("RGB",(width,height))
    i = 0
    for x in range(0,width):
        for y in range(0,height):
            cIndex = int(clusters[i])
            RGBtuple = tuple(centers[cIndex])
            newImage.putpixel((x,y),RGBtuple)
            i += 1
    
    #Save image
    if save == "y":
        newImage.save("new."+imageFile.split(".")[-1])

    #Display original and segmented image
    plt.subplot(121) 
    plt.title("Original")
    plt.imshow(image,aspect = "equal")
    plt.subplot(122)
    plt.title("K = " + str(k))
    plt.imshow(newImage,aspect = "equal")
    plt.show()
    image.close()
main()
