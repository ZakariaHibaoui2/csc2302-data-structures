#!/usr/bin/env python3
"""
CSC2302 COMPLETE DATA STRUCTURES GUIDE
Al Akhawayn University in Ifrane
Simple English - covers ALL files in data/
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
)
from reportlab.lib import colors

OUTPUT = "CSC2302_Complete_Guide.pdf"

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name='CT', fontName='Helvetica-Bold', fontSize=24,
    alignment=TA_CENTER, spaceAfter=8, textColor=HexColor('#0d47a1')))
styles.add(ParagraphStyle(name='CS', fontName='Helvetica', fontSize=13,
    alignment=TA_CENTER, spaceAfter=20, textColor=HexColor('#546e7a')))
styles.add(ParagraphStyle(name='PT', fontName='Helvetica-Bold', fontSize=18,
    spaceBefore=20, spaceAfter=8, textColor=HexColor('#0d47a1')))
styles.add(ParagraphStyle(name='CH', fontName='Helvetica-Bold', fontSize=14,
    spaceBefore=14, spaceAfter=4, textColor=HexColor('#1565c0')))
styles.add(ParagraphStyle(name='SH', fontName='Helvetica-Bold', fontSize=11,
    spaceBefore=8, spaceAfter=3, textColor=HexColor('#1e88e5')))
styles.add(ParagraphStyle(name='BD', fontName='Helvetica', fontSize=9.5,
    leading=13, spaceAfter=4, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='CB', fontName='Courier', fontSize=7.5,
    leading=9.5, leftIndent=6, spaceAfter=3, spaceBefore=2,
    backColor=HexColor('#f5f5f5'), borderWidth=0.5,
    borderColor=HexColor('#e0e0e0'), borderPadding=3))
styles.add(ParagraphStyle(name='NT', fontName='Helvetica-Oblique', fontSize=8.5,
    leading=11, spaceAfter=3, leftIndent=10,
    textColor=HexColor('#5d4037'),
    borderWidth=0.3, borderColor=HexColor('#bcaaa4'), borderPadding=2))
styles.add(ParagraphStyle(name='MT', fontName='Helvetica', fontSize=8.5,
    leading=11, spaceAfter=3, leftIndent=10,
    textColor=HexColor('#b71c1c'), backColor=HexColor('#ffebee'),
    borderWidth=0.3, borderColor=HexColor('#ef9a9a'), borderPadding=2))
styles.add(ParagraphStyle(name='EX', fontName='Helvetica', fontSize=8.5,
    leading=11, spaceAfter=3, leftIndent=8,
    textColor=HexColor('#1b5e20'), backColor=HexColor('#e8f5e9'),
    borderWidth=0.3, borderColor=HexColor('#a5d6a7'), borderPadding=2))
styles.add(ParagraphStyle(name='TB', fontName='Courier', fontSize=7,
    leading=9, leftIndent=4, spaceAfter=2, spaceBefore=1,
    backColor=HexColor('#e8eaf6'), borderPadding=2))

def body(t): return Paragraph(t, styles['BD'])
def code(t): return Paragraph(t.replace('\n','<br/>'), styles['CB'])
def note(t): return Paragraph(t, styles['NT'])
def mistake(t): return Paragraph(t, styles['MT'])
def exam(t): return Paragraph(t, styles['EX'])
def sp(h=4): return Spacer(1,h)
def hr():
    return HRFlowable(width="100%", thickness=0.5, color=HexColor('#bdbdbd'), spaceAfter=5, spaceBefore=5)

S = story = []

# ═══════════════════════════ COVER ══════════════════════
S.append(Spacer(1,50*mm))
S.append(Paragraph("CSC2302 DATA STRUCTURES", styles['CT']))
S.append(Paragraph("COMPLETE STUDY GUIDE", styles['CT']))
S.append(Spacer(1,10*mm))
S.append(Paragraph("Simple English - Step by Step - With Examples", styles['CS']))
S.append(Paragraph("For students who need help understanding Python", styles['CS']))
S.append(Spacer(1,20*mm))
S.append(body("Covers: Python Review | Linked Lists | Stacks | Queues"))
S.append(body("Trees | BST | Big O | Sorting | Searching | Graphs"))
S.append(body("Exam Format | Assignments | Practice Problems"))
S.append(Spacer(1,15*mm))
S.append(Paragraph("Al Akhawayn University in Ifrane", styles['CS']))
S.append(Paragraph("School of Science and Engineering", styles['CS']))
S.append(Paragraph("Based on the CSC2302 course materials", styles['CS']))
S.append(PageBreak())

# ═══════════════════════════ TOC ══════════════════════════
S.append(Paragraph("TABLE OF CONTENTS", styles['PT']))
S.append(hr())
toc = [
    "PART 0: Exam Format - What is on the exam",
    "PART 1: Python Review - variables, print, input, if, loops, lists, dicts, files",
    "PART 2: Big O Notation - how fast is your code",
    "PART 3: Searching and Sorting - find and organize data",
    "PART 4: Linked Lists - chain of nodes",
    "PART 5: Stacks - Last In, First Out",
    "PART 6: Queues - First In, First Out",
    "PART 7: Trees and Binary Search Trees",
    "PART 8: Graphs - nodes and connections",
    "PART 9: Recursion - function that calls itself",
    "PART 10: Assignments - BST Inventory, Student Data, Queue/Stack exercises",
    "PART 11: Practice Problems with Solutions",
    "PART 12: Quick Reference Sheets",
]
for t in toc:
    S.append(body(t))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 0: EXAM FORMAT
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 0 - EXAM FORMAT", styles['PT']))
S.append(hr())
S.append(body("This part is IMPORTANT. Read this first. It tells you exactly what is on the exam."))
S.append(sp())

S.append(Paragraph("MIDTERM EXAM (Oct 23, 8:30-10:30)", styles['CH']))
S.append(exam("10 exercises, total 100 points:"))
S.append(exam("Part 1: Python Data Structures (20 points - 2 exercises)"))
S.append(exam("  Coding exercises - you write function definitions"))
S.append(exam("Part 2: Searching and Sorting (20 points - 2 exercises)"))
S.append(exam("  Coding exercises - you write function definitions"))
S.append(exam("Part 3: Big O Notation (20 points - 2 exercises)"))
S.append(exam("  NO CODING - just analysis/written answers"))
S.append(exam("Part 4: Linked Lists (40 points - 4 exercises)"))
S.append(exam("  Coding exercises - you write function definitions"))
S.append(sp())

S.append(Paragraph("FINAL EXAM", styles['CH']))
S.append(exam("4 parts:"))
S.append(exam("Part 1: Trees (30 points)"))
S.append(exam("Part 2: Heaps (30 points)"))
S.append(exam("Part 3: Hash Tables (40 points)"))
S.append(exam("Part 4: Graphs (10 points bonus, no coding)"))

S.append(sp())
S.append(Paragraph("Exam Rules (MEMORIZE THESE)", styles['CH']))
S.append(body("1. No phones. Turn off and put in bag."))
S.append(body("2. No calculators or smart watches."))
S.append(body("3. You get 4 pages scratch paper. Use it well."))
S.append(body("4. No questions during exam. Read instructions carefully."))
S.append(body("5. Use descriptive names: <b>gpa</b> not <b>x</b>"))
S.append(body("6. Plagiarism = WF grade + report to disciplinary committee."))
S.append(body("7. Leave your AUI ID on desk."))
S.append(body("8. No leaving room unless you submit your exam."))

S.append(sp())
S.append(Paragraph("What the exam covers (from Canvas):", styles['CH']))
S.append(body("- Chapter 2 & 3: Sorting, Searching, Algorithm Analysis"))
S.append(body("- Lab Sessions: Linked List style problems"))
S.append(body("- Python: lists, tuples, dictionaries (may be combined with Ch 2, 3, 4)"))
S.append(body("- Case studies on Linked Lists"))

S.append(sp())
S.append(Paragraph("IMPORTANT: How to define functions/methods:", styles['CH']))
S.append(exam("If the problem says 'instance method' -> define INSIDE a class, first parameter = self"))
S.append(exam("If the problem says 'function' -> do NOT use self"))
S.append(exam("If file is already open -> do NOT open it again, accept file handler as parameter"))
S.append(exam("If object already created -> do NOT create it, accept as parameter"))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 1: PYTHON REVIEW
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 1 - PYTHON REVIEW", styles['PT']))
S.append(hr())
S.append(body("This part is from the <b>Python Programming Review</b> presentation."))
S.append(body("If you already know Python basics, skip to Part 4 (Linked Lists)."))
S.append(PageBreak())

S.append(Paragraph("1.1 Variables", styles['CH']))
S.append(body("A <b>variable</b> is a name for a value stored in memory. Think: box with a label."))
S.append(body("Python <b>infers</b> the type automatically (you don't need to say 'this is an integer')."))
S.append(code("""x = 10        # x is int (whole number)
y = 10.5      # y is float (decimal)
name = "Ahmed"  # str (text)
is_student = True   # bool (True/False)

# Multiple variables at once:
a, b, c = 1, 2, 3"""))

S.append(Paragraph("Variable Rules:", styles['SH']))
S.append(body("- Start with letter or _ (underscore)"))
S.append(body("- No spaces. Use _ instead."))
S.append(body("- Case sensitive: <b>name</b> and <b>Name</b> are DIFFERENT"))
S.append(body("- Cannot use Python keywords: <b>def, class, if, for, while</b> etc."))
S.append(sp())

S.append(Paragraph("1.2 Arithmetic Operations", styles['CH']))
S.append(code("""a = 10
b = 3
print(a + b)   # 13  (addition)
print(a - b)   # 7   (subtraction)
print(a * b)   # 30  (multiplication)
print(a / b)   # 3.333...  (division - always gives float)
print(a // b)  # 3   (floor division - integer result)
print(a % b)   # 1   (modulus - remainder)
print(a ** b)  # 1000 (exponent - 10 to the power 3)

# Shorthand:
a += 5   # same as: a = a + 5
a -= 3   # same as: a = a - 3"""))
S.append(sp())

S.append(Paragraph("1.3 Input and Output (from slides)", styles['CH']))
S.append(code("""# OUTPUT - print()
print("Hello")                    # basic
print("Age:", 20)                 # multiple items, separated by space
print("Age: " + str(20))         # using + (no space added)

# BEST: f-string (formatted string)
name = "Ahmed"
age = 20
print(f"My name is {name} and I am {age}")
# shows: My name is Ahmed and I am 20

# INPUT - get text from user
name = input("Enter your name: ")     # returns STRING always

# Multiple inputs on one line:
x, y = input("Enter two numbers: ").split()
# User types: "10 20"  -> x="10", y="20"
# Convert to int:  x = int(x)"""))
S.append(sp())

S.append(Paragraph("1.4 If Statements (selections)", styles['CH']))
S.append(code("""score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Comparison operators:
# ==   equal          !=   not equal
# >    greater than   <    less than
# >=   >=             <=   <=

# Logical operators (combine conditions):
# and   BOTH True      or   at least ONE True      not   reverse"""))
S.append(sp())

S.append(Paragraph("1.5 Loops (repetitions)", styles['CH']))
S.append(code("""# FOR LOOP - iterate over a sequence
for i in range(5):     # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):  # 2, 3, 4, 5
    print(i)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# WHILE LOOP - keep going while condition is True
count = 0
while count < 5:
    print(count)
    count += 1   # IMPORTANT: update or loop runs forever!

# Loop control:
# break    - exit loop immediately
# continue - skip to next iteration
# pass     - do nothing (placeholder)"""))
S.append(sp())

S.append(Paragraph("1.6 Lists (from Python Review slides)", styles['CH']))
S.append(body("A list is a collection of items. Ordered, changeable, allows duplicates."))
S.append(code("""nums = [1, 2, 3, 4, 5]

# Access:           nums[0] -> 1,  nums[-1] -> 5
# Change:           nums[0] = 10
# Add to end:       nums.append(6)
# Remove by value:  nums.remove(3)
# Sort:             nums.sort()
# Length:           len(nums)

# Slicing (take part of a list):
nums[1:3]   # [2, 3]   (from index 1 to 2, 3 is NOT included)
nums[:3]    # [1, 2, 3]
nums[2:]    # [3, 4, 5]

# Matrix (list of lists):
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # 2  (row 0, column 1)"""))

note("WARNING: [0] * 3 creates 3 references to the SAME object! [[0]*3]*3 -> all rows share same inner list!")

S.append(sp())
S.append(Paragraph("1.7 Tuples", styles['CH']))
S.append(body("A tuple is like a list but <b>immutable</b> (cannot change after creation)."))
S.append(code("""t = (1, 2, 3)
print(t[0])    # 1
# t[0] = 10   ERROR! Cannot change tuple"""))
S.append(sp())

S.append(Paragraph("1.8 Dictionaries", styles['CH']))
S.append(body("A dictionary stores <b>key-value pairs</b>. Like a phone book: name -> number."))
S.append(code("""student = {
    "name": "Ahmed",
    "age": 20,
    "major": "CS"
}
print(student["name"])         # Ahmed
print(student.get("name"))     # Ahmed (safer)
student["age"] = 21            # change value
student["city"] = "Ifrane"     # add new key

# Loop through:
for key in student:
    print(key, student[key])

for key, val in student.items():
    print(f"{key}: {val}")

# Count occurrences (common exam question):
nums = [2, 2, 4, 5, 4, 4, 5, 7]
counts = {}
for n in nums:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1
print(counts)   # {2: 2, 4: 3, 5: 2, 7: 1}"""))
S.append(sp())

S.append(Paragraph("1.9 Strings", styles['CH']))
S.append(code("""s = "Hello World"
len(s)              # 11
s.upper()           # "HELLO WORLD"
s.lower()           # "hello world"
s.find("World")     # 6  (position where "World" starts)
s.count("l")        # 3  (how many 'l'?)
s.split(" ")        # ["Hello", "World"]
" ".join(["a","b"]) # "a b"
s[0:5]              # "Hello"  (slicing works like lists)

# Check if substring exists:
if "World" in s:
    print("Found!")"""))
S.append(sp())

S.append(Paragraph("1.10 Functions", styles['CH']))
S.append(code("""def add(a, b):
    return a + b

result = add(3, 5)   # result = 8

# Default parameter values:
def greet(name="Student"):
    print(f"Hello {name}")

# *args = any number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))   # 10

# lambda = short anonymous function
double = lambda x: x * 2
print(double(5))  # 10

# map, filter, sorted (built-in functions):
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))   # [2, 4, 6, 8]
evens = list(filter(lambda x: x%2==0, nums))  # [2, 4]
s = sorted(nums, reverse=True)   # [4, 3, 2, 1]"""))
S.append(sp())

S.append(Paragraph("1.11 File I/O", styles['CH']))
S.append(body("To read or write files, use <b>open()</b>. ALWAYS close the file or use <b>with</b>."))
S.append(code("""# Modes: r = read, w = write (overwrites!), a = append
#        b = binary (for images/videos)

# Read entire file:
with open("file.txt", "r") as f:
    content = f.read()

# Read all lines into a list:
with open("file.txt", "r") as f:
    lines = f.readlines()

# Read line by line:
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Write:
with open("output.txt", "w") as f:
    f.write("Hello\\n")
    f.write("World\\n")

# seek() - move cursor to a position:
with open("file.txt", "r") as f:
    content = f.read()     # read everything
    f.seek(0)              # go back to start
    first_10 = f.read(10)  # read first 10 characters"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 2: BIG O
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 2 - BIG O NOTATION", styles['PT']))
S.append(hr())
S.append(body("Big O tells you how runtime grows as input size (n) gets bigger."))
S.append(body("Source: Course slides + Exam Part 3 (20 points, NO CODING)."))
S.append(PageBreak())

S.append(Paragraph("2.1 The Big O Classes", styles['CH']))
S.append(code("""O(1)     = CONSTANT   - same time no matter what
           Example: get arr[0], push to stack
O(log n) = LOGARITHMIC - grows very slowly
           Example: Binary Search, BST search
O(n)     = LINEAR      - grows with n
           Example: loop through a list
O(n log n) = LINEATHM  - sorting algorithms
           Example: Merge Sort, Quick Sort
O(n^2)   = QUADRATIC   - nested loops
           Example: Bubble Sort, nested for"""))
S.append(sp())

S.append(Paragraph("2.2 How to Calculate", styles['CH']))
S.append(code("""# 1. Drop constants:
# O(2n) -> O(n)     O(500) -> O(1)     O(n/2) -> O(n)

# 2. Keep the biggest term only:
# O(n + n^2) -> O(n^2)
# O(n + log n) -> O(n)
# O(1 + n + n^2) -> O(n^2)

# 3. Sequential operations add, nested loops multiply:
# for i in range(n):       O(n)
#   for j in range(n):     O(n * n) = O(n^2)
#     print(i, j)"""))

S.append(sp())
S.append(Paragraph("2.3 Complexity of Data Structures (MEMORIZE)", styles['CH']))
S.append(code("""Structure        Search    Insert    Delete
Array/List       O(n)      O(n)      O(n)
Linked List      O(n)      O(1)*     O(1)*
Stack            -         O(1)      O(1)
Queue            -         O(1)      O(1)
BST (balanced)   O(log n)  O(log n)  O(log n)
BST (worst)      O(n)      O(n)      O(n)

*Linked List: insert/delete at head is O(1), at end/tail is O(n) without tail ptr
*Stack: push/pop = O(1)
*Queue: enqueue/dequeue = O(1) with deque"""))

note("Exam: Part 3 is NO CODING. You just analyze Big O.")
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 3: SEARCHING AND SORTING
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 3 - SEARCHING AND SORTING", styles['PT']))
S.append(hr())
S.append(body("Source: Course slides. Exam: Part 2 = 20 points."))
S.append(PageBreak())

S.append(Paragraph("3.1 Linear Search - O(n)", styles['CH']))
S.append(code("""def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # FOUND, return index
    return -1          # NOT found

# Checks every element one by one.
# Simple but SLOW for big lists."""))
S.append(sp())

S.append(Paragraph("3.2 Binary Search - O(log n)", styles['CH']))
S.append(body("<b>REQUIREMENT:</b> List MUST be sorted first!"))
S.append(code("""def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2   # find middle

        if arr[mid] == target:
            return mid            # FOUND!
        elif arr[mid] < target:
            low = mid + 1         # target in right half
        else:
            high = mid - 1        # target in left half
    return -1                     # NOT found

# Trace: binary_search([2, 5, 8, 12, 16, 23], 16)
# low=0 high=5 mid=2 arr[2]=8 -> 8<16, go RIGHT
# low=3 high=5 mid=4 arr[4]=16 -> FOUND! (2 steps)
# Linear search would take 5 steps!"""))
S.append(sp())

S.append(Paragraph("3.3 Bubble Sort - O(n^2)", styles['CH']))
S.append(code("""def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Each pass: largest element "bubbles up" to correct position
# [5, 3, 8, 1] -> pass 1: [3,5,1,8] -> pass 2: [3,1,5,8] -> [1,3,5,8]"""))
S.append(sp())

S.append(Paragraph("3.4 Selection Sort - O(n^2)", styles['CH']))
S.append(code("""def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Find smallest, put at position 0.
# Find next smallest, put at position 1. Etc."""))
S.append(sp())

S.append(Paragraph("3.5 Insertion Sort - O(n^2) but fast for nearly-sorted data", styles['CH']))
S.append(code("""def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Like sorting cards in your hand.
# Take one card, insert in correct position."""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 4: LINKED LISTS (BIG SECTION - 40 points on exam)
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 4 - LINKED LISTS", styles['PT']))
S.append(hr())
S.append(body("<b>EXAM WEIGHT: Part 4 = 40 points (4 exercises)</b>"))
S.append(body("Sources: c.pptx (Linked Lists module), Python Review slides, BST file."))
S.append(body("A <b>linked list</b> is a chain of <b>nodes</b>. Each node has data and a pointer to the next node."))
S.append(body("Unlike Python lists, linked list elements are NOT stored next to each other in memory."))
S.append(body("They are connected by pointers (like a treasure hunt where each clue tells you where the next clue is)."))
S.append(PageBreak())

S.append(Paragraph("4.1 What is a Node?", styles['CH']))
S.append(code("""class Node:
    def __init__(self, data):
        self.data = data   # the value
        self.next = None   # pointer to next node

# Visual:
# [data | next] -> [data | next] -> [data | None]"""))
S.append(sp())

S.append(Paragraph("4.2 Singly Linked List Class", styles['CH']))
S.append(code("""class LinkedList:
    def __init__(self):
        self.head = None   # first node
        self.tail = None   # last node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def __str__(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return " -> ".join(result)

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count"""))
S.append(sp())

S.append(Paragraph("4.3 Remove a node by value", styles['CH']))
S.append(code("""def remove(self, target):
    curr = self.head
    prev = None
    while curr:
        if curr.data == target:
            if prev is None:
                self.head = curr.next
            else:
                prev.next = curr.next
            if curr == self.tail:
                self.tail = prev
            return True
        prev = curr
        curr = curr.next
    return False"""))
S.append(sp())

S.append(Paragraph("4.4 Pop (remove at index)", styles['CH']))
S.append(code("""def pop(self, index):
    if index < 0 or index >= len(self):
        raise IndexError("Index out of range")
    curr = self.head
    prev = None
    for _ in range(index):
        prev = curr
        curr = curr.next
    if prev is None:
        self.head = curr.next
    else:
        prev.next = curr.next
    if curr == self.tail:
        self.tail = prev
    return curr.data"""))
S.append(sp())

S.append(Paragraph("4.5 Insert at Position", styles['CH']))
S.append(code("""def insert(self, index, data):
    new_node = Node(data)
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        return
    curr = self.head
    for _ in range(index - 1):
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    if new_node.next is None:
        self.tail = new_node"""))
S.append(sp())

S.append(Paragraph("4.6 Reverse Linked List (in-place)", styles['CH']))
S.append(code("""def reverse(self):
    prev = None
    curr = self.head
    self.tail = curr
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    self.head = prev

# 10 -> 20 -> 30 -> None
# Step 1: curr=10, prev=None, save 20, 10.next=None
# Step 2: curr=20, prev=10, save 30, 20.next=10
# Step 3: curr=30, prev=20, save None, 30.next=20
# Result: 30 -> 20 -> 10 -> None"""))
S.append(sp())

S.append(Paragraph("4.7 Find Middle Node (Two-Pointer/Fast & Slow)", styles['CH']))
S.append(code("""def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# [10 -> 20 -> 30 -> 40 -> 50]
# slow: [10] [20] [30]
# fast: [10] [30] [50] (stops)
# Middle: 30"""))
S.append(sp())

S.append(Paragraph("4.8 Remove Duplicates", styles['CH']))
S.append(code("""def remove_duplicates(self):
    seen = set()
    curr = self.head
    prev = None
    while curr:
        if curr.data in seen:
            prev.next = curr.next
            if curr == self.tail:
                self.tail = prev
        else:
            seen.add(curr.data)
            prev = curr
        curr = curr.next"""))
S.append(sp())

S.append(Paragraph("4.9 Merge Two Sorted Linked Lists", styles['CH']))
S.append(code("""@staticmethod
def merge_sorted(list1, list2):
    dummy = Node(0)
    tail = dummy
    c1, c2 = list1.head, list2.head
    while c1 and c2:
        if c1.data <= c2.data:
            tail.next = c1
            c1 = c1.next
        else:
            tail.next = c2
            c2 = c2.next
        tail = tail.next
    tail.next = c1 if c1 else c2
    return dummy.next

# List1: 1 -> 5 -> 9
# List2: 3 -> 6 -> 7
# Result: 1 -> 3 -> 5 -> 6 -> 7 -> 9"""))
S.append(sp())

S.append(Paragraph("4.10 Doubly Linked List (extra)", styles['CH']))
S.append(code("""class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# None <- [prev|data|next] <-> [prev|data|next] -> None"""))
S.append(sp())

S.append(Paragraph("4.11 Linked List vs Python List", styles['CH']))
S.append(exam("Use Linked List WHEN: frequent insert/delete at beginning, unknown size, dynamic data"))
S.append(exam("Use Python List WHEN: need fast random access by index (O(1) lookup)"))
S.append(sp())
S.append(code("""Feature          Python List    Linked List
Memory           Contiguous     Non-contiguous
Random access    O(1)           O(n)
Insert at head   O(n)           O(1)
Insert at tail   O(1) amortized O(1) (with tail)
Delete at head   O(n)           O(1)
Space overhead   Low            Extra pointer per node"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 5: STACKS
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 5 - STACKS", styles['PT']))
S.append(hr())
S.append(body("<b>LIFO</b> = Last In, First Out. Like a stack of plates."))
S.append(body("Sources: Stacks & Queues slides, Stacks Case Study, Queues & Stacks Assignment."))
S.append(PageBreak())

S.append(Paragraph("5.1 Stack Operations", styles['CH']))
S.append(code("""push(value)   # add to top  O(1)
pop()         # remove from top  O(1)
peek()        # see top without removing  O(1)
is_empty()    # check if empty  O(1)"""))
S.append(sp())

S.append(Paragraph("5.2 Stack - List Implementation", styles['CH']))
S.append(code("""class Stack:
    def __init__(self):
        self.__L = []
    def push(self, value):
        self.__L.append(value)
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.__L.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.__L[-1]
    def is_empty(self):
        return len(self.__L) == 0

s = Stack()
s.push(10); s.push(20); s.push(30)
s.pop()      # 30
s.peek()     # 20"""))
S.append(sp())

S.append(Paragraph("5.3 Check Brackets - ( ) [ ] { }", styles['CH']))
S.append(code("""def is_valid_brackets(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

# "({[]})" -> True    "(]" -> False"""))
S.append(sp())

S.append(Paragraph("5.4 Browser History (Two Stacks)", styles['CH']))
S.append(code("""class BrowserHistory:
    def __init__(self):
        self.back = []
        self.forward = []
        self.current = None
    def visit(self, url):
        if self.current:
            self.back.append(self.current)
        self.current = url
        self.forward.clear()
    def back(self):
        if not self.back:
            return False
        self.forward.append(self.current)
        self.current = self.back.pop()
        return True
    def forward(self):
        if not self.forward:
            return False
        self.back.append(self.current)
        self.current = self.forward.pop()
        return True"""))
S.append(sp())

S.append(Paragraph("5.5 Reverse String Using Stack", styles['CH']))
S.append(code("""def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    result = ""
    while stack:
        result += stack.pop()
    return result

# hello -> push h,e,l,l,o -> pop o,l,l,e,h -> olleh"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 6: QUEUES
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 6 - QUEUES", styles['PT']))
S.append(hr())
S.append(body("<b>FIFO</b> = First In, First Out. Like a line at a store."))
S.append(body("Sources: Queues Case Study, Stacks & Queues slides, Queues & Stacks Assignment."))
S.append(PageBreak())

S.append(Paragraph("6.1 Queue Operations", styles['CH']))
S.append(code("""enqueue(value)  # add to back  O(1)
dequeue()       # remove from front  O(1)
front()         # see front without removing  O(1)"""))
S.append(sp())

S.append(Paragraph("6.2 Queue using deque (BEST)", styles['CH']))
S.append(code("""from collections import deque

class Queue:
    def __init__(self):
        self.__L = deque()
    def enqueue(self, value):
        self.__L.append(value)
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.__L.popleft()
    def front(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.__L[0]
    def is_empty(self):
        return len(self.__L) == 0

q = Queue()
q.enqueue(10); q.enqueue(20); q.enqueue(30)
q.dequeue()  # 10 (FIRST in, FIRST out)"""))
S.append(sp())

S.append(Paragraph("6.3 Deque - Double-Ended Queue", styles['CH']))
S.append(code("""from collections import deque
d = deque()
d.append(10)          # add right  [10]
d.appendleft(5)       # add left   [5, 10]
d.popleft() -> 5      # remove left [10, 20]
d.pop() -> 20         # remove right [10]"""))
S.append(sp())

S.append(Paragraph("6.4 Airport Security Queue", styles['CH']))
S.append(code("""class SecurityQueue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, name):
        self.queue.append(name)
    def dequeue(self):
        return self.queue.popleft() if self.queue else None

def process_events(filepath):
    q = SecurityQueue()
    served = []
    with open(filepath) as f:
        for line in f:
            parts = line.strip().split()
            if parts[0] == "ARRIVE":
                q.enqueue(parts[1])
            elif parts[0] == "SERVE":
                name = q.dequeue()
                if name:
                    served.append(name)
    return served"""))
S.append(sp())

S.append(Paragraph("6.5 Reverse Queue Using Stack", styles['CH']))
S.append(code("""def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q

# [10, 20, 30, 40, 50] -> [50, 40, 30, 20, 10]"""))
S.append(sp())

S.append(Paragraph("6.6 Filter Odd Numbers", styles['CH']))
S.append(code("""def filter_odds(q):
    result = deque()
    while q:
        val = q.popleft()
        if val % 2 == 1:
            result.append(val)
    return result

# [12, 7, 4, 15, 8, 21, 6, 9] -> [7, 15, 21, 9]"""))
S.append(sp())

S.append(Paragraph("6.7 Merge Two Sorted Queues", styles['CH']))
S.append(code("""def merge_sorted_queues(q1, q2):
    result = deque()
    while q1 and q2:
        if q1[0] <= q2[0]:
            result.append(q1.popleft())
        else:
            result.append(q2.popleft())
    while q1: result.append(q1.popleft())
    while q2: result.append(q2.popleft())
    return result

# [1,5,9,12,18] + [3,6,7,15,20,25] -> [1,3,5,6,7,9,12,15,18,20,25]"""))
S.append(sp())

S.append(Paragraph("6.8 Merge Two Stacks Alternately", styles['CH']))
S.append(code("""def merge_stacks_alternate(s1, s2):
    result = []
    while s1 and s2:
        result.append(s1.pop())
        result.append(s2.pop())
    while s1: result.append(s1.pop())
    while s2: result.append(s2.pop())
    return result

# S1: [5,10,15]  S2: [A,B,C,D]
# Result: [5,A,10,B,15,C,D]"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 7: TREES AND BST
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 7 - TREES AND BINARY SEARCH TREES", styles['PT']))
S.append(hr())
S.append(body("<b>Final exam: Trees = 30 points</b>"))
S.append(body("Sources: Tree_Data_Structures_Intro.pptx, Binary_Trees_Recursion_Practice.pdf,"))
S.append(body("BST implementation file, BST Inventory Assignment."))
S.append(PageBreak())

S.append(Paragraph("7.1 What is a Tree?", styles['CH']))
S.append(body("A <b>tree</b> is a hierarchical structure. Like a family tree or company hierarchy."))
S.append(body("- <b>Root</b> = top node (no parent)"))
S.append(body("- <b>Child</b> = node connected below another"))
S.append(body("- <b>Leaf</b> = node with no children"))
S.append(body("- <b>Edge</b> = connection between two nodes"))
S.append(body("- <b>Height</b> = edges from root to deepest leaf"))
S.append(sp())
S.append(body("Tree rules:"))
S.append(body("1. Connected - path between any two nodes"))
S.append(body("2. Acyclic - no cycles (loops)"))
S.append(body("3. n nodes = n-1 edges"))
S.append(sp())

S.append(Paragraph("7.2 Types of Trees", styles['CH']))
S.append(code("""Binary Tree:     each node has at most 2 children
Ternary Tree:    each node has at most 3 children
N-ary Tree:      any number of children
Complete Tree:   all levels full except possibly last, left-filled
Full/Perfect:    all levels completely filled
Skewed Tree:     all nodes have one child (like linked list)
Balanced Tree:   height diff between left/right <= 1
BST:             left < node < right
Heap:            parent smaller (min-heap) or larger (max-heap) than children"""))
S.append(sp())

S.append(Paragraph("7.3 TreeNode", styles['CH']))
S.append(code("""class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree:
#       1
#      / \\
#     2   3
#    /\\   /
#   4  5 6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)"""))
S.append(sp())

S.append(Paragraph("7.4 Tree Traversals", styles['CH']))
S.append(code("""# INORDER:  Left -> Node -> Right  (BST -> SORTED!)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# PREORDER: Node -> Left -> Right
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# POSTORDER: Left -> Right -> Node
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# LEVEL-ORDER (BFS using queue)
from collections import deque
def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.value, end=" ")
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

# For tree [1, 2, 3, 4, 5, 6]:
# Inorder:    4 2 5 1 6 3
# Preorder:   1 2 4 5 3 6
# Postorder:  4 5 2 6 3 1"""))
S.append(sp())

S.append(Paragraph("7.5 BST Rule (MEMORIZE THIS)", styles['CH']))
S.append(exam("For ANY node: LEFT subtree values are SMALLER. RIGHT subtree values are BIGGER."))
S.append(sp())
S.append(code("""#        50
#       /  \\
#     30    70
#    /  \\  /  \\
#   20  40 60  80
#
# Inorder: 20 30 40 50 60 70 80 (SORTED!)"""))
S.append(sp())

S.append(Paragraph("7.6 BST - Full Implementation", styles['CH']))
S.append(code("""class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if value <= root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.insert(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                self.insert(root.right, value)

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert(self.root, value)

    def search(self, target):
        def _search(root, target):
            if root is None: return False
            if root.value == target: return True
            elif target < root.value:
                return _search(root.left, target)
            else:
                return _search(root.right, target)
        return _search(self.root, target)"""))
S.append(sp())

S.append(Paragraph("7.7 BST Remove - 3 Cases", styles['CH']))
S.append(body("Case 1: Leaf (no children) - just delete"))
S.append(body("Case 2: One Child - bypass the node"))
S.append(body("Case 3: Two Children - find in-order successor (go right once, then left as far as possible)"))
S.append(sp())
S.append(code("""def remove(self, target):
    p_curr, curr = None, self.root
    while curr:
        if curr.value == target:
            break
        elif target < curr.value:
            p_curr, curr = curr, curr.left
        else:
            p_curr, curr = curr, curr.right
    if curr is None:
        raise ValueError("Target not found!")

    # CASE 3: Two children
    if curr.left and curr.right:
        p_succ = curr
        succ = curr.right
        while succ.left:
            p_succ, succ = succ, succ.left
        curr.value = succ.value
        if p_succ.left is succ:
            p_succ.left = succ.right
        else:
            p_succ.right = succ.right
    # CASES 1 & 2: 0 or 1 child
    else:
        child = curr.left or curr.right
        if p_curr is None:
            self.root = child
        elif p_curr.left is curr:
            p_curr.left = child
        else:
            p_curr.right = child"""))
S.append(sp())

S.append(Paragraph("7.8 BST Inventory Assignment", styles['CH']))
S.append(body("From the course case study. Manage products using BST."))
S.append(code("""# products.csv format: product_id,product_name,price
# 1001,Widget A,9.99
# Skip headers and empty lines

# Each BST node: key=product_id, value=(product_name, price)

# 1. Read CSV, insert into BST
# 2. search_by_id(id) -> return (name, price) or None
# 3. remove(id) -> handle 3 deletion cases
# 4. inorder_traversal() -> show products sorted by id
# 5. Answer: average-case O(log n), worst-case O(n)
# 6. Five most expensive? Traverse and keep top 5"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 8: GRAPHS
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 8 - GRAPHS", styles['PT']))
S.append(hr())
S.append(body("Final exam: Graphs = 10 points bonus (no coding)."))
S.append(PageBreak())

S.append(Paragraph("8.1 Graph Basics", styles['CH']))
S.append(body("A <b>graph</b> = nodes (vertices) connected by <b>edges</b>."))
S.append(body("Trees are a special type of graph (connected, no cycles)."))
S.append(sp())
S.append(code("""# Graph: A -- B
#        |    |
#        C -- D
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}"""))
S.append(sp())

S.append(Paragraph("8.2 BFS (Queue) - level by level", styles['CH']))
S.append(code("""from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for nb in graph[node]:
                if nb not in visited:
                    queue.append(nb)"""))
S.append(sp())

S.append(Paragraph("8.3 DFS (Stack/Recursion) - go deep first", styles['CH']))
S.append(code("""def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for nb in graph[start]:
        if nb not in visited:
            dfs(graph, nb, visited)"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 9: RECURSION
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 9 - RECURSION", styles['PT']))
S.append(hr())
S.append(body("A function that calls <b>itself</b>. Heavily used in trees and BSTs."))
S.append(PageBreak())

S.append(Paragraph("9.1 Every Recursive Function Has:", styles['CH']))
S.append(code("""def solve(problem):
    # 1. BASE CASE - when to STOP
    if problem is smallest:
        return answer
    # 2. RECURSIVE CASE - call with smaller problem
    return combine(problem, solve(smaller_problem))"""))
S.append(sp())

S.append(Paragraph("9.2 Factorial", styles['CH']))
S.append(code("""def factorial(n):
    if n <= 1: return 1  # BASE
    return n * factorial(n-1)  # RECURSIVE

# fact(4) = 4 * fact(3)
#        = 4 * 3 * fact(2)
#        = 4 * 3 * 2 * fact(1)
#        = 4 * 3 * 2 * 1 = 24"""))
S.append(sp())

S.append(Paragraph("9.3 Fibonacci", styles['CH']))
S.append(code("""def fib(n):
    if n <= 1: return n   # BASE
    return fib(n-1) + fib(n-2)  # RECURSIVE

# WARNING: fib(40) calls itself ~330 million times! O(2^n)

# ITERATIVE is much better:
def fib_iter(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b"""))
S.append(sp())

S.append(Paragraph("9.4 Recursion on Trees (template)", styles['CH']))
S.append(code("""def tree_func(root):
    if root is None:          # BASE
        return something
    left = tree_func(root.left)    # RECURSE
    right = tree_func(root.right)  # RECURSE
    return combine(root, left, right)

# Examples: height, sum nodes, search, count"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 10: ASSIGNMENTS
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 10 - ASSIGNMENTS", styles['PT']))
S.append(hr())
S.append(body("These are from the course emails and PDFs."))
S.append(PageBreak())

S.append(Paragraph("10.1 Student Data Linked List (svssvsdv.pdf)", styles['CH']))
S.append(body("File format: <b>id/name/age/gpa/major</b>"))
S.append(body("Example: <b>14752/Ghita/19/3.4/cs</b>"))
S.append(sp())
S.append(Paragraph("Q1: Append from file", styles['SH']))
S.append(code("""def append_from_file(ll, file_handler):
    for line in file_handler:
        parts = line.strip().split('/')
        if len(parts) >= 5:
            s = (int(parts[0]), parts[1], int(parts[2]),
                 float(parts[3]), parts[4])
            ll.append(s)
# File is ALREADY OPEN. Do NOT open it!"""))
S.append(sp())
S.append(Paragraph("Q2: Display (id, name)", styles['SH']))
S.append(code("""def display_students(ll):
    curr = ll.head
    while curr:
        s = curr.data
        print(f"({s[0]}, {s[1]})")
        curr = curr.next"""))
S.append(sp())
S.append(Paragraph("Q3: Remove by ID", styles['SH']))
S.append(code("""def remove_by_id(ll, target_id):
    curr, prev = ll.head, None
    while curr:
        if curr.data[0] == target_id:
            if prev is None:
                ll.head = curr.next
            else:
                prev.next = curr.next
            if curr == ll.tail:
                ll.tail = prev
            return True
        prev, curr = curr, curr.next
    return False"""))
S.append(sp())
S.append(Paragraph("Q4: Search by Major", styles['SH']))
S.append(code("""def search_by_major(ll, major):
    names = []
    curr = ll.head
    while curr:
        if curr.data[4] == major:
            names.append(curr.data[1])
        curr = curr.next
    return names"""))
S.append(sp())

S.append(Paragraph("10.2 Queues & Stacks Assignment", styles['CH']))
S.append(body("4 exercises from the assignment PDF:"))
S.append(code("""# Ex1: Reverse Queue Using Stack (see Part 6.5)
# Ex2: Filter Odd Numbers from Queue (see Part 6.6)
# Ex3: Merge Two Stacks Alternately (see Part 6.8)
# Ex4: Merge Two Sorted Queues (see Part 6.7)"""))
S.append(sp())

S.append(Paragraph("10.3 BST Inventory Assignment", styles['CH']))
S.append(body("Managing products with BST. Key details from the email:"))
S.append(code("""# Read products.csv
# product_id = BST key
# (product_name, price) = BST value
#
# Functions:
# - search_by_id(id)  -> (name, price) or None
# - remove(id)
# - inorder_traversal()
#
# Performance questions:
# - Avg case: O(log n)
# - Worst case: O(n) (skewed tree)
# - Fix: use AVL or Red-Black tree (self-balancing)
# - 5 most expensive: traverse and find top 5"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 11: PRACTICE PROBLEMS
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 11 - PRACTICE PROBLEMS", styles['PT']))
S.append(hr())
S.append(PageBreak())

S.append(Paragraph("11.1 BST Recursion Problems", styles['CH']))
S.append(sp())

S.append(Paragraph("Find level of a node:", styles['SH']))
S.append(code("""def find_level(root, target, level=1):
    if root is None: return -1
    if root.value == target: return level
    l = find_level(root.left, target, level+1)
    if l != -1: return l
    return find_level(root.right, target, level+1)"""))
S.append(sp())

S.append(Paragraph("Minimum depth:", styles['SH']))
S.append(code("""def min_depth(root):
    if root is None: return 0
    if not root.left: return 1 + min_depth(root.right)
    if not root.right: return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))"""))
S.append(sp())

S.append(Paragraph("Right view:", styles['SH']))
S.append(code("""def right_view(root):
    result = []
    def dfs(n, d):
        if not n: return
        if d == len(result): result.append(n.value)
        dfs(n.right, d+1)
        dfs(n.left, d+1)
    dfs(root, 0)
    return result"""))
S.append(sp())

S.append(Paragraph("Max path sum (root to leaf):", styles['SH']))
S.append(code("""def max_path_sum(root):
    if root is None: return float('-inf')
    if not root.left and not root.right: return root.value
    return root.value + max(max_path_sum(root.left), max_path_sum(root.right))"""))
S.append(sp())

S.append(Paragraph("Lowest Common Ancestor:", styles['SH']))
S.append(code("""def lca(root, p, q):
    if root is None: return None
    if root.value == p or root.value == q: return root.value
    L = lca(root.left, p, q)
    R = lca(root.right, p, q)
    if L and R: return root.value
    return L or R"""))
S.append(sp())

S.append(Paragraph("Symmetric tree check:", styles['SH']))
S.append(code("""def is_symmetric(root):
    def check(l, r):
        if not l and not r: return True
        if not l or not r: return False
        return (l.value == r.value and
                check(l.left, r.right) and
                check(l.right, r.left))
    return check(root.left, root.right) if root else True"""))
S.append(sp())

S.append(Paragraph("Sum of left leaves:", styles['SH']))
S.append(code("""def sum_left_leaves(root):
    def dfs(n, left):
        if not n: return 0
        if not n.left and not n.left and left:
            return n.value
        return dfs(n.left, True) + dfs(n.right, False)
    return dfs(root, False)"""))
S.append(sp())

S.append(Paragraph("Identical trees:", styles['SH']))
S.append(code("""def is_identical(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    return (t1.value == t2.value and
            is_identical(t1.left, t2.left) and
            is_identical(t1.right, t2.right))"""))
S.append(sp())

S.append(Paragraph("11.2 Python Practice", styles['CH']))
S.append(sp())

S.append(Paragraph("Rotate list right by k:", styles['SH']))
S.append(code("""def rotate(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

# [1,2,3,4,5], k=2 -> [4,5,1,2,3]"""))
S.append(sp())

S.append(Paragraph("Remove duplicates (maintain order):", styles['SH']))
S.append(code("""def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

# [1,2,2,3,4,4,5] -> [1,2,3,4,5]"""))
S.append(sp())

S.append(Paragraph("Count frequencies with dict:", styles['SH']))
S.append(code("""def count_freq(nums):
    counts = {}
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    return counts

# [2,2,4,5,4,4,5,7] -> {2:2, 4:3, 5:2, 7:1}"""))
S.append(sp())

S.append(Paragraph("Max product pair:", styles['SH']))
S.append(code("""def max_product_pair(t):
    s = sorted(t)
    a, b = s[-2], s[-1]
    c, d = s[0], s[1]
    return (a, b) if a*b > c*d else (c, d)

# (1, 10, 3, 7, -5, 6) -> (10, 7)"""))
S.append(sp())

S.append(Paragraph("Check magic square:", styles['SH']))
S.append(code("""def is_magic(m):
    n = len(m)
    t = sum(m[0])
    if any(sum(r) != t for r in m): return False
    if any(sum(m[i][j] for i in range(n)) != t for j in range(n)): return False
    if sum(m[i][i] for i in range(n)) != t: return False
    if sum(m[i][n-1-i] for i in range(n)) != t: return False
    return True"""))
S.append(PageBreak())

# ══════════════════════════════════════════════════════════
# PART 12: QUICK REFERENCE
# ══════════════════════════════════════════════════════════
S.append(Paragraph("PART 12 - QUICK REFERENCE", styles['PT']))
S.append(hr())
S.append(PageBreak())

S.append(Paragraph("Big O Cheat Sheet", styles['CH']))
S.append(code("""O(1)      array[i], push/pop, peek
O(log n)  binary search, BST balanced
O(n)      loop, linear search
O(n log n) merge sort, quick sort
O(n^2)    bubble sort, nested loops"""))
S.append(sp())

S.append(Paragraph("Stack vs Queue", styles['CH']))
S.append(code("""STACK (LIFO)          QUEUE (FIFO)
push(value)           enqueue(value)
pop()                 dequeue()
peek()                front()
plate stack           waiting line
bracket check         airport security"""))
S.append(sp())

S.append(Paragraph("BST Complexity", styles['CH']))
S.append(code("""Operation      Average    Worst (skewed)
Search         O(log n)   O(n)
Insert         O(log n)   O(n)
Delete         O(log n)   O(n)
Inorder        O(n)       O(n)"""))
S.append(sp())

S.append(Paragraph("Common Exam Mistakes", styles['CH']))
S.append(mistake("Using = instead of == in if"))
S.append(mistake("Forgetting to close files (use 'with')"))
S.append(mistake("Off-by-one (range(n) = 0 to n-1)"))
S.append(mistake("Modifying list while iterating"))
S.append(mistake("No base case in recursion"))
S.append(mistake("Opening a file that is already open"))
S.append(mistake("Creating object already passed as parameter"))
S.append(mistake("Using self in regular function"))
S.append(mistake("Forgetting to update tail in linked list"))
S.append(mistake("Forgetting empty case (list/stack/queue)"))
S.append(sp())

S.append(Paragraph("How to Start Any Coding Problem", styles['CH']))
S.append(body("1. Read twice: what am I GIVEN? what must I RETURN?"))
S.append(body("2. Try small example by hand"))
S.append(body("3. What SHAPE? (search? sort? traverse? count?)"))
S.append(body("4. Pick the data structure"))
S.append(body("5. Write steps in plain English"))
S.append(body("6. Code one step at a time"))
S.append(body("7. Check edge cases: empty, one item, all same"))
S.append(sp())

S.append(Paragraph("Exam Day Checklist", styles['CH']))
S.append(body("- Two pencils + eraser"))
S.append(body("- AUI ID on desk"))
S.append(body("- Phone OFF in bag"))
S.append(body("- Read instructions carefully"))
S.append(body("- Descriptive names (gpa, not x)"))
S.append(body("- Use scratch paper first"))
S.append(body("- Put exam inside scratch paper before submitting"))

S.append(Spacer(1,25*mm))
S.append(hr())
S.append(Paragraph("END OF GUIDE - Good luck on your exams!",
    ParagraphStyle('EN', parent=styles['BD'], alignment=TA_CENTER, textColor=HexColor('#757575'))))
S.append(Paragraph("Al Akhawayn University in Ifrane - School of Science and Engineering",
    ParagraphStyle('EN2', parent=styles['BD'], alignment=TA_CENTER, textColor=HexColor('#757575'))))
S.append(Paragraph("Based on the CSC2302 course materials",
    ParagraphStyle('EN3', parent=styles['BD'], alignment=TA_CENTER, textColor=HexColor('#757575'))))

# ══════════════════════════════════════════════════════════
doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=18*mm, bottomMargin=18*mm)
doc.build(S)
print(f"OK PDF generated: {OUTPUT}")
