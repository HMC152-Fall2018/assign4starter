# Assignment 4
# CS 152
# Fall, 2018
# non_max_suppression.py

# YOUR NAME(S) HERE

import numpy as np

def nms(boxes, scores, classes, overlap=0.45, min_score=.4):
    """ Does Non Max Suppression on the given boxes, scores, and classes.
    Any boxes with score < min_score are ignored. Boxes are chosen based on
    decreasing score.
    When a box is chosen, any overlapping boxes of the same class with IoU < overlap
    are discarded.

    Parameters:
      boxes: Numpy array of shape (k, 4). Each row consists of left, top, right, and bottom.
      scores: NumPy array of shape (k). Each value is in the range [0.0, 1.0]
      classes: NumPy array of shape (k). Each value is an integer in the range 0..100.
     

    Return result:
      a NumPy array with j elements in it, each representing a chosen box.
      Each of the j elements is an index into the original array.
    """
    # fill in this code
    return np.array([])
