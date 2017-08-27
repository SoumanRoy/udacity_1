import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Story of a Toy Star",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=sarLaVnB1Eo")

batman_vs_superman = media.Movie("Batman Vs Superman",
                                 "Dawn of Justice Fight Between Batman Vs Superman",
                                 "https://vignette1.wikia.nocookie.net/newdcmovieuniverse/images/6/60/Batman-v-Superman-IMAX-poster.jpg/revision/latest?cb=20160214161802",
                                 "https://www.youtube.com/watch?v=58KXLPE7M_s")
deadpool = media.Movie("Deadpool",
                       "Freakin-Sicken-comedy",
                       "http://getthatpaperson.com/wp-content/uploads/2016/02/deadpool-giveaway.jpg",
                       "https://www.youtube.com/watch?v=Xithigfg7dA")

spiderman = media.Movie("Spiderman",
                        "Spiderman-Ironman",
                        "http://cdn.collider.com/wp-content/uploads/amazing-spider-man-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=rk-dF1lIbIg")


wonder_women = media.Movie("Wonder Women",
                           "Wonder Woman is a 2017 American superhero film based on the DC Comics character of the same name. ",
                           "http://vignette1.wikia.nocookie.net/dccu/images/c/ce/Wonder_Woman_poster_-_Courage.jpg/revision/latest/scale-to-width-down/2000?cb=20161103195152",
                           "https://www.youtube.com/watch?v=INLzqh7rZ-U")

transformers = media.Movie("Transformers",
                           "Transformers is a 2007 American science fiction action film based on the toy line of the same name created by Hasbro.",
                           "http://www.firstshowing.net/img/optimus-poster-big.jpg",
                           "https://www.youtube.com/watch?v=yCOvcyfRPRk")


movie = [toy_story, batman_vs_superman, deadpool, spiderman, wonder_women, transformers]
fresh_tomatoes.open_movies_page(movie)
# This function call opens a page of movies generated in html.
