def calcular_area_y_perimetro(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

a, p = calcular_area_y_perimetro(10, 5)

print(a)
print(p)