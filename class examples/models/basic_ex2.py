from pydantic import BaseModel
from typing import List
from enum import Enum

class Genre(str, Enum):
	FICTION = 'Fiction'
	NONFICTION = 'Nonfiction'
	SCIENCE_FICTION = 'Science Fiction'
	FANTASY = 'Fantasy'
	MYSTERY = 'Mystery'
	BIOGRAPHY = 'Biography'


class Book(BaseModel):
	book_id: str
	title: str
	authors: List[str]
	publication_year: int
	available_copies: int
	genre: Genre
