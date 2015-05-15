__author__ = 'jannie'

import webbrowser


class Movie():
    """Class for storing movie information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, m_title, m_storyline, m_poster, m_trailer):
        """Constructor for the Movie class"""
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_poster
        self.trailer_youtube_url = m_trailer

    def show_trailer(self):
        """Opens a web browser to the movie trailer URL"""
        webbrowser.open_new(self.trailer)