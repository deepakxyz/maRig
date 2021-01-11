How To Install
-------------------------------
# Copy "bs_controls.py" and "bs_controlsUI.py" into your Maya scripts directory.
# Documents\maya\2018\prefs\scripts (replace 2018 with your version)
# Add a shelf button with the following python code:

import bs_controlsUI
reload(bs_controlsUI)
bsCon = bs_controlsUI.BSControlsUI()
bsCon.bsControlsUI()