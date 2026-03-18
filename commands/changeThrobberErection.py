import commands2

from subsystems.elevator import elevatorSubsystem

class changeThrobberErectionCommand(commands2.Command):
    def __init__(self, subsystem: elevatorSubsystem, point: float):
        super().__init__()
        self.subsystem = subsystem
        self.point = point
        self.addRequirements(subsystem)

    def initialize(self):
        self.subsystem.setThrobberSetpoint(self.point)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        return self.subsystem.isThrobberAtPoint(self.point)