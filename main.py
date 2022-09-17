import Level
import keyboard

for i in range(1, 24):
    level = Level.Level(i)
    keyboard.play(level, i)
