# Create a function that prints a right-angled triangle pattern of * based on the number of rows provided.

row=int(input("Enter number of rows: "))
for i in range(row):
    star=" "
    for j in range(i):
        star=star+"*"
        j+=1;
    print(star)
    i=i+1
