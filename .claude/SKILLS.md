# Claude Skills — Change Log

Registro de cambios realizados por Claude en este proyecto.
Formato: fecha · archivos afectados · acción brevísima.

---

## 2026-05-09

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
