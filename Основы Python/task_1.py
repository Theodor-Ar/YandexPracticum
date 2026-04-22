def get_rectangle_area(length, width):
    return length * width


def get_rectangle_perimeter(length, width):
    return 2 * (length + width)

# Длина прямоугольника.
length = 5
# Ширина прямоугольника.
width = 10

area = get_rectangle_area(length, width)
perimeter = get_rectangle_perimeter(length, width)

print(f"Площадь: {area}")
print(f"Периметр: {perimeter}")