# Incident Response Playbook 🛡️

Proyecto de playbook de respuesta a incidentes de ciberseguridad desarrollado en Python.

## Funcionalidades
- Respuesta a incidentes de Phishing, Malware y Ransomware.
- Generación de reportes.
- Enriquecimiento de amenazas (futuro).
- Reportes en múltiples formatos: JSON, PDF.

## Estructura
- `main.py`: Punto de entrada del programa.
- `src/`: Lógica principal del playbook.
- `reports/`: Directorio para guardar los reportes generados.

## Cómo usar

```bash
python main.py

Requisitos
Python 3.x

Recomendado: Crear un entorno virtual.

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
