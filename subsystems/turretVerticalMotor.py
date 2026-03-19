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
        config.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
        config.closedLoop.setFeedbackSensor(rev.FeedbackSensor.kAbsoluteEncoder)
        config.closedLoop.pid(3.0, 0.0, 0.0)  # tune P on robot major plz

        self.motor.configure(
            config,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        self.pid = self.motor.getClosedLoopController()

    def setMotorSpeed(self, speed):
        self.motor.set(speed)

    def holdPosition(self, position: float):
        # uses PID to hold at a specific encoder position
        self.pid.setReference(
            position,
            rev.SparkLowLevel.ControlType.kPosition,
            rev.ClosedLoopSlot.kSlot0,
            0.0
        )

    def getAbsolutePosition(self):
        return self.abs_encoder.getPosition()