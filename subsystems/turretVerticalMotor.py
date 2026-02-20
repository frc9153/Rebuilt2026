import commands2
import rev

from constants import turretMotorConstants

class turretVerticalMotorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        
        # check motor types for these im hallucinating and i dont know what they are 
        self.motor = rev.SparkMax(
            turretMotorConstants.TURRET_VERTICAL_MOTOR, rev.SparkLowLevel.MotorType.kBrushed
        )
        
        config = rev.SparkMaxConfig()
        # config.voltageCompensation(12)
        # config.smartCurrentLimit(DriveConstants.DRIVE_MOTOR_CURRENT_LIMIT)
        
        self.motor.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
    
    def setMotorSpeed(self, speed):
        self.motor.set(speed)