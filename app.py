import uvicorn
import math
from fastapi import FastAPI
app = FastAPI()

x = 0.0
y = 0.0
angle = 0.0  

def move_robot(distance: float, angle_offset: float = 0.0):
    global x, y
    ti = math.radians(angle + angle_offset)
    x += distance * math.cos(ti)
    y += distance * math.sin(ti)
    return {"x": round(x, 2), "y": round(y, 2), "current_angle": angle}

@app.get("/")
def home():
    return {
        "message": "Робот на тригонометрическом управлении готов.",
        "commands": [
            "/position — узнать расположение и текущий угол",
            "/turn?degrees=90 — повернуться на заданный угол",
            "/forward?steps=5 — идти вперед под текущим углом",
            "/back?steps=5 — идти назад под текущим углом",
        ],
    }

@app.get("/position")
def get_position():
    return {"x": round(x, 2), "y": round(y, 2), "angle": angle}

@app.get("/turn")
def turn_robot(degrees: float):
    global angle
    angle = (angle + degrees) % 360 
    return {
        "message": f"Робот повернулся на {degrees}°",
        "x": round(x, 2),
        "y": round(y, 2),
        "current_angle": angle,
    }

@app.get("/forward")
def move_forward(steps: float = 1.0):
    return move_robot(steps, angle_offset=0.0)

@app.get("/back")
def move_backward(steps: float = 1.0):
    return move_robot(steps, angle_offset=180.0)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=50345, reload=True)
