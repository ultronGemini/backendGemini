# Claude Skills — Change Log

Registro de cambios realizados por Claude en este proyecto.
Formato: fecha · archivos afectados · acción brevísima.

---

## 2026-05-09

### [FIX] 429 quota fallback
- **Modificado**: `app/api/creative_routes.py` — captura `ClientError` 429 de Gemini y cae al mock automáticamente (demo-safe).

### [FIX] SDK migration + pydantic extra fields
- **Modificado**: `app/infra/creative_agents.py` — migrado de `google.generativeai` (deprecado) a `google.genai` con `_client.aio.models.generate_content`.
- **Modificado**: `app/core/config.py` — añadido `"extra": "ignore"` para tolerar campos extra en `.env`.
- **Modificado**: `requirements.txt` — reemplazado `google-generativeai` por `google-genai`.

### [APP] main.py
- **Agregado**: `app/main.py` — FastAPI app con `include_router` de creative_routes.

### [TEST] test_agents.py
- **Agregado**: `test_agents.py` — script manual con `requests` para probar los 3 modos contra el server local.

### [API] Creative Routes
- **Agregado**: `app/api/creative_routes.py` — `POST /api/v1/inspire` con routing por `creative_mode`, timeout 5s y mocks de fallback por modo.

### [INFRA] Creative Agents
- **Agregado**: `app/infra/creative_agents.py` — 3 funciones async (`get_visual_palette`, `get_musical_mood`, `get_writer_quiz`) con Gemini `gemini-3.1-flash-lite` y `response_mime_type=application/json`.

### [CORE] Config + Requirements
- **Agregado**: `app/core/config.py` — `Settings` con `GEMINI_API_KEY` via pydantic-settings + dotenv.
- **Modificado**: `requirements.txt` — fastapi, uvicorn[standard], python-dotenv, google-generativeai, pydantic-settings.

### [SKILL] Caveman
- **Agregado**: `app/skills/caveman.py` — skill `CAVEMAN_INSTRUCTIONS` (artista cavernícola, lenguaje primitivo).
- **Agregado**: `app/skills/__init__.py` — módulo de skills con export de Caveman.

### [INIT]
- **Agregado**: `.claude/SKILLS.md` — creación de este archivo de seguimiento de cambios.

---
<!-- Nuevas entradas van ARRIBA de esta línea, dentro de su fecha correspondiente -->
