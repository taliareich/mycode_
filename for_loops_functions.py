#!/usr/bin/env python3
'''TReich | Alta3 Research
    Learning functions'''

# Create a list of shows
shows = ["The Crown",
        "Succession",
        "Unbreakable Kimmy Schmidt",
        "Arrested Development",
        "The Great British Baking Show"]

# Now let's say we have a second list of shows we want to loop through... do we have to copy the same code again??
shows_2 = ["The Simpsons",
            "The Office",
            "Seinfeld",
            "Friends"]
# Create a list of corresponding times I have seen each show
times_watched = [0.5, 0, 1, 10, 25]

# No!! All we need to do is define a function that will do that same for loop on any given list of shows
def short_shows(list_of_shows):
    for show in list_of_shows:
        word_list = show.split() #.split() returns a list
        if len(word_list)<=2:
            print(show)

# Now we can call on the custom function on both lists!
short_shows(shows)
short_shows(shows_2)

# Note that you can define a custom function without a necessary argument if it doesn't rely on any other variables
def two_plus_four():
    print(2+4)

two_plus_four()
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








