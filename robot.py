#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import typing

import hal
import commands2

import robotcontainer


class MyRobot(commands2.TimedCommandRobot):
    """
    Command-based robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you.
    """

    def robotInit(self) -> None:
        self.autonomousCommand: typing.Optional[commands2.Command] = None

        # Instantiate our RobotContainer. This will perform all our button bindings,
        # and put our autonomous chooser on the dashboard.
        self.container = robotcontainer.RobotContainer()

        # Used to track usage of Kitbot code, please do not remove.
        hal.report(hal.tResourceType.kResourceType_Framework, 10)

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.getAutonomousCommand()

        # schedule the autonomous command (example)
        if self.autonomousCommand is not None:
            self.autonomousCommand.schedule()

    def teleopInit(self) -> None:
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    def testInit(self) -> None:
        # Cancels all running commands at the start of test mode.
        commands2.CommandScheduler.getInstance().cancelAll()