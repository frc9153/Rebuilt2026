import math
import commands2

from constants import turretMotorConstants
from subsystems.turretHorizontalMotor import turretHorizontalMotorSubsystem
from subsystems.turretVerticalMotor import turretVerticalMotorSubsystem
from subsystems.turretCamera import turretCameraSubsystem

class shooterAutoAimCommand(commands2.Command):
    def __init__(
        self,
        horizontalsub: turretHorizontalMotorSubsystem,
        verticalsub: turretVerticalMotorSubsystem,
        turretcamerasub: turretCameraSubsystem
    ):
        self.horizontalsub = horizontalsub
        self.verticalsub = verticalsub
        self.turretcamerasub = turretcamerasub

    def initialize(self):
        self.verticalsub.setMotorSpeed(0.0)
        self.horizontalsub.setMotorSpeed(0.0)
    
    def get_average_angle(positions):
        pass
    
    def get_offset(self):
        robot_pose = self.turretcamerasub.get_pose()
        red_side = robot_pose[0] > 0.0
        target = [
            3.654,
            0.0
        ]

        if not red_side:
            target[0] *= -1.0
        
        return [
            robot_pose[0] - target[0],
            robot_pose[1] - target[1],
        ]
    
    def execute(self):
        offset = self.get_offset()
        distance = math.sqrt(offset[0] ** 2 + offset[1] ** 2)
    
        average_horizontal_angle = math.atan2(offset[1], offset[0])
        self.horizontalsub.pid_controller.setReference(
            # TODO: Figure out the actual conversion rate here. I assume 1 = 1 rotation like a little baby.
            # I know nothing. Im new. Were is mama.
            average_horizontal_angle / (2 * math.pi),
            rev.SparkBase.ControlType.kPosition
        )

        v = 3000
        x = average_offset[0]
        y = average_offset[1] # TODO: 6ft
        g = -9.81

        vertical_angle = math.atan(
            (v ** 2) + math.sqrt(
                (v ** 4) - (g * ((g * x * x) + (2 * y * v * v)))
            ) / (g * x)
        )
        # Vertical thing

    def end(self, interrupted):
        self.verticalsub.setMotorSpeed(0.0)
        self.horizontalsub.setMotorSpeed(0.0)

    def isFinished(self):
        return False