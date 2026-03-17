import json
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

    def get_raw_data(self):
        j = self.table.getString("json")
        data = json.loads(j)
        print(data)
    
    def periodic(self) -> str:
        print(self.get_raw_data())