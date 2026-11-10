"""Téléchargement des données du projet (tomate uniquement).

Usage :
    python download_data.py

Résultat :
    data/PlantVillage-Dataset/raw/color/Tomato___*   (images de laboratoire)
    data/PlantDoc-Dataset/{train,test}/Tomato*       (images de terrain)
"""
import subprocess
from pathlib import Path

DATA = Path("data")
DATA.mkdir(exist_ok=True)


def run(cmd, cwd=None):
    print(">", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


# --- PlantVillage : on ne récupère que les classes Tomato___* ---
pv = DATA / "PlantVillage-Dataset"
if not pv.exists():
    run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
         "https://github.com/spMohanty/PlantVillage-Dataset.git", str(pv)])
    run(["git", "sparse-checkout", "set", "--no-cone", "raw/color/Tomato___*"], cwd=pv)
else:
    print("PlantVillage déjà présent.")

# --- PlantDoc ---
pd_dir = DATA / "PlantDoc-Dataset"
if not pd_dir.exists():
    run(["git", "clone", "--depth", "1",
         "https://github.com/pratikkayal/PlantDoc-Dataset.git", str(pd_dir)])
else:
    print("PlantDoc déjà présent.")

print("Terminé.")
