from pydantic import BaseModel, Field


class InputData(BaseModel):
    AnxietSev_23: int 
    learning_23: int 
    ASDMed_23: int 
    
    K8Q21: int 
    DevDelay_23: int 
    ReptGrade_23: int 
    speech_23: int 
    WgtConcn_23: int 
    K7Q70_R: int
    K2Q32A: int 
    ACE11: int 
    K7Q83_R: int 
    K7Q82_R: int 
    curious6to17_23: int 
    K7Q85_R: int 
    K7Q84_R: int 
    DiffMem_23:int
    behavior_23: int 
    ACE7: int
    ACE10: int
    ACE11:int

    ACE9:int
    ACE1:int
    ACE6:int
    ACE3:int
    ACE4: int
    ACE5:int
    ACE6:int
    ACE7:int
    ACE8:int
    ACE9:int

    MealSkip_23: int
    GRADES: int
    MAKEFRIEND: int 

    PrntCncrn_23: int 
    SchlMiss_23: int
    ACE6: int 
    bullied_23: int
    
    LowInterest_23: int
    DailyAct_23: int 
    binge_23: int 
    
    SC_SEX: int 
    PickyEat_23: int 
    SpeechSev_23: int 
    
    bully_23: int 
    DevDelSev_23: int 
    DepresSev_23: int 
    BehavSev_23: int 


    DiffBreath_23: int
    DiffPain_23: int 
    DiffMem_23: int
    DiffWalk_23: int
    DiffDress_23: int 
    DiffErrand_23: int
    hearing_23:int
    vision_23: int
    DiffDigest_23: int
    DiffSwall_23: int
