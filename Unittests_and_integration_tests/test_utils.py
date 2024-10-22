#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that
inherits from unittest.TestCase.
"""
from unittest.mock import patch, Mock
from utils import get_json
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Implement TestAccessNestedMap.test_access_nested_map_exception.
        Use the assertRaises context manager to test that a KeyError is
        raised for the following inputs (use @parameterized.expand):
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """
        Define the TestGetJson(unittest.TestCase)
        class and implement the TestGetJson.test_get_json
        method to test that utils.get_json returns the
        expected result."""
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
            mock_get.reset_mock()
