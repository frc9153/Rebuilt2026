#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

# Ok so basically this stuff just gives our motors a number to reference. It'll change. Oh gosh
import math

from wpimath import units
from wpimath.geometry import Translation2d
from wpimath.kinematics import SwerveDrive4Kinematics
from wpimath.trajectory import TrapezoidProfileRadians

from rev import SparkMax, SparkBaseConfig


class NeoMotorConstants:
    kFreeSpeedRpm = 5676


class DriveConstants:
    # Driving Parameters - Note that these are not the maximum capable speeds of
    # the robot, rather the allowed maximum speeds
    # Original: 4.8
    kMaxSpeed = 4.8
    kMaxAngularSpeed = (math.tau) * 0.5  # radians per second

    kDirectionSlewRate = 1.2  # radians per second
    kMagnitudeSlewRate = 1.8  # percent per second (1 = 100%)
    kRotationalSlewRate = 2.0  # percent per second (1 = 100%)

    # Chassis configuration
    kTrackWidth = units.inchesToMeters(26.5)
    # Distance between centers of right and left wheels on robot
    kWheelBase = units.inchesToMeters(21.5)

    # Distance between front and back wheels on robot
    kModulePositions = [
        Translation2d(kWheelBase / 2, kTrackWidth / 2),
        Translation2d(kWheelBase / 2, -kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, -kTrackWidth / 2),
    ]
    kDriveKinematics = SwerveDrive4Kinematics(*kModulePositions)

    # Angular offsets of the modules relative to the chassis in radians
    kFrontLeftChassisAngularOffset = -math.pi / 2
    kFrontRightChassisAngularOffset = 0
    kBackLeftChassisAngularOffset = math.pi
    kBackRightChassisAngularOffset = math.pi / 2

    # SPARK MAX CAN IDs
    kFrontLeftDrivingCanId = 5
    kRearLeftDrivingCanId = 7
    kFrontRightDrivingCanId = 3
    kRearRightDrivingCanId = 1

    kFrontLeftTurningCanId = 6
    kRearLeftTurningCanId = 8
    kFrontRightTurningCanId = 4
    kRearRightTurningCanId = 2

    kGyroReversed = False

class ModuleConstants:
    # The MAXSwerve module can be configured with one of three pinion gears: 12T, 13T, or 14T.
    # This changes the drive speed of the module (a pinion gear with more teeth will result in a
    # robot that drives faster).
    kDrivingMotorPinionTeeth = 14

    # Invert the turning encoder, since the output shaft rotates in the opposite direction of
    # the steering motor in the MAXSwerve Module.
    kTurningEncoderInverted = True

    # Calculations required for driving motor conversion factors and feed forward
    kDrivingMotorFreeSpeedRps = NeoMotorConstants.kFreeSpeedRpm / 60
    kWheelDiameterMeters = 0.0762
    kWheelCircumferenceMeters = kWheelDiameterMeters * math.pi
    # 45 teeth on the wheel's bevel gear, 22 teeth on the first-stage spur gear, 15 teeth on the bevel pinion
    kDrivingMotorReduction = (45.0 * 22) / (kDrivingMotorPinionTeeth * 15)
    kDriveWheelFreeSpeedRps = (
        kDrivingMotorFreeSpeedRps * kWheelCircumferenceMeters
    ) / kDrivingMotorReduction

    kDrivingEncoderPositionFactor = (
        kWheelDiameterMeters * math.pi
    ) / kDrivingMotorReduction  # meters
    kDrivingEncoderVelocityFactor = (
        (kWheelDiameterMeters * math.pi) / kDrivingMotorReduction
    ) / 60.0  # meters per second

    kTurningEncoderPositionFactor = math.tau  # radian
    kTurningEncoderVelocityFactor = math.tau / 60.0  # radians per second

    kTurningEncoderPositionPIDMinInput = 0  # radian
    kTurningEncoderPositionPIDMaxInput = kTurningEncoderPositionFactor  # radian

    kDrivingP = 0.04
    kDrivingI = 0
    kDrivingD = 0
    kDrivingFF = 1 / kDriveWheelFreeSpeedRps
    kDrivingMinOutput = -1
    kDrivingMaxOutput = 1

    kTurningP = 1
    kTurningI = 0
    kTurningD = 0
    kTurningFF = 0
    kTurningMinOutput = -1
    kTurningMaxOutput = 1

    kDrivingMotorIdleMode = SparkBaseConfig.IdleMode.kBrake
    kTurningMotorIdleMode = SparkBaseConfig.IdleMode.kBrake

    kDrivingMotorCurrentLimit = 50  # amp
    kTurningMotorCurrentLimit = 20  # amp

class OIConstants:
    kDriverControllerPort = 0
    kDriveDeadband = 0.1


class turretMotorConstants:
    TURRET_VERTICAL_MOTOR = 18
    TURRET_HORIZONTAL_MOTOR = 13

    TURRET_SHOOT_MOTOR_ONE = 16
    TURRET_SHOOT_MOTOR_TWO = 17  # ?????????? WHAT IS IT??? Curse You Claire Curse You

    TURRET_SHOOT_POWER = 0.4

    TURRET_ANGLE_90 = 0.975
    TURRET_ANGLE_60 = 0.902

class fuelConstants:
    EAT_POWER = 1.0

    FUEL_UP_DOWN_SETPOINT_BOTTOM = 0.528
    FUEL_UP_DOWN_SETPOINT_TOP = 0.7

    FUEL_UP_DOWN_MOTOR = 14
    FUEL_MOTOR = 9

class elevatorConstants:
    ELEVATOR_MOTOR_ONE = 10
    ELEVATOR_MOTOR_TWO = 12

    ELEVATOR_SETPOINT_BOTTOM = 0.0
    ELEVATOR_SETPOINT_TOP = 175.0

    THROB_MOTOR = 11
    THROBBER_SETPOINT_ERECT = 0.5
    THROBBER_SETPOINT_NOT_ERECT = 0.395

class indexerConstants:
    INDEXER_POWER = 1.0
    INDEXER_MOTOR = 15