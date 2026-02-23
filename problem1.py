import numpy as np

# Kidney equation: (x^2 + y^2)^2 = x^3 + y^3
# Removed disc: (x - 0.25)^2 + (y - 0.25)^2 = 0.125

# these functions are helpers with determining the regions
def inside_kidney(x, y):
    return (x**2 + y**2)**2 <= x**3 + y**3

def inside_disc(x, y):
    return (x - 0.25)**2 + (y - 0.25)**2 <= 0.125

def integrand(x, y):
    # 1 if inside kidney AND not inside disc
    return inside_kidney(x, y) and not inside_disc(x, y)




# bounding box (covers entire kidney)
xmin, xmax = -0.5, 1.5
ymin, ymax = -0.5, 1.5

# (1) (20 pts) Rectangle method (left, right, or midpoint; specify which).
print("Rectangle Method. \nUsing the midpoint method.")

# delta x * [f(x_1^*) + ... + f(x_n^*)]
# need to go above and below the x axis
def rectangle_method(n):
    dx = (xmax - xmin) / n
    dy = (ymax - ymin) / n
    area = 0.0
    
    for i in range(n):
        for j in range(n):
            x = xmin + (i + 0.5) * dx
            y = ymin + (j + 0.5) * dy
            if integrand(x, y):
                area += dx * dy
                
    return area

n_rect = 1000 # 1000 subintervals
area_rect = rectangle_method(n_rect)
print("Rectangle (midpoint) area:", area_rect)


# (2) (20 pts) Trapezoidal method.
print("Trapezoioal Method")

# (f(a) + f(b)) / 2 (b-a)
# (delta x)/2 [f(x_0) + 2f(x_1) + ... + 2f(x_{n-1}) + f(x_n)]

def trapezoidal_method(n):
    dx = (xmax - xmin) / n
    dy = (ymax - ymin) / n
    area = 0.0
    
    for i in range(n + 1):
        for j in range(n + 1):
            x = xmin + i * dx
            y = ymin + j * dy
            
            weight = 1
            if i == 0 or i == n: # at the first or last term
                weight *= 0.5
            if j == 0 or j == n:
                weight *= 0.5
                
            if integrand(x, y):
                area += weight
    
    return area * dx * dy

n_trap = 1000
area_trap = trapezoidal_method(n_trap)
print("Trapezoidal area:", area_trap)


# (3) (10 pts) Monte Carlo method (note: this may run significantly slower than the first two).
print("Monte Carlo Method")
# 2000000 samples

def monte_carlo(num_samples):
    np.random.seed(2) # for consistency
    xs = np.random.uniform(xmin, xmax, num_samples)
    ys = np.random.uniform(ymin, ymax, num_samples)
    
    count = 0
    for x, y in zip(xs, ys):
        if integrand(x, y):
            count += 1
            
    box_area = (xmax - xmin) * (ymax - ymin)
    return box_area * count / num_samples

samples = 2_000_000
area_mc = monte_carlo(samples)
print("Monte Carlo area:", area_mc)


