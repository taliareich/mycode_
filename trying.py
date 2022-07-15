list1 = ["apple", 1, {"name":"Misty", "age":12}]

for item in list1:
    try:
        plusone = item + 1
        print(plusone)
        import fakename
    except TypeError as terr:
        print("Couldn't do that!", terr)
    except Exception as err:
        print("hmmm... not sure!", err)
    finally:
        print("All done!")
