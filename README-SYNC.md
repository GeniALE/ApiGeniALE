# Synchronisation de la branche dev avec main

## Objectif
Rendre la branche `dev` identique à la branche `main`.

## Contexte
- **Branche main** : Pointe vers le commit `9c4ecfc` (init api)
- **Branche dev** : Pointe vers le commit `e0de17b` (architecture de base fait)
- Ces deux branches ont divergé et contiennent du code différent.

## Solution

### Option 1: Via GitHub Actions (Le plus simple)

Un workflow GitHub Actions a été créé pour automatiser le processus de manière sécurisée:

1. Aller sur https://github.com/GeniALE/ApiGeniALE/actions
2. Cliquer sur "Sync Dev with Main (Manual Trigger)" dans la liste des workflows
3. Cliquer sur "Run workflow"
4. Taper "CONFIRM" dans le champ de confirmation
5. Cliquer sur "Run workflow" pour démarrer

Le workflow va automatiquement synchroniser dev avec main et vérifier que l'opération a réussi.

### Option 2: Utiliser le script automatisé local

Un script bash a été créé pour automatiser le processus. Pour l'exécuter:

```bash
# Rendre le script exécutable (si nécessaire)
chmod +x sync-dev-with-main.sh

# Exécuter le script
./sync-dev-with-main.sh
```

Le script va:
1. Récupérer les dernières modifications
2. Basculer sur la branche dev
3. Réinitialiser dev pour correspondre à main
4. Force-pusher la branche dev vers le remote
5. Afficher une vérification

### Option 3: Commandes manuelles

Si vous préférez exécuter les commandes manuellement:

```bash
# Récupérer les dernières modifications
git fetch origin

# Basculer sur la branche dev
git checkout dev

# Réinitialiser dev pour correspondre exactement à main
git reset --hard origin/main

# Force-pusher vers le remote (ATTENTION: cela écrase l'historique de dev)
git push --force origin dev
```

### Option 4: Via GitHub Web Interface

1. Aller sur https://github.com/GeniALE/ApiGeniALE
2. Créer une nouvelle Pull Request de `main` vers `dev`
3. Merger avec l'option "Create a merge commit" ou utiliser la stratégie appropriée
   - Note: Cette option créera un commit de merge, elle ne rendra pas dev identique à main

## ⚠️ AVERTISSEMENT

Cette opération va **SUPPRIMER** les commits suivants de la branche dev:

- `e0de17b` - architecture de base fait
- `a95c814` - Merge remote-tracking branch 'origin/7-mdd-modèle-de-données'
- `860fd64` - correction des docs out
- `b294cea` - correction et avancement du mld
- `7aeea38` - ajout de la table calendrier
- `3e641ef` - continuation de la documentation
- `a21708b` - add the markdown same as the pdf
- `b02077e` - add definition of API and
- Et potentiellement d'autres commits

**Assurez-vous d'avoir sauvegardé ces commits si vous en avez besoin plus tard!**

Pour créer une sauvegarde de la branche dev avant la synchronisation:

```bash
git branch dev-backup dev
git push origin dev-backup
```

## Vérification

Après la synchronisation, vérifiez que dev et main pointent vers le même commit:

```bash
git log --oneline --graph --all -10
```

Vous devriez voir que `dev` et `main` pointent tous les deux vers `9c4ecfc (init api)`.

## Contenu après synchronisation

Après la synchronisation, la branche dev contiendra:

- `.gitignore`
- `.python-version`
- `LICENSE`
- `README.md`
- `app/` (répertoire avec code Python)
- `doc/` (répertoire de documentation)
- `main.py` (fichier principal de l'API)
- `pyproject.toml` (configuration Python)
- `uv.lock` (fichier de lock des dépendances)

Les répertoires `src/` et leur contenu seront supprimés.
