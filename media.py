__author__ = 'jannie'

import webbrowser


class Media():
    def __init__(self, m_title, m_storyline, m_poster, m_trailer):
        self.title = m_title
        self.storyline = m_storyline
        self.poster = m_poster
        self.trailer = m_trailer

    def show_trailer(self):
        webbrowser.open_new(self.trailer)


