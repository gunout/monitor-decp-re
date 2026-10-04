<!-- BADGES -->
<div align="center">

# 🇫🇷 Monitor DECP

**Explorateur tout-en-un des marchés publics français**

[![Version](https://img.shields.io/badge/version-7.2-003399?style=for-the-badge&logo=semver&logoColor=white)](https://github.com/gunout/monitor-decp-re/releases)
[![Licence](https://img.shields.io/badge/licence-MIT-00a95f?style=for-the-badge)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
[![Sans dépendance](https://img.shields.io/badge/zéro%20dépendance-✓-18753c?style=for-the-badge)](#-stack-technique)
[![PWA Ready](https://img.shields.io/badge/PWA-ready-5A0FC8?style=for-the-badge&logo=pwa&logoColor=white)](#)

[![Data.gouv.fr](https://img.shields.io/badge/Source-data.gouv.fr-000091?style=flat-square)](https://www.data.gouv.fr/fr/datasets/donnees-essentielles-de-la-commande-publique-fichiers-consolides/)
[![DECP](https://img.shields.io/badge/DECP-2024-ffcc00?style=flat-square)](https://www.data.gouv.fr/)
[![Achats publics](https://img.shields.io/badge/Achats-publics-E1000F?style=flat-square)](https://www.economie.gouv.fr/)

[![Démo](https://img.shields.io/badge/▶%20Démo%20live-003399?style=for-the-badge)](https://gunout.github.io/monitor-decp-re/)
[![Signaler un bug](https://img.shields.io/badge/🐛%20Bug-E1000F?style=for-the-badge)](../../issues/new?template=bug.md)
[![Demander une fonctionnalité](https://img.shields.io/badge/💡%20Idée-00a95f?style=for-the-badge)](../../issues/new?template=feature.md)

![Aperçu](docs/screenshot.png)

</div>

---

## 📖 Sommaire

- [✨ Fonctionnalités](#-fonctionnalités)
- [🚀 Démarrage rapide](#-démarrage-rapide)
- [📸 Captures d'écran](#-captures-décran)
- [🎯 Utilisation](#-utilisation)
- [🏗️ Architecture](#️-architecture)
- [📊 Catégories CPV](#-catégories-cpv)
- [🔍 Détection d'année](#-détection-dannée)
- [⚙️ Paramètres](#️-paramètres)
- [📥 Exports](#-exports)
- [🛠️ Stack technique](#️-stack-technique)
- [🤝 Contribution](#-contribution)
- [📄 Licence](#-licence)
- [🙏 Remerciements](#-remerciements)

---

## ✨ Fonctionnalités

<table>
<tr>
<td width="50%" valign="top">

### 📊 Analyse & Visualisation

- **📋 Liste des marchés** — recherche, tri, pagination
- **📂 Catégories CPV** — 45 catégories normalisées
- **🌍 Carte de France** — coloration par volume
- **📈 Évolution** — graphique linéaire par année
- **⚖️ Comparateur** — 2 années côte à côte
- **📊 Analyses** — camembert, bar charts, top fournisseurs
- **🔍 Rapport qualité** — fiabilité de la détection d'année

</td>
<td width="50%" valign="top">

### ⚡ Performance & UX

- **🚀 Chargement parallèle** (3 workers)
- **💾 Cache IndexedDB** (7 jours, instantané au 2ᵉ chargement)
- **🧵 Web Workers** pour le parsing JSON
- **📊 Progression en temps réel** (Mo, %, statut par fichier)
- **🎬 Animations fluides** (barres, camembert, cartes)
- **🌙 Dark mode** persistant
- **📱 Responsive** (mobile → desktop)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📥 Exports & Filtres

- **📥 CSV** — colonnes configurables
- **📥 JSON** — données brutes filtrées
- **🖼️ PNG** — export du camembert / de la carte
- **🔗 URL partageable** — filtres persistants (`?q=...&cat=...`)
- **📅 Filtres cumulables** — années + catégories + départements + recherche
- **🎯 Sélection multi-fichiers** — API ou glisser-déposer

</td>
<td width="50%" valign="top">

### 🎯 Détection intelligente

- **🆔 Extraction d'année par ID** (multi-formats)
- **📅 Fallbacks** : date notif. → date pub. → fichier → défaut
- **⚙️ Mode strict / auto / ID-only**
- **📊 Rapport de fiabilité** par source
- **🔄 Ré-analyse à chaud** sans recharger
- **🌐 Fonctionne hors ligne** (mode `file://`)

</td>
</tr>
</table>

---

## 🚀 Démarrage rapide

### Option 1 — Utilisation directe (le plus simple)

1. Clonez le repo :

        git clone https://github.com/gunout/monitor-decp-re.git
        cd monitor-decp-re

2. Servez le fichier en local (les Web Workers nécessitent HTTP) :

        python3 -m http.server 8000
        # ou
        npx serve .
        # ou
        php -S localhost:8000

3. Ouvrez **http://localhost:8000** dans votre navigateur 🎉

### Option 2 — Glisser-déposer (sans serveur)

1. Ouvrez `index.html` **directement** dans le navigateur
2. Cliquez sur **📥 CHARGER** ou glissez vos fichiers `decp-*.json`
3. L'application fonctionne **100% hors ligne**

### Option 3 — Déploiement GitHub Pages

1. Activez **GitHub Pages** dans _Settings → Pages → Branch: main_
2. Poussez vos changements :

        git push origin main

3. Accédez à **https://gunout.github.io/monitor-decp-re/**

---

## 📸 Captures d'écran

<details>
<summary><b>📋 Vue Marchés — Recherche et pagination</b></summary>

![Marchés](docs/screenshot-marches.png)

</details>

<details>
<summary><b>📂 Vue Catégories — Grille CPV</b></summary>

![Catégories](docs/screenshot-categories.png)

</details>

<details>
<summary><b>🌍 Carte de France — Répartition géographique</b></summary>

![Carte](docs/screenshot-carte.png)

</details>

<details>
<summary><b>📊 Analyses — Camembert et bar charts</b></summary>

![Analyses](docs/screenshot-analyses.png)

</details>

<details>
<summary><b>📈 Évolution — Graphique par année</b></summary>

![Évolution](docs/screenshot-evolution.png)

</details>

<details>
<summary><b>⚖️ Comparateur — 2 années côte à côte</b></summary>

![Comparateur](docs/screenshot-compare.png)

</details>

<details>
<summary><b>🔍 Rapport qualité — Fiabilité de l'année</b></summary>

![Qualité](docs/screenshot-qualite.png)

</details>

<details>
<summary><b>🌙 Dark mode</b></summary>

![Dark](docs/screenshot-dark.png)

</details>

---

## 🎯 Utilisation

### Charger les données

| Méthode | Avantages | Inconvénients |
|---|---|---|
| **🌐 API data.gouv.fr** (proxy local) | Automatique, toujours à jour | Nécessite un serveur local |
| **📁 Glisser-déposer** | Fonctionne partout, hors ligne | Manuel |
| **🔌 Proxy CORS public** | Sans installation | Lent, peut échouer |

### Raccourcis clavier

| Raccourci | Action |
|---|---|
| `/` | Focus sur la recherche |
| `Échap` | Fermer la modale / annuler |
| `Ctrl/Cmd + clic` | Multi-sélection (catégories, années) |

### Filtres disponibles

    🔍 Recherche libre      → objet, ID, SIRET, CPV, titulaire…
    📅 Années              → 2019, 2020, 2021, 2022, 2023, 2024… (multi)
    📂 Catégories CPV      → 45 catégories (multi)
    🌍 Départements        → clic sur la carte
    💰 Tri                 → montant, date, catégorie, année

---

## 🏗️ Architecture

    monitor-decp-re/
    ├── index.html              # Application complète (single-file)
    ├── README.md
    ├── LICENSE
    ├── docs/
    │   ├── screenshot.png
    │   ├── screenshot-marches.png
    │   └── ...
    └── .github/
        └── workflows/
            └── deploy.yml      # Déploiement GH Pages auto

### Flux de données

    data.gouv.fr API  →  ParserPool (Web Worker)  →  JSON.parse
           ↓
    normalizeMarche  →  Détection année  →  IndexedDB Cache
           ↓
       state.all  →  Filtres  →  Rendu
           ↓
    Vues : Marchés · Catégories · Carte · Analyses · Évolution · Comparateur · Qualité

### Composants clés

| Composant | Rôle |
|---|---|
| **`ParserPool`** | Pool de 2 Web Workers pour le parsing JSON |
| **`Cache`** | Wrapper IndexedDB (TTL 7 jours) |
| **`detectYear()`** | Cœur du fix v7 — extraction intelligente |
| **`normalizeMarche()`** | Uniformisation des données |
| **`renderResults()`** | Routeur de vues |

---

## 📊 Catégories CPV

Mapping basé sur les **2 premiers chiffres** du code CPV :

| Code | Catégorie | Exemples |
|---|---|---|
| `03` `09` | 🌾 Agriculture & Pêche | Produits agricoles, bois |
| `15` | 🍞 Alimentation & Boissons | Denrées, boissons |
| `30` `48` | 💻 Informatique | Matériel, logiciels |
| `34` | 🚗 Véhicules & Transport | Voitures, camions |
| `45` | 🏗️ Travaux de construction | BTP, génie civil |
| `51` `72` | 🖥️ Services IT & R&D | Infogérance, recherche |
| `71` | 📐 Architecture & Ingénierie | Maîtrise d'œuvre |
| `75` `79` | 🏛️ Administratif & Juridique | Services admin, RH |
| `85` | 🏥 Santé & Services sociaux | Médical, social |
| `90` | 🗑️ Environnement & Déchets | Traitement, recyclage |

> 📌 45 catégories couvrent ~95% des codes CPV rencontrés.

---

## 🔍 Détection d'année

### Problème résolu en v7

Dans les fichiers DECP, **le champ `annee` n'existe pas toujours**. Avant, l'application utilisait l'année du **titre du fichier** (`"DECP 2024"`), ce qui faussait les marchés de 2019-2023.

### Solution multi-niveaux

    Priorité 1 : 🆔 ID du marché          "2022-884095-01"  → 2022
    Priorité 2 : 📅 dateNotification      "2022-03-15"      → 2022
    Priorité 3 : 📅 datePublication       idem
    Priorité 4 : 📁 Nom du fichier        "decp-2022.json"  → 2022
    Priorité 5 : ⚙️ Année par défaut      (paramètre user)
    Sinon      : ❓ "—"                    (non détectée)

### Formats d'ID supportés

| Format | Exemple | Résultat |
|---|---|---|
| Année 4 chiffres + tiret | `2022-884095-01` | ✅ 2022 |
| Année 2 chiffres + tiret | `22-076` | ✅ 2022 |
| Préfixe texte | `MP2024-006` | ✅ 2024 |
| Date compacte | `202402031200` | ✅ 2024 |
| Numérique pur | `13033460-2` | ❌ — |

### Modes configurables

| Mode | Comportement |
|---|---|
| **`auto`** ⭐ | ID → dates → fichier → défaut |
| **`id_only`** | Seulement l'ID |
| **`strict`** | ID → dateNotification |

Configurable dans **⚙️ Paramètres** (persistant en localStorage).

---

## ⚙️ Paramètres

Accessible via **⚙️** dans la topbar :

- **📅 Année par défaut** — classe les marchés sans année
- **🔧 Mode d'extraction** — `auto` / `id_only` / `strict`
- **🔄 Ré-analyser les années** — relance la détection à chaud
- **🔍 Voir le rapport qualité** — ouvre l'onglet dédié

---

## 📥 Exports

### CSV (Excel-friendly)

    year,yearSource,categorie,id,objet,codeCPV,procedure,dept,dateNotification,montant,titulaire,acheteur
    2022,id,🏗️ Travaux de construction,2022-884095-01,Transports collectifs...,60112000,Appel d'offres ouvert,44,2022-03-15,45000,SIRET-123,...

- ✅ BOM UTF-8 (`\ufeff`) → accents corrects dans Excel
- ✅ Colonnes configurables
- ✅ Respecte les filtres actifs

### JSON (data-friendly)

Structure identique à `state.filtered`, prête à réutiliser.

### PNG (share-friendly)

- **🖼️ PNG (vue)** — exporte la vue active
- **🖼️ PNG** sur le camembert → image haute résolution (×2)
- **🖼️ PNG** sur la carte → carte + légende

---

## 🛠️ Stack technique

<div align="center">

| Technologie | Utilisation |
|---|---|
| **HTML5** | Structure |
| **CSS3** | Custom properties, dark mode |
| **Vanilla JS** | Aucune dépendance |
| **Web Workers** | Parsing JSON non-bloquant |
| **IndexedDB** | Cache local 7 jours |
| **SVG** | Carte, camembert, lignes |
| **Canvas** | Export PNG |

</div>

### Compatibilité

| Navigateur | Version minimale |
|---|---|
| Chrome / Edge | 90+ |
| Firefox | 88+ |
| Safari | 14+ |
| Mobile (iOS/Android) | ✅ |

> ⚠️ Les Web Workers ne fonctionnent pas en `file://` — fallback synchrone automatique.

---

## 🤝 Contribution

Les contributions sont **les bienvenues** !

### Comment contribuer

1. **Fork** le repo
2. **Créez une branche** : `git checkout -b feature/ma-fonctionnalite`
3. **Committez** : `git commit -m 'feat: ajout X'`
4. **Poussez** : `git push origin feature/ma-fonctionnalite`
5. **Ouvrez une Pull Request**

### Conventions de commit

Nous utilisons [Conventional Commits](https://www.conventionalcommits.org/) :

    feat:     Nouvelle fonctionnalité
    fix:      Correction de bug
    docs:     Documentation
    style:    Formatage
    refactor: Refactoring
    perf:     Performance
    test:     Tests
    chore:    Maintenance

### Idées d'amélioration

- [ ] 📱 PWA (Service Worker + manifest)
- [ ] 🔍 Recherche par SIRET précis
- [ ] 📊 Graphique en aires empilées par catégorie
- [ ] 🎯 Comparateur de titulaires
- [ ] 🗺️ Vraie carte SVG avec contours
- [ ] 💰 Détection de doublons
- [ ] 📉 Détection d'anomalies (montants aberrants)
- [ ] 🌐 Multi-langue (EN, DE, ES)

Voir les [issues ouvertes](../../issues) pour la liste complète.

---

## 📄 Licence

Distribué sous licence **MIT**. Voir [`LICENSE`](LICENSE).

    MIT License

    Copyright (c) 2026 Gunout

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

---

## 🙏 Remerciements

- 💙 **[data.gouv.fr](https://www.data.gouv.fr/)** — pour l'open data DECP
- 🇫🇷 **[DINUM](https://www.numerique.gouv.fr/)** — pour le Système de Design de l'État
- 🎨 **[Marianne](https://www.gouvernement.fr/marque-de-letat)** — identité visuelle
- 📊 **[gregoiredavid/france-geojson](https://github.com/gregoiredavid/france-geojson)** — contours départements

---

<div align="center">

### ⭐ Si ce projet vous aide, mettez-lui une étoile !

[![Stars](https://img.shields.io/github/stars/gunout/monitor-decp-re?style=social)](https://github.com/gunout/monitor-decp-re)
[![Forks](https://img.shields.io/github/forks/gunout/monitor-decp-re?style=social)](https://github.com/gunout/monitor-decp-re/fork)

**Fait avec ❤️ pour la transparence des marchés publics**

[⬆ Retour en haut](#-monitor-decp)

---

### 🇫🇷 Gunout · 2026

© 2026 **Gunout** — Tous droits réservés.

</div>

---

<div align="center">

### 🇫🇷 Gunout · 2026

![Made in France](https://img.shields.io/badge/Made_in-France-002395?style=flat-square&labelColor=FFFFFF&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MDAgNjAwIj48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iIzAwMjM5NSIvPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNDAwIiB5PSIxMDAiIGZpbGw9IiNmZmYiLz48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjIwMCIgeT0iNDAwIiBmaWxsPSIjZWQyOTM5Ii8+PC9zdmc+)
![GitHub](https://img.shields.io/badge/GitHub-gunout-181717?style=flat-square&logo=github&logoColor=white)
![Year](https://img.shields.io/badge/2026-ED2939?style=flat-square&labelColor=FFFFFF)

<sub>© 2026 <strong>Gunout</strong> — Tous droits réservés.</sub>

</div>

