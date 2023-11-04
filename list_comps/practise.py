# name = "Matthew"
# letters_list = [letter for letter in "Matthew"]
# print(letters_list)

# double_list = [n * 2 for n in range(1, 5) if n % 2 == 0]
# print(double_list)

# names = ["Caroline", "Eleanor", "Freddie",  "egg", "eggy", "Eggb"]
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# square_numbers = [number*number for number in numbers]
# print(square_numbers)


# list_of_strings = input().split(',')
# result = [n for n in numbers if n % 2 == 0]
# print(result)


with open(r"file1.txt") as file1:
    list1 = file1.readlines() 
with open(r"file2.txt") as file2:
    list2 = file2.readlines() 
result = [int(num) for num in list1 if num in list2]

print(list1)
print(list2)
print(result)