#  importing web browser module to open trailer
import webbrowser


#  setting up movie class
class Movie():

#  this is the constructor for a movie object
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube,
		 main_actor, rotten_tomatoes_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.main_actor = main_actor
        self.rotten_tomatoes_rating = rotten_tomatoes_rating

#  this is a function to play the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

