import commands2
import rev

from constants import turretMotorConstants

class turretVerticalMotorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        
        self.motor = rev.SparkMax(
            turretMotorConstants.TURRET_VERTICAL_MOTOR, rev.SparkLowLevel.MotorType.kBrushless
        )

        self.abs_encoder = self.motor.getAbsoluteEncoder()
        
        config = rev.SparkMaxConfig()
        
        self.motor.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
    
    def setMotorSpeed(self, speed):
        self.motor.set(speed)

    def getAbsolutePosition(self):
        return self.abs_encoder.getPosition()