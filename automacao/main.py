import pyautogui as auto

auto.PAUSE = 0.5

auto.press("win")
auto.write("google chrome")
auto.press("enter")
auto.hotkey("alt", "space")
auto.press("x")
auto.write("python")
auto.press("enter")
auto.hotkey("ctrl", "t")
auto.write("linkedin.com")
auto.press("enter")