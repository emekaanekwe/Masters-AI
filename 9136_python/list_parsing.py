csv_data = [
"Name,Student ID,Suburb",
"Luke,202154321,2000 NSW Sydney",
"Anakin,202212345,3800 VIC Clayton",
"Boba,202223456,3800 VIC Clayton",
"Leia,202098764,3000 VIC Melbourne"
]

# remove the first el in list
csv_data.remove(csv_data[0])

#we ask the user for a year
query_year = int(input("input year to search:"))
arr = []
for data in csv_data:
    n = data.split(",")
    print(n)
    year = n[1]
    year_sliced = year[0:4]
    if int(year_sliced) == query_year:
        print(type(n[2]))
        print(n[0], (n[2])[5:8])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    count = 0
    x = csv_data[count].split(str(query_year))
    y = x[count].split(",")
    print(y)
    z = y[count][0:4]
    print(z)
    count += count
    '''
#int(input("Input year to search: "))

'''
for data in csv_data:
    arr.append(data)
    if arr[data]split(str(query_year))
print(arr)

for i in csv_data:
    list_split = i.split(",")
    year = list_split[1]
    year_sliced = year[0:4]
    if year_sliced == query_year:
        print(list_split[0]+" "+list_split[2])
'''