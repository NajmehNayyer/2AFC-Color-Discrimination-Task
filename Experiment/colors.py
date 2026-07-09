from functions import rgb_to_psy
import numpy as np

# RGB values for the experiment colors
blue_steps = np.arange(0, 250, 25)
yellow_steps = list(reversed(blue_steps))

# RGB of each spectrum
blue = [rgb_to_psy([b, b, 255]) for b in blue_steps]
yellow = [rgb_to_psy([255, 255, y]) for y in yellow_steps]

# Finalize the colors for the experiment
color_data = [('yellow', rgb) for rgb in yellow] + [('blue', rgb) for rgb in blue]
colors = [{'index': i, 'rgb': rgb, 'name': name} for i, (name, rgb) in enumerate(color_data)]
