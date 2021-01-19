# Add system path to the maya
import sys
maRig_path = "Y:/maRig_main/maRig"

if not maRig_path in sys.path:
    sys.path.append(maRig_path)
