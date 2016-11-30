import media
import fresh_tomatoes

# Create favorite movies as new Movie objects
the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels "
                         "about the true nature of his reality and his role in"
                         "the war against its controllers.",
                         "https://goo.gl/lmLIiH",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of "
                        "dream-sharing technology, is given the inverse task o"
                        "f planting an idea into the mind of a CEO.",
                        "https://goo.gl/j4vfS8",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to cha"
                         "nge his life, crosses paths with a devil-may-care so"
                         "ap maker, forming an underground fight club that evo"
                         "lves into something much, much more.",
                         "https://goo.gl/xgc3ft",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

ferris_bueller = media.Movie("Ferris Bueller's Day Off",
                             "A high school wise guy is determined to have a "
                             "day off from school, despite what the principal "
                             "thinks of that.",
                             "https://goo.gl/nU9EJP",
                             "https://www.youtube.com/watch?v=R-P6p86px6U")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc"
                              "and chaos on the people of Gotham, the caped "
                              "crusader must come to terms with one of the "
                              "greatest psychological tests of his ability to "
                              "fight injustice.",
                              "https://goo.gl/Fmi3Lr",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

mad_max_fury_road = media.Movie("Mad Max: Fury Road",
                                "A woman rebels against a tyrannical ruler in "
                                "postapocalyptic Australia in search for her "
                                "home-land with the help of a group of female "
                                "prisoners, a psychotic worshipper, and a "
                                "drifter named Max.",
                                "https://goo.gl/iM3crh",
                                "https://www.youtube.com/watch?v=hEJnMQG9ev8")

# Store all of the movie objects in a list called movies for easier retrievel
movies = [the_matrix, inception, fight_club, ferris_bueller, the_dark_knight,
          mad_max_fury_road]
# Call to the open_movies_page function to build or overwrite the html output
fresh_tomatoes.open_movies_page(movies)
