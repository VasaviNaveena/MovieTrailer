import media
import movietrailer

dumbo = media.Movie("Dumbo", "Fantasy",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/Dumbo_%282019_film%29.png/220px-Dumbo_%282019_film%29.png",
                  "https://www.youtube.com/watch?v=VFUSY5lJ218")

detective_pikachu = media.Movie("Detective Pikachu", "Pokemon",
                  "http://www.gstatic.com/tv/thumb/movies/192127/192127_aa.jpg",
                  "https://www.youtube.com/watch?v=du88WArjb8w")

a_dogs_way_home = media.Movie("A Dog's Way Home", "Adventure",
                  "http://www.gstatic.com/tv/thumb/movieposters/15484124/p15484124_p_v8_aa.jpg",
                  "https://www.youtube.com/watch?v=SS0rTQz_Ggw")

the_quake = media.Movie("The Quake", "Disaster",
                  "http://www.gstatic.com/tv/thumb/movieposters/15955599/p15955599_p_v12_aa.jpg",
                  "https://www.youtube.com/watch?v=hhzsxz4fMtM")

a_quite_place = media.Movie("A Quiet Place", "Thriller",
                  "https://cdn.flickeringmyth.com/wp-content/uploads/2018/02/a-quiet-place-600x938.jpg",
                  "https://www.youtube.com/watch?v=WR7cc5t7tv8")

hereditary = media.Movie("Hereditary", "Every family tree hides a secret",
                  "http://www.impawards.com/2018/posters/hereditary_ver3.jpg",           
                  "https://www.youtube.com/watch?v=GDjIwKvd_1A")

# assign individual movies to movies array
movies = [dumbo,detective_pikachu,a_dogs_way_home,the_quake,
         a_quite_place,hereditary]

movietrailer.open_movies_page(movies)

