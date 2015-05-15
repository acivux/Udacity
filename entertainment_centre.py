__author__ = 'jannie'

from media import Media

toy_story = Media("Toy Story", "A boy and his zombie toys",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=vwyZH85NQC4")

print toy_story.storyline

avatar = Media("Avatar", "A marine on an alien planet",
               "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

print avatar.storyline
avatar.show_trailer()


