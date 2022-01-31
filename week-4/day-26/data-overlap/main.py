
# create function to prepare file contents of each file into array
def file_handler(file):
    with open(file) as file_contents:
        file = file_contents.readlines()
    file_array = []
    for item in file:
        trimmed_item = item.strip("\n")
        file_array.append(int(trimmed_item))
    return file_array


# open .txt files and read contents into a list
file1 = file_handler("file1.txt")
file2 = file_handler("file2.txt")

result = [item for item in file1 if item in file2]

# Write your code above 👆

print(result)


