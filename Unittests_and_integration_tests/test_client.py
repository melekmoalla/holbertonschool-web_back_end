#!/usr/bin/env python3
"""
In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase)
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        test_org method.
        This method should test that GithubOrgClient.org
        returns the correct value.
        """

        expected = {org_name: 'true'}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org
        test_url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(test_url)
        print(mock_get_json)
        self.assertEqual(result, expected)
