import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life", 
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", 
                     "A marine on an alien planet", 
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg", 
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

#movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS) # class variable
print(media.Movie.__doc__) # Predefined class variable, called doc. It is the class documentation string. The code object representing the compiled function body.
print(media.Movie.__name__) # The function's name
print(media.Movie.__module__) # The name of the module the function was defined in, or None if unavailable.