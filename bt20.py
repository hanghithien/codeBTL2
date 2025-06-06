import sympy as sp

# Khai báo biến
x, y = sp.symbols('x y')
rho = 1 + 0.1 * x

# Giới hạn tích phân
x_limits = (x, 0, 2)
y_limits = (y, 0, 2)

# Mômen quán tính quanh trục x và y
I_x_expr = rho * y**2
I_y_expr = rho * x**2

# Tích phân kép
I_x = sp.integrate(sp.integrate(I_x_expr, x_limits), y_limits)
I_y = sp.integrate(sp.integrate(I_y_expr, x_limits), y_limits)

# So sánh và in kết quả
print(f"I_x = {I_x}")
print(f"I_y = {I_y}")

if I_x > I_y:
    print("Quay quanh trục x khó hơn.")
elif I_x < I_y:
    print("Quay quanh trục y khó hơn.")
else:
    print("Hai trục quay đều khó như nhau.")
