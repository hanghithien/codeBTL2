import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Định nghĩa hàm mật độ điện tích sigma(y,x)
def sigma(y, x):
    return 2*x*y + y**2

# Giới hạn miền
x_lower, x_upper = 1, 3
y_lower = lambda x: 0
y_upper = lambda x: 2

# Tính tích phân kép (tổng điện tích)
Q, error = integrate.dblquad(sigma, x_lower, x_upper, y_lower, y_upper)

print(f"Tổng điện tích tính bằng số: {Q:.6f} C")


# Kết quả tính tay để so sánh
Q_analytic = 64/3
print(f"Kết quả tính tay: {Q_analytic:.6f} C")


# Vẽ mật độ điện tích trên miền
x = np.linspace(1, 3, 100)
y = np.linspace(0, 2, 100)
X, Y = np.meshgrid(x, y)
sigma_vals = 2*X*Y + Y**2

plt.figure(figsize=(8,5))
contour = plt.contourf(X, Y, sigma_vals, cmap='viridis')
plt.colorbar(contour, label='Mật độ điện tích $\sigma(x,y)$ (C/m²)')

# Mở rộng trục để dễ quan sát hơn
plt.xlim(0, 3.5)
plt.ylim(0, 2.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Mật độ điện tích trên hình chữ nhật $1 \leq x \leq 3$, $0 \leq y \leq 2$')
plt.show()
