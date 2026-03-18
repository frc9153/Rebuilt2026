import commands2

from subsystems.elevator import elevatorSubsystem
from subsystems.fuelUpDown import fuelUpDownSubsystem

class fuelUpDownCommand(commands2.Command):
    def __init__(self, subsystem: fuelUpDownSubsystem, point: float):
        super().__init__()
        self.subsystem = subsystem
        self.point = point
        self.addRequirements(subsystem)

    def initialize(self):
        self.subsystem.setSetpoint(self.point)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        return self.subsystem.isAt(self.point)