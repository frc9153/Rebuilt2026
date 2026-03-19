import commands2
from constants import turretMotorConstants
from subsystems.turretVerticalMotor import turretVerticalMotorSubsystem

class shooterYuhHuhCommand(commands2.Command):
    def __init__(self, yessub: turretVerticalMotorSubsystem, y_speed: float):
        super().__init__()
        self.yessub = yessub
        self.y_speed = y_speed
        self.addRequirements(yessub)


    def initialize(self):
        self.yessub.setMotorSpeed(self.y_speed)

    def execute(self):
        angle = self.yessub.getAbsolutePosition()
        if self.y_speed > 0 and angle >= turretMotorConstants.TURRET_ANGLE_90:
            self.yessub.setMotorSpeed(0)  # hit top limit, stop
        elif self.y_speed < 0 and angle <= turretMotorConstants.TURRET_ANGLE_60:
            self.yessub.setMotorSpeed(0)  # hit bottom limit, stop
        else:
            self.yessub.setMotorSpeed(self.y_speed)  

    def end(self, interrupted):
        self.yessub.setMotorSpeed(0)

    def isFinished(self):
        return False  