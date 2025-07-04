from pydantic import BaseModel
from typing import Optional

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True