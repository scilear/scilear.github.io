# AlphAngel Website - Instructions d'installation

## Fichiers créés

1. **index.html** - Page d'accueil professionnelle
2. **reports.html** - Explorateur de rapports avec tree view dynamique

## Comment uploader sur GitHub

### Méthode 1: Via l'interface GitHub (plus simple)

1. Va sur https://github.com/scilear/scilear.github.io
2. Clique sur "Add file" > "Upload files"
3. Drag & drop les fichiers `index.html` et `reports.html`
4. Clique sur "Commit changes"
5. Attends 1-2 minutes pour que GitHub Pages se mette à jour
6. Ton site sera visible sur https://alphangel.com

### Méthode 2: Via Git (recommandé pour toi)

```bash
cd scilear.github.io
git pull origin main
cp /path/to/index.html .
cp /path/to/reports.html .
git add index.html reports.html
git commit -m "Add AlphAngel professional website"
git push origin main
```

## Structure des rapports

### Format des fichiers de rapports
- Nom: `reportnameYYYYMMDD.html`
- Exemples:
  - `volatility-analysis20260125.html`
  - `p2p-lending-review20260120.html`
  - `credit-markets20260118.html`
  - `capital-markets-outlook20260122.html`

### Organisation des répertoires
```
scilear.github.io/
├── index.html
├── reports.html
└── reports/
    ├── volatility-analysis20260125.html
    ├── p2p-lending-review20260120.html
    └── credit-markets20260118.html
```

### Ajouter un nouveau rapport

1. Crée ton rapport HTML (ex: `my-report20260128.html`)
2. Upload-le dans le dossier `/reports` du repo
3. La page reports.html le détectera automatiquement et l'affichera

**Note:** Pour l'instant, la page utilise des exemples de rapports. Pour scanner automatiquement tes vrais rapports, tu devras ajouter un script backend ou utiliser GitHub Actions.

## Personnalisation du logo

Pour remplacer le logo temporaire "Aα" :

1. Télécharge le logo de solvefortime.com ou crée ton propre logo
2. Sauvegarde-le comme `logo.png` dans le repo
3. Dans `index.html` et `reports.html`, remplace:
   ```html
   <div class="logo">Aα</div>
   ```
   par:
   ```html
   <div class="logo">
       <img src="logo.png" alt="AlphAngel Logo">
   </div>
   ```

## SEO et optimisation

Les deux pages incluent déjà:
- ✅ Meta descriptions optimisées
- ✅ Meta keywords pour SEO
- ✅ Structure HTML sémantique
- ✅ Design responsive (mobile-friendly)
- ✅ Navigation claire
- ✅ Performance optimisée (CSS inline, pas de dépendances externes)

## Automatisation future (optionnel)

Pour automatiser le scan des rapports, tu peux:

1. **GitHub Actions** : Créer un workflow qui génère un index JSON des rapports
2. **Script Python** : Générer dynamiquement la liste lors de la publication
3. **API GitHub** : Utiliser l'API pour lister les fichiers du répertoire /reports

Exemple de script Python pour générer l'index:
```python
import os
import json
from pathlib import Path

reports_dir = Path('reports')
reports = [f.name for f in reports_dir.glob('*.html')]
with open('reports-index.json', 'w') as f:
    json.dump(reports, f)
```

## Contact

Pour toute question: scilear@gmail.com
