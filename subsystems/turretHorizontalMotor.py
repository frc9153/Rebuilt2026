import commands2
import rev

from constants import turretMotorConstants

# This stuff just sets up our motors. Every motor that needs to move independently of one another
# Needs its own subsystem. Kinda annoying. But watevs. #LOL

class turretHorizontalMotorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        
        # check motor types for these im hallucinating and i dont know what they are 
        self.motor = rev.SparkMax(
            turretMotorConstants.TURRET_HORIZONTAL_MOTOR, rev.SparkLowLevel.MotorType.kBrushed
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