import commands2
import rev

from constants import fuelConstants

class intakeSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        self.motor = rev.SparkMax(
            fuelConstants.FUEL_MOTOR,rev.SparkLowLevel.MotorType.kBrushed
        )

        config = rev.SparkMaxConfig()
        # config.voltageCompensation(12)
        # config.smartCurrentLimit(DriveConstants.DRIVE_MOTOR_CURRENT_LIMIT)

        self.motor.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
    
    def setIntake(self, voltage: float) -> None:
        self.motor.setVoltage(voltage)