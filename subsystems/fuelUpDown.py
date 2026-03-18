import commands2
import rev

from constants import fuelConstants

class fuelUpDownSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        self.motor = rev.SparkMax(
            fuelConstants.FUEL_UP_DOWN_MOTOR, rev.SparkLowLevel.MotorType.kBrushless
        )

        config = rev.SparkMaxConfig()
        config.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
        config.closedLoop.setFeedbackSensor(rev.FeedbackSensor.kAbsoluteEncoder)
        config.closedLoop.pid(2.0, 0.0, 0.0)

        self.motor.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        
        self.pid = self.motor.getClosedLoopController()
        self.encoder = self.motor.getAbsoluteEncoder()
        self.setpoint = 0.0
    
    def setPower(self, speed: float) -> None:
        self.motor.set(speed)
    
    def setSetpoint(self, point: float):
        self.setpoint = point
        self.pid.setSetpoint(point, rev.SparkLowLevel.ControlType.kPosition)

    def isAt(self, point: float) -> bool:
        position = self.encoder.getPosition()
        delta = abs(position - point)
        done = delta < 0.01
        return done