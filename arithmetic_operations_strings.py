# 📘 Arithmetic Operations & String Manipulation in Python

## 🔢 Arithmetic Operators
```python
# Basic Arithmetic
9 + 9 - 10 * 3 - 3  # Result: -15

# Explanation:
# Operands: 9, 9, 10, 3, 3
# Operators: +, -, *
```

```python
# Multiplication
7 * 7  # 49

# Power
7 ** 7  # 823543

# ❌ Incorrect operator syntax
# 7***7  # SyntaxError
```

```python
# Float Division
10 / 4  # 2.5

# Integer Division
10 // 4  # 2

# Modulus (Remainder)
10 % 5  # 0

# ❌ Incorrect operator syntax
# 10%%5  # SyntaxError
```

## 🎯 Assignment Operators
```python
x = 10  # x is a variable (identifier), 10 is a value

# Incremental assignment
x += 2  # x = x + 2 → x becomes 12
x += 2  # x = x + 2 → x becomes 14

# Decremental assignment
x -= 2  # x = x - 2 → x becomes 12

# Multiply and assign
x *= 2  # x = x * 2 → x becomes 24
x * 2   # Only performs the operation (48)

# Divide and assign
x /= 2  # x becomes 12.0
```

## ➕ Unary Operators
```python
n = 7
m = -n  # Unary minus operator
print(m)  # -7
```

## 🔤 Strings in Python
```python
s = "nareshit"
print(s)  # 'nareshit'
print(len(s))  # 8
```

## 🧩 Indexing and Slicing
```python
s[5]     # 'h'
s[7]     # 't'
s[0:5]   # 'nares'
s[::1]   # 'nareshit'
s[::-1]  # 'tihseran'  (reverse string)
s[-1]    # 't'
```

## 🔁 Looping Through a String
```python
for i in s:
    print(i)
```

## 📦 Multiple Variable Assignment from String
```python
language = "python"
a, b, c, d, e, f = language
print(a, b, c, d, e, f)  # p y t h o n
```

```python
for i in language:
    print(i)
```

## 📄 Multi-line Strings
```python
print('''I am studying in 
Naresh IT 
with Prakash Senapathi sir''')
```

## 🔣 Escape Characters
```python
print('I hope everyone is enjoying the Python challenge.\nDo you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
```

## 🔗 String Concatenation
```python
first_name = 'Pratik'
last_name = 'Sadewad'
full_name = first_name + ' ' + last_name
print(full_name)  # 'Pratik Sadewad'
```

## 🧪 String Methods
```python
challenge = 'thirty days of python'

print(challenge.capitalize())  # 'Thirty days of python'
print(challenge.title())       # 'Thirty Days Of Python'
print(challenge.count('y'))    # 3
tprint(challenge.count('d'))   # 1
print(challenge.isalnum())     # False (because of spaces)

challenge = 'thirtydaysofpython'
print(challenge.isalnum())     # True

challenge = 'thirty'
print(challenge.isdigit())     # False
```

## 🧵 Joining and Splitting
```python
name = ['pratik', 'prakash', 'sadewad']
result = '@ '.join(name)
print(result)  # 'pratik@ prakash@ sadewad'

challenge = ' thirty days of python '
print(challenge.replace('python', 'coding'))  # ' thirty days of coding '
print(challenge.split())  # ['thirty', 'days', 'of', 'python']

name = "pratik prakash sadewad"
print(name.split())
```

## 🧠 Practice Exercises
```python
# 1. Reverse the string "Python is fun"
print("Python is fun"[::-1])

# 2. Count 'a' in "banana"
print("banana".count('a'))

# 3. Create full name from parts
first = "Alan"
last = "Turing"
print(first + ' ' + last)
