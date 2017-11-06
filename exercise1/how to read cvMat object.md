## How does a program read the cvMat object, in particular, what is the order of the pixel structure?

The cvMat is a matrix which represents the pixels in the image. We can access the pixel values in cvMat by using cvMat.at(x,y). If the pixel has multiple color channels, we can access a pixel by using cvMat.at(x,y)[index], where index allows us to process pixel values of the color channels. Then we do image tranversal to get the pixel values.

If the rows of the data matrix are saved in contiguous memory locations, this means that we can treat the 
entire matrix as a single one-dimensional array. In the case of non-continuous images, the value of numRows
and numCols remain as they are read from the Mat object.

