import commands2

from constants import turretMotorConstants
from subsystems.turretShootMotor import turretShootMotorSubsystem

class shooterShootCommand(commands2.Command):
    def __init__(self, shootsub: turretShootMotorSubsystem, speed: float):
        self.shootsub = shootsub
        self.speed = speed

    def initialize(self):
        self.shootsub.setMotorSpeed(self.speed)

    def execute(self):
        pass

    def end(self, interrupted):
        self.shootsub.setMotorSpeed(0)

    def isFinished(self):
        return False