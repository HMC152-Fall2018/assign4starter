# CS 152
# Assignment 4
# October 29, 2018
##  Due November 4, 2018, 11 PM

In this assignment, you’ll implement and test a non-max-suppression function.  You can work individually or in pairs, but if you work in pairs, all work must be done while you are physically together, working on one computer with one keyboard and mouse, switching off the driver.

This assignment does not use PyTorch, and does not need a machine with a GPU.  You will need a machine 
that has Python 3 and NumPy installed.  If you want to use a Google Compute Engine instance, you may, 
but you would probably want to create an instance without GPU (remove the ```--accelerator=count=1,type=nvidia-tesla-k80``` command-line argument when creating your instance). 

The Non-max-suppression algorithm is as follows:

1. Discard all boxes with the probability of an object (Pc) < 0.4
2. While boxes remain:
    1. Choose box with highest Pc and  mark that as a prediction
    2. Discard all boxes which predict the same class and overlap that
       prediction with IoU > 0.45
       

I've given you a starter file: non_max_suppression.py. You should fill in the implementation of ```nms```
in that file (without changing the signature of the function). I've also given you a starter unit test 
for that function in test_non_max_suppression.py. You'll need to add additional test cases to that file.


Things you’ll need:

* A Github account
* A machine with Python ≥3.5 and Numpy installed


### Grading
I'll grade considering the following:
* Correctness of ```nms```
* Potential speed of ```nms```. 
    * Are NumPy calls used instead of explicit for-loops?
    * Is there unnecessary copying of data?
* Readabiity of ```nms```. Includes the following:
    * naming of variables
    * commenting, where helpful
    * understandability
* Comprehensiveness of tests
* Readability of tests. Includes the following:
    * naming of variables
    * naming of test cases
    * does each test case have a single purpose?

### Steps

* Join a team on Github (follow the invitation link sent via email).
* Clone your team repository.
* Do your work in the files ```non_max_suppression.py``` and ```test_non_max_suppression.py```.
* Commit your files and push to Github. You only need one submission per team, and the last commit on GitHub before the due date will be your submission.
* Check the repository on Github.com to make sure your files are there.

