#!/usr/bin/env bash
set -e

echo "1) Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

echo "2) Instalando dependencias Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "¡Entorno local listo!"
echo "Para jugar localmente:"
echo "  source venv/bin/activate"
echo "  python src/spacemax_defender.py"
