from psychopy import visual, core, event, data, gui
from constants import *
from functions import quit_experiment
from colors import colors

# ====================================
# Set-up
# ====================================

# Window
win = visual.Window(size=DISPSIZE, units='norm', fullscr=True, color=BGC)

# Global 'escape' key for finishing the experiment
event.globalKeys.add(key='escape', func=quit_experiment)

# ====================================
# Shapes
# ====================================

# Instructions
instruct = visual.TextStim(win, text="Look at the color with one eye.\n"
                                      "Press 'b' for blue, 'y' for yellow.\n"
                                      "Press 'space' to start", pos=(0, 0))
instruct.draw()  # Write
win.flip()  # Update the window

# Stimulus and fixation properties
stim = visual.Rect(win, width=2, height=2, fillColor='white')
circle = visual.Circle(win, radius=6, edges=64, units='pix', lineColor=BGC, fillColor=BGC, pos=(0, 0))

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
# Experiment
# ====================================

# Define the trials
trials = data.TrialHandler(colors, nReps=reps, method='random')

# Define the experiment
exp = data.ExperimentHandler(dataFileName=f'{ID}_adapt_{adapt_eye}_responder_{respond_eye}_{adapstatus}.csv')
exp.addLoop(trials)

try:

    # ----------- STEP 1: Initial adaptation ----------- #
    if adapstatus == "Adaptation":
        adaptstim = visual.Rect(win, width=2, height=2, fillColor=adaptcolor)
        adaptstim.draw()
        circle.draw()
        win.flip()
        core.wait(long)

    # Start the experiment
    for trial in trials:

        # ----------- STEP 2: Draw stimulus and fixation ----------- #
        stim.fillColor = trial['rgb']
        stim.draw()
        circle.draw()

        # Update the screen
        win.flip()

        # ----------- STEP 3: Store the response ----------- #
        keys = event.waitKeys(keyList=['b', 'y'])
        respond = keys[0]

        # Check whether the answer is correct or not
        if (respond == 'y' and trial['name'] == 'yellow') or (respond == 'b' and trial['name'] == 'blue'):
            answer = '1'
        else: answer = "0"

        # ----------- STEP 4: Inter-trial adaptation ----------- #
        if adapstatus == "Adaptation":
            adaptstim.draw()
            circle.draw()
            win.flip()
            core.wait(short)

        # ----------- STEP 5: Save the data ----------- #
      
        # Add the response and correctness to the output
        trials.addData('response', respond)
        trials.addData('answer', answer)

        # Trial completed
        exp.nextEntry()

finally:

    # Save the output
    exp.saveAsWideText(exp.dataFileName)
  
    exp.close()
    win.close()
    core.quit()
