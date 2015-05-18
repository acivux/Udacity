__author__ = 'jannie'

import webbrowser


class Movie():
    """Class for storing movie information"""

    VALID_MPAA_RATINGS = {"G": "ribbon-green",
                          "PG": "ribbon-blue",
                          "PG-13": "ribbon-blue",
                          "R": "ribbon-orange",
                          "NC-17": "ribbon-red"}



    def __init__(self, m_title, m_storyline, m_poster, m_trailer, m_viewer_rating, m_mpaa_rating):
        """Constructor for the Movie class"""

        # MPAA rating is required
        assert m_mpaa_rating in self.VALID_MPAA_RATINGS.keys(), "MPAA rating missing or not correct: %s" % m_title
        # Viewer rating validation
        assert 0 < m_viewer_rating < 6, "Viewer rating must be between 1 and 5: %s" % m_title

        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_poster
        self.trailer_youtube_url = m_trailer
        self.viewer_rating = m_viewer_rating

        self.mpaa_rating = m_mpaa_rating
        self.mpaa_rating_style = self.VALID_MPAA_RATINGS[m_mpaa_rating]

    def show_trailer(self):
        """Opens a web browser to the movie trailer URL"""
        webbrowser.open_new(self.trailer)