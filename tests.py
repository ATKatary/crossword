"""
crossword tests
"""
import time
from .models import Puzzle
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ValidationError

##### Global Constants #####
url = {"puzzle": reverse("puzzle"),
       "autocomplete" : reverse("autocomplete")}

class CrosswordTests(APITestCase):
    """
    Testing Strategy:
        Definitions

        Partition ... 
            ... on puzzle exists, does not exists
            ... on autocomplete possible, not possible
    """
    ##### Puzzle Tests #####
    def test_create_puzzle(self):
        """ 
        Tests ... 
              ... on puzzle: does not exists
        """
        request_data = {"puzzleId" : None, "puzzleName" : "may"}
        response     = self.client.post(url['puzzle'], request_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_puzzle(self):
        """
        Tests ... 
              ... on puzzle: exists
        """
        puzzle = Puzzle.objects.create(name="may", path="puzzles/may.txt", solved=False)
        puzzle.save()

        request_data = {"puzzleId" : f"{puzzle.id}", "puzzleName" : None}
        response     = self.client.post(url['puzzle'], request_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    ##### Autocomplete Tests #####
    def test_autocomplete_notpossible(self):
        """
        Tests ... 
              ... on puzzle: exists
              ... on autocomplete: not possible 
        """
        puzzle = Puzzle.objects.create(name="may", path="puzzles/may.txt", solved=False)
        puzzle.save()

        request_data = {"puzzleId" : f"{puzzle.id}", "cellLocation" : [0, 0]}
        response     = self.client.post(url['autocomplete'], request_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    ##### Your Tests #####


    