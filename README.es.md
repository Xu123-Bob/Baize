<div align="center">

<img src="image/logopage02.png" alt="Baize Logo" width="320" />

# Baize 白泽

**Di todo lo que sabes, guarda todos los secretos**

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

Un asistente de seguridad para VibeCoding y análisis de datos inspirado en la bestia mítica china Baize.

**Una CLI de Coding Agent de código abierto, con potente protección de privacidad e interacción multilingüe. Admite múltiples backends (DeepSeek / compatible con OpenAI / Zhipu / Qwen / Kimi / Ollama local) y ofrece capacidades completas como llamadas a herramientas, carga de habilidades, delegación a subagentes, compresión de contexto y sandbox de seguridad.**

----------

# Ventajas principales

## Protección de privacidad

- **Protección de privacidad bidireccional y reversible**: La información sensible se reemplaza por marcadores de posición antes de enviarse al LLM y se restaura automáticamente después de recibir la respuesta. Todo el proceso es transparente para el usuario: el historial, los parámetros de herramientas y las respuestas finales que ves siempre son el texto original, mientras que el LLM solo ve marcadores de posición aleatorios e imposibles de adivinar, como `«PZ_PHONE_a3f8b2c1d4e5f6a7»`.
- **Desensibilización completa en disco**: Los archivos de sesión, las transcripciones comprimidas y los registros de auditoría se desensibilizan automáticamente antes de escribirse en disco (activado por defecto). Los PII en texto plano nunca aparecen en el disco.
- **Resistencia a inyecciones**: Los marcadores de posición usan tokens criptográficos aleatorios de 64 bits, imposibles de enumerar, falsificar o reproducir. Los marcadores antiguos se invalidan inmediatamente al cambiar de sesión.
- **Varias formas de activar la protección de privacidad**: Puedes activar el modo de protección de privacidad introduciendo lenguaje natural en la línea de comandos o usando el comando más preciso `/privacy`.
- **Agente local**: Este producto no tiene base de datos remota y se ejecuta completamente en local. No recopila información del usuario.

## Interacción multilingüe

- **Admite nueve idiomas**: chino, English, 日本語, 한국어, Español, Français, deutsch, русский, العربية.
- **Varias formas de cambiar de idioma**: Puedes decir directamente `please speak with english` para cambiar a inglés, o usar `/lang ja` para cambiar a japonés.

# Características

- **Compatibilidad con múltiples backends**: DeepSeek, cualquier endpoint compatible con OpenAI (GLM / Qwen / Kimi / OpenAI) y Ollama local. Cambio con un clic.

- **Inicio sin configuración**: Genera automáticamente los archivos de configuración en la primera ejecución. El usuario solo necesita rellenar la clave una vez.

- **Desensibilización de privacidad**: Identifica y desensibiliza automáticamente **más de 30 categorías** de información sensible antes de enviarla al LLM (números de teléfono, correos electrónicos, documentos de identidad, pasaportes, tarjetas bancarias, números internacionales, API Keys, JWT, cadenas de conexión a bases de datos, direcciones MAC, etc.), y las restaura automáticamente al recibir la respuesta. **También se desensibiliza al escribir en disco**, sin dejar texto plano en el disco. Admite dos niveles, Estándar / Estricto, conmutables mediante lenguaje natural o `/privacy`.

- **Interacción multilingüe**: Cambia libremente entre chino / inglés / japonés / coreano / español / francés / alemán / ruso / árabe. Basta con decir `English` o usar `/lang ja`, y la IA pensará y responderá en el idioma correspondiente durante toda la sesión.

- **Cadena de herramientas completa**: ejecución bash, lectura/escritura/edición de archivos, búsqueda glob/grep, búsqueda y obtención web, tareas en segundo plano, gestión de tareas y pendientes.

- **Sistema de habilidades (Skills)**: Carga conocimiento de dominio (SKILL.md) bajo demanda, haciendo que la IA sea más profesional en escenarios específicos.

- **Subagentes (Subagents)**: Delega tareas complejas a subagentes con contexto independiente para no contaminar la sesión principal.

- **Hooks**: Hooks en Python o Shell. Admite interceptación antes/después de llamadas a herramientas, registros de auditoría, formateo automático y control de pruebas.

- **Protocolo MCP**: Conecta servidores de herramientas externos mediante Model Context Protocol (GitHub, Filesystem, etc.).

- **Compresión de contexto**: Compresión en dos niveles (truncado de resultados de herramientas + resumen por LLM). Admite conversaciones extremadamente largas.

- **Sandbox de seguridad**: Lista blanca de comandos, detección de escape de rutas, interceptación de comandos peligrosos, protección de archivos sensibles e interceptación de inyección de scripts.

- **CLI con tema negro y dorado**: Ancho adaptativo para chino, resaltado de código, coloreado de diffs y plegado de pensamientos.

# Interfaz de Baize CLI

<div align="center">
Pantalla de inicio de Baize CLI
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="Pantalla de inicio de Baize CLI" width="800" />
</p>

<div align="center">
Pantalla de ejecución de Baize CLI -- 01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="Pantalla de ejecución de Baize CLI" width="800" />
</p>

<div align="center">
Pantalla de ejecución de Baize CLI -- 02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="Pantalla de ejecución de Baize CLI" width="800" />
</p>

# Instalación

## Requisitos previos

- Python 3.10+ (requiere tomllib, integrado en 3.11+; para 3.10 instala tomli)

- pip

## Instalación desde el código fuente

### Dos formas de descarga

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- Pulsa Win+R, escribe `cmd` y luego introduce:

    baize

2. En la página del repositorio, haz clic en `<> Code` --> `Download ZIP`

(1) Después de descomprimir, entra en el directorio de este archivo:

    bash -- Pulsa Win+R y escribe cmd

    cd directorio-descomprimido

    pip install -r requirements.txt

    python -m Baize

Después de la instalación, pulsa Win+R, escribe cmd para abrir la CLI e introduce `baize` para ejecutarlo.

(2) Descarga el ZIP e instálalo localmente. Después de descomprimirlo, entra en el directorio y ejecuta:

    bash -- Pulsa Win+R y escribe cmd

    pip install .

Después de la instalación, pulsa Win+R, escribe cmd para abrir la CLI e introduce `baize` para ejecutarlo.

### Opcional: instalar dependencias de acceso a datos (herramientas importantes para análisis de datos)

Si necesitas que Baize controle SPSS o bases de datos SQL, instala las dependencias adicionales:

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` incluye:
- `spss-studio-mcp`: servidor MCP de análisis estadístico SPSS (requiere IBM SPSS Statistics instalado localmente)
- `atengk-mcp-server-rdbms`: servidor MCP de bases de datos relacionales generales (PostgreSQL / MySQL / SQL Server / Oracle / DM, etc.)
- `pyodbc`: enlace Python ODBC necesario para SQL Server

Alternativamente, si el proyecto se instala mediante `pyproject.toml`, también puedes usar extras:

```bash
pip install -e ".[data]"          # Instalar todas las dependencias de acceso a datos de una vez
pip install -e ".[spss]"          # Instalar solo SPSS
pip install -e ".[sql]"           # Instalar solo SQL general
pip install -e ".[sql-mssql]"     # Solo SQL Server (incluye pyodbc)
```

- **⚠️ Usuarios de SQL Server: `pyodbc` solo es el enlace Python. También debes instalar Microsoft ODBC Driver 18 for SQL Server a nivel del sistema.**
- **⚠️ Usuarios de SPSS: `spss-studio-mcp` solo es una capa puente MCP. IBM SPSS Statistics (versión 20–31) debe estar ya instalado localmente y con licencia válida, y la variable de entorno `SPSS_INSTALL_PATH` debe apuntar al directorio de instalación de SPSS. Actualmente, el motor SPSS admite análisis completo principalmente en Windows; en Linux/macOS puede degradarse a "modo archivo" (leer archivos .sav, ver metadatos, previsualizar datos, pero sin análisis estadístico).**

# Inicio rápido

1. Primera ejecución

```bash
baize
```

En la primera ejecución, Baize genera automáticamente dos archivos de configuración:

```
~/.baize/config.toml   # Configuración del backend (elige DeepSeek / OpenAI / Ollama)
~/.baize/.env          # Archivo de claves
```

En Windows, la ruta es `C:\Users\TuNombreDeUsuario\.baize\`.

2. Elegir backend

Abre `~/.baize/config.toml` y modifica **active_provider** (debes modificarlo):

```toml
# Archivo de configuración de Baize
# Modifica active_provider para cambiar de backend  # Valores posibles: "deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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

3. Introducir la clave

Edita `~/.baize/.env`. **Si necesitas usar un LLM concreto, elimina el `# ` inicial de esa línea y añade `# ` delante de los demás LLM para bloquear su salida de API. Después de introducir la API Key, asegúrate de guardar; solo tendrá efecto después de guardar**:

```env
# ============================================================
# Archivo de claves de Baize
# ============================================================
# Rellena solo la clave del backend que uses; deja las demás comentadas.
# Los nombres de las variables deben coincidir con el campo env_key de config.toml.
#
# Ubicación:
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\TuNombreDeUsuario\.baize\.env
# ============================================================

# ---------- DeepSeek (backend predeterminado) ----------
# Obtén la clave en: https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI o cualquier endpoint compatible con OpenAI (opcional) ----------
# Sirve para Groq, Qwen, Moonshot, Zhipu, OpenAI, etc.
# Nota: base_url se configura en config.toml dentro de [model_providers.xxx], no aquí
# OPENAI_API_KEY=

# ---------- Qwen (opcional) ----------
# Obtén la clave en: https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot (opcional) ----------
# Obtén la clave en: https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- Zhipu GLM (opcional) ----------
# Obtén la clave en: https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- Gateway personalizado (opcional) ----------
# CUSTOM_API_KEY=

# ---------- Ollama (modelo local, no requiere clave) ----------
# Solo asegúrate de que Ollama esté ejecutándose en localhost:11434. No hace falta configurar nada aquí.
```

4. Reiniciar

```bash
baize
```

Si ves el logotipo negro y dorado y el mensaje de bienvenida, el inicio ha sido correcto.

# Ejemplos de uso

Después del inicio, describe tus necesidades en lenguaje natural en el indicador `>>> 降旨：`:

```
>>> 降旨：Escribe un script de Python para hacer scraping del Top250 de Douban y guardarlo como CSV

>>> 降旨：Ayúdame a revisar los errores de tipo en todos los archivos Python de src/

>>> 降旨：Busca en este repositorio todos los lugares donde se use requests y cámbialos por httpx
```

## Interacción multilingüe

Baize admite **nueve idiomas**: chino, English, 日本語, 한국어, Español, Français, deutsch, русский, العربية.

Hay dos formas de cambiar:

### Opción 1: hablar directamente (detección automática)

Baize detecta automáticamente el idioma de tu entrada y cambia:

```
>>> 降旨：Hello, help me write a Python script
[Sistema] Idioma de entrada detectado: English. Baize ha cambiado a interacción en English.
(Baize responde en inglés)

>>> 降旨：日本語で答えてください
[Sistema] Idioma de entrada detectado: 日本語. Baize ha cambiado a interacción en 日本語.
(Baize responde en japonés)
```

### Opción 2: comando manual

```
>>> 降旨：/lang                # Ver el idioma actual y la lista disponible
[Sistema] Idioma actual: chino (zh)
[Sistema] Idiomas disponibles:
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> 降旨：/lang English        # Cambiar por nombre de idioma
>>> 降旨：/lang ja             # Cambiar por código de idioma
>>> 降旨：/lang 西班牙语        # También se admiten nombres en chino
```

Admite cuatro formas: **nombre del idioma / código de idioma / nombre en chino / nombre nativo**. Por ejemplo, para cambiar a inglés, sirve cualquiera de `English`, `en`, `英语` o `英文`.

## Comandos integrados

- `/exit, /quit` --> Salir de Baize
- `/clear` --> Borrar historial de conversación, pendientes, registros de pensamiento y registros de herramientas
- `/compact` --> Comprimir manualmente el contexto (usar cuando la conversación sea demasiado larga)
- `/commit` --> Guardar la sesión actual y hacer commit en Git (si estás dentro de un repositorio Git)
- `/lang` --> Ver el idioma actual; `/lang en` cambia a inglés (admite código o nombre de idioma)
- `/skills` --> Listar todas las habilidades disponibles
- `/skills reload` --> Recargar el directorio de habilidades de usuario
- `/unload` --> Descargar la habilidad activa actual
- `/show thought` --> Ver el registro completo de pensamientos
- `/show tool` --> Ver el registro de llamadas a herramientas
- `/show all` --> Ver todo el historial de la sesión
- `/技能名` --> Cargar la habilidad especificada (admite coincidencia difusa)
- `/privacy` --> Control de desensibilización de privacidad (on / off / strict / status / rules / test / clear)
- `/privacy rule-off <name>` --> Desactivar una regla de desensibilización (por ejemplo, `/privacy rule-off phone_intl`)
- `/privacy rule-on  <name>` --> Reactivar una regla

## Ejemplos de uso de acceso a datos

Después de configurar SPSS / SQL, puedes controlarlos directamente con lenguaje natural:

```text
>>> 降旨：Usa SPSS para abrir data.sav y dime la lista de variables y el tamaño de la muestra

>>> 降旨：Haz estadísticas descriptivas sobre data.sav y luego ejecuta una regresión lineal

>>> 降旨：Consulta los pedidos de la tabla sales con importe superior a 100.000 el mes pasado, agrupados por cliente

>>> 降旨：Exporta los resultados del análisis de SPSS a CSV y luego únelos con los datos maestros de clientes usando SQL
```

# Modelos locales Ollama (coste cero)

¿No quieres usar una API en la nube? Usa Ollama local:

```bash
# 1. Instala Ollama: https://ollama.com/download
# 2. Descarga un modelo
ollama pull qwen2.5:7b

# 3. Inicia el servicio Ollama
ollama serve

# 4. Modifica ~/.baize/config.toml
active_provider = "ollama"

# 5. Inicia Baize
baize
```

Modelos recomendados: `qwen2.5:7b` (fuerte en chino), `llama3.1:8b`, `deepseek-r1:7b`.

# Mecanismos de extensión

Baize admite cuatro formas de extensión. Basta con colocarlas en el directorio de trabajo actual para que surtan efecto.

## Habilidades (Skills)

Escribe conocimiento de dominio en `./skills/nombre-de-habilidad/SKILL.md`. La IA las cargará de forma proactiva cuando encuentre tareas complejas.

```markdown
---
name: pandas-eda
description: Buenas prácticas para análisis exploratorio de datos con pandas
tags: data,python
---

# Guía de Pandas EDA

## Pasos principales
1. Usa df.info() para ver tipos de campos y valores faltantes
2. Usa df.describe() para estadísticas descriptivas
...
```

También puedes cargarla manualmente en la conversación con `/pandas-eda`.

## Subagentes (Subagents)

Define subagentes dedicados en `./subagent/nombre-de-rol/AGENT.md`. El agente principal puede delegar tareas mediante la herramienta agent.

```markdown
---
name: code-reviewer
description: Revisor de código estricto
---

Eres un revisor de código senior. Al revisar, prioriza:
1. Condiciones límite y manejo de excepciones
2. Fugas de recursos
3. Seguridad de concurrencia
...
```

## Hooks

Coloca lo siguiente en `./hooks/`:

- `PreToolUse-*.sh`
- `PostToolUse-*.sh`
- `Stop-*.sh`

Reciben entrada JSON y devuelven decisiones:

```bash
#!/bin/bash

# PreToolUse-guard.sh

read -r input

if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Deletion prohibited"}}'
fi
```

Los hooks de Python pueden llamar directamente a las API integradas (consulta las funciones `hook_*` en `Baize.py`).

## Servidores MCP

Configura servidores de herramientas externos en `./MCP/mcp_config.json`:

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

# Diseño de seguridad (núcleo)

Baize activa por defecto los siguientes mecanismos de seguridad:

- **Lista blanca de comandos**: Solo se permiten comandos comunes como `ls`, `cat`, `grep`, `git`, `python3`, etc.
- **Detección de escape de rutas**: Todas las operaciones de archivos se limitan al directorio de trabajo actual y a `/tmp`.
- **Interceptación de comandos peligrosos**: Intercepta patrones como `rm -rf /`, fork bombs, `curl | sh`, `git push --force`, etc.
- **Protección de archivos sensibles**: Prohíbe modificar `.env`, `.ssh/`, `id_rsa`, `*.pem`, etc.
- **Interceptación de inyección de scripts**: Detecta bypasses como `python -c "os.system(...)"`.
- **Límites de recursos de proceso**: Limita CPU, memoria y número de procesos en Linux/macOS.
- **Desensibilización de privacidad (bidireccional reversible)**: Los PII se reemplazan por marcadores aleatorios al salir y se restauran al entrar; desensibilización independiente en disco.
- **Resistencia a inyección de marcadores**: Tokens criptográficos aleatorios de 64 bits + neutralización en el lado de entrada + aislamiento de sesión.
- **Desensibilización de registros de auditoría**: `hook_audit_log` desensibiliza antes de escribir en disco + trunca + rechaza escribir en caso de fallo.

Si necesitas relajar las restricciones en proyectos de confianza, puedes modificar `ALLOWED_COMMANDS` y `FORBIDDEN_PATH_PATTERNS` en `Baize.py`.

# Desensibilización de privacidad (núcleo)

Baize incorpora un mecanismo de protección de privacidad **bidireccional reversible + desensibilización en disco**, que cubre toda la ruta desde la entrada hasta el disco:

- **Salida**: Antes de enviar al LLM, los PII se reemplazan por marcadores imposibles de adivinar
- **Entrada**: Los marcadores en las respuestas del LLM se restauran al texto original
- **Disco**: Los archivos de sesión, las transcripciones comprimidas y los registros de auditoría se **desensibilizan de forma independiente** antes de escribirse en disco. No queda texto plano en el disco

**Desactivado por defecto**, actívalo cuando sea necesario.

## Dos formas de activarlo

### Opción 1: lenguaje natural

Di directamente en la conversación:

```
>>> 降旨：Activa la desensibilización de privacidad
[Sistema] Desensibilización de privacidad activada (modo Estándar).

>>> 降旨：Activa la desensibilización estricta
[Sistema] Desensibilización de privacidad activada (modo Estricto).

>>> 降旨：Desactiva la protección de privacidad
[Sistema] Desensibilización de privacidad desactivada.
```

### Opción 2: comandos con barra

- `/privacy on` Activar modo Estándar
- `/privacy strict` Activar modo Estricto
- `/privacy off` Desactivar
- `/privacy status` Ver estado, ID de sesión, número de reglas, estadísticas LRU/TTL
- `/privacy rules` Listar todas las reglas (incluido su estado de activación)
- `/privacy rule-off <name>` Desactivar una regla
- `/privacy rule-on  <name>` Reactivar una regla
- `/privacy test <text>` Probar el efecto de desensibilización
- `/privacy clear` Borrar el mapeo de marcadores y **rotar el ID de sesión**

## Dos niveles

**Estándar**: Números de móvil de China continental, números de documento de identidad, números de tarjeta bancaria (validación Luhn), correos electrónicos, IPv4/IPv6, API Keys de OpenAI/Anthropic/GitHub/AWS, Bearer Tokens, bloques de clave privada, campos de contraseña, credenciales en URL.

**Estricto**: Todo lo del modo Estándar + nombres chinos, números QQ, IDs de WeChat, matrículas de vehículos de China continental.

## Cómo funciona

Entrada del usuario (con PII reales) → messages guarda el texto original

↓ `sanitize_messages()`

Lo que se envía al LLM es `[[PHONE_1]]`, `[[EMAIL_1]]`

↓ Respuesta del LLM

Los marcadores devueltos → `restore_message()`

Se restauran al texto original → escritura en disco / visualización / ejecución de herramientas

- **Desensibilización de privacidad (bidireccional reversible)**: Los PII se reemplazan por marcadores aleatorios al salir y se restauran al entrar; desensibilización independiente en disco.
- **Resistencia a inyección de marcadores**: Tokens criptográficos aleatorios de 64 bits + neutralización en el lado de entrada + aislamiento de sesión.
- **Desensibilización de registros de auditoría**: `hook_audit_log` desensibiliza antes de escribir en disco + trunca + rechaza escribir en caso de fallo.

## Clasificación inteligente de parámetros de herramientas

**Se desensibilizan** (parámetros de texto plano que no participan en la ejecución real):
- `todo`, `ask_user_question`, `task_create`, `task_update`

**No se desensibilizan** (las rutas/comandos/URL se usan realmente):
- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep` (las rutas se usan para IO)
- `run_bash` / `background_run` (los comandos se ejecutan)
- `run_webfetch` / `web_search` (las URL se envían realmente a la red)
- `set_workspace` (la ruta se usa para `chdir`)
- `load_skills` (los nombres de habilidades son enumeraciones)
- `agent` (el contexto del subagente se desensibiliza de forma independiente)
- `mcp_*` (semántica desconocida, tratamiento conservador)

**Todo se desensibiliza al persistir** (porque el contenido persistido no se reejecutará; la seguridad es lo primero).

## Desensibilización en disco

**Activada por defecto**, independiente de la desensibilización en memoria. Incluso si usas `/privacy off` (sin desensibilización en memoria), la desensibilización en disco sigue aplicando al menos las reglas Estándar.

**Características clave**:
- La desensibilización en disco usa una **tabla de mapeo independiente y de un solo uso**: los marcadores escritos en disco **no se pueden restaurar**, porque la tabla de mapeo se descarta.
- Si la desensibilización en disco **falla, se rechaza escribir texto plano** (sin degradación, sin omisión silenciosa).
- Si archivos de sesión antiguos contienen texto plano, se desensibilizan y reescriben automáticamente en el primer guardado.

**Cómo desactivarla** (no recomendado): Modifica `PERSIST_REDACT_ENABLED = False` en `Baize.py`.

## Ejemplo

```
>>> 降旨：/privacy test Mi número de teléfono es 13812345678, mi correo es a@b.com
Original: Mi número de teléfono es 13812345678, mi correo es a@b.com
Desensibilizado: Mi número de teléfono es [[PHONE_1]], mi correo es [[EMAIL_1]]
Restaurado: Mi número de teléfono es 13812345678, mi correo es a@b.com

>>> 降旨：/privacy status
[Desensibilización de privacidad]
Modo actual : Modo Estándar (standard)
ID de sesión : 7d2f5e91
Reglas activas : 34 / 41
Marcadores activos : 2
Capacidad de mapeo : 2 / 2000
TTL : 86400 segundos
Evicciones LRU : 0
Evicciones TTL : 0
Llamadas de desensibilización: 3
Llamadas de restauración: 3

>>> 降旨：/privacy rules
[Lista de reglas de desensibilización de privacidad] Total 41
[Estándar + Estricto]
[✓] phone_cn Número de móvil de China continental (standard,strict)
[✓] id_card_cn Número de documento de identidad de China continental (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
[Solo Estricto]
[✓] name_cn Nombre chino (strict)
[✓] address_cn Dirección detallada china (strict)
...
Uso:
/privacy rule-off <name> Desactivar una regla
/privacy rule-on <name> Reactivar una regla
```

### Ejemplos de prueba

<div align="center">
Pantalla de prueba de protección de privacidad -- 01
</div>

<p align="center">
  <img src="image/privary01.jpg" alt="Pantalla de prueba de protección de privacidad" width="800" />
</p>

<div align="center">
Pantalla de prueba de protección de privacidad -- 02
</div>

<p align="center">
  <img src="image/privary02.jpg" alt="Pantalla de prueba de protección de privacidad" width="800" />
</p>

# Acceso a datos (núcleo)

Baize se conecta a software empresarial de análisis de datos mediante **MCP (Model Context Protocol)**. El programa principal no necesita ninguna modificación: basta con registrar el servidor en `MCP/mcp_config.json`.

## Integración con SPSS

### Requisitos previos

- IBM SPSS Statistics instalado localmente (versión 20–31; se recomienda Windows)
- SPSS con licencia válida y capaz de iniciarse correctamente

### Pasos de configuración

1. **Localiza el directorio de instalación de SPSS:** La ruta predeterminada suele ser `C:\Program Files\IBM\SPSS Statistics\` seguida del número de versión (por ejemplo, 31).

2. **Configura la variable de entorno** (puede estar en `.env` o en las variables de entorno del sistema):

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **Verifica el estado**:

```bash
spss-studio-mcp status
```

Salida esperada:

```text
=== SPSS MCP Capability Status ===
pyreadstat : OK v1.3.6
pandas     : OK v3.0.2
SPSS batch : OK
```

4. **Registra en `MCP/mcp_config.json`**:

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

### Si aparece `SPSS batch: NOT FOUND`

Significa que `spss-studio-mcp` no encontró el motor SPSS, pero `pyreadstat` + `pandas` funcionan correctamente. En este caso entra en **modo archivo**:

- Puede leer `.sav`, ver metadatos, previsualizar datos y convertir CSV ↔ SAV
- No puede ejecutar estadísticas (prueba t, regresión, ANOVA, etc.)

Solución: configura correctamente `SPSS_INSTALL_PATH` en `MCP/mcp_config.json`, o acepta la degradación a modo archivo.

## Integración con SQL

### Bases de datos compatibles

PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, DM, KingbaseES, TiDB, OceanBase, etc. (basado en controladores SQLAlchemy 2.0).

### Pasos de configuración

1. **Prepara una cuenta de base de datos de solo lectura** (muy recomendado):

```sql
CREATE USER baize_ro WITH PASSWORD 'xxx';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO baize_ro;
```

2. **Prepara la cadena de conexión**:

- PostgreSQL --> `postgresql+psycopg://user:pwd@host:5432/db`
- MySQL --> `mysql+pymysql://user:pwd@host:3306/db`
- SQL Server --> `mssql+pyodbc://user:pwd@host:1433/db?driver=ODBC+Driver+18+for+SQL+Server`
- Oracle --> `oracle+oracledb://user:pwd@host:1521/?service_name=ORCL`

3. **Registra en `MCP/mcp_config.json`**:

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

### Barreras de seguridad (integradas)

`atengk-mcp-server-rdbms` ofrece varias capas de protección:

- **Guarda SELECT a nivel AST**: Analiza el árbol de sintaxis con `sqlglot` y bloquea físicamente operaciones de escritura como `DELETE/UPDATE/DROP/TRUNCATE`.
- **Inyección automática de LIMIT**: Las consultas sin número de filas especificado reciben forzosamente `LIMIT 100`, evitando que un escaneo completo de tabla provoque desbordamiento de memoria.
- **Solo lectura por defecto**: Las operaciones de escritura deben autorizarse explícitamente mediante `--allow-dml` / `--allow-ddl`.
- **Interceptación de inyección SQL**: Rechaza en la capa AST sentencias maliciosas construidas por concatenación de cadenas.

### Configurar varias bases de datos a la vez

Si quieres conectarte a varias bases de datos al mismo tiempo, registra varios servidores:

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

Baize fusionará automáticamente todas sus herramientas en `MATERTOOLS`, y el LLM elegirá automáticamente según la tarea.

# Estructura de directorios

```
baize-agent/
├── pyproject.toml              # Configuración de empaquetado
├── requirements-data.txt       # Dependencias de acceso a datos (opcional)
├── requirements-data           # Dependencias de acceso
├── README.md
├── tests/                      # Pruebas (no se publican con el paquete)
|   ├── __init__.py
|   ├── test_history.py
|   └── test_skill_loader.py
├── .env.example                # Ejemplo de variables de entorno
├── .gitignore
└── agent/                      # Paquete principal
    ├── __init__.py
    ├── Baize.py                # Programa principal y Agent Loop
    ├── config.py               # Carga de configuración multi-backend
    ├── ui_theme.py             # Tema de renderizado de la CLI
    ├── utils.py                # Utilidades generales
    ├── logo.txt
    ├── skills/                 # Habilidades integradas
    ├── subagent/               # Subagentes integrados
    ├── core/                   # Lógica central (sin efectos secundarios, testeable unitariamente)
    |   ├── __init__.py
    |   ├── history.py          # Limpieza de historial de sesión / estimación de tokens / compresión
    |   └── privacy.py          # Desensibilización de privacidad: detección de PII / reemplazo por marcadores / restauración reversible
    ├── hooks/                  # Hooks integrados
    └── MCP/                    # Cliente MCP y configuración
        ├── __init__.py
        ├── mcp_client.py
        └── mcp_config.json
```

# Referencia de variables de entorno

| Variable | Descripción | Valor predeterminado |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | Clave de API de DeepSeek | — |
| `DEEPSEEK_BASE_URL` | Endpoint de DeepSeek | `https://api.deepseek.com` |
| `OPENAI_API_KEY` | Clave del endpoint compatible con OpenAI | — |
| `OPENAI_BASE_URL` | Endpoint compatible con OpenAI | `https://api.openai.com/v1` |
| `OLLAMA_BASE_URL` | Dirección del servicio Ollama | `http://localhost:11434` |

**Escribe las variables anteriores en `~/.baize/.env`; no es necesario modificar archivos de configuración del shell.**

Variables de análisis de datos:

| Variable | Descripción | Valor predeterminado |
| --- | --- | --- |
| `SPSS_INSTALL_PATH` | Directorio de instalación de IBM SPSS Statistics | — (si no se define, se degrada a modo archivo) |
| `DATABASE_URL` | Cadena de conexión de base de datos para SQL MCP | — (la lee el servidor MCP) |

**Escribe las variables anteriores en `MCP/mcp_config.json`.**

# Desarrollo

## Ejecutar pruebas

Este proyecto usa pytest. Antes de desarrollar, instala el paquete en modo editable con las dependencias de desarrollo:

```bash
pip install -e ".[dev]"
```

Ejecutar todas las pruebas:

```bash
python -m pytest tests/ -v
```

Ejecutar solo un archivo:

```bash
python -m pytest tests/test_history.py -v
```

## Convenciones de estructura del código

- `agent/`: Paquete principal que se publica con el paquete. Toda la lógica de ejecución y los recursos (skills, subagent, hooks, MCP) están aquí.
- `agent/core/`: Módulos de lógica pura, sin efectos secundarios externos. **Deben poder probarse de forma independiente.** Añade aquí este tipo de lógica nueva, con sus pruebas.
- `tests/`: Correspondencia uno a uno con los archivos fuente bajo `agent/`, nombrados `test_<módulo>.py`.
- Cualquier función con dependencias externas (red, disco, estado global) debe inyectar dependencias mediante parámetros para poder sustituirlas en las pruebas.

# ❓ Preguntas frecuentes

- P: ¿Dónde debo poner la clave?

R: En `~/.baize/.env`, no en el `.env` de la raíz del proyecto.

- P: ¿Hay que reinstalar al cambiar de backend?

R: No. Basta con cambiar `active_provider` en `~/.baize/config.toml`.

- P: ¿Ollama local necesita clave?

R: No. Selecciona `active_provider = "ollama"` y deja `env_key` vacío.

- P: ¿Cómo cambio el directorio de trabajo?

R: En la conversación, di directamente "cambia a /path/to/project", y Baize llamará a la herramienta `set_workspace`.

- P: ¿Qué ocurre si el contexto es demasiado largo?

R: Baize comprime automáticamente en dos niveles: primero trunca los resultados antiguos de herramientas y luego pide al LLM que genere un resumen. También puedes usar `/compact` manualmente.

- P: ¿Puede borrar mis archivos por error?

R: La lista blanca de comandos predeterminada intercepta operaciones peligrosas como `rm -rf /`; antes de escribir archivos, muestra un Diff y pide confirmación.

- P: ¿Cómo hago que Baize se conecte a SPSS?

R: 1. Instala `pip install -r requirements-data.txt`; 2. Define la variable de entorno `SPSS_INSTALL_PATH` apuntando al directorio de instalación de SPSS; 3. Activa el servidor spss en `MCP/mcp_config.json`. Consulta la sección "Acceso a datos (SPSS / SQL)" para más detalles.

- P: ¿Qué hago si aparece `SPSS batch: NOT FOUND`?

R: Significa que no se encontró el motor SPSS. Comprueba si `SPSS_INSTALL_PATH` apunta correctamente al directorio que contiene `stats.exe`; si solo procesas archivos `.sav`, puedes ignorar este aviso (se degradará a modo archivo).

- P: ¿Qué hay que instalar adicionalmente para conectarse a una base de datos SQL?

R: A nivel de Python, instala `atengk-mcp-server-rdbms` (`pip install` lo hace automáticamente). **Los usuarios de SQL Server también deben instalar Microsoft ODBC Driver 18 a nivel del sistema**, lo cual no se puede instalar con pip.

- P: ¿Baize puede borrar por error los datos de mi base de datos?

R: No. SQL MCP solo permite SELECT por defecto y bloquea todas las operaciones de escritura a nivel del árbol de sintaxis AST. Aun así, se recomienda encarecidamente crear una **cuenta de base de datos de solo lectura** exclusiva para Baize como doble garantía.

- P: ¿Los datos de los resultados de análisis de SPSS se filtran al LLM?

R: Si la desensibilización de privacidad está activada (`/privacy on`), los resultados devueltos por las herramientas se desensibilizan automáticamente de PII como números de teléfono, correos electrónicos y documentos de identidad antes de enviarse al LLM. **Pero se recomienda usar también una cuenta de base de datos de solo lectura + muestreo de datos** (consultar solo los campos necesarios) para reducir el riesgo.

- P: ¿Por qué después de añadir SPSS/SQL cada conversación de Baize es más lenta y usa más tokens?

R: Porque las definiciones de herramientas expuestas por los servidores MCP se envían al LLM en cada ronda de conversación. SPSS tiene más de 60 herramientas, lo que añade unos 6.000–12.000 tokens de sobrecarga fija. Si tu flujo de trabajo habitual no implica SPSS, puedes poner su `enabled` en `false` y activarlo cuando sea necesario.

# 🤝 Contribuir

Se agradecen Issues y PRs. Se recomienda leer `CONTRIBUTOR.md` antes de enviar un PR.

### Gracias a cada colaborador que envía PR

- Colaboradores de GitHub:
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# Licencia

MIT License

# Agradecimientos

- Este proyecto está alojado en AtomGit en China. Enlace del proyecto: https://atomgit.com/Com_Xu/Baize

- Gracias a AtomGit por incluir este proyecto en el programa de incubación G-star.

- Gracias a los colaboradores de PR, a los seguidores de Douyin y a los estudiantes que me siguen.

- Inspirado por excelentes herramientas de AI Coding como Claude Code y Codex.

- Construido sobre DeepSeek, OpenAI SDK y MCP.

- Gracias a todos los desarrolladores que recorren juntos el camino del Vibe Coding.

# ☕ Patrocinio

Si Baize te resulta útil, te invito a patrocinar y apoyar. El desarrollo independiente también requiere mucho tiempo. El patrocinio no cambiará el calendario de actualizaciones del producto. ¡Gracias por tu apoyo!

<p align="center">
  <img src="image/support.jpg" alt="Código QR de WeChat" width="200" />
</p>

# Contacto

- Si te interesa Baize o quieres participar en colaboración de código abierto, puedes contactarme de las siguientes formas.
- **Actualmente estoy buscando empleo. He trabajado en investigación de mercado e investigación de usuarios, y también tengo cierto conocimiento de Agents. Si mis capacidades encajan con tus necesidades, espero trabajar contigo (puestos objetivo: Operaciones de producto de IA / Investigación de usuarios / Investigación de mercado).**

<p align="center">
  <img src="image/weixin.jpg" alt="Código QR de WeChat" width="200" />
</p>

<p align="center">Escanea el código QR de WeChat. Indica colaboración de código abierto de Baize o reclutamiento empresarial.</p>

<p align="center">
  <img src="image/抖音.png" alt="Código QR de Douyin" width="200" />
</p>

<p align="center">Escanea el código QR de Douyin para seguir.</p>