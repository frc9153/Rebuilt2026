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

from commands.fuelEat import fuelEatCommand
from constants import OIConstants
from commands.driveCommand import DriveCommand
from subsystems.drive import DriveSubsystem
from subsystems.fuelConsumer import intakeSubsystem
from subsystems.fuelUpDown import intakeUpDownSubsystem
from subsystems.turretVerticalMotor import turretVerticalMotorSubsystem
from subsystems.turretHorizontalMotor import turretHorizontalMotorSubsystem
from commands.shooterLeftRight import shooterNuhUhCommand
from commands.shooterUpDown import shooterYuhHuhCommand

class RobotContainer:
    def __init__(self) -> None:
        self.gyro = navx.AHRS.create_spi() 
        self.robot_drive = DriveSubsystem(self.gyro) 
        self.fuel = intakeSubsystem()
        self.fuelUpDown = intakeUpDownSubsystem()
        # self.nosub = turretHorizontalMotorSubsystem()
        # self.yessub = turretVerticalMotorSubsystem()

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
                    rateLimit=False,
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

        # reset_gyro = commands2.InstantCommand(
        #     lambda: self.robot_drive.gyro.reset(),
        #     self.robot_drive
        # )
        self.driverController.a().onTrue(fuelEatCommand(self.fuel))

    def getAutonomousCommand(self) -> commands2.Command:
        return commands2.InstantCommand(lambda: None)