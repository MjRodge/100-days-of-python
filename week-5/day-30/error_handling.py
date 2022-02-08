# file not found error handling

try:
    file = open("this_text_file.txt")
except FileNotFoundError as error_message:
    print(f"the file {error_message} does not exist")
    file = open("this_text_file.txt", "w")
    print("creating file")
    file.write("this was written from an except block of a try error handler")
    print("writing to file")
else:
    content = file.read()
    print("reading contents of file:")
    print(content)
finally:
    file.close()
    print("file was closed - this always runs")
