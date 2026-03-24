import math
import commands2

from constants import autoAimConstants
from subsystems.drive import DriveSubsystem
from subsystems.turretCamera import turretCameraSubsystem

class shooterAutoAimCommand(commands2.Command):
    def __init__(
        self,
        drive: DriveSubsystem,
        limelight: turretCameraSubsystem
    ):
        self.drive = drive
        self.limelight = limelight

        self.addRequirements(drive)
        self.addRequirements(limelight)

    def initialize(self):
        self.drive.drive(0.0, 0.0, 0.0)

    def get_target_reptile(self) -> list[float]:
        raise NotImplementedError

    def get_chutzpah(
        self,
        position: list[float],
        target_position: list[float],
    ) -> list[float]:
        p = 0.2

        error = [
            target_position[0] - position[0],
            target_position[1] - position[1],
        ]

        return [
            min(autoAimConstants.SWERVE_MAX_POWER, p * error[0]),
            min(autoAimConstants.SWERVE_MAX_POWER, p * error[1])
        ]

    def execute(self):
        robot_position = self.limelight.get_field_position()
        reptile_position = self.get_target_reptile()

        delta = [
            robot_position[0] - reptile_position[0],
            robot_position[1] - reptile_position[1],
        ]

        angle_from_reptile_to_robot = math.atan2(delta[1], delta[0])
        target_robot_position = [
            autoAimConstants.JAMIE_DISTANCE * math.cos(angle_from_reptile_to_robot),
            autoAimConstants.JAMIE_DISTANCE * math.sin(angle_from_reptile_to_robot),
        ]

        chutzpah = self.get_chutzpah(robot_position, target_robot_position)
        self.drive.drive(
            xSpeed=chutzpah[0],
            ySpeed=chutzpah[1],
            rot=0.0,
            fieldRelative=True,
        )


    def end(self, interrupted):
        self.drive.drive(0.0, 0.0, 0.0)

    def isFinished(self):
        return False