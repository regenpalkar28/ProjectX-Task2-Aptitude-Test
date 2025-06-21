# ProjectX-Task2-Aptitude-Test

In this task, we were given several images in each testcase {namely Raghav, Ganshyam, Bhaskar, Yash, Om/Omkar and Chintan which corresponded to the colors red, green, blue, yellow, orange and cyan.

Its hmentioned in the description of the task that Raghav, Ganshyam and Bhaskar are very close friends which hints that the task has something to do with the red, blue and green (RGB) images.
So I applied various operations on these images (including the cyan, orange and yellow however these failed to give any meaningful patterns)
However, on applying BITWISE OR on red blue and green resulted in these images:
![image](https://github.com/user-attachments/assets/44ffd63a-1b12-4aa5-b68a-a1c939bec1e4)
 BITWISE OR on RGB for testcase 1 (pattern1)
![image](https://github.com/user-attachments/assets/03d63f07-fa27-4c02-a026-c6ea1fb0a79f)
 BITWISE OR on RGB for testcase 2 (pattern2)

Here a very obvious pattern is emerging. 
In each row, there are 4 options (shapes) and 3 of them are outlines of shapes and one of them is a solid (or filled) shape.
This seems to indicate an answer key for a multiple choice test.

However, the hard part is still left. We have to make a program which will detect the solid shapes and classify them into the corresponding row and column combination.

for this, I wrote a function called *solid_detector*, which takes an image as an input. The input images for this function are the two images which we generated before, we will call them **pattern1** and **pattern2** respectively.

Firstly, we convert input image into grayscale and then thresh it to convert it into a binarized image, since we arent concerned with the colors of the shapes, we just have to check whether they are outlines or filled shapes. 

We hide the 70 pixels from the left and 50 pixels from the top in the threshed image to avoid the software from detecting/classifying the numbers and letters as outlined/solid. (we will detect these later)

![1](https://github.com/user-attachments/assets/8ca7254e-34f0-48a1-b64f-c97bae5027ca)
![image](https://github.com/user-attachments/assets/0ce57e22-f346-4d02-b3f8-f97ccea4e1ad)
The resulting threshed image looks like this.


