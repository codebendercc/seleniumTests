import sys

from selenium import webdriver
import pytest

from codebender_testing.config import WEBDRIVERS


class SeleniumTestCase(object):
    """Base class for all Selenium tests."""

    @classmethod
    @pytest.fixture(scope="class", autouse=True, params=WEBDRIVERS.keys())
    def setup(self, request):
        """Sets up attributes that should be accessible to all test cases."""

        # We repeat each test for each webdriver configuration
        webdriver_cls = WEBDRIVERS[request.param]
        self.driver = webdriver_cls()
