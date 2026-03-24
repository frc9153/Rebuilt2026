import json
import commands2
from ntcore import NetworkTableInstance
from constants import DriveConstants

# -- NOTES FOR WHOEVER WRITTEN BY THE HIGH QUEEN OF MAGICA --
# 1. Calibrate via setup here: https://docs.limelightvision.io/docs/docs-limelight/pipeline-apriltag/apriltags
# 2. I can't test this code. I don't have a robot in my little tower cell
# 3. !! SET A TAG FILTER FOR ONE ID PER EACH SIDE (SINCE THEYRE DIFFERNET PER RED/BLUE TEAM I THINK) !!
# 4. MAKE SURE TO TUNE ISPASTCLIMBALIGNMENTPOINT OR YOU JUST MIGHT GET YOUR PINKY EATEN

class turretCameraSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        # name of table can change depending on wat we name it... be careful
        self.table = NetworkTableInstance.getDefault().getTable("limelight")
        self.tx = self.table.getDoubleTopic("tx").subscribe(0.0)
        self.ta = self.table.getDoubleTopic("ta").subscribe(0.0)
        self.pose = self.table.getDoubleArrayTopic("botpose").subscribe([])

    def isPastClimbAlignmentPoint(self) -> bool:
        # TODO: CHANGE THIS CONDITION!!!
        # jamie add-on note for geniuses:
        # the value below is the HORIZONTAL OFFSET of the camera to the apriltag
        # if the value is equal to 0.0, the robot is perfectly centered
        # if the value is LESS than 0.0, the target is to the right 
        # if the value is MORE than 0.0, the target is to the left
        # tune... tune... tune... please tune... please... 
        return self.ta.get() > 0.1
    
    def centerPlease(self) -> float:
        return (self.tx.get() / 27) * DriveConstants.kAutoSpeed

    def get_field_pose(self) -> list[float]:
        raise self.pose.get()

    # def get_pose(self):
    #     return self.pose.get()
    # 
    # def periodic(self) -> str:
    #     print(self.get_raw_data())
