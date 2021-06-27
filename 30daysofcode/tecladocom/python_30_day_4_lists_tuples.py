
# Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.

movies = [("Spider-Man: Far from Home","Jon Watts",2019,160000000),]

print(movies)
type(movies)

# Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
# Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.

new_movie = (input("Please, enter new movie name: "), input("Director's name: "), int(input("Enter year of release: ")), int(input("Enter movie budget: ")))
new_movie

# Use an f-string to print the movie name and release year by accessing your new movie tuple.

print(f"Latest movie added: {new_movie[0]}, released in {new_movie[2]}.")

# Add the new movie tuple to the movies collection using append.

movies.append(new_movie)

print(movies)

# Remove the first movie from movies. Use any method you like.

movies.pop(0)

print(movies)
