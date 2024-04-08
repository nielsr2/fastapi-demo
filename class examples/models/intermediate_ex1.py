from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from enum import Enum

# This model example is an intermediate level example that includes more advanced Pydantic features.
#  - optional fields
#  - field constraints (min_length, max_length, gt (greater than), lt, ge)
#  - description for each field
#  - EmailStr for email validation
# See pydantic documentation for more information: https://pydantic-docs.helpmanual.io/

class Book(BaseModel):
	book_id: str = Field(..., description="Unique identifier for the book")
	title: str = Field(..., min_length=1, max_length=100)
	authors: List[str] = Field(..., description="List of book's authors")
	publication_year: int = Field(..., gt=0, lt=2100, description="Year the book was published")
	publisher_email:  Optional[EmailStr]
	genre: Genre
	available_copies: int = Field(..., ge=0, description="Number of available copies in the library")
	isbn: Optional[str] = Field(None, description="International Standard Book Number")
	summary: Optional[str] = Field(None, max_length=1000, description="Brief summary of the book")

