import asyncio
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google.genai import errors as genai_errors
from app.infra.creative_agents import get_visual_palette, get_musical_mood, get_writer_quiz

router = APIRouter(prefix="/api/v1")

_TIMEOUT = 5.0

_MOCKS = {
    "visual": {
        "palette": ["#1A1A2E", "#16213E", "#0F3460", "#E94560", "#F5A623"],
        "composition_tip": "Use rule of thirds with high contrast between warm and cool tones.",
        "opposite_prompt": "A volcanic eruption at sunset, molten lava flowing over black rock.",
    },
    "musical": {
        "tempo": 92,
        "key": "D minor",
        "instruments": ["cello", "synthesizer pad", "sparse piano", "ambient guitar"],
        "mood_description": "A melancholic yet hopeful atmosphere, like rain clearing after a storm.",
    },
    "writer": {
        "questions": [
            {
                "id": 1,
                "question": "Would you rather your protagonist lose their memory or their voice?",
                "option_a": "Lose their memory",
                "option_b": "Lose their voice",
            },
            {
                "id": 2,
                "question": "Would you rather the story end in sacrifice or in exile?",
                "option_a": "Sacrifice",
                "option_b": "Exile",
            },
            {
                "id": 3,
                "question": "Would you rather reveal the villain in act one or the final page?",
                "option_a": "Act one",
                "option_b": "Final page",
            },
        ]
    },
}


class InspireRequest(BaseModel):
    creative_mode: str
    user_input: str


@router.post("/inspire")
async def inspire(body: InspireRequest):
    mode = body.creative_mode.lower()

    if mode == "visual":
        coro = get_visual_palette(body.user_input)
    elif mode == "musical":
        coro = get_musical_mood(body.user_input)
    elif mode == "writer":
        coro = get_writer_quiz(body.user_input)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid creative_mode '{mode}'. Use: visual, musical, writer.")

    try:
        result = await asyncio.wait_for(coro, timeout=_TIMEOUT)
        return {"source": "gemini", "mode": mode, "data": result}
    except asyncio.TimeoutError:
        return {"source": "mock", "mode": mode, "data": _MOCKS[mode]}
    except genai_errors.ClientError as e:
        if e.code == 429:
            return {"source": "mock", "mode": mode, "data": _MOCKS[mode]}
        raise HTTPException(status_code=500, detail=f"Gemini error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {e}")
