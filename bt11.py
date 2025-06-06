import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Khai báo biến
r, theta = sp.symbols('r theta')

# Hàm mật độ: rho = y = r * sin(theta)
rho = r * sp.sin(theta)

# Vi phân diện tích trong tọa độ cực: r * dr * dθ
dA = r

# Giới hạn tích phân: r từ 0 đến 1, theta từ 0 đến π/2
# --- Khối lượng ---
mass = sp.integrate(sp.integrate(rho * dA, (r, 0, 1)), (theta, 0, sp.pi/2))

# --- Tọa độ x̄ ---
x_bar = sp.integrate(sp.integrate((r * sp.cos(theta)) * rho * dA, (r, 0, 1)), (theta, 0, sp.pi/2)) / mass

# --- Tọa độ ȳ ---
y_bar = sp.integrate(sp.integrate((r * sp.sin(theta)) * rho * dA, (r, 0, 1)), (theta, 0, sp.pi/2)) / mass

# Kết quả
print(f"Khối lượng M = {mass.evalf()}")
print(f"Tâm khối lượng: x̄ = {x_bar.evalf()}, ȳ = {y_bar.evalf()}")

# --- Vẽ hình và tâm khối ---
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Vẽ phần tư đĩa
theta_vals = np.linspace(0, np.pi/2, 300)
r_vals = np.ones_like(theta_vals)
x_vals = r_vals * np.cos(theta_vals)
y_vals = r_vals * np.sin(theta_vals)

# Miền: góc phần tư đĩa
ax.fill(np.append([0], x_vals), np.append([0], y_vals), color='lightblue', label='Miền D')

# Vẽ tâm khối lượng
ax.plot(float(x_bar), float(y_bar), 'ro', label='Tâm khối lượng')
ax.text(float(x_bar)+0.02, float(y_bar), f"({x_bar.evalf():.3f}, {y_bar.evalf():.3f})", color='red')

# Trục và thiết lập
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Góc phần tư đĩa và Tâm khối lượng')
ax.legend()
plt.grid(True)
plt.show()
