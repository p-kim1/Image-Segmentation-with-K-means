# Image-Segmentation-with-K-means
A simple implementation of image segmentation using the K-means clustering algorithm. Given _K_ number of clusters, the program uses K-means to determine the _K_ colors to use in the partitioning process. Each pixel in the original image is replaced by the color that most closely corresponds to its RGB value. Once complete, the original and segmented images will be displayed side by side. The file "glass.jpg" is provided as a sample image.

Note: The implementation of K-means is provided for free use by the textbook "Machine Learning: An Algorithmic Perspective".  All credit goes to the author, Stephen Marsland (https://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html).

To run on terminal: python3 seg.py <image>^1^ <number of clusters>^2^ <save image>^3^
 
 1. The full file name of the image (e.g. "glass.jpg").
 2. The number of clusters used in image segmentation. Larger values will take longer to process. Note that duplicate colors may be chosen.
 3. _y_: save the segmented image; _n_: do not save the segmented image
