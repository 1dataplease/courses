#these 2 files should be in same folder
#import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Post.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch@v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3BBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                          "Going back in time to meet authors",
                          "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                          "A really real reality show",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#dl fresh_tomatoes.py
#fresh_tomatoes.open_movies_page(movies)

#print(toy_story.storyline)
avatar.show_trailer()

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)


#notes
# blueprint has info like # rooms, heights - can build instances or objects
# what data should class Movie contain?
# storyline, movie poster, trailer, reviews, title -> show_trailer()
# 'google style guide for python' class - MovieEtc
# good practice to keep class def in 1 file, call/use in another

#media.Movie() called the init fxn inside class Movie
# it initializes, creates space in memory for it
#fxn __init__ is a constructor
#instance variable are the arguments - the fxns u can call

# if media doesnt have self.storyline, it will work locally in that fxn, not att
# have attribute trailer, also create fxn show_trailer() - instance method

#fresh tomatoes file has fxn def open_movies_page(list of movies) -> website that shows movies
#has to be in same folder

#all instances can share the list valid_ratings - class variable
# should be all caps for default values VALIID_RATINGS
