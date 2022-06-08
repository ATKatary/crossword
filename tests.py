"""
crossword tests
"""
import time
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ValidationError

##### Global Constants #####
url = {"autocomplete" : reverse("autocomplete")}

class MailTests(APITestCase):
    """
    Testing Strategy:
        Definitions

        Partition ... 
            ... on autocomplete possible, not possible
    """
    ##### Contact Tests #####
    def test_autocomplete_valid(self):
        """ 
        Tests ... 
              ... on autocomplete: possible
        """
        raise NotImplementedError