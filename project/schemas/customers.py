from pydantic import BaseModel, field_validator, PositiveInt, Field
from typing import Optional
from string import ascii_uppercase


class CustomerSchema(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=100)
    address: str = Field(min_length=3, max_length=100)
    document_number: str = Field(min_length=9, max_length=9)

    @field_validator('document_number')
    def validate_id_number(cls, id_number: str) -> str:
        '''
        validator for polish id numbers
        :param id_number: str
        :return: str
        '''
        check_numbers = [7, 3, 1, 7, 3, 1, 7, 3]
        values = [int(char) if not char.isalpha() else ascii_uppercase.find(char) + 10 for char in id_number]
        control_number = values.pop(3)
        sum_control = sum(check_numbers * value for check_numbers, value in zip(check_numbers, values))
        if not sum_control % 10 == control_number:
            raise ValueError('Document number is not valid')

        return id_number
