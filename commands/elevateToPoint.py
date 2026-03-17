import commands2

from subsystems.elevator import elevatorSubsystem

class elevateToPointCommand(commands2.Command):
    def __init__(self, subsystem: elevatorSubsystem, point: float):
        self.subsystem = subsystem
        self.point = point

    def initialize(self):
        self.subsystem.setElevatorSetpoint(self.point)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        print("are we done? ")
        return self.subsystem.isElevatorAt(self.point)