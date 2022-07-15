#!/usr/bin/python3
'''TReich | Alta3 Research
    Make get request and parse response'''

# import statement
import requests

# Define url as global constant
URL= "http://api.open-notify.org/astros.json"

def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL)
    
    # print the class of object our resp is
    print(type(resp))
    # display status code & reason (HTTP codes)
    print(resp.status_code, resp.reason)
    # strip JSON off, translate to python
    astros = resp.json()
    # display pythonic data type
    print(type(astros))
    print(astros.keys())
    # grab the number of astros in space
    astrosnum = astros["number"]
    print("People in Space:", astrosnum)

    # iterate through list of dictionaries to grab each astro's name and craft
    for astro in astros["people"]:
        astroname = astro["name"]
        astrocraft = astro["craft"]
        print(f"{astroname} is on the {astrocraft}")

    
main()


