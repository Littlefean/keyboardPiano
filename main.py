import os
import threading

import keyboard
import pygame

from settings import SETTINGS

pygame.mixer.init()

sound_cache = {}
# 记录每个按键是否是按下的状态
is_key_press = {}
lock = threading.Lock()


def load_sound(file_name: str):
    path = f'sound/wav/{file_name}.wav'
    if not os.path.exists(path):
        print(f"Error: File '{path}' not found.")
        return None
    if file_name not in sound_cache:
        path = f'sound/wav/{file_name}.wav'
        sound_cache[file_name] = pygame.mixer.Sound(path)
    return sound_cache[file_name]


def play_sound(file_name: str):
    sound = load_sound(file_name)
    sound.play()


def on_key_press(event):
    key = event.name
    print(key, event.event_type)

    if event.event_type == keyboard.KEY_UP:
        # 将一个键设置为松开的状态
        is_key_press[key] = False
        ...
    if key in SETTINGS and event.event_type == keyboard.KEY_DOWN and not is_key_press.get(key):
        is_key_press[key] = True
        with lock:
            play_sound(SETTINGS[key])


# 监听按键按下事件
keyboard.hook(on_key_press)

# 保持程序运行
keyboard.wait('esc')  # 等待按下ESC键退出程序
