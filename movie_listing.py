# Author Michael Zarate
# movie listing is where I create a bunch of objects of type "Movie"
import movies
import fresh_tomatoes


toy_story = movies.Movie("Toy Story",
                        "A story of his boys and his toys",
                        "http://vignette4.wikia.nocookie.net/disney/images/4"
                        "/4c/Toy-story-movie-posters-4.jpg/revision/latest?"
                        "cb=20140816182710",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = movies.Movie("Avatar",
                      "Conflict of life interests on a foriegn planent",
                      "http://s3.foxmovies.com/foxmovies/production/films/18"
                      "/images/posters/251-asset-page.jpg",
                      "https://youtu.be/5PSNL1qE6VY")

the_matrix = movies.Movie("The Matrix",
                          "You are the one Neo!",
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-"
                          "aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
                          "https://youtu.be/vKQi3bBA1y8")

ip_man = movies.Movie("Ip Man",
                      "A story of a Kung Fu master Ip Man",
                      "http://img.moviepostershop.com/ip-man-movie-poster-2008"
                      "-1020698460.jpg",
                      "https://youtu.be/1AJxXQ7xojE")

the_lord_of_the_rings = movies.Movie("The Lord of the Rings",
                                     "A story of brave Hobbit and his friends"
                                     "that fight to save MiddleEarth",
                                     "https://www.movieposter.com/posters"
                                     "/archive/main/105/MPW-52979",
                                     "https://youtu.be/V75dMMIW2B4")


princess_mononoke = movies.Movie("Princess Mononoke",
                                 "A story of a prince who fights a off demons"
                                 " to save his village."
                                 "Who later gets corrupted and seeks out a"
                                 " princess to find a cure to his corruption",
                                 "http://t2.gstatic.com/images?q=tbn:ANd9GcS3"
                                 "ReuE3ksrdNabf0K7frhelHm-05ec4a_1mIxQUqNiRdu"
                                 "HNrJ5",
                                 "https://youtu.be/4OiMOHRDs14")

spirited_away = movies.Movie("Sprited Away",
                             "A story of a young girl who finds her self and"
                             " gains the courage to save her parents",
                             "https://celluloidwritings.files.wordpress.com/"
                             "2015/07/spirited_away.jpg",
                             "https://youtu.be/ByXuk9QqQkk")

movies_list = [toy_story, avatar, the_matrix, ip_man, the_lord_of_the_rings,
               princess_mononoke, spirited_away]

# makes a call to the fresh_tomatoes module I imported to run this
# its important to note that this will create some html that can be later
#  used to render in a browser :)
fresh_tomatoes.open_movies_page(movies_list)
