#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that
inherits from unittest.TestCase.
"""
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
       Implement the TestAccessNestedMap.test_access_nested_map
       method to test that the method returns what it is
       supposed to.
        """
        actual = access_nested_map(nested_map, path)
        self.assertEqual(actual, expected)
