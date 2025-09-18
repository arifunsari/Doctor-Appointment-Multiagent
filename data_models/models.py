import re # import regular expression
from pydantic import BaseModel, Field, field_validator

# with the help of Basemodel we convert the class into pydantic
# field_validator 

class DateTimeModel(BaseModel): # it will check the format of the date and tiime
    date:str=Field(description="Properly formatted date", pattern=r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$')
    ## we check date will be upto 2 digit, month 2digit, year 4 digit , hourr and minute
    
    @field_validator("date") #validation of data time  used that wheter it is correct or not following the pattern or not.
    def check_format_date(cls, v):
        if not re.match(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$', v):  # Ensures 'DD-MM-YYYY HH:MM' format
            raise ValueError("The date should be in format 'DD-MM-YYYY HH:MM'")
        return v
    
class DateModel(BaseModel):# It only for time, like koi sirf date daga then we will check , then we can validate the using this class
    date: str = Field(description="Properly formatted date", pattern=r'^\d{2}-\d{2}-\d{4}$')
    @field_validator("date")
    def check_format_date(cls, v):
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', v):  # Ensures DD-MM-YYYY format
            raise ValueError("The date must be in the format 'DD-MM-YYYY'")
        return v
     
class IdentificationNumberModel(BaseModel): # ID number must be 7-8 digit, agat isse jyada ya kam hoga then error, so for the validation we use this.
    id: int = Field(description="Identification number (7 or 8 digits long)")
    @field_validator("id")
    def check_format_id(cls, v):
        if not re.match(r'^\d{7,8}$', str(v)):  # Convert to string before matching
            raise ValueError("The ID number should be a 7 or 8-digit number")
        return v