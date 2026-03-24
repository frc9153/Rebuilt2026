import commands2
import rev

from constants import fuelConstants

class intakeSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        self.motor = rev.SparkMax(
            fuelConstants.FUEL_MOTOR, rev.SparkLowLevel.MotorType.kBrushless
        )

        config = rev.SparkMaxConfig()

        self.motor.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        config.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
    
    def setPower(self, speed: float) -> None:
        self.motor.set(speed)