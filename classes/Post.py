import pygame
from constants import *
from helpers import screen, from_text_to_array
from comments import Comment  # Updated import


class Post:
    """
    A class used to represent a post on Nitzagram. This is the base class for
    both ImagePost and TextPost.
    """

    def __init__(self, username, location, description):
        """
        Initialize a Post with the given parameters.

        Args:
            username (str): The username of the post creator
            location (str): The location tag for the post
            description (str): The post description/caption
        """
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0  # For cycling through comments display

    def add_like(self):
        """Adds one like to the post"""
        self.likes_counter += 1

    def add_comment(self, text):
        """
        Adds a new comment to the post

        Args:
            text (str): The comment text
        """
        new_comment = Comment(text)
        self.comments.append(new_comment)

    def display_user_details(self):
        details_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        username_text = details_font.render(self.username, True, BLACK)
        location_text = details_font.render(self.location, True, BLACK)
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        screen.blit(username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))

    def display_likes_and_description(self):
        details_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)

        # Render likes count
        likes_text = details_font.render(f"{self.likes_counter} likes", True, BLACK)
        screen.blit(likes_text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        # Break description into lines if needed and display
        description_lines = from_text_to_array(self.description)
        current_y = DESCRIPTION_TEXT_Y_POS

        for line in description_lines:
            desc_text = details_font.render(line, True, BLACK)
            screen.blit(desc_text, (DESCRIPTION_TEXT_X_POS, current_y))
            current_y += UI_FONT_SIZE  # Move down for next line

    def display_comments(self):
        position_index = self.comments_display_index
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render(
                "view more comments", True, LIGHT_GRAY)
            screen.blit(view_more_comments_button,
                        (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def display(self):
        self.display_user_details()
        self.display_likes_and_description()
        self.display_comments()
        # self.test()

    def reset_comments_display_index(self):
        if self.comments:
            self.comments_display_index = (self.comments_display_index + 1) % len(self.comments)
        else:
            False
