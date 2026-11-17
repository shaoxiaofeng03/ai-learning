## model的请求，model的响应
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class EchoIn(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    remark: str | None = Field(default=None, max_length=100, description="可选的备注信息")


class EchoOut(BaseModel):
    text: str
    length: int
    remark: str | None = Field(default=None, max_length=100, description="可选的备注信息")


@router.post("/echo_model", response_model=EchoOut)
def echo_model(payload: EchoIn) -> EchoOut:
    return EchoOut(text=payload.text, length=len(payload.text), remark=payload.remark)
