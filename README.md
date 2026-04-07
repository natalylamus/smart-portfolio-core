#  SmartPortfolio Core

Sistema de gestión de portafolio de inversiones desarrollado en Python moderno.

##  Integrantes
| Nombre | Rol |
|---|---|
| Nathaly Lamus | 🏗️ Arquitecta (Repository Owner) |
| Nathaly Ospitia | 💻 Desarrolladora - Modelos |
| Laura Roa | 💻 Desarrolladora - Reportes |

##  Arquitectura
smart-portfolio-core/
├── src/
│   ├── __init__.py
│   ├── modelos.py
│   ├── portafolio.py
│   └── reportes.py
├── tests/
│   ├── conftest.py
│   └── test_models.py
├── main.py
└── pyproject.toml

##  Resultados de Tests y Cobertura
| Módulo | Cobertura |
|---|---|
| src/modelos.py | 100%  |
| src/portafolio.py | 100%  |
| src/reportes.py | 100% |
| **TOTAL** | **100%**  |

##  Cómo ejecutar
# Correr el sistema
python main.py

# Correr tests con cobertura
PYTHONPATH=. poetry run pytest -v --cov=src --cov-report=term-missing
