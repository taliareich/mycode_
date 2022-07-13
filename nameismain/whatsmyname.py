# Let's define a function main() that will print the name of the current module
def main():

    print("My name is ", __name__)

# This condition specifies that the main() function will only be called if this script is run directly (not imported elsewhere)
if __name__ == "__main__":
    main()
