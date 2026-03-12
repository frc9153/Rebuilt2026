import commands2
import rev

from constants import turretMotorConstants

class turretShootMotorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        
        # check motor types for these im hallucinating and i dont know what they are 
        self.motor_one = rev.SparkMax(
            turretMotorConstants.TURRET_SHOOT_MOTOR_ONE, rev.SparkLowLevel.MotorType.kBrushless
        )
        self.motor_two = rev.SparkMax(
            turretMotorConstants.TURRET_SHOOT_MOTOR_TWO, rev.SparkLowLevel.MotorType.kBrushless
        )
        
        config = rev.SparkMaxConfig()
        # config.voltageCompensation(12)
        # config.smartCurrentLimit(DriveConstants.DRIVE_MOTOR_CURRENT_LIMIT)
        
        self.motor_one.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        self.motor_two.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
    
    def setMotorSpeed(self, speed):
        self.motor_one.set(speed)
        self.motor_two.set(-speed)