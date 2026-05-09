import json
import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

_MODEL = "gemini-3.1-flash-lite"
_JSON_CONFIG = {"response_mime_type": "application/json"}


def _model() -> genai.GenerativeModel:
    return genai.GenerativeModel(model_name=_MODEL, generation_config=_JSON_CONFIG)


async def get_visual_palette(topic: str) -> dict:
    prompt = f"""
    You are a professional visual artist and color theorist.
    Given the topic "{topic}", return a JSON object with exactly these keys:
    - "palette": array of exactly 5 complementary HEX color codes (e.g. "#A3C4BC")
    - "composition_tip": one concise artistic composition tip inspired by the topic
    - "opposite_prompt": a vivid text prompt to generate an image of the conceptual opposite
      of the topic (example: if topic is "ice", the opposite prompt should evoke "lava")
    Return only valid JSON, no extra text.
    """
    response = await _model().generate_content_async(prompt)
    return json.loads(response.text)


async def get_musical_mood(emotion: str) -> dict:
    prompt = f"""
    You are a music composer and producer.
    Given the emotion "{emotion}", return a JSON object with exactly these keys:
    - "tempo": recommended BPM as an integer
    - "key": musical key and mode (e.g. "D minor", "G major")
    - "instruments": array of 3 to 5 instrument names that best convey this emotion
    - "mood_description": one sentence describing the intended sonic atmosphere
    This output will be passed to the Lyria 3 music generation model.
    Return only valid JSON, no extra text.
    """
    response = await _model().generate_content_async(prompt)
    return json.loads(response.text)


async def get_writer_quiz(context: str) -> dict:
    prompt = f"""
    You are a creative writing coach specializing in narrative unblocking.
    Given the writing context "{context}", generate exactly 3 "Would You Rather" questions
    designed to help a writer make bold story decisions and overcome creative block.
    Return a JSON object with exactly this key:
    - "questions": array of 3 objects, each with:
        - "id": integer 1 to 3
        - "question": the full "Would you rather..." question string
        - "option_a": first option
        - "option_b": second option
    Return only valid JSON, no extra text.
    """
    response = await _model().generate_content_async(prompt)
    return json.loads(response.text)
