# coding: utf-8

import unittest
import D
import random

class TestD(unittest.TestCase):

    def test_D_1(self):
        n = 2
        m = 2
        t = 5
        th = [1, 3]
        graph = [
            [0, 2],
            [1, 0]
        ]
        reverse_graph = [
            [0, 1],
            [2, 0]
        ]

        self.assertEqual(D.treasure_hant(n, m, t, th, graph, reverse_graph), 6)

    def test_D_2(self):
        n = 2
        m = 2
        t = 3
        th = [1, 3]
        graph = [
            [0, 2],
            [1, 0]
        ]
        reverse_graph = [
            [0, 1],
            [2, 0]
        ]

        self.assertEqual(D.treasure_hant(n, m, t, th, graph, reverse_graph), 3)

    def test_D_3(self):
        n = 8
        m = 15
        t = 120
        th = [1, 2, 6, 16, 1, 3, 11, 9]
        graph = [
            [0, 0, 0, 2, 0, 0, 0, 1],
            [0, 0, 0, 12, 0, 5, 0, 0],
            [10, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [30, 0, 0, 0, 0, 0, 5, 0],
            [3, 0, 0, 1, 0, 0, 0, 17],
            [0, 0, 14, 0, 0, 0, 0, 5],
            [0, 13, 0, 0, 0, 0, 0, 0]
        ]
        reverse_graph = [
            [0, 0, 10, 0, 30, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 14, 0],
            [2, 12, 0, 0, 0, 1, 0, 0],
            [0, 0, 4, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 5, 0, 0, 0],
            [1, 0, 0, 0, 0, 17, 5, 0]
        ]

        self.assertEqual(D.treasure_hant(n, m, t, th, graph, reverse_graph), 1488)
