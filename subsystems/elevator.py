import commands2
import rev

from constants import elevatorConstants

class elevatorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        self.elevator_motor_one = rev.SparkMax(
            elevatorConstants.ELEVATOR_MOTOR_ONE, rev.SparkLowLevel.MotorType.kBrushless
        )

        self.elevator_motor_two = rev.SparkMax(
            elevatorConstants.ELEVATOR_MOTOR_TWO, rev.SparkLowLevel.MotorType.kBrushless
        )

        config_one = rev.SparkMaxConfig()
        config_one.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
        config_one.closedLoop.setFeedbackSensor(rev.FeedbackSensor.kPrimaryEncoder)
        config_one.closedLoop.pid(1.0, 0.0, 0.0)
        # config_one.closedLoop.maxMotion.cruiseVelocity(elevatorConstants.ELEVATOR_POWER)
        self.elevator_motor_one.configure(
            config_one,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
        self.elevator_pid_controller = self.elevator_motor_one.getClosedLoopController()
        self.elevator_encoder = self.elevator_motor_one.getEncoder()
        
        config_two = rev.SparkMaxConfig()
        config_two.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
        config_two.follow(elevatorConstants.ELEVATOR_MOTOR_ONE, invert=True)
        self.elevator_motor_two.configure(
            config_two,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )

        self.throb_motor = rev.SparkMax(
            elevatorConstants.THROB_MOTOR, rev.SparkLowLevel.MotorType.kBrushless
        )
        self.throbber_pid_controller = self.elevator_motor_one.getClosedLoopController()
        config_throb = rev.SparkMaxConfig()
        config_throb.setIdleMode(rev.SparkBaseConfig.IdleMode.kBrake)
        config_throb.closedLoop.setFeedbackSensor(rev.FeedbackSensor.kAbsoluteEncoder)
        config_throb.closedLoop.pid(15.0, 0.0, 0.0)

        self.throbber_encoder = self.throb_motor.getAbsoluteEncoder()
        self.throb_motor.configure(
            config_throb,
            rev.ResetMode.kResetSafeParameters,
            rev.PersistMode.kPersistParameters,
        )
    
    def setThrobberSetpoint(self, point: float):
        self.throbber_pid_controller.setSetpoint(point, rev.SparkLowLevel.ControlType.kPosition)
    
    def isThrobberAtPoint(self, point: float) -> bool:
        position = self.throbber_encoder.getPosition()
        delta = abs(position - point)
        done = delta < 0.01
        return done

    def setElevatorSetpoint(self, point: float):
        self.elevator_pid_controller.setSetpoint(point, rev.SparkLowLevel.ControlType.kPosition)

    def isElevatorAt(self, point: float) -> bool:
        position = self.elevator_encoder.getPosition()
        delta = abs(position - point)
        done = delta < 0.1
        print("Pos", position, "setpoint", point, "Delta", delta, "done", done)
        return done