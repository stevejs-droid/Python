fruits=['apple','banana','orange','grape','kiwi']
search=input("Enter a fruit to search:")
for fruit in fruits:
    if fruit==search:
        print("Found",search,"in the list.")
        break
    else:
        print(search,"not found in the list.")
