import sympy as sp
import matplotlib.pyplot as plt

# Biến
x, y = sp.symbols('x y')

# Mật độ
rho = x + y

# Giới hạn miền: x từ 0 đến 2, y từ 0.5x đến 3 - x
y_lower = 0.5 * x
y_upper = 3 - x

# Khối lượng
mass = sp.integrate(sp.integrate(rho, (y, y_lower, y_upper)), (x, 0, 2))

# Tâm khối lượng
x_bar = sp.integrate(sp.integrate(x * rho, (y, y_lower, y_upper)), (x, 0, 2)) / mass
y_bar = sp.integrate(sp.integrate(y * rho, (y, y_lower, y_upper)), (x, 0, 2)) / mass

# In kết quả
print(f"Khối lượng M = {mass}")
print(f"Tâm khối lượng: x̄ = {x_bar}, ȳ = {y_bar}")

# --- Vẽ miền tam giác và tâm khối ---
fig, ax = plt.subplots()

# Tọa độ các đỉnh tam giác
vertices = [(0, 0), (2, 1), (0, 3)]
polygon = plt.Polygon(vertices, closed=True, facecolor='lightblue', edgecolor='blue', alpha=0.5)
ax.add_patch(polygon)

# Vẽ tâm khối lượng
ax.plot(float(x_bar), float(y_bar), 'ro', label='Tâm khối lượng')
ax.text(float(x_bar) + 0.1, float(y_bar), f'({x_bar:.2f}, {y_bar:.2f})', color='red')

# Cài đặt trục
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 3.5)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Tam giác và Tâm khối lượng')
ax.legend()
plt.grid(True)
plt.show()
