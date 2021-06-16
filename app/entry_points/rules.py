from fastapi import APIRouter
from app.schema.inputs import Input
from app.services_layer.rules import Rules

router = APIRouter(
    prefix="/api"
)


@router.post("/")
async def index(input: Input):
    return Rules().evalue(input)


