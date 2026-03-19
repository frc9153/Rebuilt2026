import commands2
from constants import turretMotorConstants
from subsystems.turretVerticalMotor import turretVerticalMotorSubsystem

class holdShooterAngleCommand(commands2.Command):
    def __init__(self, subsystem: turretVerticalMotorSubsystem):
        super().__init__()
        self.subsystem = subsystem
        self.addRequirements(subsystem)

    def initialize(self):
        self.subsystem.holdPosition(self.subsystem.getAbsolutePosition())

    def execute(self):
        self.subsystem.holdPosition(self.subsystem.holdPos)

    def end(self, interrupted):
        pass

    def isFinished(self):
        return False