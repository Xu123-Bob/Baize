<div align="center">

<img src="image/logopage02.png" alt="Logo Baize" width="320" />

# Baize

**Connaît toutes choses, code par intuition avec toi.**

<p align="center">
  <a href="https://atomgit.com/Com_Xu/Baize">
    <img src="https://atomgit.com/Com_Xu/Baize/star/new_badge.svg" alt="AtomGit">
  </a>
</p>

<p align="center">
  <a href="https://github.com/Xu123-Bob/Baize/stargazers">
    <img src="https://img.shields.io/github/stars/Xu123-Bob/Baize?style=flat-square&logo=github" alt="GitHub stars">
  </a>
  <a href="https://github.com/Xu123-Bob/Baize/forks">
    <img src="https://img.shields.io/github/forks/Xu123-Bob/Baize?style=flat-square&logo=github" alt="GitHub forks">
  </a>
  <a href="https://github.com/Xu123-Bob/Baize/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Xu123-Bob/Baize?style=flat-square" alt="License">
  </a>
  <a href="https://github.com/Xu123-Bob/Baize/pulls?q=is%3Apr+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-pr-closed/Xu123-Bob/Baize?style=flat-square&logo=github&label=Closed%20PRs" alt="GitHub Closed Pull Requests">
  </a>
  <a href="https://github.com/Xu123-Bob/Baize/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Xu123-Bob/Baize?style=flat-square&logo=github&label=Contributors" alt="GitHub Contributors">
  </a>
</p>

<p align="center">
  <a href="https://github.com/Xu123-Bob/Baize/releases">
    <img src="https://img.shields.io/github/v/release/Xu123-Bob/Baize?style=flat-square&logo=github&label=Release&include_prereleases" alt="GitHub release">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  </a>
</p>

<p align="center">
  <a href="README.cn.md">简体中文</a> |
  <a href="README.en.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.fr.md">Français</a>
</p>

</div>

----------

Baize — la créature auspcieuse de la mythologie chinoise qui connaît toutes choses, réincarnée en assistant Vibe Coding.

**Un CLI d'agent de codage IA open source, alternative directe à Claude Code CLI. Prend en charge plusieurs backends (DeepSeek / toute API compatible OpenAI / Zhipu / Qwen / Kimi / Ollama local), avec une chaîne d'outils complète : appels d'outils, chargement de skills, délégation à des sous-agents, compression de contexte et sandbox sécurisé. Programmez en binôme avec l'IA directement dans le terminal.**

----------

# Fonctionnalités

- **Multi-backends** : DeepSeek, tout endpoint compatible OpenAI (GLM / Qwen / Kimi / OpenAI) et Ollama local — basculez en une ligne.
- **Démarrage sans configuration** : Le premier lancement génère automatiquement les fichiers de config ; vous ne saisissez votre clé qu'une fois.
- **Chaîne d'outils complète** : exécution bash, lecture/écriture/édition de fichiers, recherche glob/grep, recherche et récupération web, tâches d'arrière-plan, gestion des tâches et des todos.
- **Système de skills** : Chargement à la demande de connaissances métier (SKILL.md) pour que l'IA se comporte comme une spécialiste.
- **Sous-agents** : Déléguez les tâches complexes à des sous-agents au contexte isolé, en gardant la session principale propre.
- **Hooks** : Hooks Python ou Shell pour intercepter avant/après les appels d'outils, journaliser, formater automatiquement et bloquer sur échec de tests.
- **Protocole MCP** : Connectez des serveurs d'outils externes (GitHub, Filesystem, etc.) via Model Context Protocol.
- **Compression de contexte** : Compression à deux niveaux (troncature des anciens résultats + résumé par LLM) pour de très longues conversations.
- **Sandbox sécurisé** : Liste blanche de commandes, détection d'évasion de chemin, blocage de commandes dangereuses, protection des fichiers sensibles, blocage d'injection de scripts.
- **Interaction multilingue** : Basculez librement entre chinois / anglais / japonais / coréen / espagnol / français. Dites simplement `English` ou utilisez `/lang ja`, et l'IA pense et répond dans cette langue.
- **CLI thème noir-or** : Largeur CJK adaptative, coloration syntaxique, coloration des diffs, repli de la réflexion.

# Installation

## Prérequis

- Python 3.10+ (nécessite `tomllib` ; intégré en 3.11+, installez `tomli` en 3.10)
- pip

## Installation depuis les sources

### Deux façons de télécharger

1. `pip install https://github.com/Xu123-Bob/Baize.git`

   Ensuite, ouvrez cmd et lancez :

   ```
   baize
   ```

2. Sur la page du dépôt, cliquez sur `<> Code` → `Download ZIP`.

   (1) Décompressez et entrez dans le dossier :

   ```
   cd <dossier-décompressé>
   pip install -r requirements.txt
   python -m Baize
   ```

   (2) Installation locale :

   ```
   pip install .
   ```

   Après installation, ouvrez cmd et tapez `baize` pour lancer.

# Démarrage rapide

1. Premier lancement

   ```
   baize
   ```

   Baize génère automatiquement deux fichiers de configuration :

   ```
   ~/.baize/config.toml   # configuration des backends
   ~/.baize/.env          # clés d'API
   ```

   Sous Windows : `C:\Users\<utilisateur>\.baize\`.

2. Choisir un backend

   Ouvrez `~/.baize/config.toml` et éditez `active_provider` :

   ```toml
   active_provider = "deepseek"    # ou "openai" / "ollama"

   [model_providers.deepseek]
   name = "DeepSeek"
   base_url = "https://api.deepseek.com"
   env_key = "DEEPSEEK_API_KEY"
   model = "deepseek-v4-pro"

   [model_providers.openai]
   name = "OpenAI"
   base_url = "https://api.openai.com/v1"
   env_key = "OPENAI_API_KEY"
   model = "gpt-4o-mini"

   [model_providers.ollama]
   name = "Ollama (local)"
   base_url = "http://localhost:11434/v1"
   env_key = ""
   model = "qwen2.5:7b"
   ```

3. Saisir la clé

   Éditez `~/.baize/.env` :

   ```
   # Obligatoire pour le backend DeepSeek
   DEEPSEEK_API_KEY=sk-votre-clé-ici

   # Obligatoire pour un endpoint compatible OpenAI (GLM / Qwen / Kimi / OpenAI)
   # OPENAI_API_KEY=votre-clé-ici

   # Ollama n'a pas besoin de clé
   ```

4. Redémarrer

   ```
   baize
   ```

   Si vous voyez le logo noir-or et le message d'accueil, c'est lancé.

# Exemples d'utilisation

Écrivez en langage naturel au prompt `>>> 降旨：` :

```
>>> 降旨：Écris un script Python qui scrape le Top250 de Douban et l'enregistre en CSV
>>> 降旨：Vérifie les erreurs de type dans tous les fichiers Python sous src/
>>> 降旨：Trouve toutes les utilisations de `requests` dans ce dépôt et remplace-les par `httpx`
```

## Interaction multilingue

Baize prend en charge **six langues** : 中文, English, 日本語, 한국어, Español, Français.

Deux façons de basculer :

### Option 1 : parlez directement (détection automatique)

Baize détecte la langue de votre saisie et bascule automatiquement :

```
>>> 降旨：Bonjour, peux-tu m'écrire un script Python ?
[system] Langue d'entrée détectée : Français. Baize bascule en Français.
(répond en français)

>>> 降旨：Hello, write me a script
[system] Langue d'entrée détectée : English. Baize bascule en English.
(répond en anglais)
```

### Option 2 : commande manuelle

```
>>> 降旨：/lang                # Affiche la langue courante et la liste disponible
[system] Langue actuelle : Français (fr)
[system] Langues disponibles :
    zh    中文
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français ←

>>> 降旨：/lang English        # Changer par nom de langue
>>> 降旨：/lang ja             # Changer par code de langue
>>> 降旨：/lang 西班牙语        # Noms chinois également acceptés
```

Accepte **nom de langue / code / nom natif**. Pour basculer en anglais, `English`, `en`, `英语` ou `英文` fonctionnent indifféremment.

## CLI Baize

<div align="center">
Baize CLI — démarrage
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="Baize CLI démarrage" width="800" />
</p>

<div align="center">
Baize CLI — exécution
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="Baize CLI exécution" width="800" />
</p>

## Commandes intégrées

- `/exit`, `/quit` → Quitter
- `/clear` → Efface l'historique, les todos, les réflexions et les journaux d'outils
- `/compact` → Compresse manuellement le contexte (utile si la conversation est longue)
- `/commit` → Sauvegarde la session et commit dans Git (si dans un dépôt Git)
- `/lang` → Affiche la langue actuelle ; `/lang en` bascule en anglais (code ou nom)
- `/skills` → Liste toutes les skills disponibles
- `/skills reload` → Recharge le dossier de skills utilisateur
- `/unload` → Décharge la skill active
- `/show thought` → Affiche la réflexion complète
- `/show tool` → Affiche le journal des appels d'outils
- `/show all` → Affiche tout l'historique de session
- `/<nom-skill>` → Charge une skill (correspondance floue)

# Ollama local (coût zéro)

Vous ne voulez pas d'API cloud ? Utilisez Ollama local :

```bash
# 1. Installez Ollama : https://ollama.com/download
# 2. Récupérez un modèle
ollama pull qwen2.5:7b

# 3. Démarrez Ollama
ollama serve

# 4. Éditez ~/.baize/config.toml
active_provider = "ollama"

# 5. Lancez Baize
baize
```

Modèles recommandés : `qwen2.5:7b` (fort en chinois), `llama3.1:8b`, `deepseek-r1:7b`.

# Extensions

Baize prend en charge quatre mécanismes d'extension, tous placés dans le répertoire de travail courant.

## Skills

Écrivez des connaissances métier dans `./skills/<nom>/SKILL.md`. L'IA les charge à la demande.

```markdown
---
name: pandas-eda
description: Bonnes pratiques d'analyse exploratoire avec pandas
tags: data,python
---

# Guide Pandas EDA

## Étapes clés
1. df.info() pour inspecter les types et les valeurs manquantes
2. df.describe() pour les statistiques descriptives
...
```

Vous pouvez aussi charger une skill manuellement avec `/pandas-eda` dans la conversation.

## Sous-agents

Définissez des sous-agents spécialisés dans `./subagent/<rôle>/AGENT.md`. L'agent principal peut déléguer via l'outil `agent`.

```markdown
---
name: code-reviewer
description: Relecteur de code strict
---

Vous êtes un relecteur de code senior. Priorisez :
1. Cas limites et gestion d'erreurs
2. Fuites de ressources
3. Sûreté en concurrence
...
```

## Hooks

Placez `PreToolUse-*.sh`, `PostToolUse-*.sh`, `Stop-*.sh` dans `./hooks/`. Ils reçoivent du JSON sur stdin et renvoient une décision.

```bash
#!/bin/bash
# PreToolUse-guard.sh
read -r input
if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"rm -rf est interdit"}}'
fi
```

Les hooks Python peuvent appeler directement l'API interne (voir les fonctions `hook_*` dans `Baize.py`).

## Serveurs MCP

Configurez des serveurs d'outils externes dans `./MCP/mcp_config.json` :

```json
{
  "mcpServers": [
    {
      "name": "filesystem",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
      "env": {},
      "enabled": true
    }
  ]
}
```

# Sécurité

Les mécanismes suivants sont activés par défaut :

- **Liste blanche de commandes** : seules `ls`, `cat`, `grep`, `git`, `python3` et consorts sont autorisées.
- **Détection d'évasion de chemin** : toutes les opérations de fichiers sont limitées au répertoire courant et à `/tmp`.
- **Blocage de commandes dangereuses** : bloque `rm -rf /`, fork bombs, `curl | sh`, `git push --force`, etc.
- **Protection des fichiers sensibles** : interdit la modification de `.env`, `.ssh/`, `id_rsa`, `*.pem`, etc.
- **Blocage d'injection de scripts** : détecte les contournements du type `python -c "os.system(...)"`.
- **Limites de ressources** : sous Linux/macOS, limite CPU, mémoire et nombre de processus.

Pour assouplir les restrictions dans un projet de confiance, modifiez `ALLOWED_COMMANDS` et `FORBIDDEN_PATH_PATTERNS` dans `Baize.py`.

# Structure du projet

```
baize-agent/
├── pyproject.toml              # configuration de packaging
├── README.md
├── tests/                      # tests (non publiés)
│   ├── __init__.py
│   ├── test_history.py
│   └── test_skill_loader.py
├── .env.example
├── .gitignore
└── agent/                      # paquet principal
    ├── __init__.py
    ├── Baize.py                # programme principal & Agent Loop
    ├── config.py               # chargeur multi-backend
    ├── ui_theme.py             # thème du CLI
    ├── utils.py
    ├── logo.txt
    ├── skills/                 # skills intégrées
    ├── subagent/               # sous-agents intégrés
    ├── core/                   # logique pure (sans effet de bord, testable)
    │   ├── __init__.py
    │   └── history.py          # nettoyage / estimation de tokens / compression
    ├── hooks/                  # hooks intégrés
    └── MCP/                    # client MCP et configuration
        ├── __init__.py
        ├── mcp_client.py
        └── mcp_config.json
```

# Variables d'environnement

| Variable | Description | Valeur par défaut |
|---|---|---|
| `DEEPSEEK_API_KEY` | Clé d'API DeepSeek | — |
| `DEEPSEEK_BASE_URL` | URL de base DeepSeek | `https://api.deepseek.com` |
| `OPENAI_API_KEY` | Clé compatible OpenAI | — |
| `OPENAI_BASE_URL` | URL compatible OpenAI | `https://api.openai.com/v1` |
| `OLLAMA_BASE_URL` | URL du service Ollama | `http://localhost:11434` |

Il suffit de les mettre dans `~/.baize/.env` — pas besoin de toucher au shell.

# Développement

## Lancer les tests

Le projet utilise pytest. Installez en mode éditable avec les dépendances de développement :

```
pip install -e ".[dev]"
```

Lancer tous les tests :

```
python -m pytest tests/ -v
```

Un seul fichier :

```
python -m pytest tests/test_history.py -v
```

## Conventions de structure

- `agent/` : paquet principal distribué. Toute la logique d'exécution et les ressources (skills, subagent, hooks, MCP) sont ici.
- `agent/core/` : modules de logique pure, sans effet de bord — **doivent être testables isolément**. Placez-y la nouvelle logique, avec ses tests.
- `tests/` : miroir des sources de `agent/`, nommé `test_<module>.py`.
- Toute fonction avec dépendances externes (réseau, disque, état global) doit les recevoir en paramètre pour être testable.

# ❓ FAQ

**Q : Où mettre la clé d'API ?**

R : Dans `~/.baize/.env`, pas dans le `.env` du projet.

**Q : Faut-il réinstaller en changeant de backend ?**

R : Non. Modifiez simplement `active_provider` dans `~/.baize/config.toml`.

**Q : Ollama local a-t-il besoin d'une clé ?**

R : Non. Mettez `active_provider = "ollama"` et laissez `env_key` vide.

**Q : Comment changer de répertoire de travail ?**

R : Dites simplement « bascule vers /path/to/project » dans la conversation — Baize appellera l'outil `set_workspace`.

**Q : Que se passe-t-il si le contexte devient trop long ?**

R : Baize compresse en deux niveaux : il tronque d'abord les anciens résultats d'outils, puis demande un résumé au LLM. Vous pouvez aussi lancer `/compact` manuellement.

**Q : Peut-il supprimer mes fichiers par erreur ?**

R : La liste blanche bloque les opérations comme `rm -rf /`. Avant chaque écriture, Baize affiche un diff et demande confirmation.

**Q : Comment faire répondre Baize en anglais ou en japonais ?**

R : Dites simplement `English` ou `日本語` et il basculera automatiquement. Vous pouvez aussi utiliser `/lang en` (ou `/lang ja`). Toute la réflexion et les réponses suivantes utiliseront cette langue. Pour revenir au chinois, dites `中文` ou tapez `/lang zh`.

# 🤝 Contribuer

Les issues et PRs sont bienvenus. Avant d'étendre, lisez la fonction `agent_loop` dans `Baize.py` pour comprendre la boucle principale.

### Merci à tous les contributeurs qui envoient des PRs

- Contributeurs GitHub :
  - [@anupamme](https://github.com/anupamme)
  - [@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# Licence

MIT License

# Remerciements

- Hébergé sur AtomGit : https://atomgit.com/Com_Xu/Baize
- Merci à AtomGit pour l'inclusion dans le programme d'incubation G-star
- Merci aux contributeurs de PRs, aux abonnés Douyin et aux étudiants
- Inspiré par Claude Code, Codex et d'autres excellents outils IA de codage
- Construit sur DeepSeek, le SDK OpenAI et MCP
- Merci à chaque développeur sur la voie du Vibe Coding
- Les développeurs se concentrent sur les idées et les décisions ; Baize s'occupe des tâches ingrates.

# ☕ Soutien

Si Baize vous est utile, offrez-moi un café. Le développement solo prend beaucoup de temps ; le sponsoring ne change pas le calendrier des versions. Merci !

<p align="center">
  <img src="image/support.jpg" alt="QR WeChat" width="200" />
</p>

# Contact

- Si Baize vous intéresse ou si vous souhaitez collaborer en open source, écrivez-moi par les canaux ci-dessous.
- **Je suis actuellement en recherche d'emploi. Mon expérience est en études de marché et de recherche utilisateur, avec une bonne compréhension des agents. Si mes compétences correspondent à vos besoins, je serais ravi de collaborer (postes visés : Opérations produit IA / Recherche utilisateur / Études de marché).**

<p align="center">
  <img src="image/weixin.jpg" alt="QR WeChat" width="200" />
</p>

<p align="center">Scannez sur WeChat, précisez « collaboration open source Baize » ou « recrutement »</p>

<p align="center">
  <img src="image/抖音.png" alt="QR Douyin" width="200" />
</p>

<p align="center">Suivez-moi sur Douyin</p>