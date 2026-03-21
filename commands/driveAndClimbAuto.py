import commands2
from commands.elevateToPoint import elevateToPointCommand
from subsystems.drive import DriveSubsystem
from subsystems.elevator import elevatorSubsystem
from subsystems.turretCamera import turretCameraSubsystem
from constants import elevatorConstants

class driveAndClimbAuto(commands2.SequentialCommandGroup):
    def __init__(
        self,
        limelight: turretCameraSubsystem,
        drive: DriveSubsystem,
        elevator: elevatorSubsystem,
    ):
        super().__init__()
        self.addCommands(
            # haii jamieee
            # makes us drive forward 
            # note: first value in the .drive controls speed, the timeout controls time driving
            commands2.RunCommand(
                lambda: drive.drive(0.0, -0.2, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ).until(lambda: limelight.isPastClimbAlignmentPoint()),
            # ).withTimeout(3.5),

            # stops driving
            commands2.InstantCommand(
                lambda: drive.drive(0.0, 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ),

            # 
            commands2.RunCommand(
                lambda: drive.drive(limelight.centerPlease(), 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ).until(lambda: abs(limelight.tx.get()) < 1.0),  # stop when within 1 degree of center

            # Stop
            commands2.InstantCommand(
                lambda: drive.drive(0.0, 0.0, 0.0, fieldRelative=False, rateLimit=False),
                drive
            ),

            # climb! hopefully.....
            elevateToPointCommand(elevator, elevatorConstants.ELEVATOR_SETPOINT_BOTTOM)
        )
