import json
import commands2
from ntcore import NetworkTableInstance

class turretCameraSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        # name of table can change depending on wat we name it... be careful
        self.table = NetworkTableInstance.getDefault().getTable("limelight")
        self.pose = self.table.getDoubleArrayTopic("botpose").subscribe([])

    def get_pose(self):
        return self.pose.get()
    
    def periodic(self) -> str:
        print(self.get_raw_data())