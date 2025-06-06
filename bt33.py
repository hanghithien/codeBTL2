import numpy as np

# Cấu hình thành phố
R = 10   # bán kính thành phố
k = 1    # mật độ người nhiễm trên mỗi dặm vuông (có thể chỉnh)

# Độ phân giải lưới tích phân
N = 1000
x = np.linspace(-R, R, N)
y = np.linspace(-R, R, N)
dx = dy = (2 * R) / N

X, Y = np.meshgrid(x, y)
mask = X**2 + Y**2 <= R**2  # chỉ lấy phần nằm trong hình tròn

# Hàm khoảng cách đến điểm A(x0, y0)
def exposure_at(x0, y0):
    D = np.sqrt((X - x0)**2 + (Y - y0)**2)
    f = 1 - D / 20
    f = np.clip(f, 0, None)  # vì f không thể âm
    total_exposure = k * np.sum(f[mask]) * dx * dy
    return total_exposure

# Tính mức độ phơi nhiễm tại tâm và rìa
center_exposure = exposure_at(0, 0)
edge_exposure = exposure_at(10, 0)

print(f"Mức độ phơi nhiễm tại tâm thành phố: {center_exposure:.4f}")
print(f"Mức độ phơi nhiễm tại rìa thành phố: {edge_exposure:.4f}")

if center_exposure > edge_exposure:
    print("→ Sống ở rìa thành phố an toàn hơn.")
else:
    print("→ Sống ở tâm thành phố an toàn hơn.")
