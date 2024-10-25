#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that
inherits from unittest.TestCase.
"""
from utils import memoize
from unittest.mock import patch, Mock
from utils import get_json
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Start patching requests.get with fixtures."""
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
    """Start patching requests.get with fixtures."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that utils.get_json returns the expected result.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Read about memoization and familiarize
    yourself with the utils.memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Use unittest.mock.patch to mock a_method. Test that
         when calling a_property twice, the correct result
          is returned but a_method is only called once using
           assert_called_once.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:

            test_obj = TestClass()
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            mock_method.assert_called_once()
