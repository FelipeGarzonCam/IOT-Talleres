import tkinter as tk
import math
import time

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

class LineFollowerCar:
    def __init__(self, canvas, center, radius, start_angle=0):
        self.canvas = canvas
        self.cx, self.cy = center
        self.radius = radius
        # Initial position on circle
        self.car_angle = start_angle  # degrees
        rad = math.radians(self.car_angle)
        self.car_x = self.cx + self.radius * math.cos(rad)
        self.car_y = self.cy + self.radius * math.sin(rad)
        self.speed = 4  # movement per frame
        self.pid = PIDController(2.0, 0.001, 0.5)
        self.last_time = time.time()
        # Draw car parts
        self.body = self.canvas.create_polygon([0,0, 40,0, 40,20, 0,20], fill='#2E86C1', outline='#1B4F72')
        self.update_car()

    def update_car(self):
        a = math.radians(self.car_angle)
        cos_a, sin_a = math.cos(a), math.sin(a)
        coords = [
            self.car_x + 20*cos_a - 10*sin_a,
            self.car_y + 20*sin_a + 10*cos_a,
            self.car_x + 20*cos_a + 10*sin_a,
            self.car_y + 20*sin_a - 10*cos_a,
            self.car_x - 20*cos_a + 10*sin_a,
            self.car_y - 20*sin_a - 10*cos_a,
            self.car_x - 20*cos_a - 10*sin_a,
            self.car_y - 20*sin_a + 10*cos_a
        ]
        self.canvas.coords(self.body, *coords)

    def move(self):
        now = time.time()
        dt = now - self.last_time
        self.last_time = now
        # Compute radial error
        dx = self.car_x - self.cx
        dy = self.car_y - self.cy
        dist = math.hypot(dx, dy)
        error = dist - self.radius
        # PID correction
        correction = self.pid.compute(error, dt)
        # Move along tangent: increment angle (CCW) and apply correction
        # Tangent direction: car_angle + 90 deg
        self.car_angle += (self.speed / self.radius) * (180/math.pi) - correction
        # Update position
        rad = math.radians(self.car_angle)
        self.car_x = self.cx + self.radius * math.cos(rad)
        self.car_y = self.cy + self.radius * math.sin(rad)
        self.update_car()

# Setup window
root = tk.Tk()
root.title("Carro en Pista Circular - Control Analítico")
canvas = tk.Canvas(root, width=800, height=600, bg='#ECF0F1')
canvas.pack()

# Track: anillo definido por dos círculos concéntricos
cx, cy = 400, 300
r_outer = 200
r_inner = 150
# Dibujar anillo en canvas
n = 100
outer_pts = [(cx + r_outer*math.cos(2*math.pi*i/n), cy + r_outer*math.sin(2*math.pi*i/n)) for i in range(n+1)]
inner_pts = [(cx + r_inner*math.cos(2*math.pi*i/n), cy + r_inner*math.sin(2*math.pi*i/n)) for i in range(n+1)][::-1]
pts = outer_pts + inner_pts
flat = [c for p in pts for c in p]
canvas.create_polygon(*flat, fill='#7F8C8D', outline='#2C3E50', width=2)

# Initialize car on top of circle (angle -90 deg)
car = LineFollowerCar(canvas, (cx, cy), (r_outer+r_inner)/2, start_angle=-90)

def loop():
    car.move()
    # trail
    canvas.create_oval(car.car_x-1, car.car_y-1, car.car_x+1, car.car_y+1, fill='#F1C40F', outline='')
    root.after(30, loop)

loop()
root.mainloop()