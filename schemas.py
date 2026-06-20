from pydantic import BaseModel, Field


class InputData(BaseModel):
    AnxietSev_23: int = Field(..., ge=0, le=3)
    learning_23: int = Field(..., ge=0, le=1)
    ASDMed_23: int = Field(..., ge=0, le=1)
    
    K8Q21: int = Field(..., ge=0, le=3)
    DevDelay_23: int = Field(..., ge=0, le=1)
    ReptGrade_23: int = Field(..., ge=0, le=1)
    speech_23: int = Field(..., ge=0, le=1)
    WgtConcn_23: int = Field(..., ge=0, le=3)
    K7Q70_R: int = Field(..., ge=0, le=1)
    K2Q32A: int = Field(..., ge=0, le=1)
    ACE11: int = Field(..., ge=0, le=1)
    K7Q83_R: int = Field(..., ge=0, le=1)
    K7Q82_R: int = Field(..., ge=0, le=1)
    curious6to17_23: int = Field(..., ge=0, le=1)
    K7Q85_R: int = Field(..., ge=0, le=1)
    K7Q84_R: int = Field(..., ge=0, le=1)
    DiffMem_23:int
    behavior_23: int = Field(..., ge=0, le=3)
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

    MealSkip_23: int = Field(..., ge=0, le=1)
    GRADES: int = Field(..., ge=0, le=3)
    MAKEFRIEND: int = Field(..., ge=0, le=1)

    PrntCncrn_23: int = Field(..., ge=0, le=3)
    SchlMiss_23: int = Field(..., ge=0, le=3)
    ACE6: int = Field(..., ge=0, le=1)
    bullied_23: int = Field(..., ge=0, le=1)
    
    LowInterest_23: int = Field(..., ge=0, le=1)
    DailyAct_23: int = Field(..., ge=0, le=1)
    binge_23: int = Field(..., ge=0, le=1)
    
    SC_SEX: int = Field(..., ge=0, le=1)
    PickyEat_23: int = Field(..., ge=0, le=1)
    SpeechSev_23: int = Field(..., ge=0, le=3)
    
    bully_23: int = Field(..., ge=0, le=1)
    DevDelSev_23: int = Field(..., ge=0, le=3)
    DepresSev_23: int = Field(..., ge=0, le=3)
    BehavSev_23: int = Field(..., ge=0, le=3)
