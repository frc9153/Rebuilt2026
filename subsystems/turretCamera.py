import commands2
from ntcore import NetworkTableInstance

class turretCameraSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        # name of table can change depending on wat we name it... be careful
        self.table = NetworkTableInstance.getDefault().getTable("limelight")

        self.tx = self.table.getDoubleTopic("tx").subscribe(0.0) # horizontal offset
        self.ty = self.table.getDoubleTopic("ty").subscribe(0.0) # vertical offset
        self.tv = self.table.getIntegerTopic("tv").subscribe(0)  # do we see a valid target
        self.ta = self.table.getDoubleTopic("ta").subscribe(0.0) # area of target on screen

        # ok time for weird things:
        self.tl = self.table.getDoubleTopic("tl").subscribe(0.0) # what's the pipeline latency
        self.cl = self.table.getDoubleTopic("cl").subscribe(0.0) # what's the capture latency

        self.botpose = self.table.getFloatArrayTopic("botpose").subscribe([0.0] * 6) # gets x, y, z coordinates (supposedly?) and field rotation... idk ask gemini.

    # ok so this one takes our valid target thing and turns it into a true/false
    def has_target(self) -> bool:
        return self.tv.get() == 1

    # how far left/right is the crosshair
    def get_horizontal_offset(self) -> float:
        return self.tx.get()
    
    # how far up/down is the crosshair
    def get_vertical_offset(self) -> float:
        return self.ty.get()

    # what is the latency in seconds
    def get_total_latency(self) -> float:
        return (self.tl.get() + self.cl.get()) / 1000.0

    # gets x, y, z, yaw, pitch, and roll in field coordinates
    def get_robot_pose(self):
        return self.botpose.get()
    
    # ask claire abt the rest... ummm