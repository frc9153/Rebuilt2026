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
        
        config_one = rev.SparkMaxConfig()
        # config.voltageCompensation(12)
        # config.smartCurrentLimit(DriveConstants.DRIVE_MOTOR_CURRENT_LIMIT)
        
        self.motor_one.configure(
            config_one,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )

        config_two = rev.SparkMaxConfig()
        config_two.follow(turretMotorConstants.TURRET_SHOOT_MOTOR_ONE, invert=True)
        self.motor_two.configure(
            config_two,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
    
    def setPower(self, speed):
        self.motor_one.set(speed)