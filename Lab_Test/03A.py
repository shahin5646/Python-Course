""" Question:
 Could you explain how the recommend_movies function operates and how it determines the recommended movies based on the user's preferred genres? Additionally, how does the function handle ties in the number of common genres between movies and the user's preferences?

Given the recommend_movies function and the following dataset: 
movies = {
    "The Shawshank Redemption": ["drama"],
    "The Godfather": ["crime", "drama"],
    "The Dark Knight": ["action", "crime", "thriller"],
    "Fight Club": ["drama", "thriller"]
}
user_genres = ["action", "thriller"]

"""

def recommend_movies(movies, user_genres):
    recommended_movies = []
    max_common_genres = 0
    
    for movie, genres in movies.items():
        common_genres = len(set(genres) & set(user_genres))
        if common_genres > max_common_genres:
            recommended_movies = [movie]
            max_common_genres = common_genres
        elif common_genres == max_common_genres:
            recommended_movies.append(movie)
    
    return recommended_movies


movies = {
    "The Shawshank Redemption": ["drama"],
    "The Godfather": ["crime", "drama"],
    "The Dark Knight": ["action", "crime", "thriller"],
    "Fight Club": ["drama", "thriller"]
}
user_genres = ["action", "thriller"]


recommendations = recommend_movies(movies, user_genres)
print("Recommendations:", recommendations)
