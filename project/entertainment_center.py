import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
                        "Story of a Toy Star",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=sarLaVnB1Eo")

batman_vs_superman = media.Movie("Batman Vs Superman",
                                 "Dawn of Justice Fight Between Batman Vs Superman",
                                 "http://www.joblo.com/movie-posters/batman-v-superman-dawn-of-justice-02"
                                 ,"https://www.youtube.com/watch?v=58KXLPE7M_s")
deadpool = media.Movie("Deadpool", "Freakin-Sicken-comedy",
                      "http://getthatpaperson.com/wp-content/uploads/2016/02/deadpool-giveaway.jpg",
                       "https://www.youtube.com/watch?v=Xithigfg7dA")
spiderman = media.Movie("Spidermen", 
                        "Spiderman-Ironman",
                        "http://cdn.collider.com/wp-content/uploads/amazing-spider-man-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=yd_DIlguI6A")

# This function call opens a page of movies generated
movie = [toy_story, batman_vs_superman, deadpool, spiderman]
fresh_tomatoes.open_movies_page(movie)
