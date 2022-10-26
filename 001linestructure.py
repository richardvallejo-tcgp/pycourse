# Physical lines in Python are terminated by a new-line character (a simple return) unlike languages such as JavaScript
# Below are three logical lines across four physical lines
x0 = 1
y0 = 1

z0 = 1
# Here are the same three logical lines on a single physical line
x1 = 1 ; y1 = 1 ; z1 = 1
# Here is one logical line written on a single physical line
b0 = 1 + 2
# This is the same single logical line written on two physical lines
b1 = 1 \
+ 2

print('Single Lines')
print(x0)
print(y0)
print(z0)
print('Multiple Logical Lines')
print(x1) ; print(y1) ; print(z1)
print('Single Line')
print(b0)
print('Multiple Physical Lines')
print(b1)
