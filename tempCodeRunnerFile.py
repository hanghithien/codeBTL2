import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 3, 100)
y = np.linspace(0, 2, 100)
X, Y = np.meshgrid(x, y)

sigma = 2 * X * Y + Y**2

plt.figure(figsize=(8,5))
contour = plt.contourf(X, Y, sigma, cmap='viridis')
plt.colorbar(contour, label='Mật độ điện tích $\sigma(x,y)$ (C/m²)')

# Mở rộng trục
plt.xlim(0, 3.5)  # rộng hơn từ 0.5 đến 3.5 thay vì 1 đến 3
plt.ylim(0, 2.5) # rộng hơn từ -0.5 đến 2.5 thay vì 0 đến 2

plt.xlabel('x')
plt.ylabel('y')
plt.title('Mật độ điện tích trên hình chữ nhật $1 \leq x \leq 3$, $0 \leq y \leq 2$')
plt.show()