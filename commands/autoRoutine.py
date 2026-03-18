import commands2
from commands.shooterShoot import shooterShootCommand
from commands.indexerPuke import indexerPukeCommand
from commands.elevateToPoint import elevateToPointCommand
from subsystems.turretShootMotor import turretShootMotorSubsystem
from subsystems.indexer import indexerSubsystem
from subsystems.elevator import elevatorSubsystem
from constants import turretMotorConstants, elevatorConstants

class autoRoutine(commands2.SequentialCommandGroup):
    def __init__(
        self,
        shooter: turretShootMotorSubsystem,
        indexer: indexerSubsystem,
        elevator: elevatorSubsystem,
    ):
        super().__init__()

        self.addCommands(
            # spins da shooter until up 2 speed
            shooterShootCommand(shooter, turretMotorConstants.TURRET_SHOOT_POWER)
                .withTimeout(1.0),

            # feeds balls thru indexer but adjust timeout in tuning
            commands2.ParallelCommandGroup(
                shooterShootCommand(shooter, turretMotorConstants.TURRET_SHOOT_POWER),
                indexerPukeCommand(indexer),
            ).withTimeout(5.0),

            # L1 climb
            elevateToPointCommand(elevator, elevatorConstants.ELEVATOR_SETPOINT_TOP),
        )