<div align="center">

<img src="image/logopage02.png" alt="Baize Logo" width="320" />

# Baize 白泽

**Dire tout ce que l'on sait, garder tous les secrets**

<p align="center">
  <a href="https://atomgit.com/Com_Xu/Baize">
    <img src="https://atomgit.com/Com_Xu/Baize/star/new_badge.svg" alt="AtomGit">
  </a>
  &nbsp;&nbsp;
  <a href="https://trendshift.io/repositories/233391?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-233391" target="_blank" rel="noopener noreferrer">
    <img src="https://trendshift.io/api/badge/trendshift/repositories/233391/daily?language=JavaScript" alt="Xu123-Bob%2FBaize | Trendshift" width="250" height="55"/>
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
</p>

<p align="center">
  <a href="https://github.com/Xu123-Bob/Baize/releases">
    <img src="https://img.shields.io/github/v/release/Xu123-Bob/Baize?style=flat-square&logo=github&label=Release&include_prereleases" alt="GitHub release">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  </a>
  <a href="image/抖音.png">
    <img src="https://img.shields.io/badge/Douyin-Scan%20to%20Follow-FE2C55?style=flat-square&logo=douyin&logoColor=white" alt="Douyin">
  </a>
</p>

<p align="center">
  <a href="README.cn.md">简体中文</a> |
  <a href="README.en.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.ru.md">Русский</a>
</p>

</div>

----------

Un assistant de sécurité pour le VibeCoding et l'analyse de données, inspiré d'une créature mythique chinoise.

**Une CLI de Coding Agent open source, dotée d'une puissante protection de la vie privée et d'une interaction multilingue. Elle prend en charge plusieurs backends (DeepSeek / compatible OpenAI / Zhipu / Qwen / Kimi / Ollama local) et offre des capacités complètes : appel d'outils, chargement de compétences, délégation à des sous-agents, compression du contexte, bac à sable sécurisé, etc.**

----------

# Avantages principaux

## Protection de la vie privée

- **Protection bidirectionnelle réversible de la vie privée** : les informations sensibles sont remplacées par des espaces réservés avant d'être envoyées au LLM, puis automatiquement restaurées après réception de la réponse. Tout le processus est transparent pour l'utilisateur : l'historique, les paramètres d'outils et les réponses finales que vous voyez restent toujours le texte original, tandis que le LLM ne voit que des espaces réservés aléatoires et impossibles à deviner, comme `«PZ_PHONE_a3f8b2c1d4e5f6a7»`.
- **Pseudonymisation complète sur disque** : les fichiers de session, les transcriptions compressées et les journaux d'audit sont automatiquement pseudonymisés avant écriture sur disque (activé par défaut). Les PII en clair n'apparaissent jamais sur le disque.
- **Résistance aux injections** : les espaces réservés utilisent des jetons cryptographiques aléatoires de 64 bits, impossibles à énumérer, falsifier ou rejouer. Les anciens espaces réservés deviennent immédiatement invalides après un changement de session.
- **Plusieurs façons d'activer la protection de la vie privée** : vous pouvez activer le mode de protection de la vie privée en saisissant du langage naturel en ligne de commande, ou utiliser la commande plus précise `/privacy`.
- **Agent local** : ce produit n'a pas de base de données distante et fonctionne entièrement en local. Il ne collecte aucune information utilisateur.

## Interaction multilingue

- **Prend en charge neuf langues** : chinois, English, 日本語, 한국어, Español, Français, deutsch, русский, العربية.
- **Plusieurs façons de changer de langue** : vous pouvez dire directement `please speak with english` pour passer à l'anglais, ou utiliser `/lang ja` pour passer au japonais.

# Fonctionnalités

- **Prise en charge multi-backends** : DeepSeek, tout endpoint compatible OpenAI (GLM / Qwen / Kimi / OpenAI), et Ollama local. Changement en un clic.

- **Démarrage sans configuration** : génère automatiquement les fichiers de configuration au premier lancement. L'utilisateur n'a qu'à saisir sa clé une seule fois.

- **Pseudonymisation de la vie privée** : identifie et pseudonymise automatiquement **plus de 30 catégories** d'informations sensibles avant l'envoi au LLM (numéros de téléphone, e-mails, cartes d'identité, passeports, cartes bancaires, numéros internationaux, clés API, JWT, chaînes de connexion à des bases de données, adresses MAC, etc.), puis les restaure automatiquement après réception de la réponse. **La pseudonymisation s'applique aussi sur disque**, ne laissant aucun texte en clair. Prend en charge deux niveaux, Standard / Strict, commutables via le langage naturel ou `/privacy`.

- **Interaction multilingue** : changez librement entre chinois / anglais / japonais / coréen / espagnol / français / allemand / russe / arabe. Dites simplement `English` ou utilisez `/lang ja`, et l'IA pensera et répondra dans la langue correspondante pendant toute la session.

- **Chaîne d'outils complète** : exécution bash, lecture/écriture/édition de fichiers, recherche glob/grep, recherche et récupération web, tâches en arrière-plan, gestion des tâches et des todo.

- **Système de compétences (Skills)** : charge à la demande des connaissances métier (SKILL.md), rendant l'IA plus professionnelle dans des scénarios spécifiques.

- **Sous-agents (Subagents)** : délègue les tâches complexes à des sous-agents avec un contexte indépendant, évitant de polluer la session principale.

- **Hooks** : hooks Python ou Shell. Prend en charge l'interception avant/après appel d'outil, les journaux d'audit, le formatage automatique et le contrôle des tests.

- **Protocole MCP** : connecte des serveurs d'outils externes via Model Context Protocol (GitHub, Filesystem, etc.).

- **Compression du contexte** : compression à deux niveaux (troncature des résultats d'outils + résumé par LLM). Prend en charge les conversations très longues.

- **Bac à sable sécurisé** : liste blanche de commandes, détection d'évasion de chemin, interception de commandes dangereuses, protection des fichiers sensibles et interception d'injection de scripts.

- **CLI thème noir et or** : largeur adaptative pour le chinois, coloration syntaxique, coloration des diffs et repli des pensées.

# Interface CLI de Baize

<div align="center">
Écran de démarrage de Baize CLI
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="Écran de démarrage de Baize CLI" width="800" />
</p>

<div align="center">
Écran d'exécution de Baize CLI -- 01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="Écran d'exécution de Baize CLI" width="800" />
</p>

<div align="center">
Écran d'exécution de Baize CLI -- 02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="Écran d'exécution de Baize CLI" width="800" />
</p>

# Installation

## Prérequis

- Python 3.10+ (nécessite tomllib, intégré à partir de 3.11 ; pour 3.10, installez tomli)

- pip

## Installation depuis les sources

### Deux méthodes de téléchargement

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- Appuyez sur Win+R, saisissez `cmd`, puis entrez :

    baize

2. Sur la page du dépôt, cliquez sur `<> Code` --> `Download ZIP`

(1) Après décompression, entrez dans le répertoire de ce fichier :

    bash -- Appuyez sur Win+R et saisissez cmd

    cd répertoire-décompressé

    pip install -r requirements.txt

    python -m Baize

Après l'installation, appuyez sur Win+R, saisissez cmd pour ouvrir la CLI, puis entrez `baize` pour l'exécuter.

(2) Téléchargez le ZIP et installez-le localement. Après décompression, entrez dans le répertoire et exécutez :

    bash -- Appuyez sur Win+R et saisissez cmd

    pip install .

Après l'installation, appuyez sur Win+R, saisissez cmd pour ouvrir la CLI, puis entrez `baize` pour l'exécuter.

### Optionnel : installer les dépendances d'accès aux données (outils importants pour l'analyse de données)

Si vous souhaitez que Baize pilote SPSS ou des bases de données SQL, installez les dépendances supplémentaires :

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` contient :
- `spss-studio-mcp` : serveur MCP d'analyse statistique SPSS (nécessite IBM SPSS Statistics installé localement)
- `atengk-mcp-server-rdbms` : serveur MCP de bases de données relationnelles génériques (PostgreSQL / MySQL / SQL Server / Oracle / DM, etc.)
- `pyodbc` : liaison Python ODBC requise pour SQL Server

Alternativement, si le projet est installé via `pyproject.toml`, vous pouvez aussi utiliser les extras :

```bash
pip install -e ".[data]"          # Installe toutes les dépendances d'accès aux données d'un coup
pip install -e ".[spss]"          # Installe uniquement SPSS
pip install -e ".[sql]"           # Installe uniquement SQL générique
pip install -e ".[sql-mssql]"     # SQL Server uniquement (inclut pyodbc)
```

- **⚠️ Utilisateurs de SQL Server : `pyodbc` n'est que la liaison Python. Vous devez aussi installer Microsoft ODBC Driver 18 for SQL Server au niveau système.**
- **⚠️ Utilisateurs de SPSS : `spss-studio-mcp` n'est qu'une couche de pont MCP. IBM SPSS Statistics (version 20–31) doit déjà être installé localement et disposer d'une licence valide, et la variable d'environnement `SPSS_INSTALL_PATH` doit pointer vers le répertoire d'installation de SPSS. Actuellement, le moteur SPSS prend principalement en charge l'analyse complète sous Windows ; sous Linux/macOS, il peut se dégrader en « mode fichier » (lecture de fichiers .sav, consultation des métadonnées, prévisualisation des données, mais pas d'analyse statistique).**

# Démarrage rapide

1. Première exécution

```bash
baize
```

Lors de la première exécution, Baize génère automatiquement deux fichiers de configuration :

```
~/.baize/config.toml   # Configuration du backend (choisir DeepSeek / OpenAI / Ollama)
~/.baize/.env          # Fichier de clés
```

Sous Windows, le chemin est `C:\Users\VotreNomUtilisateur\.baize\`.

2. Choisir un backend

Ouvrez `~/.baize/config.toml` et modifiez **active_provider** (obligatoire) :

```toml
# Fichier de configuration de Baize
# Modifiez active_provider pour changer de backend  # Valeurs possibles : "deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

active_provider = "deepseek"

[model_providers.deepseek]
name = "DeepSeek"
base_url = "https://api.deepseek.com"
env_key = "DEEPSEEK_API_KEY"
model = "deepseek-flash"

[model_providers.qwen]
name = "Qwen"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
env_key = "DASHSCOPE_API_KEY"
model = "qwen-plus"

[model_providers.kimi]
name = "Kimi"
base_url = "https://api.moonshot.cn/v1"
env_key = "MOONSHOT_API_KEY"
model = "kimi-k2.7-code"

[model_providers.glm]
name = "GLM"
base_url = "https://open.bigmodel.cn/api/paas/v4"
env_key = "ZHIPUAI_API_KEY"
model = "glm-4-plus"

[model_providers.openai]
name = "OpenAI"
base_url = "https://api.openai.com/v1"
env_key = "OPENAI_API_KEY"
model = "gpt-4o"

[model_providers.ollama]
name = "Ollama (local)"
base_url = "http://localhost:11434/v1"
env_key = ""
model = "qwen2.5:7b"
```

3. Saisir la clé

Modifiez `~/.baize/.env`. **Si vous devez utiliser un LLM donné, supprimez le `# ` en début de ligne correspondant, et ajoutez `# ` devant les autres LLM pour verrouiller leur sortie API. Après avoir saisi l'API Key, pensez impérativement à enregistrer ; cela ne prend effet qu'après sauvegarde** :

```env
# ============================================================
# Fichier de clés de Baize
# ============================================================
# Ne remplissez que la clé du backend que vous utilisez ; laissez les autres commentées.
# Les noms de variables doivent correspondre au champ env_key de config.toml.
#
# Emplacement :
#   Linux / macOS : ~/.baize/.env
#   Windows :       C:\Users\VotreNomUtilisateur\.baize\.env
# ============================================================

# ---------- DeepSeek (backend par défaut) ----------
# Obtenez-la sur : https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI ou tout endpoint compatible OpenAI (optionnel) ----------
# Pour Groq, Qwen, Moonshot, Zhipu, OpenAI, etc.
# Remarque : base_url se configure dans config.toml sous [model_providers.xxx], pas ici
# OPENAI_API_KEY=

# ---------- Qwen (optionnel) ----------
# Obtenez-la sur : https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot (optionnel) ----------
# Obtenez-la sur : https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- Zhipu GLM (optionnel) ----------
# Obtenez-la sur : https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- Passerelle personnalisée (optionnel) ----------
# CUSTOM_API_KEY=

# ---------- Ollama (modèle local, aucune clé requise) ----------
# Assurez-vous simplement qu'Ollama tourne sur localhost:11434. Aucune configuration ici.
```

4. Redémarrer

```bash
baize
```

Si vous voyez le logo noir et or et le message de bienvenue, le démarrage a réussi.

# Exemples d'utilisation

Après le démarrage, décrivez vos besoins en langage naturel à l'invite `>>> 降旨：` :

```
>>> 降旨：Écris un script Python pour scraper le Top250 de Douban et l'enregistrer en CSV

>>> 降旨：Aide-moi à vérifier les erreurs de type dans tous les fichiers Python de src/

>>> 降旨：Trouve dans ce dépôt tous les endroits qui utilisent requests et remplace-les par httpx
```

## Interaction multilingue

Baize prend en charge **neuf langues** : chinois, English, 日本語, 한국어, Español, Français, deutsch, русский, العربية.

Deux façons de changer :

### Option 1 : parler directement (détection automatique)

Baize détecte automatiquement la langue de votre saisie et bascule :

```
>>> 降旨：Hello, help me write a Python script
[Système] Langue d'entrée détectée : English. Baize est passé à l'interaction en English.
(Baize répond en anglais)

>>> 降旨：日本語で答えてください
[Système] Langue d'entrée détectée : 日本語. Baize est passé à l'interaction en 日本語.
(Baize répond en japonais)
```

### Option 2 : commande manuelle

```
>>> 降旨：/lang                # Voir la langue actuelle et la liste disponible
[Système] Langue actuelle : chinois (zh)
[Système] Langues disponibles :
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> 降旨：/lang English        # Changer par nom de langue
>>> 降旨：/lang ja             # Changer par code de langue
>>> 降旨：/lang 西班牙语        # Les noms en chinois sont aussi acceptés
```

Prend en charge quatre formes : **nom de langue / code de langue / nom chinois / nom natif**. Par exemple, pour passer à l'anglais, `English`, `en`, `英语` ou `英文` fonctionnent.

## Commandes intégrées

- `/exit, /quit` --> Quitter Baize
- `/clear` --> Effacer l'historique de conversation, les todo, les enregistrements de réflexion et les enregistrements d'outils
- `/compact` --> Compresser manuellement le contexte (à utiliser quand la conversation est trop longue)
- `/commit` --> Enregistrer la session actuelle et commit dans Git (si dans un dépôt Git)
- `/lang` --> Voir la langue actuelle ; `/lang en` passe à l'anglais (accepte code ou nom de langue)
- `/skills` --> Lister toutes les compétences disponibles
- `/skills reload` --> Recharger le répertoire de compétences utilisateur
- `/unload` --> Décharger la compétence actuellement active
- `/show thought` --> Voir l'enregistrement complet des réflexions
- `/show tool` --> Voir l'enregistrement des appels d'outils
- `/show all` --> Voir tout l'historique de session
- `/技能名` --> Charger la compétence spécifiée (correspondance floue prise en charge)
- `/privacy` --> Contrôle de pseudonymisation de la vie privée (on / off / strict / status / rules / test / clear)
- `/privacy rule-off <name>` --> Désactiver une règle de pseudonymisation (ex. `/privacy rule-off phone_intl`)
- `/privacy rule-on  <name>` --> Réactiver une règle

## Exemples d'utilisation de l'accès aux données

Après avoir configuré SPSS / SQL, vous pouvez les piloter directement en langage naturel :

```text
>>> 降旨：Utilise SPSS pour ouvrir data.sav et donne-moi la liste des variables et la taille de l'échantillon

>>> 降旨：Fais des statistiques descriptives sur data.sav, puis lance une régression linéaire

>>> 降旨：Interroge la table sales pour les commandes de plus de 100 000 le mois dernier, groupées par client

>>> 降旨：Exporte les résultats d'analyse SPSS en CSV, puis joins-les aux données maîtres clients avec SQL
```

# Modèles locaux Ollama (coût zéro)

Vous ne voulez pas utiliser d'API cloud ? Utilisez Ollama en local :

```bash
# 1. Installer Ollama : https://ollama.com/download
# 2. Télécharger un modèle
ollama pull qwen2.5:7b

# 3. Démarrer le service Ollama
ollama serve

# 4. Modifier ~/.baize/config.toml
active_provider = "ollama"

# 5. Démarrer Baize
baize
```

Modèles recommandés : `qwen2.5:7b` (fort en chinois), `llama3.1:8b`, `deepseek-r1:7b`.

# Mécanismes d'extension

Baize prend en charge quatre méthodes d'extension. Placez-les dans le répertoire de travail courant pour qu'elles prennent effet.

## Compétences (Skills)

Écrivez des connaissances métier dans `./skills/nom-de-compétence/SKILL.md`. L'IA les chargera de manière proactive lorsqu'elle rencontrera des tâches complexes.

```markdown
---
name: pandas-eda
description: Bonnes pratiques pour l'analyse exploratoire de données avec pandas
tags: data,python
---

# Guide Pandas EDA

## Étapes principales
1. Utiliser df.info() pour inspecter les types de champs et les valeurs manquantes
2. Utiliser df.describe() pour les statistiques descriptives
...
```

Vous pouvez aussi la charger manuellement dans la conversation avec `/pandas-eda`.

## Sous-agents (Subagents)

Définissez des sous-agents dédiés dans `./subagent/nom-de-rôle/AGENT.md`. L'agent principal peut déléguer des tâches via l'outil agent.

```markdown
---
name: code-reviewer
description: Réviseur de code strict
---

Vous êtes un réviseur de code senior. Lors de la revue, priorisez :
1. Les conditions limites et la gestion des exceptions
2. Les fuites de ressources
3. La sécurité de concurrence
...
```

## Hooks

Placez ce qui suit dans `./hooks/` :

- `PreToolUse-*.sh`
- `PostToolUse-*.sh`
- `Stop-*.sh`

Ils reçoivent une entrée JSON et renvoient une décision :

```bash
#!/bin/bash

# PreToolUse-guard.sh

read -r input

if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Deletion prohibited"}}'
fi
```

Les hooks Python peuvent appeler directement les API intégrées (voir les fonctions `hook_*` dans `Baize.py`).

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

# Conception de sécurité (cœur)

Baize active par défaut les mécanismes de sécurité suivants :

- **Liste blanche de commandes** : seules les commandes courantes comme `ls`, `cat`, `grep`, `git`, `python3`, etc. sont autorisées.
- **Détection d'évasion de chemin** : toutes les opérations de fichiers sont limitées au répertoire de travail courant et à `/tmp`.
- **Interception de commandes dangereuses** : intercepte des motifs comme `rm -rf /`, fork bomb, `curl | sh`, `git push --force`, etc.
- **Protection des fichiers sensibles** : interdit la modification de `.env`, `.ssh/`, `id_rsa`, `*.pem`, etc.
- **Interception d'injection de scripts** : détecte les contournements comme `python -c "os.system(...)"`.
- **Limites de ressources de processus** : limite CPU, mémoire et nombre de processus sous Linux/macOS.
- **Pseudonymisation de la vie privée (bidirectionnelle réversible)** : les PII sont remplacées par des espaces réservés aléatoires en sortie et restaurées en entrée ; pseudonymisation indépendante sur disque.
- **Résistance à l'injection d'espaces réservés** : jetons cryptographiques aléatoires de 64 bits + neutralisation côté entrée + isolation de session.
- **Pseudonymisation des journaux d'audit** : `hook_audit_log` pseudonymise avant écriture sur disque + tronque + refuse d'écrire en cas d'échec.

Si vous devez assouplir les restrictions dans des projets de confiance, vous pouvez modifier `ALLOWED_COMMANDS` et `FORBIDDEN_PATH_PATTERNS` dans `Baize.py`.

# Pseudonymisation de la vie privée (cœur)

Baize intègre un mécanisme de protection de la vie privée **bidirectionnel réversible + pseudonymisation sur disque**, couvrant tout le trajet depuis l'entrée jusqu'au disque :

- **Sortie** : avant l'envoi au LLM, les PII sont remplacées par des espaces réservés impossibles à deviner
- **Entrée** : les espaces réservés dans les réponses du LLM sont restaurés en texte original
- **Sur disque** : les fichiers de session, les transcriptions compressées et les journaux d'audit sont **pseudonymisés indépendamment** avant écriture. Aucun texte en clair ne reste sur le disque

**Désactivé par défaut**, à activer si nécessaire.

## Deux façons de l'activer

### Option 1 : langage naturel

Dites directement dans la conversation :

```
>>> 降旨：Active la pseudonymisation de la vie privée
[Système] Pseudonymisation de la vie privée activée (mode Standard).

>>> 降旨：Active la pseudonymisation stricte
[Système] Pseudonymisation de la vie privée activée (mode Strict).

>>> 降旨：Désactive la protection de la vie privée
[Système] Pseudonymisation de la vie privée désactivée.
```

### Option 2 : commandes slash

- `/privacy on` Activer le mode Standard
- `/privacy strict` Activer le mode Strict
- `/privacy off` Désactiver
- `/privacy status` Voir l'état, l'ID de session, le nombre de règles, les statistiques LRU/TTL
- `/privacy rules` Lister toutes les règles (y compris leur état d'activation)
- `/privacy rule-off <name>` Désactiver une règle
- `/privacy rule-on  <name>` Réactiver une règle
- `/privacy test <text>` Tester l'effet de pseudonymisation
- `/privacy clear` Vider le mapping des espaces réservés et **faire tourner l'ID de session**

## Deux niveaux

**Standard** : numéros de mobile de Chine continentale, numéros de carte d'identité, numéros de carte bancaire (vérification Luhn), e-mails, IPv4/IPv6, clés API OpenAI/Anthropic/GitHub/AWS, Bearer Tokens, blocs de clé privée, champs de mot de passe, identifiants dans les URL.

**Strict** : tout le mode Standard + noms chinois, numéros QQ, identifiants WeChat, plaques d'immatriculation de Chine continentale.

## Fonctionnement

Entrée utilisateur (contenant de vrais PII) → messages stocke le texte original

↓ `sanitize_messages()`

Ce qui est envoyé au LLM est `[[PHONE_1]]`, `[[EMAIL_1]]`

↓ Réponse du LLM

Les espaces réservés renvoyés → `restore_message()`

Restaurés en texte original → écriture sur disque / affichage / exécution d'outils

- **Pseudonymisation de la vie privée (bidirectionnelle réversible)** : les PII sont remplacées par des espaces réservés aléatoires en sortie et restaurées en entrée ; pseudonymisation indépendante sur disque.
- **Résistance à l'injection d'espaces réservés** : jetons cryptographiques aléatoires de 64 bits + neutralisation côté entrée + isolation de session.
- **Pseudonymisation des journaux d'audit** : `hook_audit_log` pseudonymise avant écriture sur disque + tronque + refuse d'écrire en cas d'échec.

## Classement intelligent des paramètres d'outils

**Pseudonymisés** (paramètres texte pur, ne participant pas à l'exécution réelle) :
- `todo`, `ask_user_question`, `task_create`, `task_update`

**Non pseudonymisés** (les chemins/commandes/URL sont réellement utilisés) :
- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep` (les chemins servent aux IO)
- `run_bash` / `background_run` (les commandes sont exécutées)
- `run_webfetch` / `web_search` (les URL sont réellement envoyées au réseau)
- `set_workspace` (le chemin sert à `chdir`)
- `load_skills` (les noms de compétences sont des énumérations)
- `agent` (le contexte du sous-agent est pseudonymisé indépendamment)
- `mcp_*` (sémantique inconnue, traitement conservateur)

**Tout est pseudonymisé lors de la persistance** (car le contenu persisté ne sera pas réexécuté ; la sécurité prime).

## Pseudonymisation sur disque

**Activée par défaut**, indépendante de la pseudonymisation en mémoire. Même si vous utilisez `/privacy off` (pas de pseudonymisation en mémoire), la pseudonymisation sur disque applique au moins les règles Standard.

**Caractéristiques clés** :
- La pseudonymisation sur disque utilise une **table de mapping indépendante et à usage unique** : les espaces réservés écrits sur disque **ne peuvent pas être restaurés**, car la table de mapping est jetée.
- Si la pseudonymisation sur disque **échoue, elle refuse d'écrire du texte en clair** (pas de dégradation, pas d'omission silencieuse).
- Si d'anciens fichiers de session contiennent du texte en clair, ils sont automatiquement pseudonymisés et réécrits lors de la première sauvegarde.

**Comment la désactiver** (non recommandé) : modifiez `PERSIST_REDACT_ENABLED = False` dans `Baize.py`.

## Exemple

```
>>> 降旨：/privacy test Mon numéro de téléphone est 13812345678, mon e-mail est a@b.com
Original : Mon numéro de téléphone est 13812345678, mon e-mail est a@b.com
Pseudonymisé : Mon numéro de téléphone est [[PHONE_1]], mon e-mail est [[EMAIL_1]]
Restauré : Mon numéro de téléphone est 13812345678, mon e-mail est a@b.com

>>> 降旨：/privacy status
[Pseudonymisation de la vie privée]
Mode actuel : Mode Standard (standard)
ID de session : 7d2f5e91
Règles actives : 34 / 41
Espaces réservés actifs : 2
Capacité de mapping : 2 / 2000
TTL : 86400 secondes
Évictions LRU : 0
Évictions TTL : 0
Appels de pseudonymisation : 3
Appels de restauration : 3

>>> 降旨：/privacy rules
[Liste des règles de pseudonymisation] Total 41
[Standard + Strict]
[✓] phone_cn Numéro de mobile de Chine continentale (standard,strict)
[✓] id_card_cn Numéro de carte d'identité de Chine continentale (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
[Strict uniquement]
[✓] name_cn Nom chinois (strict)
[✓] address_cn Adresse détaillée chinoise (strict)
...
Utilisation :
/privacy rule-off <name> Désactiver une règle
/privacy rule-on <name> Réactiver une règle
```

### Exemples de test

<div align="center">
Écran de test de protection de la vie privée -- 01
</div>

<p align="center">
  <img src="image/privary01.jpg" alt="Écran de test de protection de la vie privée" width="800" />
</p>

<div align="center">
Écran de test de protection de la vie privée -- 02
</div>

<p align="center">
  <img src="image/privary02.jpg" alt="Écran de test de protection de la vie privée" width="800" />
</p>

# Accès aux données (cœur)

Baize se connecte aux logiciels d'analyse de données d'entreprise via **MCP (Model Context Protocol)**. Le programme principal ne nécessite aucune modification : il suffit d'enregistrer le serveur dans `MCP/mcp_config.json`.

## Intégration SPSS

### Prérequis

- IBM SPSS Statistics installé localement (version 20–31 ; Windows recommandé)
- SPSS sous licence et capable de démarrer normalement

### Étapes de configuration

1. **Trouver le répertoire d'installation de SPSS :** le chemin par défaut est généralement `C:\Program Files\IBM\SPSS Statistics\` suivi du numéro de version (par exemple 31).

2. **Définir la variable d'environnement** (peut être dans `.env` ou dans les variables d'environnement système) :

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **Vérifier l'état** :

```bash
spss-studio-mcp status
```

Sortie attendue :

```text
=== SPSS MCP Capability Status ===
pyreadstat : OK v1.3.6
pandas     : OK v3.0.2
SPSS batch : OK
```

4. **Enregistrer dans `MCP/mcp_config.json`** :

```json
{
  "mcpServers": [
    {
      "name": "spss",
      "command": "spss-studio-mcp",
      "args": ["serve", "--transport", "stdio"],
      "env": {
        "SPSS_INSTALL_PATH": "C:\\Program Files\\IBM\\SPSS Statistics\\31"
      },
      "enabled": true
    }
  ]
}
```

### Si `SPSS batch: NOT FOUND`

Cela signifie que `spss-studio-mcp` n'a pas trouvé le moteur SPSS, mais que `pyreadstat` + `pandas` fonctionnent. Dans ce cas, il passe en **mode fichier** :

- Peut lire `.sav`, consulter les métadonnées, prévisualiser les données et convertir CSV ↔ SAV
- Ne peut pas exécuter de statistiques (test t, régression, ANOVA, etc.)

Solution : configurez correctement `SPSS_INSTALL_PATH` dans `MCP/mcp_config.json`, ou acceptez la dégradation en mode fichier.

## Intégration SQL

### Bases de données prises en charge

PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, DM, KingbaseES, TiDB, OceanBase, etc. (basé sur les pilotes SQLAlchemy 2.0).

### Étapes de configuration

1. **Préparer un compte de base de données en lecture seule** (fortement recommandé) :

```sql
CREATE USER baize_ro WITH PASSWORD 'xxx';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO baize_ro;
```

2. **Préparer la chaîne de connexion** :

- PostgreSQL --> `postgresql+psycopg://user:pwd@host:5432/db`
- MySQL --> `mysql+pymysql://user:pwd@host:3306/db`
- SQL Server --> `mssql+pyodbc://user:pwd@host:1433/db?driver=ODBC+Driver+18+for+SQL+Server`
- Oracle --> `oracle+oracledb://user:pwd@host:1521/?service_name=ORCL`

3. **Enregistrer dans `MCP/mcp_config.json`** :

```json
{
  "mcpServers": [
    {
      "name": "sql",
      "command": "atengk-mcp-server-rdbms",
      "args": ["--transport", "stdio"],
      "env": {
        "DATABASE_URL": "postgresql+psycopg://baize_ro:pwd@localhost:5432/prod"
      },
      "enabled": true
    }
  ]
}
```

### Garde-fous de sécurité (intégrés)

`atengk-mcp-server-rdbms` offre plusieurs couches de protection :

- **Garde SELECT au niveau AST** : analyse l'arbre syntaxique avec `sqlglot` et bloque physiquement les opérations d'écriture comme `DELETE/UPDATE/DROP/TRUNCATE`.
- **Injection automatique de LIMIT** : les requêtes sans nombre de lignes spécifié reçoivent obligatoirement `LIMIT 100`, évitant qu'un balayage complet de table ne provoque un débordement mémoire.
- **Lecture seule par défaut** : les opérations d'écriture doivent être explicitement autorisées via `--allow-dml` / `--allow-ddl`.
- **Interception d'injection SQL** : rejette au niveau AST les instructions malveillantes construites par concaténation de chaînes.

### Configurer plusieurs bases de données à la fois

Si vous voulez vous connecter à plusieurs bases simultanément, enregistrez plusieurs serveurs :

```json
{
  "mcpServers": [
    {
      "name": "sql_prod",
      "command": "atengk-mcp-server-rdbms",
      "args": ["--transport", "stdio"],
      "env": { "DATABASE_URL": "postgresql+psycopg://ro:pwd@prod:5432/db" },
      "enabled": true
    },
    {
      "name": "sql_warehouse",
      "command": "atengk-mcp-server-rdbms",
      "args": ["--transport", "stdio"],
      "env": { "DATABASE_URL": "mysql+pymysql://ro:pwd@dw:3306/analytics" },
      "enabled": true
    }
  ]
}
```

Baize fusionnera automatiquement tous leurs outils dans `MATERTOOLS`, et le LLM choisira automatiquement selon la tâche.

# Structure du répertoire

```
baize-agent/
├── pyproject.toml              # Configuration d'empaquetage
├── requirements-data.txt       # Dépendances d'accès aux données (optionnel)
├── requirements-data           # Dépendances d'accès
├── README.md
├── tests/                      # Tests (non publiés avec le paquet)
|   ├── __init__.py
|   ├── test_history.py
|   └── test_skill_loader.py
├── .env.example                # Exemple de variables d'environnement
├── .gitignore
└── agent/                      # Paquet principal
    ├── __init__.py
    ├── Baize.py                # Programme principal et Agent Loop
    ├── config.py               # Chargement de configuration multi-backend
    ├── ui_theme.py             # Thème de rendu CLI
    ├── utils.py                # Utilitaires généraux
    ├── logo.txt
    ├── skills/                 # Compétences intégrées
    ├── subagent/               # Sous-agents intégrés
    ├── core/                   # Logique cœur (sans effet de bord, testable unitairement)
    |   ├── __init__.py
    |   ├── history.py          # Nettoyage de l'historique de session / estimation des tokens / compression
    |   └── privacy.py          # Pseudonymisation : détection PII / remplacement par espaces réservés / restauration réversible
    ├── hooks/                  # Hooks intégrés
    └── MCP/                    # Client MCP et configuration
        ├── __init__.py
        ├── mcp_client.py
        └── mcp_config.json
```

# Référence des variables d'environnement

| Variable | Description | Valeur par défaut |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | Clé API DeepSeek | — |
| `DEEPSEEK_BASE_URL` | Endpoint DeepSeek | `https://api.deepseek.com` |
| `OPENAI_API_KEY` | Clé de l'endpoint compatible OpenAI | — |
| `OPENAI_BASE_URL` | Endpoint compatible OpenAI | `https://api.openai.com/v1` |
| `OLLAMA_BASE_URL` | Adresse du service Ollama | `http://localhost:11434` |

**Écrivez les variables ci-dessus dans `~/.baize/.env` ; inutile de modifier les fichiers de configuration du shell.**

Variables d'analyse de données :

| Variable | Description | Valeur par défaut |
| --- | --- | --- |
| `SPSS_INSTALL_PATH` | Répertoire d'installation d'IBM SPSS Statistics | — (si non défini, dégradation en mode fichier) |
| `DATABASE_URL` | Chaîne de connexion à la base pour SQL MCP | — (lue par le serveur MCP) |

**Écrivez les variables ci-dessus dans `MCP/mcp_config.json`.**

# Développement

## Exécuter les tests

Ce projet utilise pytest. Avant de développer, installez le paquet en mode éditable avec les dépendances de développement :

```bash
pip install -e ".[dev]"
```

Exécuter tous les tests :

```bash
python -m pytest tests/ -v
```

Exécuter un seul fichier :

```bash
python -m pytest tests/test_history.py -v
```

## Conventions de structure du code

- `agent/` : paquet principal publié avec le paquet. Toute la logique d'exécution et les ressources (skills, subagent, hooks, MCP) sont ici.
- `agent/core/` : modules de logique pure, sans effets de bord externes. **Ils doivent pouvoir être testés indépendamment.** Ajoutez ce type de logique ici, avec des tests.
- `tests/` : correspondance un-à-un avec les fichiers source sous `agent/`, nommés `test_<module>.py`.
- Toute fonction avec dépendances externes (réseau, disque, état global) doit injecter ses dépendances via des paramètres pour pouvoir être remplacée dans les tests.

# ❓ FAQ

- Q : Où dois-je mettre la clé ?

R : `~/.baize/.env`, pas le `.env` à la racine du projet.

- Q : Faut-il réinstaller en changeant de backend ?

R : Non. Modifiez simplement `active_provider` dans `~/.baize/config.toml`.

- Q : Ollama local nécessite-t-il une clé ?

R : Non. Choisissez `active_provider = "ollama"` et laissez `env_key` vide.

- Q : Comment changer le répertoire de travail ?

R : Dans la conversation, dites directement « change vers /path/to/project », et Baize appellera l'outil `set_workspace`.

- Q : Que se passe-t-il si le contexte est trop long ?

R : Baize compresse automatiquement en deux niveaux : d'abord il tronque les anciens résultats d'outils, puis demande au LLM de générer un résumé. Vous pouvez aussi utiliser `/compact` manuellement.

- Q : Va-t-il supprimer mes fichiers par erreur ?

R : La liste blanche de commandes par défaut intercepte les opérations dangereuses comme `rm -rf /` ; avant d'écrire un fichier, il affiche un Diff et demande confirmation.

- Q : Comment connecter Baize à SPSS ?

R : 1. Installez `pip install -r requirements-data.txt` ; 2. définissez la variable d'environnement `SPSS_INSTALL_PATH` vers le répertoire d'installation de SPSS ; 3. activez le serveur spss dans `MCP/mcp_config.json`. Voir la section « Accès aux données (SPSS / SQL) ».

- Q : Que faire si `SPSS batch: NOT FOUND` apparaît ?

R : Cela signifie que le moteur SPSS n'a pas été trouvé. Vérifiez que `SPSS_INSTALL_PATH` pointe correctement vers le répertoire contenant `stats.exe` ; si vous ne traitez que des fichiers `.sav`, vous pouvez ignorer cet avertissement (dégradation en mode fichier).

- Q : Que faut-il installer en plus pour se connecter à une base SQL ?

R : Au niveau Python, installez `atengk-mcp-server-rdbms` (`pip install` le fait automatiquement). **Les utilisateurs de SQL Server doivent aussi installer Microsoft ODBC Driver 18 au niveau système**, ce qui ne peut pas être installé avec pip.

- Q : Baize peut-il supprimer par erreur les données de ma base ?

R : Non. SQL MCP n'autorise que SELECT par défaut et bloque toutes les opérations d'écriture au niveau de l'arbre syntaxique AST. Il est toujours fortement recommandé de créer un **compte de base de données en lecture seule** dédié à Baize comme double garantie.

- Q : Les données des résultats d'analyse SPSS fuiteront-elles vers le LLM ?

R : Si la pseudonymisation de la vie privée est activée (`/privacy on`), les résultats renvoyés par les outils sont automatiquement pseudonymisés pour les PII comme numéros de téléphone, e-mails et cartes d'identité avant d'être envoyés au LLM. **Mais il est recommandé d'utiliser aussi un compte en lecture seule + un échantillonnage des données** (ne requêter que les champs nécessaires) pour réduire le risque.

- Q : Pourquoi Baize devient-il plus lent et consomme-t-il plus de tokens après l'ajout de SPSS/SQL ?

R : Parce que les définitions d'outils exposées par les serveurs MCP sont envoyées au LLM à chaque tour de conversation. SPSS a plus de 60 outils, ajoutant environ 6 000–12 000 tokens de surcoût fixe. Si votre flux de travail habituel n'implique pas SPSS, vous pouvez mettre son `enabled` à `false` et l'activer au besoin.

# 🤝 Contribution

Les Issues et PR sont les bienvenus. Il est recommandé de lire `CONTRIBUTOR.md` avant de soumettre une PR.

### Merci à chaque contributeur qui soumet une PR

- Contributeurs GitHub :
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# Licence

MIT License

# Remerciements

- Ce projet est hébergé sur AtomGit en Chine. Lien du projet : https://atomgit.com/Com_Xu/Baize

- Merci à AtomGit d'avoir inclus ce projet dans le programme d'incubation G-star.

- Merci aux contributeurs de PR, aux abonnés Douyin et aux étudiants qui me suivent.

- Inspiré par d'excellents outils d'AI Coding comme Claude Code et Codex.

- Construit sur DeepSeek, OpenAI SDK et MCP.

- Merci à tous les développeurs qui parcourent ensemble le chemin du Vibe Coding.

# ☕ Soutien

Si Baize vous est utile, vous êtes invité à le sponsoriser et à le soutenir. Le développement indépendant prend aussi beaucoup de temps. Le sponsoring ne changera pas le calendrier de mise à jour du produit. Merci pour votre soutien !

<p align="center">
  <img src="image/support.jpg" alt="QR code WeChat" width="200" />
</p>

# Me contacter

- Si Baize vous intéresse, ou si vous souhaitez participer à une collaboration open source, vous pouvez me contacter de la manière suivante.
- **Actuellement, je suis en recherche d'emploi. J'ai travaillé dans l'étude de marché et la recherche utilisateur, et je connais aussi un peu les Agents. Si mes compétences correspondent à vos besoins, j'espère travailler avec vous (postes visés : Opérations produit IA / Recherche utilisateur / Étude de marché).**

<p align="center">
  <img src="image/weixin.jpg" alt="QR code WeChat" width="200" />
</p>

<p align="center">Scannez le QR code WeChat. Précisez collaboration open source Baize ou recrutement entreprise.</p>

<p align="center">
  <img src="image/抖音.png" alt="QR code Douyin" width="200" />
</p>

<p align="center">Scannez le QR code Douyin pour suivre.</p>