#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import commands2.button
import commands2.cmd
import wpimath
import navx

from commands.changeThrobberErection import changeThrobberErectionCommand
from commands.elevateToPoint import elevateToPointCommand
from commands.fuelEat import fuelEatCommand
from commands.fuelUpDown import fuelUpDownCommand
from commands.indexerPuke import indexerPukeCommand
from commands.indexerReversePuke import indexerReversePukeCommand 
from commands.shooterShoot import shooterShootCommand
from constants import OIConstants, elevatorConstants, fuelConstants, turretMotorConstants
from commands.driveCommand import DriveCommand
from subsystems.drive import DriveSubsystem
from subsystems.elevator import elevatorSubsystem
from subsystems.fuelConsumer import intakeSubsystem
from subsystems.fuelUpDown import fuelUpDownSubsystem
from subsystems.indexer import indexerSubsystem
from subsystems.turretCamera import turretCameraSubsystem
from subsystems.turretShootMotor import turretShootMotorSubsystem
from subsystems.turretVerticalMotor import turretVerticalMotorSubsystem
from subsystems.turretHorizontalMotor import turretHorizontalMotorSubsystem
from commands.shooterLeftRight import shooterNuhUhCommand
from commands.shooterUpDown import shooterYuhHuhCommand
from commands.autoRoutine import autoRoutine

class RobotContainer:
    def __init__(self) -> None:
        self.gyro = navx.AHRS.create_spi()
        self.robot_drive = DriveSubsystem(self.gyro)
        self.fuelIntake = intakeSubsystem()
        self.indexer = indexerSubsystem()
        self.fuelUpDown = fuelUpDownSubsystem()
        self.shooter = turretShootMotorSubsystem()
        # self.limelight = turretCameraSubsystem()
        # self.nosub = turretHorizontalMotorSubsystem()
        # self.yessub = turretVerticalMotorSubsystem()
        self.elevator = elevatorSubsystem()
        self.autoCommand = autoRoutine(
            self.shooter,
            self.indexer,
            self.elevator
        )

        # Command groups

        self.shooterYuhHuhCommand = shooterYuhHuhCommand(self.shooter, 0.1)
        
        self.elevatorFloorToRungCommand = commands2.SequentialCommandGroup(
            # Assume we start at BOTTOM
            # elevateToPointCommand(self.elevator, elevatorConstants.ELEVATOR_SETPOINT_TOP),
            # elevateToPointCommand(self.elevator, elevatorConstants.ELEVATOR_SETPOINT_BOTTOM),
            changeThrobberErectionCommand(self.elevator, elevatorConstants.THROBBER_SETPOINT_NOT_ERECT),
            changeThrobberErectionCommand(self.elevator, elevatorConstants.THROBBER_SETPOINT_ERECT),
        )

        # controller 
        self.driverController = commands2.button.CommandXboxController(OIConstants.kDriverControllerPort)

        # configure button bindings
        self.configureButtonBindings()

        self.robot_drive.setDefaultCommand(
            # The left stick controls translation of the robot.
            # Turning is controlled by the X axis of the right stick.
            commands2.RunCommand(
                lambda: self.robot_drive.drive(
                    -wpimath.applyDeadband(
                        self.driverController.getLeftY(), OIConstants.kDriveDeadband
                    ),
                    -wpimath.applyDeadband(
                        self.driverController.getLeftX(), OIConstants.kDriveDeadband
                    ),
                    -wpimath.applyDeadband(
                        self.driverController.getRightX(), OIConstants.kDriveDeadband
                    ),
                    fieldRelative=True,
                    rateLimit=True,
                ),
                self.robot_drive,
            )
        )

    def configureButtonBindings(self) -> None:
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """
        # THAT
        # controls turret going left/right
        # self.driverController.leftBumper().whileTrue(shooterNuhUhCommand(self.nosub,-0.05))
        # self.driverController.rightBumper().whileTrue(shooterNuhUhCommand(self.nosub,0.05))

        # # controls turret going up/down
        # self.driverController.povDown().whileTrue(shooterYuhHuhCommand(self.yessub, -0.05))
        # self.driverController.povUp().whileTrue(shooterYuhHuhCommand(self.yessub, 0.05))

        reset_gyro = commands2.InstantCommand(
            lambda: self.robot_drive.gyro.reset(),
            self.robot_drive
        )

        self.driverController.povUp().onTrue(fuelUpDownCommand(self.fuelUpDown, fuelConstants.FUEL_UP_DOWN_SETPOINT_TOP))
        self.driverController.povLeft().onTrue(fuelUpDownCommand(self.fuelUpDown, fuelConstants.FUEL_UP_DOWN_SETPOINT_MIDDLE))
        self.driverController.povDown().onTrue(fuelUpDownCommand(self.fuelUpDown, fuelConstants.FUEL_UP_DOWN_SETPOINT_BOTTOM))

        self.driverController.leftBumper().onTrue(shooterYuhHuhCommand(self.shooter, turretMotorConstants.TURRET_ANGLE_90))
        self.driverController.rightBumper().onTrue(shooterYuhHuhCommand(self.shooter, turretMotorConstants.TURRET_ANGLE_60))

        self.driverController.rightTrigger().whileTrue(shooterShootCommand(self.shooter, turretMotorConstants.TURRET_SHOOT_POWER))
        self.driverController.leftTrigger().whileTrue(indexerPukeCommand(self.indexer))
        self.driverController.povRight().whileTrue(indexerReversePukeCommand(self.indexer))

        self.driverController.x().onTrue(reset_gyro)
        self.driverController.a().whileTrue(fuelEatCommand(self.fuelIntake))
        self.driverController.b().onTrue(self.elevatorFloorToRungCommand)

    def getAutonomousCommand(self) -> commands2.Command:
        return self.autoCommand