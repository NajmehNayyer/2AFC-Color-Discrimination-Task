from psychopy import visual, core, event, data, gui
import numpy as np
from constants import *

# ====================================
# Dialog Box
# ====================================

# Create the dialog box
info = gui.Dlg(title="2AFC Color Discrimination")
info.addField("Subject's Number:", required=True)
info.addField("Adapting eye:", choices=["Both", "Left", "Right"], required=True)
info.addField("Responder eye:", choices=["Both", "Left", "Right"], required=True)
info.addField("Adaptation status:", choices=["No_Adaptation", "Adaptation"], required=True)

# Display
okdata = info.show()
if not okdata: core.quit()

# Save the data in variables
ID = info.data[0]
adapt_eye = info.data[1]
respond_eye = info.data[2]
adapstatus = info.data[3]

# ====================================
# Experiment Colors
# ====================================

# RGB values for the experiment colors
blue_steps = np.arange(0, 250, 25)
yellow_steps = list(reversed(blue_steps))

# Convert the color from the 0-255 RGB scale to the PsychoPy scale
def rgb_to_psy(color):
    return [c / 127.5 - 1 for c in color]

# RGB of each spectrum
blue = [rgb_to_psy([b, b, 255]) for b in blue_steps]
yellow = [rgb_to_psy([255, 255, y]) for y in yellow_steps]

# Finalize the colors for the experiment
color_data = [('yellow', rgb) for rgb in yellow] + [('blue', rgb) for rgb in blue]
colors = [{'index': i, 'rgb': rgb, 'name': name} for i, (name, rgb) in enumerate(color_data)]

# ====================================
# Experiment Setup
# ====================================

# Window
win = visual.Window(size=DISPSIZE, units='norm', fullscr=True, color=BGC)

# Instructions
instruct = visual.TextStim(win, text="Look at the color with one eye.\n"
                                      "Press 'b' for blue, 'y' for yellow.\n"
                                      "Press 'space' to start", pos=(0, 0))
instruct.draw()  # Write
win.flip()  # Update the window

# Quit with the "esc" key
prim_keys = event.waitKeys(keyList=['space', 'escape'])
if 'escape' in prim_keys: core.quit()

# Define the trials
trials = data.TrialHandler(colors, nReps=reps, method='random')

# Define the experiment
exp = data.ExperimentHandler(dataFileName=f'{ID}_adapt_{adapt_eye}_responder_{respond_eye}_{adapstatus}.csv')
exp.extraInfo = {'participant': ID, 'adapting_eye': adapt_eye, 'responding_eye': respond_eye, 'adaptstatus': adapstatus}  # Metadata
exp.addLoop(trials)

# Stimulus and fixation properties
stim = visual.Rect(win, width=2, height=2, fillColor='white')
circle = visual.Circle(win, radius=6, edges=64, units='pix', lineColor=BGC, fillColor=BGC, pos=(0, 0))

# ===================
# Experiment
# ===================
try:

    # Initial adaptation
    if adapstatus == "Adaptation":
        adaptstim = visual.Rect(win, width=2, height=2, fillColor=adaptcolor)
        adaptstim.draw()
        circle.draw()
        win.flip()
        core.wait(long)

    for trial in trials:

        # Draw the stimulus
        stim.fillColor = trial['rgb']
        stim.draw()

        # Draw the fixation
        circle.draw()

        # Update the screen
        win.flip()

        # Store the response
        keys = event.waitKeys(keyList=['b', 'y', 'escape'])
        if keys == 'escape':
            core.quit()
        respond = keys[0]

        # Check whether the answer is correct or not
        if (respond == 'y' and trial['name'] == 'yellow') or (respond == 'b' and trial['name'] == 'blue'):
            answer = '1'
        else: answer = "0"

        # Add the response and correctness to the output
        trials.addData('response', respond)
        trials.addData('answer', answer)

        # Trial completed
        exp.nextEntry()

        # Inter-trial adaptation
        if adapstatus == "Adaptation":
            adaptstim.draw()
            circle.draw()
            win.flip()
            core.wait(short)

finally:

    # Save and end the experiment
    exp.saveAsWideText(exp.dataFileName)
    exp.close()

    win.close()
    core.quit()
