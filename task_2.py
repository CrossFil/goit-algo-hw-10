import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло
num_samples = 10000
samples = np.random.uniform(a, b, num_samples)
sample_values = f(samples)
monte_carlo_integral = (b - a) * np.mean(sample_values)

# Аналітичний розрахунок інтегралу
analytical_integral = (b ** 3) / 3 - (a ** 3) / 3

# Використання функції quad для перевірки результату
quad_integral, _ = quad(f, a, b)

print(f"Monte Carlo Integral: {monte_carlo_integral}")
print(f"Analytical Integral: {analytical_integral}")
print(f"Quad Integral: {quad_integral}")
