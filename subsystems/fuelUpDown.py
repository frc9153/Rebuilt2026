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
        config.closedLoop.pid(5.0, 0.002, 0.1)

        config.closedLoop.IZone(0.05) # makes it so the I only kicks in when close 
        config.closedLoop.outputRange(-0.5, 0.5) # caps output so no slamming

        self.motor.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        
        self.pid = self.motor.getClosedLoopController()
        self.encoder = self.motor.getAbsoluteEncoder() 
        self.setpoint = self.encoder.getPosition()
    
    def setPower(self, speed: float) -> None:
        self.motor.set(speed)
    
    def setSetpoint(self, point: float):
        self.setpoint = point
        current = self.encoder.getPosition()

        if point > current:
            arb_ff = 0.07   # fighting gravity going up
        else:
            arb_ff = 0.0    # gravity helps going down

        self.pid.setReference(
            point,
            rev.SparkLowLevel.ControlType.kPosition,
            rev.ClosedLoopSlot.kSlot0,
            arb_ff
        )

    def isAt(self, point: float) -> bool:
        position = self.encoder.getPosition()
        delta = abs(position - point)
        done = delta < 0.008
        return done