import commands2
from commands.elevateToPoint import elevateToPointCommand
from subsystems.drive import DriveSubsystem
from subsystems.elevator import elevatorSubsystem
from constants import elevatorConstants

class driveAndClimbAuto(commands2.SequentialCommandGroup):
    def __init__(self, drive: DriveSubsystem, elevator: elevatorSubsystem):
        super().__init__()
        self.addCommands(
            # rotate 90 degrees - TUNE
            commands2.RunCommand(
                lambda: drive.drive(0.0, 0.0, 0.5, fieldRelative=False, rateLimit=False),
                drive
            ).withTimeout(1.0),  # TUNE UNTIL MAKES 90 DEGREE TURN

            # no more rotate
            commands2.InstantCommand(
                lambda: drive.drive(0.0, 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ),

            # drives forward, TUNE SPEED AND TIME  WHY DOESNT ANYTHING GO AHHH
            commands2.RunCommand(
                lambda: drive.drive(0.3, 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ).withTimeout(3.0), # this number tunes the time

            # no more drive
            commands2.InstantCommand(
                lambda: drive.drive(0.0, 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ),

            # climb
            elevateToPointCommand(elevator, elevatorConstants.ELEVATOR_SETPOINT_BOTTOM),
        )