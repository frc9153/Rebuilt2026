import commands2

from subsystems.elevator import elevatorSubsystem

class changeThrobberErectionCommand(commands2.Command):
    def __init__(self, subsystem: elevatorSubsystem, erect: bool):
        self.subsystem = subsystem
        self.erect = erect

    def initialize(self):
        self.subsystem.setThrobberErect(self.erect)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        return self.subsystem.isThrobberDone()