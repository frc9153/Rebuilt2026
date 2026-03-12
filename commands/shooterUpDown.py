import commands2

from constants import turretMotorConstants
from subsystems.turretVerticalMotor import turretVerticalMotorSubsystem

class shooterYuhHuhCommand(commands2.Command):

    def __init__(self, yessub: turretVerticalMotorSubsystem, y_speed: float):
        self.yessub = yessub
        self.y_speed = y_speed

    def initialize(self):
        self.yessub.setMotorSpeed(self.y_speed)

    def execute(self):
        pass

    def end(self, interrupted):
        self.yessub.setMotorSpeed(0)

    def isFinished(self):
        angle = self.yessub.getAbsolutePosition()

        if (y>0 and angle>60) or (y<0 and angle<90):
            return True
        else:
            return False