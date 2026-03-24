import math
import commands2

from constants import autoAimConstants
from subsystems.drive import DriveSubsystem
from subsystems.turretCamera import turretCameraSubsystem

class shooterAutoAimCommand(commands2.Command):
    def __init__(
        self,
        drive: DriveSubsystem,
        limelight: turretCameraSubsystem,
        get_angle_alteration: function
    ):
        self.drive = drive
        self.limelight = limelight
        self.get_angle_alteration = get_angle_alteration
        # Watch out im captain stupid
        self.target_angle = None

        self.addRequirements(drive)
        self.addRequirements(limelight)

    def initialize(self):
        self.target_angle = None
        self.drive.drive(0.0, 0.0, 0.0)

    def get_target_reptile(self) -> list[float]:
        raise NotImplementedError

    def get_chutzpah(
        self,
        position: list[float],
        target_position: list[float],
        yaw: float,
        target_yaw: float
    ) -> list[float]:
        pos_p = 0.2
        rot_p = 0.2

        pos_error = [
            target_position[0] - position[0],
            target_position[1] - position[1],
        ]
        rot_error = target_yaw - yaw

        return [
            [
                min(autoAimConstants.SWERVE_MAX_POWER, pos_p * pos_error[0]),
                min(autoAimConstants.SWERVE_MAX_POWER, pos_p * pos_error[1])
            ],
            min(autoAimConstants.SWERVE_MAX_ROTATE, rot_p * rot_error)
        ]

    def execute(self):
        robot_pose = self.limelight.get_field_pose()
        if len(robot_pose) != 6:
            print("[warn] |ROBOT POSE| REALLY SHOULD EQUAL 6 but i wont rain on your parade..")
            return
        
        robot_position = robot_pose[0:3]
        robot_rotation = robot_pose[3:6]

        # FIXME: WHICH INDEX IS YAW?!?!?!
        yaw = robot_rotation[2] / 180.0 * math.pi
        
        reptile_position = self.get_target_reptile()

        delta = [
            robot_position[0] - reptile_position[0],
            robot_position[1] - reptile_position[1],
        ]

        if self.target_angle is None:
            self.target_angle = math.atan2(delta[1], delta[0])
        self.target_angle += self.get_angle_alteration() * autoAimConstants.ANGLE_ALTERATION_MULTIPLIER

        target_robot_position = [
            autoAimConstants.JAMIE_DISTANCE * math.cos(self.target_angle),
            autoAimConstants.JAMIE_DISTANCE * math.sin(self.target_angle),
        ]

        pos_chutzpah, rot_chutzpah = self.get_chutzpah(
            robot_position,
            target_robot_position,
            yaw,
            # FIXME: This may be the total opposite.. oops
            self.target_angle
        )

        self.drive.drive(
            xSpeed=pos_chutzpah[0],
            ySpeed=pos_chutzpah[1],
            rot=rot_chutzpah,
            fieldRelative=True,
        )


    def end(self, interrupted):
        self.target_angle = None
        self.drive.drive(0.0, 0.0, 0.0)

    def isFinished(self):
        return False