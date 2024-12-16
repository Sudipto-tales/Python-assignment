a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

print(f"The quadratic expression is: {a}x^2 + {b}x + {c}")

d = pow(b, 2) - (4 * a * c)

if d > 0:
    root1 = (-b + pow(d, 0.5)) / (2 * a)
    root2 = (-b - pow(d, 0.5)) / (2 * a)
    print(f"The roots are real and distinct: {root1} and {root2}")
elif d == 0:
    root = -b / (2 * a)
    print(f"The root is real and equal: {root}")
else:
    img_root1 = -b / (2 * a)
    img_root2 = pow(abs(d), 0.5) / (2 * a)
    print(f"The roots are complex: {img_root1} + {img_root2}i and {img_root1} - {img_root2}i")
