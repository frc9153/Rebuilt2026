import commands2
from subsystems.turretVerticalMotor import turretVerticalMotorSubsystem

class holdShooterAngleCommand(commands2.Command):
    def __init__(self, subsystem: turretVerticalMotorSubsystem):
        super().__init__()
        self.subsystem = subsystem
        self.addRequirements(subsystem)

    def initialize(self):
        # hold where we are
        self.subsystem.holdPosition(self.subsystem.getAbsolutePosition())

    def execute(self):
        # send hold every tick
        self.subsystem.holdPosition(self.subsystem.holdPos)

    def end(self, interrupted):
        pass

    def isFinished(self):
        return False  