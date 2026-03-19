import commands2
from commands.shooterShoot import shooterShootCommand
from commands.indexerPuke import indexerPukeCommand
from commands.elevateToPoint import elevateToPointCommand
from commands.fuelUpDown import fuelUpDownCommand
from subsystems.turretShootMotor import turretShootMotorSubsystem
from subsystems.indexer import indexerSubsystem
from subsystems.elevator import elevatorSubsystem
from subsystems.fuelUpDown import fuelUpDownSubsystem
from constants import turretMotorConstants, elevatorConstants, fuelConstants

class autoRoutine(commands2.SequentialCommandGroup):
    def __init__(
        self,
        shooter: turretShootMotorSubsystem,
        indexer: indexerSubsystem,
        # elevator: elevatorSubsystem,
        fuel: fuelUpDownSubsystem
    ):
        super().__init__()

        self.addCommands(
            fuelUpDownCommand(fuel,fuelConstants.FUEL_UP_DOWN_SETPOINT_BOTTOM)
                .withTimeout(1.0),

            # puts intake to middle
            fuelUpDownCommand(fuel, fuelConstants.FUEL_UP_DOWN_SETPOINT_MIDDLE),

            # spins da shooter until up 2 speed
            shooterShootCommand(shooter, turretMotorConstants.TURRET_SHOOT_POWER_AUTO)
                .withTimeout(1.0),

            # feeds balls thru indexer but adjust timeout in tuning
            commands2.ParallelCommandGroup(
                shooterShootCommand(shooter, turretMotorConstants.TURRET_SHOOT_POWER),
                indexerPukeCommand(indexer),
            ).withTimeout(15.0),

            # L1 climb
            # elevateToPointCommand(elevator, elevatorConstants.ELEVATOR_SETPOINT_TOP),
        )