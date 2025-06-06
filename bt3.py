import sympy as sp
import matplotlib.pyplot as plt

# Khai báo biến
x, y = sp.symbols('x y')

# Hàm mật độ
rho = x * y**2

# Tính khối lượng
mass = sp.integrate(sp.integrate(rho, (y, -1, 1)), (x, 0, 2))

# Tính tọa độ tâm khối lượng
x_bar = sp.integrate(sp.integrate(x * rho, (y, -1, 1)), (x, 0, 2)) / mass
y_bar = sp.integrate(sp.integrate(y * rho, (y, -1, 1)), (x, 0, 2)) / mass

print(f"Khối lượng M = {mass}")
print(f"Tâm khối lượng: x̄ = {x_bar}, ȳ = {y_bar}")

# Vẽ miền D và tâm khối lượng
fig, ax = plt.subplots()
# Vẽ hình chữ nhật D
rectangle = plt.Rectangle((0, -1), 2, 2, edgecolor='blue', facecolor='lightblue', alpha=0.5)
ax.add_patch(rectangle)

# Vẽ tâm khối lượng
ax.plot(float(x_bar), float(y_bar), 'ro', label='Tâm khối lượng')
ax.text(float(x_bar) + 0.1, float(y_bar), f'({x_bar}, {y_bar})', color='red')

# Thiết lập trục
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Miền D và Tâm khối lượng')
ax.legend()
plt.grid(True)
plt.show()
