from pydantic import BaseModel

class CustomerData(BaseModel):

    tenure:int
    MonthlyCharges:float
    TotalCharges:float

    gender:str
    Partner:str
    Dependents:str
    PhoneService:str
    MultipleLines:str
    InternetService:str
    OnlineSecurity:str
    OnlineBackup:str
    DeviceProtection:str
    TechSupport:str
    StreamingTV:str
    StreamingMovies:str
    Contract:str
    PaperlessBilling:str
    PaymentMethod:str