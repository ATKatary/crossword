"""
crossword views
"""
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Puzzle

@api_view(['POST'])
def autocomplete(request, *args, **kwargs) -> HttpResponse:
    """
    Gives autocomplete vertical and horizontal suggestions given a filled cell, the puzzle containing 
    the cell, and the location of the cell in the puzzle. The suggested word must be consistent with the
    rules of the game and the vertical and horizontal sizes of the word the cell is part of. 
    Note that if there are an infinite number of possible suggestions, the behavior is up to you. 
    Note that this function does not care about the size of the puzzle

    Example:
        For a puzzle in this state and the filled in cell is located at (0,0)
        Some suggestions are:
                - Funny (Across)
                - Fan (Down)
                - Fanny (Across)
            F _ _ n _ #
            _ n n _ a l
            n _ c _ # #
      
    Inputs
        :request: <HttpRequest> containing all the puzzle and the cellLocation for autocompletion suggesting
    
    Output
        :returns: Status ... 
                         ... HTTP_201_CREATED if the autocomplete algorithm ran to completion
                         ... HTTP_403_FORIBIDDEN if the autocomplete algorithm did not run to completion
                         ... HTTP_412_PRECONDITION_FAILED if one or more of the request fields don't meet their precondition(s)
    """
    raise NotImplementedError

@api_view(['POST'])
def fetch_puzzle(request, *args, **kwargs) -> HttpResponse:
    """
    Fetches a puzzle (if it exists) or creates a new one and returns a 2D matrix representation of it

    Inputs    
       :param request: <HttpRequest> containing a puzzle's id and name

    Outputs
        :returns: Status … 
                         … HTTP_200_OK if the puzzle exists and can be fetched
                         … HTTP_403_FORBIDDEN if the puzzle does not exist or can not be fetched
    """
    raise NotImplementedError