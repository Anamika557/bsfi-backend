from pydantic import BaseModel, ConfigDict


class SolutionCreate(BaseModel):
    name: str
    description: str | None = None


class SolutionResponse(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)