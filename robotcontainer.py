#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import commands2.button
import commands2.cmd

from constants import OIConstants
from commands.drive import Drive
from commands.eject import Eject
from commands.exampleauto import ExampleAuto
from commands.intake import Intake
from commands.launchsequence import LaunchSequence
from subsystems.drive import DriveSubsystem
from subsystems.fuelConsumer import intakeSubsystem

class RobotContainer:
    def __init__(self) -> None:
        # The robot's subsystems
        self.robot_drive = DriveSubsystem()
        self.fuel = intakeSubsystem()

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

        # # Run default command on the lift_intake subsystem. This will basically run it over
        # # and over until something else runs on lift_intake.
        # self.robot_lift.setDefaultCommand(
        #     # RunCommand is a function that turns a function into a Command. Good for less complicated stuff.
        #     commands2.RunCommand(
        #         # You need to pass a function to this. You can't pass parameters to a function normally,
        #         # and we need to pass getLeftY(), so we make a lambda around it. Basically we're constantly
        #         # setting the intake power to the left joystick's Y value.
        #         lambda: self.robot_lift.set_motor_power(self.driverController.getLeftY()),
        #         self.robot_lift
        #     )
        # )

        # self.robot_joint.setDefaultCommand(
        #     commands2.RunCommand(
        #         lambda: self.robot_joint.set_motor_power(self.driverController.getRightY()),
        #         self.robot_joint
        #     )
        # )
        
        # One time action--much simpler.
        # replace Y with the button you want. the thing passed to onTrue is a Command.
        # self.driverController.a().onTrue(SourceIntake(self.robot_lift, self.robot_joint, self.robot_grabber, self.robot_drive))
        # self.driverController.a().onFalse(SourceRestore(self.robot_lift, self.robot_joint, self.robot_grabber, self.robot_drive))
        # self.driverController.b().whileTrue(ReefScoreL2(self.robot_lift, self.robot_joint, self.robot_grabber, self.robot_drive))
        # self.driverController.x().whileTrue(ReefScoreL3(self.robot_lift, self.robot_joint, self.robot_grabber, self.robot_drive))
        # self.driverController.y().whileTrue(ReefScoreL4(self.robot_lift, self.robot_joint, self.robot_grabber, self.robot_drive))

        # self.driverController.leftTrigger().onTrue(AlgaeIntake(self.robot_lift, self.robot_algae))
        # self.driverController.leftTrigger().onFalse(AlgaeRestore(self.robot_lift, self.robot_algae))
        # self.driverController.rightTrigger().onTrue(self.algae_outtake)
        # self.driverController.rightTrigger().onFalse(self.algae_stoptake)

        # self.driverController.leftBumper().onTrue(ReefBludgeonHigh(self.robot_lift, self.robot_joint, self.robot_grabber, self.robot_drive)) # Algae Bludgeon
        # self.driverController.rightBumper().onTrue(ReefBludgeonLow(self.robot_lift, self.robot_joint, self.robot_grabber, self.robot_drive)) # Algae Bludgeon

        # self.driverController.start().onTrue(GrabberGrabReset(self.robot_grabber))
        # self.driverController.start().onFalse(self.grabber_stop)

        # self.driverController.leftBumper().onTrue(GrabberGrabReset(self.robot_grabber))
        # self.driverController.rightBumper().onTrue(GrabberToSetpoint(self.robot_grabber, GrabberConstants.setpoint_open, True))
        
        # self.driverController.a().onTrue(self.roller_grab)
        # self.driverController.a().onFalse(self.roller_stop)
        # self.driverController.b().onTrue(self.roller_release)
        # self.driverController.b().onFalse(self.roller_stop)

        reset_gyro = commands2.InstantCommand(
            lambda: self.robot_drive.gyro.reset(),
            self.robot_drive
        )
        self.driverController.a().onTrue(reset_gyro)

