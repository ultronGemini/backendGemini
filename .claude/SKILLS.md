# Claude Skills — Change Log

Registro de cambios realizados por Claude en este proyecto.
Formato: fecha · archivos afectados · acción brevísima.

---

## 2026-05-09

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
