
#creates an array with the path of every image
pictures = ["/home/alovelace/Project1Images/1.png", "/home/alovelace/Project1Images/2.png", "/home/alovelace/Project1Images/3.png", "/home/alovelace/Project1Images/4.png", "/home/alovelace/Project1Images/5.png", "/home/alovelace/Project1Images/6.png", "/home/alovelace/Project1Images/7.png", "/home/alovelace/Project1Images/8.png", "/home/alovelace/Project1Images/9.png"]

#creates an object for every image
pic1 = makePicture(pictures[0])
pic2 = makePicture(pictures[1])
pic3 = makePicture(pictures[2])
pic4 = makePicture(pictures[3])
pic5 = makePicture(pictures[4])
pic6 = makePicture(pictures[5])
pic7 = makePicture(pictures[6])
pic8 = makePicture(pictures[7])
pic9 = makePicture(pictures[8])


#array of one pixel for every image
pixels = [getPixels(pic1), getPixels(pic2), getPixels(pic3), getPixels(pic4), getPixels(pic5), getPixels(pic6), getPixels(pic7), getPixels(pic8), getPixels(pic9)]

#arrays of RGB colors set to nine empty indexes
colorRed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
colorGreen = [0, 0, 0, 0, 0, 0, 0, 0, 0]
colorBlue =[0, 0, 0, 0, 0, 0, 0, 0, 0] 

height = getHeight(pic1)
width = getWidth(pic1)

#initializes final picture object to an actual image
finalPic = makeEmptyPicture(width, height)
finalPixels = getPixels(finalPic)

#runs through the same pixel at every image
for i in range(len(pixels[0])):#calls pixels array which has the index that calls how many pixels are in that image. this for loop will run for however many pixels there are
  for j in range(9):#set range to 9 so it will get the same pixel at every image
    colorRed[j] = getRed(pixels[j][i])#starts to fill the red array with the redness of that pixel. The nine empty indexes become the redness of pixel in the same location of the 9 images
    colorGreen[j] = getGreen(pixels[j][i])#starts to fill the green array with the greenness of that pixel. The nine empty indexes become the greenness of pixel in the same location of the 9 images
    colorBlue[j] = getBlue(pixels[j][i])#starts to fill the blue array with the blueness of that pixel. The nine empty indexes become the blueness of pixel in the same location of the 9 images
    colorRed.sort()#sorts the redness in the array so it is easier to find the median
    colorGreen.sort()#sorts the greenness in the array so it is easier to find the median
    colorBlue.sort()#sorts the blueness in the array so it is easier to find the median
  
  #these set the pixel location at the final image to the corresponding median of the pixel of the sorted arrays
  setRed(finalPixels[i], colorRed[5]) 
  setGreen(finalPixels[i], colorGreen[5])
  setBlue(finalPixels[i], colorBlue[5])

show(finalPic)