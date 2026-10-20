import uvicorn
import random
from fastapi import FastAPI, Request

app = FastAPI()

# Начальные координаты робота
x = 0
y = 0

@app.get("/")
def home():
    return {"message": "Управление роботом готово. Доступные команды: /position, /up, /down, /left, /right"}

# 1. Узнать расположение
@app.get("/position")
def get_position():
    return {"x": x, "y": y}

# 2. Вверх (увеличиваем y)
@app.get("/up")
def move_up():
    global y
    y += 1
    return {"message": "Робот сдвинулся вверх", "x": x, "y": y}

# 3. Вниз (уменьшаем y)
@app.get("/down")
def move_down():
    global y
    y -= 1
    return {"message": "Робот сдвинулся вниз", "x": x, "y": y}

# 4. Влево (уменьшаем x)
@app.get("/left")
def move_left():
    global x
    x -= 1
    return {"message": "Робот сдвинулся влево", "x": x, "y": y}

# 5. Вправо (увеличиваем x)
@app.get("/right")
def move_right():
    global x
    x += 1
    return {"message": "Робот сдвинулся вправо", "x": x, "y": y}

if __name__ == "__main__":
    # ВАЖНО: для Docker host должен быть "0.0.0.0". 
    # Порт 50345 прокидывается внутри Dockerfile и команды запуска.
    uvicorn.run("app:app", host="0.0.0.0", port=50345, reload=True)
