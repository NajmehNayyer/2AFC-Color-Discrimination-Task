# Convert the color from the 0-255 RGB scale to the PsychoPy scale
def rgb_to_psy(color):
    return [c / 127.5 - 1 for c in color]

def quit_experiment():
    win.close()
    core.quit()
