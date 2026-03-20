import commands2
from commands.elevateToPoint import elevateToPointCommand
from subsystems.drive import DriveSubsystem
from subsystems.elevator import elevatorSubsystem
from constants import elevatorConstants

class driveAndClimbAuto(commands2.SequentialCommandGroup):
    def __init__(
        self,
        drive: DriveSubsystem,
        elevator: elevatorSubsystem,
    ):
        super().__init__()
        self.addCommands(
            # makes us drive forward 
            # note: first value in the .drive controls speed, the timeout controls time driving
            commands2.RunCommand(
                lambda: drive.drive(0.3, 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ).withTimeout(3.0),

            # stops driving
            commands2.InstantCommand(
                lambda: drive.drive(0.0, 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ),

            # climb! hopefully.....
            elevateToPointCommand(elevator, elevatorConstants.ELEVATOR_SETPOINT_TOP),
        )