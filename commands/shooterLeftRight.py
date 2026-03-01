import commands2

from constants import turretMotorConstants
from subsystems.turretHorizontalMotor import turretHorizontalMotorSubsystem

class shooterNuhUhCommand(commands2.Command):

    def __init__(self, nosub: turretHorizontalMotorSubsystem, x_speed: float):
        self.nosub = nosub
        self.x_speed = x_speed

    def initialize(self):
        self.nosub.setMotorSpeed(self.x_speed)

    def execute(self):
        pass

    def end(self, interrupted):
        self.nosub.setMotorSpeed(0)

    def isFinished(self):
        return False