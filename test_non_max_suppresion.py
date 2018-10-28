# Assignment 4
# CS 152
# Fall, 2018
# test_non_max_suppression.py

# YOUR NAME(S) HERE

from collections import Counter
from datetime import date
from non_max_suppression import nms
import numpy as np
import random
import unittest


class TestNonMaxSuppression(unittest.TestCase):

    def assertEqualAnyOrder(self, a, b):
        """ Asserts that a and b contain the same values, in any order.
        Assumes that a and b are one-dimensional NumPy arrays. """
        a.sort()
        b.sort()
        self.assertEqual(list(a), list(b))
       

    def test_no_boxes_returns_empty(self):
        empty = np.array([])
        self.assertEqual(0, nms(empty, empty, empty).size)


    def test_random_overlapping(self):
        def random_in_range(a_min, a_max):
            return a_min + random.random() * (a_max - a_min)

        # Use today's date as a seed, so that we are reproducible all day
        # today (while debugging:)
        random.seed(str(date.today()))
        MIN_COORD = 0
        MAX_COORD = 1000

        boxes = []
        scores = []
        classes = []
        good_indexes = []
        for c in range(0, 99):
            # For each class, create one real box, and a number
            # of boxes with lower scores that overlap the real box
            left = random.randrange(MAX_COORD)
            top = random.randrange(MAX_COORD)
            right = random.randrange(left, MAX_COORD)
            bottom = random.randrange(top, MAX_COORD)
            real_box = [left, top, right, bottom]
            real_score = random_in_range(.7, .9)
            boxes.append(real_box)
            scores.append(real_score)
            classes.append(c)
            if real_score > 0.4:
                good_indexes.append(len(boxes) - 1)
            for fake_boxes in range(0, 20):
                h_factor = random_in_range(-.2, .2)
                v_factor = random_in_range(-.2, .2)
                delta_h = (right - left) * h_factor
                delta_v = (bottom - top) * v_factor
                fake_box = [
                        left + delta_h, top + delta_v,
                        right + delta_h, bottom + delta_v]
                boxes.append(fake_box)
                fake_score = random_in_range(real_score - .2, real_score - .001)
                scores.append(fake_score)
                classes.append(c)

        self.assertEqualAnyOrder(np.array(good_indexes),
                nms(np.array(boxes), np.array(scores), np.array(classes)))

if __name__ == '__main__':
    unittest.main()

