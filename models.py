"""
crossword models
"""
import uuid
from django.db import models

class Puzzle(models.Model):
    """
    AF(puzzle_id) = puzzle puzzle_id 

    Representation Invariant
        - inherits from models.Model
    
    Representation Exposure
        - inherits from models.Model
        - access allowed to all fields but they are all immutable
    """
    ##### Representation #####
    alphabet_size = 26
    name   = models.CharField(max_length  = alphabet_size)
    path   = models.CharField(max_length  = alphabet_size**2)

    solved = models.BooleanField(default  = True)
    id     = models.UUIDField(primary_key = True,  editable = False, unique = True, default = uuid.uuid4)

    def parse(self, puzzle_path):
        """
        Parses a puzzle from puzzle_path and returns a Puzzle object representation
    
        Inputs
            :param puzzle_path: <str> of where the puzzle is
    
        Outputs
            :returns: <Puzzle> representing the parsed puzzle txt file
        """
        with open(puzzle_path, 'rb') as puzzle:
            #TODO: read and parse the puzzle
            pass 
            
        return self
    
    def __str__(self) -> str:
        """ Override models.Model.__str__() """
        raise NotImplementedError

