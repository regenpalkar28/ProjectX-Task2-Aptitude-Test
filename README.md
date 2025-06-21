# ProjectX-Task2-Aptitude-Test

In this task, we were given several images in each testcase {namely Raghav, Ganshyam, Bhaskar, Yash, Om/Omkar and Chintan which corresponded to the colors red, green, blue, yellow, orange and cyan.

Its hmentioned in the description of the task that Raghav, Ganshyam and Bhaskar are very close friends which hints that the task has something to do with the red, blue and green (RGB) images.
So I applied various operations on these images (including the cyan, orange and yellow however these failed to give any meaningful patterns)
However, on applying BITWISE OR on red blue and green resulted in these images:
![image](https://github.com/user-attachments/assets/44ffd63a-1b12-4aa5-b68a-a1c939bec1e4) BITWISE OR on RGB for testcase 1
![image](https://github.com/user-attachments/assets/03d63f07-fa27-4c02-a026-c6ea1fb0a79f) BITWISE OR on RGB for testcase 2

Here a very obvious pattern is emerging. 
In each row, there are 4 options (shapes) and 3 of them are outlines of shapes and one of them is a solid (or filled) shape.
This seems to indicate an answer key for a multiple choice test.

However, the hard part is still left. We have to make a program which will detect the solid shapes and classify them into the corresponding row and column combination.

