current_movies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    "Frosty the Snowman": "3:00pm",
    "Christmas Vacation": "5:00pm",
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("Hi, welcome to the theater. What movie would you like to watch? \n")

movie_time = current_movies.get(movie)

if movie_time == None:
    print("Requested movie is not playing")
else:
    print(movie, "is playing at", movie_time)
