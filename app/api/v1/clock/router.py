from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
from .services import gen_event

router = APIRouter(prefix="/clock", tags=["Clock"])

@router.get("/stream")
async def get_event_stream():
    return EventSourceResponse(gen_event())