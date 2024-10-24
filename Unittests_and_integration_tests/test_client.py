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
    """
    TestGithubOrgClient
    """
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
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """
        test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url.
        Use patch as a context manager to patch
        GithubOrgClient.org and make it return a known payload.
        Test that the result of _public_repos_url
        is the expected one based on the mocked payload.
        """
        test_url = f'https://api.github.com/orgs/test/repo'

        mock_org.return_value = {'repos_url': test_url}

        client = GithubOrgClient('test')
        result = client._public_repos_url()

        self.assertEqual(result, test_url)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_json, moc_test):
        """
        TestGithubOrgClient.test_public_repos to
        unit-test GithubOrgClient.public_repos.
        """
        res = {'name': 'test'}
        mock_json.return_value = res

        client = GithubOrgClient('test')
        result = client._public_repos_url()

        moc_test.return_value = 'https://github.com/test'
        mock_json.assert_called_once()
        moc_test.assert_called_once()

        self.assertEqual(res, result)
