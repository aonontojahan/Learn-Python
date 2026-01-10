# Explicit Type Conversion Example

# Integer to Float
a = 10
b = float(a)
print("Integer to Float:", b)

# Float to Integer
c = 12.7
d = int(c)
print("Float to Integer:", d)

# Integer to String
e = 100
f = str(e)
print("Integer to String:", f)

# String to Integer
g = "25"
h = int(g)
print("String to Integer:", h)

# Implicit Type Conversion
x = 5      # int
y = 2.5    # float
z = x + y
print("Implicit Conversion Result:", z)
print("Type of z:", type(z))