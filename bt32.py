import sympy as sp

# Khai báo biến
x, y = sp.symbols('x y')

# Hàm mật độ xác suất
f1 = sp.exp(-x)             # Xavier: mũ trên (0, ∞)
f2 = 1/50                   # Yolanda: đều trên [0, 10]

# Mật độ chung: f(x, y) = f1(x) * f2(y)
joint_density = f1 * f2

# Miền tích phân: 0 <= y <= 10, y <= x <= y+30
inner_integral = sp.integrate(joint_density, (x, y, y + 30))
outer_integral = sp.integrate(inner_integral, (y, 0, 10))

# Kết quả chính xác và gần đúng
print("Xác suất gặp nhau (dạng chính xác):", outer_integral.simplify())
print("Xác suất gặp nhau (gần đúng):", outer_integral.evalf())
