#!/usr/bin/env python3
'''TReich | Alta3 Research
    Learning for loops'''

# Create a list of shows
shows = ["The Crown",
        "Succession",
        "Unbreakable Kimmy Schmidt",
        "Arrested Development",
        "The Great British Baking Show"]

# Create a list of corresponding times I have seen each show
times_watched = [0.5, 0, 1, 10, 25]

# I only want to print the shows with fewer than 10 characters in their title
for show in shows:
    if len(show) < 10:
        print(show)

# Now I only want to print shows with at most 2 words in their title
for show in shows:
    word_list = show.split() #.split() returns a list
    if len(word_list)<=2:
        print(show)

# Next, I want to create a dictionary that maps each show title as a key to its corresponding number of viewings
if len(shows) == len(times_watched): #first check to make sure the lists have the same length
    show_times = {}
    print(range(len(shows))) #going to use a range object to create a numberical iterator
    print(list(range(len(shows))))
    for i in range(len(shows)):
        show_times[shows[i]] = times_watched[i] #maps each corresponding show in shows with time in times watched and creates a new key-value pair in show_times

print(show_times)

# Oops! There was no need for that for loop, since the zip function does pretty much the same thing!
print(dict(zip(shows, times_watched)) == show_times)

# Finally, let's try iterating over our new dictionary to count how many times I've completed viewings of shows, and which show titles they are
counter = 0
shows_completed = []
viewings_counter = 0 

# Since dictionaries are unordered, they are a bit trickier to iterate over than lists. We need to force them into something iterable, the .items() method does that nicely
for key, value in show_times.items():
    if value >= 1: #value represents times watched
        counter += 1 #update show counter by 1
        viewings_counter += value #update viewings counter by however many viewings were completed
        shows_completed.append(key) #add show title to shows completed list

print("Total completed viewings: ", viewings_counter)
print("Number of show titles completed: ", counter)
print(f"Titles of completed shows {shows_completed}")








