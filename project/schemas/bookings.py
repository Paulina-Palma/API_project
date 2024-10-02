from datetime import datetime
from pydantic import BaseModel, PositiveInt, PositiveFloat, model_validator
from typing import Optional


class BookingSchema(BaseModel):
    id: Optional[PositiveInt]
    spaceship_id: PositiveInt
    customer_id: PositiveInt
    date_start: datetime
    date_end: datetime
    total_cost: PositiveFloat

    class Config:
        orm_mode = True  # To allow compatibility with ORM models

    # Model-level validator to check date_start and date_end after all fields are initialized
    @model_validator(mode='after')
    def validate_dates(cls, values):
        date_start = values.date_start
        date_end = values.date_end

        if date_end < date_start:
            raise ValueError('date_end should be greater than date_start')

        return values
    # root_validator is deprecated - we use model_validator instead
    #
    # another way to check it:

    # def validate_dates(cls, values):
    #     if values.get('date_end') < values.get('date_start'):
    #         raise ValueError('date_end should be greater than date_start')
    #     return values

    # # Validator for the start and end dates
    # @field_validator('date_end')
    # def validate_dates(cls, date_end, info: FieldValidationInfo):
    #     date_start = info.data.get('date_start')
    #     if date_start and date_end < date_start:
    #         raise ValueError('date_end should be greater than date_start')
    #     return date_end
