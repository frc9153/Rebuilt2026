import commands2

from constants import indexerConstants
from subsystems.indexer import indexerSubsystem

class indexerReversePukeCommand(commands2.Command):
    def __init__(self, subsystem: indexerSubsystem):
        self.subsystem = subsystem

    def initialize(self):
        self.subsystem.setPower(-indexerConstants.INDEXER_POWER)

    def execute(self):
        pass

    def end(self, interrupted):
        self.subsystem.setPower(0.0)

    def isFinished(self):
        return False