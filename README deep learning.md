# Détection des maladies de la tomate par CNN : du laboratoire au champ

Projet de fin de module Deep Learning (cohorte 3 AI hub).

Objectif : construire un classifieur de maladies de la feuille de tomate qui fonctionne sur des photos de terrain, et mesurer l'écart entre des images de laboratoire (PlantVillage) et des images réelles (PlantDoc).

## Contenu du dépôt

| Fichier | Rôle |
|---|---|
| `Projet_CNN_Tomate.ipynb` | Notebook reproductible (étapes 2 à 5 de l'énoncé) |
| `download_data.sh` | Télécharge PlantVillage (tomate) et PlantDoc |
| `requirements.txt` | Dépendances Python |
| `fiche_impact.pdf` | Fiche d'impact (1 page) |
| `rapport.pdf` | Rapport technique (5 à 8 pages) |

## Classes étudiées

6 classes présentes dans les deux jeux de données : saine, tache bactérienne, alternariose (early blight), mildiou (late blight), septoriose, virus de l'enroulement jaune (yellow leaf curl).

## Exécution sur Google Colab (recommandé)

1. Ouvrir `Projet_CNN_Tomate.ipynb` dans Colab.
2. Activer un GPU : `Exécution > Modifier le type d'exécution > GPU (T4)`.
3. `Exécution > Tout exécuter`. Le notebook télécharge lui-même les données (même commandes que `download_data.sh`). Durée : environ 20 à 30 minutes.
4. Les résultats (CSV, graphique, poids du modèle final) sont écrits dans `/content/outputs`.

## Exécution en local

```bash
pip install -r requirements.txt
bash download_data.sh ./data
```

Puis adapter les chemins `PV_ROOT` et `PD_ROOT` dans la cellule de configuration du notebook, et lancer Jupyter.

## Protocole expérimental

- Découpage stratifié sans fuite : PlantVillage 70/15/15, PlantDoc 50/15/35 (les ensembles `train` et `test` officiels de PlantDoc sont regroupés puis redécoupés). Doublons exacts supprimés par hash, absence de recouvrement vérifiée.
- Le choix des modèles se fait uniquement sur les jeux de validation, jamais sur les jeux de test.
- Graine fixée (`SEED = 42`). Un seul run par configuration.
- Métrique principale : rappel macro et F1 macro, avec le taux de maladies prises pour saines. L'accuracy n'est jamais utilisée pour conclure.

## Modèles et stratégies comparés

MLP baseline, CNN A (3 blocs sans BN), CNN B (3 blocs avec BN), CNN C (4 blocs avec BN), augmentation forte avec changement de fond, fine-tuning sur 10/25/50/100 % de PlantDoc, entraînement mixte PV+PD, mixte avec augmentation, PlantDoc seul. Analyse d'erreurs, matrices de confusion et Grad-CAM pour le modèle final.

## Limites

Voir la section « Limites et risques » du rapport : effectifs réduits sur PlantDoc test, un seul run par configuration, photos multiples d'une même feuille dans PlantVillage, étiquettes PlantDoc non vérifiées par un expert, aucune validation sur le terrain.

## Auteurs

À compléter (noms du groupe).
Monique SENE