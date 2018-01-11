#title
#storyline

#def show_trailer(title, youtube_url):
    # Open browser and play trailer.

#def show_info(title, storyline, release_date, rating, youtube_url, director, box_office):
    # Print movie information

import webbrowser

class Movie():
    """ This class provides a way to store movie related information. """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)