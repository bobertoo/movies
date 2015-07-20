# Here I import the fresh_tomatoes website generator and the media.py that is the movie constructor and methods
import fresh_tomatoes
import media

# Here are the instances of each movie with their title, storyline, poster and trailer
evil_dead = media.Movie("Evil Dead",
                        "A story of a haunted house",
                        "https://upload.wikimedia.org/wikipedia/en/7/7d/Evil_dead_ver1.jpg",
                        "https://www.youtube.com/watch?v=wXpjFAisVvY")

evil_dead_2 = media.Movie("Evil Dead 2",
                          "Revenge of a story of a haunted house",
                          "https://upload.wikimedia.org/wikipedia/en/6/6d/Evil_Dead_II_poster.jpg",
                          "https://www.youtube.com/watch?v=w6mEiJRiXqc")

dead_alive = media.Movie("Dead Alive",
                         "Bitten by rat-monkey",
                         "http://wrongsideoftheart.com/wp-content/gallery/posters-b/braindead_poster_02.jpg",
                         "https://www.youtube.com/watch?v=O8LIug1cP04")

army_of_darkness = media.Movie("Army of Darkness",
                               "Medieval spooks",
                               "http://ecx.images-amazon.com/images/I/51QgCAqNPcL._SY355_.jpg",
                               "https://www.youtube.com/watch?v=4vvJCg2JsIc")

bubba_ho_tep = media.Movie("Bubba Ho-Tep",
                           "Spooks from the tomb to the old folks home",
                           "http://www.schlechtergeschmack.net/wp-content/uploads/2014/05/bubba_hotep_cover.jpg",
                           "https://www.youtube.com/watch?v=X7Qo74_L3vo")

drag_me_to_hell = media.Movie("Drag Me to Hell",
                              "Spooky curse from spooky old lady",
                              "http://ia.media-imdb.com/images/M/MV5BMTYzOTc2NDIwMF5BMl5BanBnXkFtZTcwNzAxMTM2Mg@@._V1_SX640_SY720_.jpg",
                              "https://www.youtube.com/watch?v=BUZTybLlWKI")

# this array is what the fresh_tomatoes script needs for input
movies = [evil_dead, evil_dead_2, dead_alive, army_of_darkness, bubba_ho_tep, drag_me_to_hell]

# this passes the movies array to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
