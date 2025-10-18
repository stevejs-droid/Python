start=int(input("Enter start of range:"))
end=int(input("Enter end of range:"))
print("Odd numbers between",start,"and",end,"are:")
for num in range(start,end+1):
    if num%2!=0:
        print(num)
    else:
        print("End of loop.")
