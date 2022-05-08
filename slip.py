import sys
import ac
import acsys
import platform
import os

if platform.architecture()[0] == "64bit":
    libdir = 'third_party/lib64'
else:
    libdir = 'third_party/lib'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), libdir))
os.environ['PATH'] = os.environ['PATH'] + ";."

from third_party.sim_info import info


class SlipDisplay:

    def __init__(self):
        self.doRender = False
        self.appWindow = None

        self.lapcount = 0
        self.l_lapcount = None  # label widget

    def acMain(self):
        self.appWindow = ac.newApp("Slip Display")
        ac.setSize(self.appWindow, 200, 200)

        ac.log("Hello, Assetto Corsa application world!")
        ac.console("Hello, Assetto Corsa console!")


        # Only enable rendering if app is activated
        ac.addOnAppActivatedListener(self.appWindow, self.onAppActivated)
        ac.addOnAppDismissedListener(self.appWindow, self.onAppDismissed)

        self.l_lapcount = ac.addLabel(self.appWindow, "Laps: 0")
        ac.setPosition(self.l_lapcount, 3, 30)

        ac.addRenderCallback(self.appWindow, self.onFormRender)

        return "slipDisplay"

    def acUpdate(self):
        laps = ac.getCarState(0, acsys.CS.LapCount)
        if laps > self.lapcount:
            lapcount = laps
            ac.setText(self.l_lapcount, "Laps: {}".format(lapcount))

        angle = ac.getCarState(0, acsys.CS.SlipAngle)
        ratio = ac.getCarState(0, acsys.CS.SlipRatio)

        ac.log(angle)
        ac.log(ratio)

    def onAppActivated(self):
        self.doRender = True

    def onAppDismissed(self):
        self.doRender = False

    def onFormRender(self):
        self.acUpdate()


slipDisplay = SlipDisplay()


def acMain(ac_version):
    ac.log("Hello Slip Display")
    return slipDisplay.acMain()


"""def acUpdate(deltaT):
    return slipDisplay.acUpdate()"""
