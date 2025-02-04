# comment.py
import pygame
from constants import *
from helpers import screen, from_text_to_array


class Comment:
    """
    A class used to represent a comment on a Nitzagram post
    """

    def __init__(self, text):
        """
        Initialize a comment with the given text

        Args:
            text (str): The comment text
        """
        self.text = text

    def display(self, position):
        """
        Display the comment on screen at the specified position in the comments list

        Args:
            position (int): The index position of this comment in the display list
        """
        # Create font for comments
        comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)

        # Break comment into lines if needed
        comment_lines = from_text_to_array(self.text)

        # Calculate starting y position based on comment position
        current_y = FIRST_COMMENT_Y_POS + (position * COMMENT_LINE_HEIGHT)

        # Display each line of the comment
        for line in comment_lines:
            text_surface = comment_font.render(line, True, BLACK)
            screen.blit(text_surface, (FIRST_COMMENT_X_POS, current_y))
            current_y += COMMENT_LINE_HEIGHT