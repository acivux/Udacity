from Project1 import fresh_tomatoes

__author__ = 'jannie'

from Project1.media import Movie

aliens = Movie("Aliens", "A scary movie",
               "http://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Aliens_poster.jpg/220px-Aliens_poster.jpg",
               "https://www.youtube.com/watch?v=hU1YaowhYKM")

toy_story = Movie("Toy Story", "A boy and his zombie toys",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = Movie("Avatar", "A marine on an alien planet",
               "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = Movie("School of Rock", "Using rock music to learn",
                       "http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                       "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = Movie("Ratatouille", "A rat is a chef in Paris",
                    "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = Movie("Midnight in Paris", "Going back in time to meet Authors",
                          "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=BYRWfS2s2v4")

goonies = Movie("The Goonies", "Kids hunting for treasure",
                "http://upload.wikimedia.org/wikipedia/en/thumb/c/c6/The_Goonies.jpg/220px-The_Goonies.jpg",
                "https://www.youtube.com/watch?v=pWgc8Ute2tU")

sw4 = Movie("Start Wars IV", "Rebellion groes stronger",
            "http://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
            "https://www.youtube.com/watch?v=9gvqpFbRKtQ")

#print toy_story.storyline
#print avatar.storyline
#avatar.show_trailer()


movies = [aliens, toy_story, avatar, sw4, ratatouille, goonies]
fresh_tomatoes.open_movies_page(movies)




