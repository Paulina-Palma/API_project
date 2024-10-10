from pydantic import BaseModel, field_validator, PositiveInt, Field
from string import ascii_uppercase


class CustomerCreateSchema(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    address: str = Field(min_length=3, max_length=100)
    phone: str
    email: str
    document_number: str = Field(min_length=9, max_length=9)

    class Config:
        from_attributes = True


class CustomerSchema(BaseModel):
    id: PositiveInt
    name: str = Field(min_length=3, max_length=100)
    address: str = Field(min_length=3, max_length=100)
    phone: str
    email: str
    document_number: str = Field(min_length=9, max_length=9)

    class Config:
        from_attributes = True  # To allow compatibility with ORM models

    @field_validator('document_number')
    def validate_id_number(cls, id_number: str) -> str:
        '''
        validator for polish id numbers
        :param id_number: str
        :return: str
        '''
        check_numbers = [7, 3, 1, 7, 3, 1, 7, 3]
        # Ensure that the id_number has exactly 9 characters
        if len(id_number) != 9:
            raise ValueError('Document number must be exactly 9 characters long')
        # Convert characters to appropriate numeric values (letters to 10-35, digits stay as they are)
        # values = [int(char) if not char.isalpha() else ascii_uppercase.find(char) + 10 for char in id_number]
        values = [int(char) if char.isdigit() else ascii_uppercase.index(char.upper()) + 10 for char in id_number]

        # Extract the control number (4th character, index 3)
        control_number = values.pop(3)
        # Perform the checksum calculation
        sum_control = sum(cn * value for cn, value in zip(check_numbers, values))
        # sum_control = sum(check_numbers * value for check_numbers, value in zip(check_numbers, values))
        # Validate the checksum (sum_control mod 10 must equal the control number)
        if sum_control % 10 != control_number:
            raise ValueError('Document number is not valid')

        return id_number
