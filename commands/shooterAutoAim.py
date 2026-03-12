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
    
    def get_center_offsets(self):
        # Returns a list of robot offsets relative to the target. TODO
        # NOTE: Please offset center coordinates here :3
        return []

    def execute(self):
        offsets = get_center_offsets()
        # print("Offset count", len(offsets))

        # TODO: Print difference from avg or something jamiepilled
        average_offset = [
            sum([o[0] for o in offsets]) / len(offsets),
            sum([o[1] for o in offsets]) / len(offsets)
        ]
        # print("Avg offset", average_offset)

        if len(offsets) == 0:
            # Find mama. Where is mama, help.
            self.horizontalsub.setMotorSpeed(0.1)
        else:
            average_horizontal_angle = math.atan2(average_offset[1], average_offset[0])
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