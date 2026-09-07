# ==========================================
# Basics: String Manipulation & Math Methods
# ==========================================
import math

# String Slicing
name = "gennifer"
print(name[1:-1])  # Slices from index 1 up to last character

# Formatted Strings (f-strings)
first = "john"
last = "smith"
msg = f"{first} [{last}] is a coder"
print(msg)

# Built-in String Methods
course = "python for beginners"
print(f"Length: {len(course)}")
print(f"Uppercase: {course.upper()}")
print(f"Find 'beginners' index: {course.find('beginners')}")
print(f"Replace: {course.replace('beginners', 'absolute beginners')}")
print(f"Is 'python' in course? {'python' in course}")

# Math operations
print(f"Ceil of 2.9: {math.ceil(2.9)}")