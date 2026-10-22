<div align="center">

<img src="image/logopage02.png" alt="Logo Baize" width="320" />

# Baize

**Dis tout ce que tu sais, garde bien les secrets**

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

Un assistant de sécurité pour le Vibe Coding et l'analyse de données, inspiré d'une bête mythique chinoise.

**Une CLI de Coding Agent open source dotée d'une forte protection de la vie privée et d'une interaction multilingue. Elle prend en charge plusieurs backends (DeepSeek / compatible OpenAI / Zhipu / Tongyi / Kimi / Ollama local) et offre des capacités complètes telles que l'appel d'outils, le chargement de compétences, la délégation à des sous-agents, la compression de contexte et un bac à sable sécurisé.**

----------

# Avantages principaux

## Protection de la vie privée

- **Protection de la vie privée bidirectionnelle réversible** : Les informations sensibles sont remplacées par des espaces réservés avant d'être envoyées au LLM, puis restaurées automatiquement après réception de la réponse. Tout le processus est invisible pour l'utilisateur : l'historique, les paramètres d'outils et les réponses finales que vous voyez contiennent toujours le texte original, tandis que le LLM ne voit que des espaces réservés aléatoires et impossibles à deviner, comme `«PZ_PHONE_a3f8b2c1d4e5f6a7»`.
- **Masquage complet sur disque** : Les fichiers de session, les transcriptions compressées et les journaux d'audit sont automatiquement masqués avant d'être écrits sur disque (activé par défaut). Aucune PII en clair n'apparaît jamais sur le disque.
- **Résistance aux injections** : Les espaces réservés utilisent des jetons cryptographiques aléatoires de 64 bits et ne peuvent être énumérés, falsifiés ou rejoués. Les anciens espaces réservés deviennent immédiatement invalides après un changement de session.
- **Plusieurs façons d'activer la protection de la vie privée** : Vous pouvez l'activer via le langage naturel dans la CLI, ou utiliser la commande plus précise `/privacy`.
- **Agent local-first** : Ce produit ne dispose d'aucune base de données distante et fonctionne entièrement en local. Il ne collecte aucune information utilisateur.

# Fonctionnalités

- **Prise en charge multi-backend** : DeepSeek, tout endpoint compatible OpenAI (GLM / Qwen / Kimi / OpenAI) et Ollama local. Changement en une seule configuration.

- **Démarrage sans configuration** : Les fichiers de configuration sont générés automatiquement au premier lancement. L'utilisateur n'a besoin de saisir sa clé API qu'une seule fois.

- **Masquage de confidentialité** : Identifie et masque automatiquement **plus de 30 types** d'informations sensibles avant l'envoi au LLM (numéros de téléphone, e-mails, cartes d'identité, passeports, cartes bancaires, numéros internationaux, clés API, JWT, chaînes de connexion à des bases de données, adresses MAC, etc.), puis les restaure après réception de la réponse. **Le même masquage est appliqué lors de l'écriture sur disque**, de sorte qu'aucun texte en clair ne reste sur le disque. Prend en charge les modes standard et strict, commutables via le langage naturel ou la commande `/privacy`.

- **Interaction multilingue** : Basculez librement entre neuf langues : chinois, anglais, japonais, coréen, espagnol, français, allemand, russe et arabe. Dites `English` ou utilisez `/lang ja`, et l'IA réfléchira et répondra dans la langue correspondante tout au long de la session.

- **Chaîne d'outils complète** : exécution bash, lecture/écriture/édition de fichiers, recherche glob/grep, recherche et récupération web, tâches en arrière-plan, gestion des tâches et des to-do.

- **Système de compétences (Skills)** : Chargez des connaissances métier à la demande (`SKILL.md`) pour que l'IA soit plus professionnelle dans des scénarios spécifiques.

- **Sous-agents (Subagents)** : Déléguez des tâches complexes à des sous-agents au contexte indépendant pour éviter de polluer la session principale.

- **Hooks** : Hooks Python ou Shell prenant en charge l'interception avant/après les appels d'outils, les journaux d'audit, le formatage automatique et le contrôle des tests.

- **Protocole MCP** : Connectez des serveurs d'outils externes (GitHub, Filesystem, etc.) via le Model Context Protocol.

- **Compression de contexte** : Compression à deux niveaux (troncature des résultats d'outils + résumé par LLM) prenant en charge les conversations très longues.

- **Bac à sable sécurisé** : Liste blanche de commandes, détection d'évasion de chemin, blocage des commandes dangereuses, protection des fichiers sensibles et interception d'injection de scripts.

- **CLI à thème noir et or** : Adaptation automatique de la largeur des caractères chinois, coloration syntaxique, coloration des diffs et repli de la réflexion.

# Interface de la CLI Baize

<div align="center">
Écran de démarrage de la CLI Baize
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="Écran de démarrage de la CLI Baize" width="800" />
</p>

<div align="center">
Écran d'exécution de la CLI Baize -- 01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="Écran d'exécution de la CLI Baize" width="800" />
</p>

<div align="center">
Écran d'exécution de la CLI Baize -- 02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="Écran d'exécution de la CLI Baize" width="800" />
</p>

# Installation

## Prérequis

- Python 3.10+ (nécessite `tomllib` ; intégré à partir de 3.11 ; sur 3.10, installez `tomli`)
- pip

## Installation depuis les sources

### Deux méthodes de téléchargement

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- appuyez sur Win+R, saisissez `cmd`, puis exécutez :

    baize

2. Sur la page du dépôt, cliquez sur `<> Code` --> `Download ZIP`.

(1) Après extraction, entrez dans le répertoire :

    bash -- appuyez sur Win+R, saisissez cmd

    cd chemin\vers\le\répertoire\extrait

    pip install -r requirements.txt

    python -m Baize

Après l'installation, appuyez sur Win+R, saisissez `cmd`, ouvrez la CLI, tapez `baize` et exécutez-le.

(2) Après avoir téléchargé le ZIP, installez en local. Extrayez-le, entrez dans le répertoire et exécutez :

    bash -- appuyez sur Win+R, saisissez cmd

    pip install .

Après l'installation, appuyez sur Win+R, saisissez `cmd`, ouvrez la CLI, tapez `baize` et exécutez-le.

### Optionnel : installer les dépendances d'accès aux données (important pour l'analyse de données)

Si vous souhaitez que Baize pilote SPSS ou des bases de données SQL, installez les dépendances supplémentaires :

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` inclut :
- `spss-studio-mcp` : serveur MCP d'analyse statistique SPSS (nécessite IBM SPSS Statistics installé localement)
- `atengk-mcp-server-rdbms` : serveur MCP générique pour bases de données relationnelles (PostgreSQL / MySQL / SQL Server / Oracle / Dameng, etc.)
- `pyodbc` : liaison Python ODBC requise par SQL Server

Alternativement, si le projet est installé via `pyproject.toml`, vous pouvez utiliser les extras :

```bash
pip install -e ".[data]"          # Installer toutes les dépendances d'accès aux données
pip install -e ".[spss]"          # SPSS uniquement
pip install -e ".[sql]"           # SQL générique uniquement
pip install -e ".[sql-mssql]"     # SQL Server uniquement (inclut pyodbc)
```

- **⚠️ Utilisateurs de SQL Server : `pyodbc` n'est que la liaison Python. Vous devez également installer Microsoft ODBC Driver 18 for SQL Server au niveau du système.**
- **⚠️ Utilisateurs de SPSS : `spss-studio-mcp` n'est qu'une couche de pont MCP. IBM SPSS Statistics (versions 20–31) doit être installé localement et sous licence active, et la variable d'environnement `SPSS_INSTALL_PATH` doit pointer vers le répertoire d'installation de SPSS. L'analyse statistique complète avec le moteur SPSS est principalement prise en charge sous Windows. Sous Linux/macOS, il peut basculer en « mode fichier » (lire des fichiers `.sav`, inspecter les métadonnées, prévisualiser les données, mais sans analyse statistique).**

# Démarrage rapide

## Exécution avec une API LLM

1. Premier lancement

```bash
baize
```

Lors du premier lancement, Baize génère automatiquement deux fichiers de configuration :

```
~/.baize/config.toml   # Configuration du backend (choisir DeepSeek / OpenAI / Ollama)

~/.baize/.env          # Fichier de clés
```

Sous Windows, le chemin est `C:\Users\VotreNomUtilisateur\.baize\`.

**2. Choisir un backend**

Ouvrez `~/.baize/config.toml` et modifiez **active_provider** (cette étape est obligatoire) :

```toml
# Fichier de configuration Baize
# Modifiez active_provider pour changer de backend
# Valeurs possibles : "deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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

**3. Saisir votre clé API**

Éditez `~/.baize/.env`. **Si vous devez utiliser un LLM particulier, supprimez le `#` initial de la ligne de clé de ce fournisseur, ajoutez `#` devant les clés des autres LLM pour verrouiller leur sortie, saisissez la clé API et assurez-vous d'enregistrer le fichier. Il ne prend effet qu'après l'enregistrement** :

```env
# ============================================================
# Fichier de clés Baize
# ============================================================
# Ne renseignez que la clé du backend que vous souhaitez utiliser ; laissez le reste commenté.
# Les noms de variables doivent correspondre aux champs env_key de config.toml.
#
# Emplacement :
#   Linux / macOS : ~/.baize/.env
#   Windows :       C:\Users\VotreNomUtilisateur\.baize\.env
# ============================================================

# ---------- DeepSeek (backend par défaut) ----------
# Obtenez-la sur : https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI ou tout endpoint compatible OpenAI (optionnel) ----------
# Convient à Groq, Tongyi, Moonshot, Zhipu, OpenAI, etc.
# Remarque : base_url se configure dans [model_providers.xxx] de config.toml, pas ici.
# OPENAI_API_KEY=

# ---------- Tongyi Qianwen (optionnel) ----------
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
# Assurez-vous simplement qu'Ollama est en cours d'exécution sur localhost:11434. Aucune configuration n'est nécessaire ici.
```

4. Redémarrer

```bash
baize
```

Si vous voyez le logo noir et or et le message de bienvenue, le démarrage a réussi.

## Modèles locaux Ollama (coût zéro)

Vous ne voulez pas utiliser une API cloud ? Utilisez Ollama en local :

    bash

    # 1. Installer Ollama : https://ollama.com/download
    # 2. Télécharger un modèle
    ollama pull qwen2.5:7b

    # 3. Démarrer le service Ollama
    ollama serve

    # 4. Modifier ~/.baize/config.toml
    active_provider = "ollama"

    # 5. Démarrer Baize
    baize

Modèles recommandés : `qwen2.5:7b` (fort en chinois), `llama3.1:8b`, `deepseek-r1:7b`.

# Exemples d'utilisation

Après le démarrage, décrivez vos besoins en langage naturel à l'invite `>>> 降旨：` :

```
>>> 降旨：Écris un script Python pour scraper Douban Top250 et l'enregistrer en CSV

>>> 降旨：Aide-moi à vérifier les erreurs de type dans tous les fichiers Python sous src/

>>> 降旨：Trouve dans ce dépôt tous les endroits qui utilisent requests et remplace-les par httpx
```

## Interaction multilingue

Baize prend en charge **neuf langues** : chinois, anglais, japonais, coréen, espagnol, français, allemand, russe et arabe.

Il existe deux façons de changer :

### Méthode 1 : parler directement (détection automatique)

Baize détecte automatiquement la langue de votre saisie et bascule :

```
>>> 降旨：Hello, help me write a Python script
[Système] Langue d'entrée détectée : English. Baize est passé à l'interaction en English.
(Baize répond en anglais)

>>> 降旨：日本語で答えてください
[Système] Langue d'entrée détectée : 日本語. Baize est passé à l'interaction en 日本語.
(Baize répond en japonais)
```

### Méthode 2 : commande manuelle

```
>>> 降旨：/lang                # Afficher la langue actuelle et la liste disponible
[Système] Langue actuelle : 中文 (zh)
[Système] Langues disponibles :
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> 降旨：/lang English        # Changer par nom de langue
>>> 降旨：/lang ja             # Changer par code de langue
>>> 降旨：/lang 西班牙语        # Le nom en chinois fonctionne aussi
```

Prend en charge **nom de langue / code de langue / nom en chinois / nom natif**. Par exemple, pour passer à l'anglais, n'importe lequel de `English`, `en`, `英语` ou `英文` fonctionne.

## Commandes intégrées

- `/exit`, `/quit` --> Quitter Baize
- `/clear` --> Effacer l'historique de conversation, les to-do, les enregistrements de réflexion et les enregistrements d'outils
- `/compact` --> Compresser manuellement le contexte (à utiliser lorsque la conversation est trop longue)
- `/commit` --> Enregistrer la session actuelle et faire un commit Git (si dans un dépôt Git)
- `/lang` --> Afficher la langue actuelle ; `/lang en` passe à l'anglais (prend en charge les codes ou noms de langue)
- `/skills` --> Lister toutes les compétences disponibles
- `/skills reload` --> Recharger le répertoire des compétences utilisateur
- `/unload` --> Décharger la compétence actuellement active
- `/show thought` --> Afficher l'enregistrement complet de réflexion
- `/show tool` --> Afficher les enregistrements d'appels d'outils
- `/show all` --> Afficher tout l'historique de la session
- `/nom-de-compétence` --> Charger une compétence spécifiée (prend en charge la correspondance floue)
- `/privacy` --> Contrôle du masquage de confidentialité (`on / off / strict / status / rules / test / clear`)
- `/privacy rule-off <name>` --> Désactiver une règle de masquage (ex. `/privacy rule-off phone_intl`)
- `/privacy rule-on <name>` --> Réactiver une règle

## Exemples d'utilisation de l'accès aux données

Après avoir configuré SPSS / SQL, vous pouvez les piloter directement en langage naturel :

```text
>>> 降旨：Utilise SPSS pour ouvrir data.sav et indique-moi la liste des variables et la taille de l'échantillon

>>> 降旨：Lance des statistiques descriptives sur data.sav, puis une régression linéaire

>>> 降旨：Interroge la table sales pour les commandes dont le montant dépasse 100 000 le mois dernier, groupées par client

>>> 降旨：Exporte les résultats de l'analyse SPSS en CSV, puis joins-les aux données maîtres clients avec SQL
```

# Mécanismes d'extension

Baize prend en charge quatre mécanismes d'extension. Placez-les dans le répertoire de travail actuel et ils prendront effet.

## Compétences (Skills)

Écrivez des connaissances métier dans `./skills/<nom-de-compétence>/SKILL.md`. L'IA le chargera proactivement lorsqu'elle rencontrera des tâches complexes.

    markdown

    ---
    name: pandas-eda

    description: Bonnes pratiques pour l'analyse exploratoire de données avec pandas

    tags: data,python
    ---

    # Guide Pandas EDA

    ## Étapes principales
    1. df.info() pour inspecter les types de champs et les valeurs manquantes
    2. df.describe() pour la description statistique
    ...

Vous pouvez également la charger manuellement dans la conversation avec `/pandas-eda`.

## Sous-agents (Subagents)

Définissez des sous-agents spécialisés dans `./subagent/<nom-de-rôle>/AGENT.md`. L'agent principal peut déléguer des tâches via l'outil `agent`.

    markdown

    ---
    name: code-reviewer

    description: Réviseur de code strict
    ---

    Vous êtes un réviseur de code senior. Lors de la revue, priorisez :
    1. Les conditions limites et la gestion des exceptions
    2. Les fuites de ressources
    3. La sécurité de concurrence
    ...

## Hooks

Placez `PreToolUse-*.sh`, `PostToolUse-*.sh` et `Stop-*.sh` sous `./hooks/`. Ils reçoivent une entrée JSON et renvoient une décision :

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

- **Liste blanche de commandes** : Seules les commandes courantes telles que `ls`, `cat`, `grep`, `git` et `python3` sont autorisées.
- **Détection d'évasion de chemin** : Toutes les opérations de fichiers sont restreintes au répertoire de travail actuel et à `/tmp`.
- **Blocage des commandes dangereuses** : Bloque des motifs tels que `rm -rf /`, les fork bombs, `curl | sh` et `git push --force`.
- **Protection des fichiers sensibles** : Interdit la modification de `.env`, `.ssh/`, `id_rsa`, `*.pem`, etc.
- **Interception d'injection de scripts** : Détecte les contournements comme `python -c "os.system(...)"`.
- **Limites de ressources de processus** : Limite le CPU, la mémoire et le nombre de processus sous Linux/macOS.
- **Masquage de confidentialité (bidirectionnel réversible)** : Les PII sont remplacées par des espaces réservés aléatoires en sortie et restaurées en entrée ; les écritures sur disque sont masquées indépendamment.
- **Résistance à l'injection d'espaces réservés** : Jetons cryptographiques aléatoires de 64 bits + neutralisation côté entrée + isolation de session.
- **Masquage des journaux d'audit** : `hook_audit_log` masque avant écriture, tronque et refuse d'écrire en cas d'échec.

Si vous devez assouplir les restrictions dans des projets de confiance, vous pouvez modifier `ALLOWED_COMMANDS` et `FORBIDDEN_PATH_PATTERNS` dans `Baize.py`.

# Masquage de confidentialité (cœur)

Baize intègre un mécanisme de protection de la vie privée **bidirectionnel réversible + masquage sur disque** couvrant tout le chemin de l'entrée au disque :

- **Sortie** : Avant l'envoi au LLM, les PII sont remplacées par des espaces réservés impossibles à deviner.
- **Entrée** : Les espaces réservés dans les réponses du LLM sont restaurés en texte original.
- **Écritures sur disque** : Les fichiers de session, les transcriptions compressées et les journaux d'audit sont **masqués indépendamment** avant d'être écrits sur disque. Aucun texte en clair ne reste sur le disque.

**Désactivé par défaut** ; activez-le si nécessaire.

## Deux façons de l'activer

### Méthode 1 : langage naturel

Dites directement dans la conversation :

```
>>> 降旨：Activer le masquage de confidentialité
[Système] Masquage de confidentialité activé (mode standard).

>>> 降旨：Activer le masquage strict
[Système] Masquage de confidentialité activé (mode strict).

>>> 降旨：Désactiver la protection de la vie privée
[Système] Masquage de confidentialité désactivé.
```

### Méthode 2 : commandes slash

- `/privacy on` active le mode standard
- `/privacy strict` active le mode strict
- `/privacy off` le désactive
- `/privacy status` affiche l'état, l'ID de session, le nombre de règles et les statistiques LRU/TTL
- `/privacy rules` liste toutes les règles (y compris leur état)
- `/privacy rule-off <name>` désactive une règle
- `/privacy rule-on <name>` la réactive
- `/privacy test <texte>` teste le résultat du masquage
- `/privacy clear` efface le mappage des espaces réservés et **fait tourner l'ID de session**

## Deux modes

**Standard** : Numéros mobiles de Chine continentale, numéros de carte d'identité, numéros de carte bancaire (validation Luhn), e-mails, IPv4/IPv6, clés API OpenAI/Anthropic/GitHub/AWS, jetons Bearer, blocs de clé privée, champs de mot de passe, identifiants d'URL.

**Strict** : Toutes les règles standard + noms chinois, numéros QQ, identifiants WeChat, plaques d'immatriculation de Chine continentale.

## Fonctionnement

Entrée utilisateur (avec PII réelles) → les messages stockent le texte original

↓ `sanitize_messages()`

Ce qui est envoyé au LLM est `[[PHONE_1]]`, `[[EMAIL_1]]`

↓ Réponse du LLM

Espaces réservés renvoyés → `restore_message()`

Restaurés en texte original → écriture sur disque / affichage / exécution d'outils

- **Masquage de confidentialité (bidirectionnel réversible)** : Les PII sont remplacées par des espaces réservés aléatoires en sortie et restaurées en entrée ; les écritures sur disque sont masquées indépendamment.
- **Résistance à l'injection d'espaces réservés** : Jetons cryptographiques aléatoires de 64 bits + neutralisation côté entrée + isolation de session.
- **Masquage des journaux d'audit** : `hook_audit_log` masque avant écriture, tronque et refuse d'écrire en cas d'échec.

## Classification intelligente des paramètres d'outils

**Masqués** (paramètres en texte brut qui ne participent pas à l'exécution réelle) :

- `todo`, `ask_user_question`, `task_create`, `task_update`

**Non masqués** (les chemins/commandes/URL sont réellement utilisés) :

- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep` (les chemins servent à l'IO)
- `run_bash` / `background_run` (les commandes sont exécutées)
- `run_webfetch` / `web_search` (les URL sont réellement envoyées au réseau)
- `set_workspace` (le chemin sert à `chdir`)
- `load_skills` (les noms de compétences sont énumérés)
- `agent` (le contexte du sous-agent est masqué indépendamment)
- `mcp_*` (sémantique inconnue ; traité de manière conservatrice)

**Tous masqués lors de l'écriture sur disque** (car le contenu du disque n'est pas réexécuté, priorité à la sécurité).

## Masquage sur disque

**Activé par défaut**, indépendant du masquage en mémoire. Même avec `/privacy off` (pas de masquage en mémoire), les écritures sur disque passent au moins par les règles standard.

**Caractéristiques clés** :

- Le masquage sur disque utilise une **table de mappage indépendante et à usage unique**. Les espaces réservés écrits sur disque **ne peuvent pas être restaurés**, car la table de mappage est jetée.
- Si le masquage sur disque **échoue, Baize refuse d'écrire du texte en clair** (pas de dégradation, pas d'omission silencieuse).
- Si un ancien fichier de session contient du texte en clair, il sera automatiquement masqué et réécrit lors de sa première sauvegarde.

**Comment le désactiver** (non recommandé) : Définissez `PERSIST_REDACT_ENABLED = False` dans `Baize.py`.

## Exemple

```
>>> 降旨：/privacy test Mon numéro de téléphone est 13812345678, e-mail a@b.com
Original : Mon numéro de téléphone est 13812345678, e-mail a@b.com
Masqué : Mon numéro de téléphone est [[PHONE_1]], e-mail [[EMAIL_1]]
Restauré : Mon numéro de téléphone est 13812345678, e-mail a@b.com

>>> 降旨：/privacy status
[Masquage de confidentialité]
Mode actuel : Mode standard (standard)
ID de session : 7d2f5e91
Règles actives : 34 / 41
Espaces réservés actifs : 2
Capacité de mappage : 2 / 2000
TTL : 86400 secondes
Évictions LRU : 0
Évictions TTL : 0
Appels de masquage : 3
Appels de restauration : 3

>>> 降旨：/privacy rules
[Liste des règles de masquage de confidentialité] 41 règles au total
[Standard + Strict]
[✓] phone_cn Numéro mobile de Chine continentale (standard,strict)
[✓] id_card_cn Numéro de carte d'identité de Chine continentale (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
[Strict uniquement]
[✓] name_cn Nom chinois (strict)
[✓] address_cn Adresse détaillée chinoise (strict)
...
Utilisation :
/privacy rule-off <name> désactiver une règle
/privacy rule-on <name> réactiver une règle
```

### Captures de test

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

- IBM SPSS Statistics installé localement (versions 20–31 ; Windows recommandé)
- SPSS sous licence et capable de démarrer normalement

### Étapes de configuration

1. **Localiser le répertoire d'installation de SPSS** : Le chemin par défaut est généralement `C:\Program Files\IBM\SPSS Statistics\` suivi du numéro de version (ex. `31`).

2. **Définir la variable d'environnement** (dans `.env` ou les variables d'environnement système) :

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

4. **L'enregistrer dans `MCP/mcp_config.json`** :

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

### Si `SPSS batch: NOT FOUND` apparaît

Cela signifie que `spss-studio-mcp` n'a pas trouvé le moteur SPSS, mais que `pyreadstat` + `pandas` fonctionnent. Dans ce cas, il passe en **mode fichier** :

- Peut lire `.sav`, inspecter les métadonnées, prévisualiser les données et convertir CSV ↔ SAV
- Ne peut pas exécuter de statistiques (test t, régression, ANOVA, etc.)

Solution : Configurez correctement `SPSS_INSTALL_PATH` dans `MCP/mcp_config.json`, ou acceptez la dégradation en mode fichier.

## Intégration SQL

### Bases de données prises en charge

PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, Dameng, Kingbase, TiDB, OceanBase, etc. (basé sur les pilotes SQLAlchemy 2.0).

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

3. **L'enregistrer dans `MCP/mcp_config.json`** :

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

### Garde-fous de sécurité intégrés

`atengk-mcp-server-rdbms` fournit plusieurs couches de protection :

- **Garde SELECT au niveau AST** : Utilise `sqlglot` pour analyser l'arbre syntaxique et bloquer physiquement les opérations d'écriture telles que `DELETE/UPDATE/DROP/TRUNCATE`.
- **Injection automatique de LIMIT** : Les requêtes sans nombre de lignes spécifié se voient forcer l'ajout de `LIMIT 100` pour éviter que les extractions de table complète n'épuisent la mémoire.
- **Lecture seule par défaut** : Les opérations d'écriture doivent être explicitement autorisées via `--allow-dml` / `--allow-ddl`.
- **Interception d'injection SQL** : Rejette au niveau AST les instructions malveillantes construites par concaténation de chaînes.

### Configurer plusieurs bases de données à la fois

Si vous souhaitez vous connecter simultanément à plusieurs bases de données, enregistrez plusieurs serveurs :

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

Baize fusionnera automatiquement tous leurs outils dans `MATERTOOLS`, et le LLM sélectionnera celui qui convient en fonction de la tâche.

# Structure des répertoires

```
    baize-agent/
    ├── pyproject.toml              # Configuration du packaging
    ├── requirements-data.txt       # Dépendances d'accès aux données (optionnel)
    ├── requirements-data           # Dépendances d'accès
    ├── README.md
    ├── tests/                      # Tests (non inclus dans le paquet)
    |   ├── __init__.py
    |   ├── test_history.py
    |   └── test_skill_loader.py
    ├── .env.example                # Exemple de variables d'environnement
    ├── .gitignore
    └── agent/                      # Paquet principal
        ├── logo_*                  # Logo de l'écran de connexion
        ├── LOGO和启动交互界面       # Image du logo de l'écran de connexion
        ├── __init__.py             # Version
        ├── Baize.py                # Programme principal et Agent Loop
        ├── config.py               # Chargement de la configuration multi-backend
        ├── ui_theme.py             # Thème de rendu de la CLI
        ├── utils.py                # Utilitaires généraux
        ├── logo.txt
        ├── skills/                 # Compétences intégrées
        ├── subagent/               # Sous-agents intégrés
        ├── core/                   # Logique centrale (sans effet de bord, testable unitairement)
        |   ├── __init__.py
        |   ├── history.py          # Nettoyage de l'historique de session / estimation des tokens / compression
        |   └── privacy.py          # Masquage de confidentialité : détection de PII / remplacement par espaces réservés / restauration réversible
        ├── hooks/                  # Hooks intégrés
        └── MCP/                    # Client et configuration MCP
            ├── __init__.py
            ├── mcp_client.py       # Client MCP
            └── mcp_config.json     # Configuration MCP
```

# Référence des variables d'environnement

- Variable : `DEEPSEEK_API_KEY` — Description : Clé API DeepSeek — Valeur par défaut : — (secret)
- Variable : `DEEPSEEK_BASE_URL` — Description : URL de l'endpoint DeepSeek — Valeur par défaut : `https://api.deepseek.com`
- Variable : `OPENAI_API_KEY` — Description : Clé API compatible OpenAI — Valeur par défaut : — (secret)
- Variable : `OPENAI_BASE_URL` — Description : URL de l'endpoint compatible OpenAI — Valeur par défaut : `https://api.openai.com/v1`
- Variable : `OLLAMA_BASE_URL` — Description : URL du service Ollama — Valeur par défaut : `http://localhost:11434`

**Écrivez les variables ci-dessus dans `~/.baize/.env` ; aucune modification des fichiers de configuration du shell n'est nécessaire.**

- Variable d'analyse de données : `SPSS_INSTALL_PATH` — Description : Répertoire d'installation d'IBM SPSS Statistics — Valeur par défaut : — (bascule en mode fichier si non défini)
- Variable d'analyse de données : `DATABASE_URL` — Description : Chaîne de connexion de base de données pour SQL MCP — Valeur par défaut : — (lue par le serveur MCP)

**Écrivez les variables ci-dessus dans `MCP/mcp_config.json`.**

# Développement

## Exécution des tests

Ce projet utilise pytest. Avant de développer, installez le paquet en mode éditable avec les dépendances de développement :
```
    pip install -e ".[dev]"
```
Exécuter tous les tests :
```
    python -m pytest tests/ -v
```
Exécuter un seul fichier :
```
    python -m pytest tests/test_history.py -v
```
## Conventions de structure du code

- `agent/` : Le paquet principal distribué avec le paquet. Toute la logique d'exécution et les ressources (skills, subagent, hooks, MCP) se trouvent ici.
- `agent/core/` : Modules de logique pure sans effets de bord externes. **Ils doivent pouvoir être testés indépendamment.** Ajoutez ici toute nouvelle logique de ce type et incluez des tests.
- `tests/` : Correspond un à un aux fichiers sources sous `agent/`, nommés `test_<module>.py`.
- Toute fonction ayant des dépendances externes (réseau, disque, état global) doit injecter les dépendances via des paramètres afin qu'elles puissent être remplacées dans les tests.

# FAQ

- Q : Où dois-je placer la clé API ?

R : Dans `~/.baize/.env`, pas dans le `.env` à la racine du projet.

- Q : Dois-je réinstaller après avoir changé de backend ?

R : Non. Modifiez simplement `active_provider` dans `~/.baize/config.toml`.

- Q : Ollama local nécessite-t-il une clé API ?

R : Non. Définissez `active_provider = "ollama"` et laissez `env_key` vide.

- Q : Comment changer le répertoire de travail ?

R : Dans la conversation, dites simplement « passe à /path/to/project », et Baize appellera l'outil `set_workspace`.

- Q : Que se passe-t-il si le contexte devient trop long ?

R : Baize effectue automatiquement une compression à deux niveaux : d'abord la troncature des anciens résultats d'outils, puis une demande de résumé au LLM. Vous pouvez également utiliser `/compact` manuellement.

- Q : Va-t-il supprimer mes fichiers par accident ?

R : La liste blanche de commandes par défaut bloque les opérations dangereuses comme `rm -rf /` ; avant d'écrire des fichiers, il affiche un diff et demande confirmation.

- Q : Comment connecter Baize à SPSS ?

R : 1. Installez `pip install -r requirements-data.txt` ; 2. Définissez la variable d'environnement `SPSS_INSTALL_PATH` en pointant vers le répertoire d'installation de SPSS ; 3. Activez le serveur `spss` dans `MCP/mcp_config.json`. Voir la section « Accès aux données (SPSS / SQL) » pour plus de détails.

- Q : Que faire avec `SPSS batch: NOT FOUND` ?

R : Cela signifie que le moteur SPSS n'a pas été trouvé. Vérifiez si `SPSS_INSTALL_PATH` pointe correctement vers le répertoire contenant `stats.exe` ; si vous ne traitez que des fichiers `.sav`, vous pouvez ignorer cet avertissement (il basculera en mode fichier).

- Q : Quelles choses supplémentaires dois-je installer pour me connecter à une base de données SQL ?

R : Installez `atengk-mcp-server-rdbms` au niveau Python (`pip install` s'en charge). **Les utilisateurs de SQL Server doivent également installer Microsoft ODBC Driver 18 au niveau du système**, ce qui ne peut pas être installé via pip.

- Q : Baize supprimera-t-il accidentellement les données de ma base de données ?

R : Non. SQL MCP n'autorise que SELECT par défaut et bloque toutes les opérations d'écriture au niveau de l'arbre syntaxique AST. Il est néanmoins fortement recommandé de créer un **compte de base de données en lecture seule** pour Baize comme deuxième garde-fou.

- Q : Les données des résultats d'analyse SPSS fuiront-elles vers le LLM ?

R : Si le masquage de confidentialité est activé (`/privacy on`), les résultats des outils sont automatiquement masqués pour les numéros de téléphone, les e-mails, les cartes d'identité et autres PII avant d'être envoyés au LLM. **Il est toutefois recommandé d'utiliser également un compte de base de données en lecture seule + un échantillonnage des données** (interroger uniquement les champs nécessaires) pour réduire les risques.

- Q : Pourquoi Baize devient-il plus lent et utilise-t-il plus de tokens à chaque conversation après l'ajout de SPSS/SQL ?

R : Parce que les définitions d'outils exposées par les serveurs MCP sont envoyées au LLM à chaque tour de conversation. SPSS dispose de plus de 60 outils, ajoutant une surcharge fixe d'environ 6 000 à 12 000 tokens. Si votre flux de travail habituel n'implique pas SPSS, vous pouvez mettre son `enabled` à `false` et l'activer en cas de besoin.

# Contribution

Les Issues et PRs sont les bienvenues. Veuillez lire `CONTRIBUTOR.md` avant de soumettre une PR.

**Merci à chaque Contributor qui soumet une PR.**

- GitHub Contributors :
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# Licence

MIT License

# Remerciements

- Ce projet est hébergé sur AtomGit en Chine : https://atomgit.com/Com_Xu/Baize
- Merci à AtomGit d'avoir inclus ce projet dans le programme d'incubation G-star.
- Merci aux contributeurs de PR, aux abonnés Douyin et aux étudiants qui me suivent.
- Inspiré par d'excellents outils d'AI Coding tels que Claude Code et Codex.
- Construit sur DeepSeek, OpenAI SDK et MCP.
- Merci à tous les développeurs qui parcourent ensemble le chemin du Vibe Coding.

# ☕ Soutien

Si Baize vous est utile, vous êtes invités à le sponsoriser et à le soutenir. Le développement indépendant prend beaucoup de temps. Le sponsoring ne modifiera pas le calendrier de mise à jour du produit. Merci pour votre soutien !

<p align="center">
  <img src="image/support.jpg" alt="QR code WeChat" width="200" />
</p>

# Contact

- Si Baize vous intéresse ou si vous souhaitez participer à une collaboration open source, vous pouvez me contacter via les canaux suivants.
- **Je suis actuellement à la recherche d'opportunités professionnelles. J'ai de l'expérience en études de marché et en recherche utilisateur, et je comprends aussi quelque peu les Agents. Si mes compétences correspondent à vos besoins, j'espère travailler avec vous (postes visés : Opérations Produit IA / Recherche Utilisateur / Études de Marché).**

<p align="center">
  <img src="image/weixin.jpg" alt="QR code WeChat" width="200" />
</p>

<p align="center">Scannez le QR code WeChat et indiquez « collaboration open source Baize » ou « recrutement d'entreprise ».</p>

<p align="center">
  <img src="image/抖音.png" alt="QR code Douyin" width="200" />
</p>

<p align="center">Scannez le QR code Douyin pour suivre.</p>