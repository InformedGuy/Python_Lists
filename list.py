# Create an empty list
my_list = []

# Append some elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position
my_list.insert(1, 15)

temp_list = [50, 60, 70]

# Extend my_list
my_list.extend(temp_list)

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Print the index of the value 30
print(my_list.index(30))
