import sympy as sp

# Khai báo biến
x, y = sp.symbols('x y')

# Định nghĩa miền và mật độ
y_max = sp.sin(x)
rho = x * y  # Mật độ

# === 1. Tính khối lượng M ===
M = sp.integrate(sp.integrate(rho, (y, 0, y_max)), (x, 0, sp.pi))
print("Khối lượng M =", M.simplify())

# === 2. Tọa độ tâm khối lượng ===

# Hoành độ trọng tâm (x̄)
x_bar_integrand = x * rho
x_bar = sp.integrate(sp.integrate(x_bar_integrand, (y, 0, y_max)), (x, 0, sp.pi)) / M
print("x̄ =", x_bar.simplify())

# Tung độ trọng tâm (ȳ)
y_bar_integrand = y * rho
y_bar = sp.integrate(sp.integrate(y_bar_integrand, (y, 0, y_max)), (x, 0, sp.pi)) / M
print("ȳ =", y_bar.simplify())

# === 3. Mômen quán tính ===

# Ix = ∫∫ y² * ρ(x,y) dA
Ix_integrand = y**2 * rho
Ix = sp.integrate(sp.integrate(Ix_integrand, (y, 0, y_max)), (x, 0, sp.pi))
print("Moment Ix =", Ix.simplify())

# Iy = ∫∫ x² * ρ(x,y) dA
Iy_integrand = x**2 * rho
Iy = sp.integrate(sp.integrate(Iy_integrand, (y, 0, y_max)), (x, 0, sp.pi))
print("Moment Iy =", Iy.simplify())
