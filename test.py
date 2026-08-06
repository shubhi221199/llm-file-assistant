from fs_tools import read_file, search_in_file, write_file
from fs_tools import list_files

# Read a file and print the result
result = read_file("data/resumes/resume_shubhi.txt")
# print(result)

# List files in a directory with a specific extension and print the results
# print(list_files("data/resumes", ".txt"))
# print(list_files("data/resumes", ".pdf"))

# Write a file and print the result
result1 = write_file(
    "output/test.txt",
    "Hello! This is my first generated file."
)

# print(result1)


result = search_in_file(
    "data/resumes/resume_shubhi.txt",
    "Python"
)

print(result)