# ProjectX-Task2-Aptitude-Test


[O/P AT THE VERY END OF THIS DOCUMENT] 


In this task, we were given several images in each testcase {namely Raghav, Ganshyam, Bhaskar, Yash, Om/Omkar and Chintan which corresponded to the colors red, green, blue, yellow, orange and cyan.

It's mentioned in the description of the task that Raghav, Ganshyam and Bhaskar are very close friends which hints that the task has something to do with the red, blue and green (RGB) images.
So I applied various operations on these images (including the cyan, orange and yellow however these failed to give any meaningful patterns)
However, on applying BITWISE OR on red blue and green resulted in these images:


 ![1](https://github.com/user-attachments/assets/c6a2c057-80fc-4e57-b840-0a75864d00bd)
 
 BITWISE OR on RGB for testcase 1 (pattern1)


 
 ![1](https://github.com/user-attachments/assets/dcb6825b-71af-4e19-bacd-9b688f1fb9d5)
 
 BITWISE OR on RGB for testcase 2 (pattern2)

Here a very obvious pattern is emerging. 
In each row, there are 4 options (shapes) and 3 of them are outlines of shapes and one of them is a solid (or filled) shape.
This seems to indicate an answer key for a multiple choice test.

However, the hard part is still left. We have to make a program which will detect the solid shapes and classify them into the corresponding row and column combination.

for this, I wrote a function called *solid_detector*, which takes an image as an input. The input images for this function are the two images which we generated before, we will call them **pattern1** and **pattern2** respectively.

Firstly, we convert input image into grayscale and then thresh it to convert it into a binarized image, since we aren't concerned with the colors of the shapes, we just have to check whether they are outlines or filled shapes. 

We hide the 70 pixels from the left and 50 pixels from the top in the threshed image to avoid the software from detecting/classifying the numbers and letters as outlined/solid. (we will detect these later)

![1](https://github.com/user-attachments/assets/8ca7254e-34f0-48a1-b64f-c97bae5027ca)
![1](https://github.com/user-attachments/assets/be58f746-0eaf-4624-8998-b065bbf3f0ed)


The resulting threshed image looks like this.

Then we use the findContours function in cv2 to find the outlines of all the shapes (whether solid or just outlined).

**solid_centers** is a list which will contain the x and y coordinates of the centers of the solid shapes that we will detect.

We find the area of each contour, and if it is too small ( in particular less than 50, we ignore it assuming it to be irrelevant noise)

Then we create a mask, with the dimensions of the threshed / grayscale image (theyre the same dimensions). This mask will be a blank image, which will be used to isolate the area inside the current contour. Then we draw the contour on the mask, and fill the interior of it with white. Then we perform a BITWISE AND of the threshed image and the mask to isolate the white pixels that present in both the mask and the threshed image. 

Example of one contour : 


![1](https://github.com/user-attachments/assets/14305e52-8b78-4978-b582-b8377619c901)

Then we count how many white pixels are present in the intersection of threshed and the mask. This is a crucial step in determining whether a contour is an outline or a solid. If the ratio of the pixel count and the area is greater than 0.85 {this 0.85 is denoted as the **solidity_threshold**} , then that contour is determined as a SOLID and its centroid is calculated. These centroid coordinates are appended in the solid_centers list that we created earlier.

Now we notice that some of the centers of the solid shapes ( cx , cy ) are in the same column/ row but their x coordinates (for points in same column) and their y coordinates (for points in the same row) are not exactly equal. 


![1](https://github.com/user-attachments/assets/8f39356b-c44c-4bf5-b76b-90f1845909f3)

points being in the same column but not having exact same x coordinates 

This adds another layer of complexity. 
So to group these points (in particular centroids) in the same row / column, we define the *group_centroid* function.

The *group_centroid* function takes some values as an input and a threshold = 0.3 is set.
clusters[]  stores the final cluster positions.
temp[] temporarily holds values of the current group.

if temp is empty, start a new cluster. if v in values is close enough (within the threshold) then add it to the cluster. otherwise start a new cluster.
![1](https://github.com/user-attachments/assets/cb38b492-d8d0-48b4-ba73-7ebd463274e3)

The blue point is beyond the threshold, hence it will be part of a new cluster.

The function returns the list of clustered coordinate centers (either row-centers or column-centers).

back to the *solid_detector* function,
we apply the *group_centroid* function to the centroids (which are contained in solid_centers) that we had obtained earlier. 

col_labels is just A, B, C, D, ... for the number of x_clusters's that are present. In both testcases, 4 cx's are present. Hence, col_labels = A,B,C,D

row_labels is just 1,2,3... for number of y_clusters that are present. In testcase 1 there are 8 y_clusters and in testcase 2 there are 10 y_clusters.

Then for for each cx, cy, we find the nearest column (x) and nearest row (y). Name these as col_id and row_id.

Then we define label as the final row/column, or number/alphabet combination where the centroid of solid shapes is present.

For better visibility, we add a black dot at the centroid of the solid shapes; and add the label of that point near the point.
We also print the labels in the terminal.


![1](https://github.com/user-attachments/assets/60b54067-0603-4a92-9d34-65e07d3bf239)
![image](https://github.com/user-attachments/assets/0c9d996a-6306-461d-a845-e5b6f40fdd9f)


![1](https://github.com/user-attachments/assets/079ae7ff-c461-445e-bdce-ff7795a9fa46)
![image](https://github.com/user-attachments/assets/59d07e3d-b7ee-4a2a-b94a-ec74f69b0e49)


Thus we have successfully found the hidden logic of the test.
