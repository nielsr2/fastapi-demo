from pydantic import BaseModel
from typing import List

class Book(BaseModel):
	book_id: str
	title: str
	authors: List[str]
	publication_year: int
	available_copies: int
