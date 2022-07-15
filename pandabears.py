#!/usr/bin/env python3
'''TReich | Alta3 Research
    Intro to pandas'''

# import statement
import pandas as pd

# Define three dictionaries following the same structure
pet1 = {"name":"Misty", "age":12, "species":"cat"}
pet2 = {"name":"Fluffy", "age":5, "species":"dog"}
pet3 = {"name":"Peanut", "age":2, "species":"guinea pig"}

# Construct a DataFrame object
pets_df = pd.DataFrame([pet1, pet2, pet3])

# Display first 5 (default value) rows of dataframe
print(pets_df.head())

# Display column info & data types
print(pets_df.info())

# Display shape as a tuple of rows, cols
print(pets_df.shape)

