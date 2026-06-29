# 🎨 2AFC Color Discrimination Task

A Python-based two-alternative forced-choice (2AFC) color discrimination experiment designed to investigate chromatic adaptation and color perception in human vision. This experiment employs rigorous psychophysical methods to measure perceptual discrimination abilities under different adaptation states.


## 📊 Dataset Overview

- **Participants:** 12 adult female subjects
- **Experimental Conditions:** 2 (Adaptation vs. No Adaptation)
- **Total Responses:** 9,600


## 🔬 Core Features

### **1. Two-Alternative Forced-Choice (2AFC) Paradigm**
Participants select between two color alternatives (blue or yellow), enabling precise measurement of color discrimination thresholds with minimal bias.

### **2. Chromatic Adaptation Protocol**
- **Adaptation Condition:** Participants adapt to a reference color (blue) for 30 seconds, then view test stimuli interspersed with 10-second adaptation re-exposures
- **No Adaptation Control:** Direct color discrimination without prior adaptation

### **3. Monocular Testing**
- Independent left/right eye assessment
- Captures potential inter-ocular differences

### **4. Real-Time Experiment Control**
- Interactive participant interface with dialog box for session metadata
- Participant ID, eye selection, and adaptation status input
- Instant data recording with automatic CSV output
- Escape key functionality for safe experiment termination

### **5. Comprehensive Data Logging**
Each trial captures:
- Participant identifier
- Eye tested (left/right)
- Adaptation status (adapted/unadapted)
- Stimulus RGB values
- Participant response (b/y)
- Correctness (binary: correct/incorrect)
- Trial index and temporal information


## 📁 Project Structure

```
2AFC-Color-Discrimination-Task/
├── README.md                          # This file
├── Experiment/
│   ├── experiment.py                  # Main experimental script (PsychoPy-based)
│   └── Constants.py                   # Configurable parameters
└── Design/
    ├── Visualization.ipynb            # Color palette validation & visualization
    ├── colorbar.ipynb                 # Used color palette
    └── Sample Data/                   # Example datasets for testing
```

### **Quick Start**

1. Navigate to the Experiment folder
2. Ensure `Constants.py` and `experiment.py` are in the same directory
3. Run the experiment:
   ```bash
   python Experiment/experiment.py
   ```
4. Complete the dialog box (Participant ID, eye, adaptation status)
5. Follow on-screen instructions
6. Data will be saved as `{ParticipantID}_{Eye}_{AdaptationStatus}.csv`


## ⚙️ Configurable Parameters

Edit `Constants.py` to customize your experiment:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `DISPSIZE` | (1920, 1080) | Display resolution |
| `NumOfColors` | 20 | Total colors per trial block (10 blue + 10 yellow) |
| `reps` | 20 | Repetitions per color |
| `long` | 30 sec | Initial adaptation duration |
| `short` | 10 sec | Inter-trial adaptation re-exposure |
| `adaptcolor` | (-1, -1, 1) | Blue adaptation reference |

**Pro Tip:** Set `reps=1` for a quick test run before data collection!


## 📊 Data Visualization

**`Design/Visualization.ipynb`**
- Visualizes the complete color palette
- Validates that colors achieve the 75% discrimination threshold
- Provides psychometric curve analysis
- Uses sample data for demonstration


## 💡 Tips for Best Results

1. **Lighting:** Conduct in a dark room to maximize perceptual sensitivity
2. **Calibration:** Run the Visualization notebook before data collection
3. **Practice:** Have participants complete 5-10 practice trials first
4. **Monitor Calibration:** Ensure monitor color accuracy with a colorimeter if possible
5. **Session Logs:** Back up CSV files immediately after each session


## Preview
https://github.com/user-attachments/assets/c88aae96-d0ae-4f08-8d9b-7814fbfb474b
