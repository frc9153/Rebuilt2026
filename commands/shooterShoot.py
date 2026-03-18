import commands2

from constants import turretMotorConstants
from subsystems.turretShootMotor import turretShootMotorSubsystem

class shooterShootCommand(commands2.Command):
    def __init__(self, shootsub: turretShootMotorSubsystem, speed: float):
        super().__init__()
        self.shootsub = shootsub
        self.speed = speed
        self.addRequirements(shootsub)

    def initialize(self):
        self.shootsub.setPower(self.speed)

    def execute(self):
        pass

    def end(self, interrupted):
        self.shootsub.setPower(0)

    def isFinished(self):
        return False