"""
Crie um programa que commita o projeto de vocês e envia o repositório para o github
"""

import pyautogui as auto

auto.PAUSE = 2

auto.hotkey("ctrl", "'")
auto.write("git status ")
auto.press("enter")
auto.write("git add . ")
auto.press("enter")
auto.write("git status ")
auto.press("enter")
auto.write("git commit -m 'terminando de aprender funções e iniciando automação, inclusive subindo o projeto com programa criado com tal finalidade'")
auto.press("enter")
auto.write("git push ")
auto.press("enter")