# All that we will do here is import the script whatsmyname. Since that script contains the condition if __name__ == "__main__", we need to explicitly call on the main function to run
import whatsmyname

# We can decide when in this script to use the main function by calling on it like so:
whatsmyname.main()

# When you run this script, the variable __name__ should display whatsmyname, NOT the name of this module! That's because we are pointing to the original script's name that contains the code of the main function
