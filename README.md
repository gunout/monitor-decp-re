# 🇫🇷 Monitor DECP — Tableau de bord des Marchés Publics

> **Monitor interactif et autonome pour explorer les Données Essentielles de la Commande Publique (DECP)**  
> Lecture automatique des fichiers `decp-*.json` · Visualisations · Filtres · Exports

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![DSFR](https://img.shields.io/badge/DSFR-1.11.2-000091?style=flat-square)](https://www.systeme-de-design.gouv.fr/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Zero Dependency](https://img.shields.io/badge/dependencies-0-brightgreen?style=flat-square)]()
[![Data: DECP](https://img.shields.io/badge/data-DECP%202021--2026-003399?style=flat-square)](https://www.data.gouv.fr/fr/datasets/donnees-essentielles-de-la-commande-publique-fichiers-consolides/)

---

## 📸 Aperçu

```
┌─────────────────────────────────────────────────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░███████████████████ │  ← Bandeau UE
├─────────────────────────────────────────────────────────────────────┤
│ RÉPUBLIQUE FRANÇAISE · Liberté Égalité Fraternité                   │
├─────────────────────────────────────────────────────────────────────┤
│ ● MONITOR DECP  / marchés publics   [🔍][📊][📁]   STATUT 6/6 · 67 │
├──────────────┬────────────────────────────────────┬─────────────────┤
│ 📅 Années    │  🔍 Rechercher un marché...        │ 📊 INTELLIGENCE │
│ ─────────────│  ─────────────────────────────     │ ─────────────── │
│ ☑ 2021       │  [Marchés] [Montant] [Moyenne]...  │ Total : 67      │
│ ☑ 2022       │  ─────────────────────────────     │ Montant : 15 M€ │
│ ☑ 2023       │  📋 2026T00023 — GGR_26012026      │ Titulaires : 35 │
│ ☑ 2024       │  🏢 Acheteur · Titulaire           │ CPV : 25        │
│ ☑ 2025       │  CPV 45200000 · Dépt 974 · 10 M€   │ Activité : …    │
│ ☑ 2026       │  📋 2026T00013 — Construction...   │                 │
│              │  📋 202600042T — RLE_27012026      │                 │
└──────────────┴────────────────────────────────────┴─────────────────┘
```

---

## 📖 Sommaire

- [✨ Fonctionnalités](#-fonctionnalités)
- [🚀 Démarrage rapide](#-démarrage-rapide)
- [📁 Structure du projet](#-structure-du-projet)
- [🗂️ Format des données](#️-format-des-données)
- [🎛️ Utilisation](#️-utilisation)
- [📊 Vue Analyses](#-vue-analyses)
- [📁 Vue Fichiers](#-vue-fichiers)
- [🎨 Design System](#-design-system)
- [🔧 Personnalisation](#-personnalisation)
- [⚠️ CORS et `file://`](#️-cors-et-file)
- [🧪 Tests et validation](#-tests-et-validation)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contribution](#-contribution)
- [📄 Licence](#-licence)

---

## ✨ Fonctionnalités

| Catégorie | Fonctionnalité | Statut |
|---|---|:---:|
| **Chargement** | Lecture automatique de `decp-2021.json` → `decp-2026.json` | ✅ |
| | Gestion d'erreur par fichier (dégrade gracieusement) | ✅ |
| | Déduplication des IDs identiques entre fichiers | ✅ |
| | Extraction du montant après modification | ✅ |
| **Filtres** | Sélection d'années (sidebar à cases à cocher) | ✅ |
| | Recherche plein texte (objet, ID, SIRET, CPV…) | ✅ |
| | Debounce 250 ms sur la recherche | ✅ |
| | Tri dynamique : montant ↑↓, date ↑↓ | ✅ |
| **Visualisations** | 6 KPI cards : Total, Montant, Moyenne, Médiane, Max, À 0 € | ✅ |
| | Graphique montant par année | ✅ |
| | Graphique montant par procédure | ✅ |
| | Top 12 fournisseurs | ✅ |
| | Top 12 codes CPV | ✅ |
| | Répartition par département | ✅ |
| | Répartition par nature | ✅ |
| **Navigation** | Pagination complète (⏮ ← page → ⏭) | ✅ |
| | Taille de page : 10 / 25 / 50 / 100 / 500 | ✅ |
| **Vues** | 📋 Résultats · 📄 JSON brut · ⏱️ Statistiques | ✅ |
| | 📁 Fichiers (statut, comptage, montant par fichier) | ✅ |
| **Exports** | CSV (UTF-8 avec BOM, compatible Excel) | ✅ |
| | JSON (données filtrées complètes) | ✅ |
| **UX** | Bandeau UE + bloc-marque République Française | ✅ |
| | Colonne Intelligence (4 panneaux + activité) | ✅ |
| | Responsive mobile | ✅ |
| | Zéro dépendance runtime (CDN DSFR uniquement) | ✅ |

---

## 🚀 Démarrage rapide

### 1. Cloner / copier le projet

```bash
mkdir -p ~/Desktop/"dpt ue" && cd ~/Desktop/"dpt ue"
```

Placez dans ce dossier :
- `monitor-decп.html` (le fichier du monitor)
- `decp-2021.json` → `decp-2026.json`

### 2. Lancer un serveur local

> ⚠️ `fetch()` ne fonctionne **pas** sur `file://` à cause des restrictions CORS.

**Python 3** (recommandé) :
```bash
python3 -m http.server 8000
```

**Node.js** :
```bash
npx serve -l 8000
```

**PHP** :
```bash
php -S localhost:8000
```

### 3. Ouvrir le monitor

```
http://localhost:8000/monitor-decп.html
```

---

## 📁 Structure du projet

```
dpt ue/
├── monitor-decп.html          # Monitor autonome (HTML + CSS + JS inline)
├── decp-2021.json             # Données DECP 2021
├── decp-2022.json             # Données DECP 2022
├── decp-2023.json             # Données DECP 2023
├── decp-2024.json             # Données DECP 2024
├── decp-2025.json             # Données DECP 2025
├── decp-2026.json             # Données DECP 2026
├── estat_ilc_di01_en.json     # (optionnel) Autres datasets
└── README.md                  # Ce fichier
```

---

## 🗂️ Format des données

Le monitor attend le **schéma DECP standard** :

```json
{
  "marches": {
    "marche": [
      {
        "id": "2026T00001",
        "acheteur": { "id": "44090956200033" },
        "nature": "Marché",
        "objet": "Prestations de nettoyage...",
        "codeCPV": "90911000",
        "procedure": "Appel d'offres ouvert",
        "lieuExecution": { "code": "01", "typeCode": "Code département" },
        "dureeMois": 4,
        "dateNotification": "2026-01-23",
        "datePublicationDonnees": "2026-01-25",
        "montant": 50000.0,
        "titulaires": [
          { "titulaire": { "typeIdentifiant": "SIRET", "id": "44090956200041" } }
        ],
        "modifications": [
          { "modification": { "id": 1, "montant": 45000.0, "dateNotificationModification": "..." } }
        ]
      }
    ],
    "contrat-concession": []
  }
}
```

### Champs utilisés par le monitor

| Champ JSON | Usage dans le monitor |
|---|---|
| `id` | Identifiant unique, clé de déduplication |
| `objet` | Titre affiché dans la carte résultat |
| `codeCPV` | Badge CPV + agrégation Top 12 |
| `procedure` | Badge procédure + filtre |
| `nature` | Agrégation par nature |
| `lieuExecution.code` | Département / pays |
| `dateNotification` | Tri par date + affichage |
| `montant` | Calculs KPI + tri + agrégations |
| `modifications[].montant` | Remplacé si présent (dernier connu) |
| `titulaires[0].titulaire.id` | SIRET du titulaire principal |
| `acheteur.id` | SIRET acheteur |
| `considerationsSociales` | Badge 🤝 |
| `considerationsEnvironnementales` | Badge 🌱 |
| `sousTraitanceDeclaree` | Badge 🔧 |
| `marcheInnovant` | Badge 💡 |
| `attributionAvance` + `tauxAvance` | Badge 💰 |

---

## 🎛️ Utilisation

### Filtres rapides (sidebar)

| Bouton | Action |
|---|---|
| **Tout** | Active toutes les années |
| **Aucun** | Désactive toutes les années |
| **3 dernières** | Active 2024, 2025, 2026 |

### Raccourcis clavier

| Touche | Action |
|---|---|
| `Entrée` dans la recherche | Lance le filtre immédiatement |
| Clic sur `▶ FILTRER` | Relance le filtre |

### Colonnes triables

Cliquez sur les en-têtes de la table pour trier. Un second clic inverse le tri.

---

## 📊 Vue Analyses

6 graphiques en barres CSS générés dynamiquement à partir des données filtrées :

| # | Graphique | Agrégation |
|---|---|---|
| 1 | Montant par année | `group by year → sum(montant)` |
| 2 | Montant par procédure | `group by procedure → sum(montant)` |
| 3 | Top 12 fournisseurs | `group by titulaire → sum(montant)` |
| 4 | Top 12 CPV | `group by codeCPV → sum(montant)` |
| 5 | Montant par département | `group by dept → sum(montant)` |
| 6 | Montant par nature | `group by nature → sum(montant)` |

---

## 📁 Vue Fichiers

Affiche pour chaque fichier attendu :

- ✅ ou ❌ statut de chargement
- Nombre d'entrées
- Montant cumulé
- Année détectée

Exemple :

```
✅ decp-2021.json     [12 entrées]    12 500 000 €
✅ decp-2022.json     [45 entrées]    48 200 000 €
✅ decp-2023.json     [78 entrées]    92 100 000 €
❌ decp-data-gouv.json  (fichier vide)
```

---

## 🎨 Design System

Le monitor utilise le **Système de Design de l'État (DSFR)** via CDN.

### Palette

| Variable | Valeur | Usage |
|---|---|---|
| `--blue-france` | `#000091` | Texte principal bleu |
| `--blue-eu` | `#003399` | Accent européen |
| `--gold-eu` | `#ffcc00` | Bandeau UE |
| `--red-marianne` | `#E1000F` | Erreurs, alertes |
| `--green-emeraude` | `#00a95f` | Statut OK |
| `--grey-50` | `#f6f6f6` | Fond |
| `--grey-900` | `#1e1e1e` | Texte |

### Typographies

- **Marianne** (DSFR) pour l'UI
- **SF Mono / Menlo / Consolas** pour les valeurs numériques

---

## 🔧 Personnalisation

### Changer la liste des fichiers

Dans `<script>`, modifiez :

```js
const FILES = [
  "decp-2021.json",
  "decp-2022.json",
  "decp-2023.json",
  "decp-2024.json",
  "decp-2025.json",
  "decp-2026.json"
];
```

### Ajouter un fichier data.gouv.fr

Téléchargez le fichier depuis data.gouv.fr, convertissez-le au format DECP si nécessaire, puis ajoutez-le à `FILES`.

```bash
# Exemple : télécharger une ressource
curl -L "https://www.data.gouv.fr/api/1/datasets/r/xxxxx" -o decp-data-gouv.json
```

### Changer la taille de page par défaut

```js
const state = {
  pageSize: 50,   // ← au lieu de 25
  // ...
};
```

### Modifier le seuil du badge « big » (montants ≥ 1 M€)

```js
const montantClass = m.montant >= 500000 ? 'big' : '';  // ← 500 k€ au lieu de 1 M€
```

---

## ⚠️ CORS et `file://`

**Le monitor ne fonctionnera PAS** si vous ouvrez directement `monitor-decп.html` par double-clic (`file://`).

Les navigateurs bloquent `fetch('decp-2021.json')` pour des raisons de sécurité.

### Solutions

| Solution | Commande |
|---|---|
| **Python** (recommandé) | `python3 -m http.server 8000` |
| **Node.js** | `npx serve -l 8000` |
| **PHP** | `php -S localhost:8000` |
| **VS Code** | Extension *Live Server* |

Puis ouvrir `http://localhost:8000/monitor-decп.html`.

---

## 🧪 Tests et validation

### Vérifier que les fichiers sont valides

```bash
for f in decp-*.json; do
  echo -n "$f : "
  python3 -c "import json,sys; d=json.load(open('$f')); print(len(d['marches']['marche']), 'marchés')"
done
```

### Vérifier la somme totale des montants

```bash
python3 << 'EOF'
import json, glob
total = 0
count = 0
for f in glob.glob("decp-*.json"):
    d = json.load(open(f))
    for m in d['marches']['marche']:
        total += m.get('montant', 0) or 0
        count += 1
print(f"{count} marchés · {total:,.2f} €")
EOF
```

---

## 🗺️ Roadmap

- [x] Chargement multi-fichiers DECP
- [x] KPI cards + graphiques
- [x] Pagination + exports CSV/JSON
- [x] Design DSFR + bandeau UE
- [ ] 🔜 Carte de France interactive (Leaflet)
- [ ] 🔜 Comparaison inter-annuelle côte à côte
- [ ] 🔜 Export PDF (rapport de synthèse)
- [ ] 🔜 Mode sombre automatique (`prefers-color-scheme`)
- [ ] 🔜 Détection auto des nouveaux fichiers via `manifest.json`
- [ ] 🔜 Intégration live de l'API data.gouv.fr

---

## 🤝 Contribution

Les contributions sont bienvenues !

1. **Fork** le dépôt
2. Créez une branche : `git checkout -b feature/ma-fonctionnalite`
3. Committez : `git commit -m "Ajoute ma fonctionnalité"`
4. Poussez : `git push origin feature/ma-fonctionnalite`
5. Ouvrez une **Pull Request**

### Conventions

- **HTML** : sémantique, accessible (ARIA si nécessaire)
- **CSS** : variables CSS, pas de framework additionnel
- **JS** : ES6+, `const`/`let`, pas de `var`
- **Commits** : [Conventional Commits](https://www.conventionalcommits.org/)

---

## 📄 Licence

Ce projet est sous licence **MIT**.

```
MIT License

Copyright (c) 2026 Monitor DECP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🔗 Ressources

| Ressource | Lien |
|---|---|
| 📊 DECP — Données essentielles | [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/donnees-essentielles-de-la-commande-publique-fichiers-consolides/) |
| 🎨 Système de Design de l'État | [systeme-de-design.gouv.fr](https://www.systeme-de-design.gouv.fr/) |
| 📖 Documentation DECP | [commande-publique.gouv.fr](https://www.economie.gouv.fr/dae/les-donnees-essentielles-de-la-commande-publique) |
| 🇪🇺 Open Data Européen | [data.europa.eu](https://data.europa.eu/) |

---

## 👤 Auteur

**Monitor DECP** — Projet open source d'analyse de la commande publique française.

<div align="center">

**⭐ Si ce projet vous est utile, n'oubliez pas de laisser une étoile ! ⭐**

Made with ❤️ en France 🇫🇷

</div>

---

<div align="center">

### 🇫🇷 Gunout · 2026

![Made in France](https://img.shields.io/badge/Made_in-France-002395?style=flat-square&labelColor=FFFFFF&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MDAgNjAwIj48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iIzAwMjM5NSIvPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNDAwIiB5PSIxMDAiIGZpbGw9IiNmZmYiLz48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjIwMCIgeT0iNDAwIiBmaWxsPSIjZWQyOTM5Ii8+PC9zdmc+)
![GitHub](https://img.shields.io/badge/GitHub-gunout-181717?style=flat-square&logo=github&logoColor=white)
![Year](https://img.shields.io/badge/2026-ED2939?style=flat-square&labelColor=FFFFFF)

<sub>© 2026 <strong>Gunout</strong> — Tous droits réservés.</sub>

</div>

