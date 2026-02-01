"""
Day 08 File Handling (Reading Files)

Topics covered:
- read()
- readline()
- iterating over files
- chunk reading
- file pointer behavior
- seek() and tell()
"""

# -----------------------------
# Basic file reading
# -----------------------------

# f = open("day08_file_handling/sample.txt", "r")
# content = f.read()
# print(content)
# f.close()


# -----------------------------
# Professional approach using context manager..thats safe as well.
# -----------------------------

with open("day08_file_handling/sample.txt", "r") as f:
    content = f.read()
    print(content)
    print("Total characters:", len(content))

# File is automatically closed after 'with'
# print(f.closed)  # Would be True outside the block


# -----------------------------
# Reading lines (pointer moves automatically)
# -----------------------------

with open("day08_file_handling/sample.txt", "r") as f:
    print(f.readline())        # First line
    print(f.readline())        # Second line
    print(f.readline(), end="")  # Prevent extra newline


# -----------------------------
# Looping over a file (recommended for text files)
# -----------------------------

with open("day08_file_handling/sample.txt", "r") as f:
    for line in f:
        print(line, end="")


# -----------------------------
# Reading fixed number of characters
# -----------------------------

with open("day08_file_handling/sample.txt", "r") as f:
    print(f.read(100))  # First 100 characters
    print(f.read(100))  # Next 100 characters
    print(f.read(100))  # Empty string (EOF)


# -----------------------------
# Chunk reading + pointer position
# -----------------------------

with open("day08_file_handling/sample.txt", "r") as f:
    size_to_read = 5
    chunk = f.read(size_to_read)
    print(chunk)
    print("Pointer position:", f.tell())


# -----------------------------
# seek() – resetting pointer
# -----------------------------

with open("day08_file_handling/sample.txt", "r") as f:
    size_to_read = 5
    print(f.read(size_to_read))
    f.seek(0)
    print(f.read(size_to_read))  # Same output after reset
































