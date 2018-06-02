import webbrowser

class Video():
    """
    This class provides a way to play videos
    """
    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline

class Movie(Video):
    """
    This class provides a way to store movie related information
    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title, storyline, poster_image,
                 trailer_youtube):
        Video.__init__(self, title, storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    """
    This class provides a way to store TV show info
    """
    def __init__(self, season, episode, tv_station):
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        
    #def get_local_listing(self):
        











#notes
# blueprint has info like # rooms, heights - can build instances or objects
# what data should class Movie contain?
# storyline, movie poster, trailer, reviews, title -> show_trailer()
# 'google style guide for python' class - MovieEtc
# __ is reserved __ - to remember title,story,etc for movies
#init takes arguments self - the instance/object being created (toy story)
#toy story = media.movie(nm,story,poster,vid)
#1st argument is self which is toy story calling __init__

#class - blueprint - can have data and methods
# instances - create something that can have fxns called on it
# constructor - the init method of a class, uses keyword...
# self - the instance
# instance variables - all the variables in an object self inside, object nm out
# instance methods - all the fxns in a class associated with obj, have self

#class variables - valid ratings - def at class level, outside init
#
