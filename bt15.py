import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import dblquad

# Độ dài cạnh tam giác
a = 1  # Có thể thay đổi giá trị này

# Hàm mật độ: tỉ lệ với bình phương khoảng cách tới gốc tọa độ (đỉnh đối diện với cạnh huyền)
def density(x, y):
    return x**2 + y**2

# Miền tam giác vuông cân: x từ 0 đến a, y từ 0 đến a - x
def y_lower(x): return 0
def y_upper(x): return a - x

# Tính khối lượng m
m, _ = dblquad(lambda y, x: density(x, y), 0, a, y_lower, y_upper)

# Tính x̄ = (1/m) ∬ x * ρ(x,y) dA
x_bar_numerator, _ = dblquad(lambda y, x: x * density(x, y), 0, a, y_lower, y_upper)
x_bar = x_bar_numerator / m

# Tính ȳ = (1/m) ∬ y * ρ(x,y) dA
y_bar_numerator, _ = dblquad(lambda y, x: y * density(x, y), 0, a, y_lower, y_upper)
y_bar = y_bar_numerator / m
print(f"Tâm khối của tấm mỏng là ({x_bar:.5f}, {y_bar:.5f})")

# Vẽ hình tam giác
plt.figure(figsize=(6, 6))
x_vals = np.array([0, a, 0])
y_vals = np.array([0, 0, a])
plt.fill(x_vals, y_vals, 'skyblue', edgecolor='black', alpha=0.5)

# Vẽ tâm khối
plt.plot(x_bar, y_bar, 'ro', label=f"Tâm khối ({x_bar:.3f}, {y_bar:.3f})")
plt.text(x_bar + 0.02, y_bar, 'Center of Mass', color='red')

# Đánh dấu các đỉnh tam giác
plt.plot([0, a, 0], [0, 0, a], 'ko')  # Các đỉnh O, A, B
plt.text(0, 0, 'O(0,0)', fontsize=10, verticalalignment='top', horizontalalignment='right')
plt.text(a, 0, f'A({a},0)', fontsize=10, verticalalignment='top', horizontalalignment='left')
plt.text(0, a, f'B(0,{a})', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

# Cài đặt đồ họa
plt.xlim(-0.1, a + 0.1)
plt.ylim(-0.1, a + 0.1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Tấm mỏng hình tam giác vuông cân và tâm khối')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# In ra tọa độ tâm khối
(x_bar, y_bar)
