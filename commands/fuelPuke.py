import commands2

from constants import fuelConstants
from subsystems.fuelConsumer import intakeSubsystem

class fuelPukeCommand(commands2.Command):
    def __init__(self, subsystem: intakeSubsystem):
        self.subsystem = subsystem

    def initialize(self):
        self.subsystem.setPower(-fuelConstants.EAT_POWER)

    def execute(self):
        pass

    def end(self, interrupted):
        self.subsystem.setPower(0.0)

    def isFinished(self):
        return False