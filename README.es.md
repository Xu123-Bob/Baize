<div align="center">

<img src="image/logopage02.png" alt="Logotipo de Baize" width="320" />

# Baize

**Di todo lo que sabes, guarda bien los secretos**

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

Un asistente de seguridad para Vibe Coding y análisis de datos, inspirado en una bestia mítica china.

**Una CLI de Coding Agent de código abierto con fuerte protección de privacidad e interacción multilingüe. Admite múltiples backends (DeepSeek / compatible con OpenAI / Zhipu / Tongyi / Kimi / Ollama local) y ofrece capacidades completas como llamada a herramientas, carga de habilidades, delegación a subagentes, compresión de contexto y sandbox seguro.**

----------

# Ventajas principales

## Protección de privacidad

- **Protección de privacidad bidireccional reversible**: La información sensible se reemplaza por marcadores de posición antes de enviarse al LLM y se restaura automáticamente después de recibir la respuesta. Todo el proceso es invisible para el usuario: el historial, los parámetros de herramientas y las respuestas finales que ves siempre contienen el texto original, mientras que el LLM siempre ve marcadores de posición aleatorios e imposibles de adivinar, como `«PZ_PHONE_a3f8b2c1d4e5f6a7»`.
- **Redacción integral en disco**: Los archivos de sesión, las transcripciones comprimidas y los registros de auditoría se redactan automáticamente antes de escribirse en disco (activado por defecto). Nunca aparecen PII en texto plano en el disco.
- **Resistencia a inyecciones**: Los marcadores de posición usan tokens criptográficos aleatorios de 64 bits y no pueden enumerarse, falsificarse ni reutilizarse. Los marcadores antiguos se invalidan inmediatamente al cambiar de sesión.
- **Múltiples formas de activar la protección de privacidad**: Puedes activarla mediante lenguaje natural en la CLI o usar el comando más preciso `/privacy`.
- **Agente local-first**: Este producto no tiene base de datos remota y se ejecuta completamente en local. No recopila información del usuario.

# Características

- **Soporte multimotor**: DeepSeek, cualquier endpoint compatible con OpenAI (GLM / Qwen / Kimi / OpenAI) y Ollama local. Cambia con un solo ajuste de configuración.

- **Inicio sin configuración**: Los archivos de configuración se generan automáticamente en la primera ejecución. El usuario solo necesita introducir su API key una vez.

- **Redacción de privacidad**: Identifica y redacta automáticamente **más de 30 tipos** de información sensible antes de enviarla al LLM (números de teléfono, correos electrónicos, documentos de identidad, pasaportes, tarjetas bancarias, números internacionales, API keys, JWT, cadenas de conexión a bases de datos, direcciones MAC, etc.) y las restaura después de recibir la respuesta. **Se aplica la misma redacción al escribir en disco**, por lo que no queda texto plano en disco. Admite modos estándar y estricto, conmutables mediante lenguaje natural o el comando `/privacy`.

- **Interacción multilingüe**: Cambia libremente entre nueve idiomas: chino, inglés, japonés, coreano, español, francés, alemán, ruso y árabe. Di `English` o usa `/lang ja`, y la IA pensará y responderá en el idioma correspondiente durante toda la sesión.

- **Cadena de herramientas completa**: ejecución de bash, lectura/escritura/edición de archivos, búsqueda glob/grep, búsqueda y descarga web, tareas en segundo plano y gestión de tareas y pendientes.

- **Sistema de habilidades (Skills)**: Carga conocimiento de dominio bajo demanda (`SKILL.md`) para que la IA sea más profesional en escenarios específicos.

- **Subagentes (Subagents)**: Delega tareas complejas a subagentes con contexto independiente para evitar contaminar la sesión principal.

- **Hooks**: Hooks en Python o Shell que admiten intercepción antes/después de llamadas a herramientas, registros de auditoría, formato automático y control de pruebas.

- **Protocolo MCP**: Conecta servidores de herramientas externos (GitHub, Filesystem, etc.) mediante Model Context Protocol.

- **Compresión de contexto**: Compresión en dos niveles (truncado de resultados de herramientas + resumen por LLM) que admite conversaciones muy largas.

- **Sandbox seguro**: Lista blanca de comandos, detección de escape de rutas, bloqueo de comandos peligrosos, protección de archivos sensibles e intercepción de inyección de scripts.

- **CLI con tema negro-dorado**: Ajuste automático del ancho de caracteres chinos, resaltado de código, coloración de diffs y plegado del pensamiento.

# Interfaz de la CLI de Baize

<div align="center">
Pantalla de inicio de la CLI de Baize
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="Pantalla de inicio de la CLI de Baize" width="800" />
</p>

<div align="center">
Pantalla de ejecución de la CLI de Baize -- 01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="Pantalla de ejecución de la CLI de Baize" width="800" />
</p>

<div align="center">
Pantalla de ejecución de la CLI de Baize -- 02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="Pantalla de ejecución de la CLI de Baize" width="800" />
</p>

# Instalación

## Requisitos previos

- Python 3.10+ (requiere `tomllib`; incluido en 3.11+; en 3.10 instala `tomli`)
- pip

## Instalar desde el código fuente

### Dos métodos de descarga

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- pulsa Win+R, escribe `cmd` y ejecuta:

    baize

2. En la página del repositorio, haz clic en `<> Code` --> `Download ZIP`.

(1) Tras extraerlo, entra en el directorio:

    bash -- pulsa Win+R, escribe cmd

    cd ruta\al\directorio\extraído

    pip install -r requirements.txt

    python -m Baize

Tras la instalación, pulsa Win+R, escribe `cmd`, abre la CLI, escribe `baize` y ejecútalo.

(2) Tras descargar el ZIP, instala en local. Extráelo, entra en el directorio y ejecuta:

    bash -- pulsa Win+R, escribe cmd

    pip install .

Tras la instalación, pulsa Win+R, escribe `cmd`, abre la CLI, escribe `baize` y ejecútalo.

### Opcional: instalar dependencias de acceso a datos (importante para análisis de datos)

Si necesitas que Baize controle SPSS o bases de datos SQL, instala las dependencias adicionales:

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` incluye:
- `spss-studio-mcp`: servidor MCP de análisis estadístico SPSS (requiere IBM SPSS Statistics instalado localmente)
- `atengk-mcp-server-rdbms`: servidor MCP genérico para bases de datos relacionales (PostgreSQL / MySQL / SQL Server / Oracle / Dameng, etc.)
- `pyodbc`: enlace Python ODBC requerido por SQL Server

Alternativamente, si el proyecto se instala mediante `pyproject.toml`, puedes usar extras:

```bash
pip install -e ".[data]"          # Instalar todas las dependencias de acceso a datos
pip install -e ".[spss]"          # Solo SPSS
pip install -e ".[sql]"           # Solo SQL genérico
pip install -e ".[sql-mssql]"     # Solo SQL Server (incluye pyodbc)
```

- **⚠️ Usuarios de SQL Server: `pyodbc` es solo el enlace Python. También necesitas instalar Microsoft ODBC Driver 18 for SQL Server a nivel del sistema.**
- **⚠️ Usuarios de SPSS: `spss-studio-mcp` es solo una capa puente MCP. IBM SPSS Statistics (versiones 20–31) debe estar instalado localmente y con licencia activa, y la variable de entorno `SPSS_INSTALL_PATH` debe apuntar al directorio de instalación de SPSS. El análisis estadístico completo con el motor SPSS se admite principalmente en Windows. En Linux/macOS puede degradarse al "modo archivo" (leer archivos `.sav`, inspeccionar metadatos, previsualizar datos, pero sin análisis estadístico).**

# Inicio rápido

## Ejecutar con una API de LLM

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

**2. Elegir un backend**

Abre `~/.baize/config.toml` y modifica **active_provider** (este paso es obligatorio):

```toml
# Archivo de configuración de Baize
# Modifica active_provider para cambiar de backend
# Valores posibles: "deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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

**3. Introducir la API key**

Edita `~/.baize/.env`. **Si necesitas usar un LLM concreto, elimina el `#` inicial de la línea de clave de ese proveedor, añade `#` delante de las claves de los demás LLM para bloquear su salida, introduce la API key y asegúrate de guardar el archivo. Solo surte efecto después de guardar**:

```env
# ============================================================
# Archivo de claves de Baize
# ============================================================
# Rellena solo la clave del backend que quieras usar; deja el resto comentado.
# Los nombres de variables deben coincidir con los campos env_key de config.toml.
#
# Ubicación:
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\TuNombreDeUsuario\.baize\.env
# ============================================================

# ---------- DeepSeek (backend predeterminado) ----------
# Obtenla en: https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI o cualquier endpoint compatible con OpenAI (opcional) ----------
# Adecuado para Groq, Tongyi, Moonshot, Zhipu, OpenAI, etc.
# Nota: base_url se configura en [model_providers.xxx] de config.toml, no aquí.
# OPENAI_API_KEY=

# ---------- Tongyi Qianwen (opcional) ----------
# Obtenla en: https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot (opcional) ----------
# Obtenla en: https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- Zhipu GLM (opcional) ----------
# Obtenla en: https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- Gateway personalizado (opcional) ----------
# CUSTOM_API_KEY=

# ---------- Ollama (modelo local, no requiere clave) ----------
# Solo asegúrate de que Ollama esté ejecutándose en localhost:11434. No se necesita configuración aquí.
```

4. Reiniciar

```bash
baize
```

Si ves el logotipo negro-dorado y el mensaje de bienvenida, el inicio fue correcto.

## Modelos locales con Ollama (coste cero)

¿No quieres usar una API en la nube? Usa Ollama local:

    bash

    # 1. Instalar Ollama: https://ollama.com/download
    # 2. Descargar un modelo
    ollama pull qwen2.5:7b

    # 3. Iniciar el servicio de Ollama
    ollama serve

    # 4. Modificar ~/.baize/config.toml
    active_provider = "ollama"

    # 5. Iniciar Baize
    baize

Modelos recomendados: `qwen2.5:7b` (fuerte en chino), `llama3.1:8b`, `deepseek-r1:7b`.

# Ejemplos de uso

Tras el inicio, describe tus necesidades en lenguaje natural en el prompt `>>> 降旨：`:

```
>>> 降旨：Escribe un script en Python para hacer scraping de Douban Top250 y guárdalo como CSV

>>> 降旨：Ayúdame a comprobar los errores de tipo en todos los archivos Python bajo src/

>>> 降旨：Encuentra en este repositorio todos los lugares que usan requests y cámbialos por httpx
```

## Interacción multilingüe

Baize admite **nueve idiomas**: chino, inglés, japonés, coreano, español, francés, alemán, ruso y árabe.

Hay dos formas de cambiar:

### Método 1: simplemente habla (detección automática)

Baize detecta automáticamente el idioma de tu entrada y cambia:

```
>>> 降旨：Hello, help me write a Python script
[Sistema] Idioma de entrada detectado: English. Baize ha cambiado a interacción en English.
(Baize responde en inglés)

>>> 降旨：日本語で答えてください
[Sistema] Idioma de entrada detectado: 日本語. Baize ha cambiado a interacción en 日本語.
(Baize responde en japonés)
```

### Método 2: comando manual

```
>>> 降旨：/lang                # Mostrar idioma actual y lista disponible
[Sistema] Idioma actual: 中文 (zh)
[Sistema] Idiomas disponibles:
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> 降旨：/lang English        # Cambiar por nombre de idioma
>>> 降旨：/lang ja             # Cambiar por código de idioma
>>> 降旨：/lang 西班牙语        # El nombre en chino también funciona
```

Admite **nombre de idioma / código de idioma / nombre en chino / nombre nativo**. Por ejemplo, para cambiar a inglés, cualquiera de `English`, `en`, `英语` o `英文` funciona.

## Comandos integrados

- `/exit`, `/quit` --> Salir de Baize
- `/clear` --> Limpiar historial de conversación, pendientes, registros de pensamiento y registros de herramientas
- `/compact` --> Comprimir manualmente el contexto (usar cuando la conversación sea demasiado larga)
- `/commit` --> Guardar la sesión actual y hacer commit en Git (si estás dentro de un repositorio Git)
- `/lang` --> Mostrar el idioma actual; `/lang en` cambia a inglés (admite códigos o nombres de idioma)
- `/skills` --> Listar todas las habilidades disponibles
- `/skills reload` --> Recargar el directorio de habilidades del usuario
- `/unload` --> Descargar la habilidad actualmente activa
- `/show thought` --> Mostrar el registro completo de pensamiento
- `/show tool` --> Mostrar registros de llamadas a herramientas
- `/show all` --> Mostrar todo el historial de la sesión
- `/nombre-de-habilidad` --> Cargar una habilidad especificada (admite coincidencia difusa)
- `/privacy` --> Control de redacción de privacidad (`on / off / strict / status / rules / test / clear`)
- `/privacy rule-off <name>` --> Desactivar una regla de redacción (p. ej. `/privacy rule-off phone_intl`)
- `/privacy rule-on <name>` --> Reactivar una regla

## Ejemplos de uso de acceso a datos

Tras configurar SPSS / SQL, puedes controlarlos directamente con lenguaje natural:

```text
>>> 降旨：Usa SPSS para abrir data.sav y dime la lista de variables y el tamaño de la muestra

>>> 降旨：Ejecuta estadísticas descriptivas sobre data.sav y luego una regresión lineal

>>> 降旨：Consulta en la tabla sales los pedidos con importe superior a 100.000 del mes pasado, agrupados por cliente

>>> 降旨：Exporta los resultados del análisis de SPSS a CSV y luego únelos con los datos maestros de clientes usando SQL
```

# Mecanismos de extensión

Baize admite cuatro mecanismos de extensión. Colócalos en el directorio de trabajo actual y surtirán efecto.

## Habilidades (Skills)

Escribe conocimiento de dominio en `./skills/<nombre-de-habilidad>/SKILL.md`. La IA lo cargará de forma proactiva cuando encuentre tareas complejas.

    markdown

    ---
    name: pandas-eda

    description: Buenas prácticas para análisis exploratorio de datos con pandas

    tags: data,python
    ---

    # Guía de Pandas EDA

    ## Pasos principales
    1. df.info() para inspeccionar tipos de campo y valores faltantes
    2. df.describe() para descripción estadística
    ...

También puedes cargarla manualmente en la conversación con `/pandas-eda`.

## Subagentes (Subagents)

Define subagentes especializados en `./subagent/<nombre-de-rol>/AGENT.md`. El agente principal puede delegar tareas mediante la herramienta `agent`.

    markdown

    ---
    name: code-reviewer

    description: Revisor de código estricto
    ---

    Eres un revisor de código senior. Durante la revisión, prioriza:
    1. Condiciones límite y manejo de excepciones
    2. Fugas de recursos
    3. Seguridad de concurrencia
    ...

## Hooks

Coloca `PreToolUse-*.sh`, `PostToolUse-*.sh` y `Stop-*.sh` bajo `./hooks/`. Reciben entrada JSON y devuelven una decisión:

```bash
#!/bin/bash
# PreToolUse-guard.sh
read -r input
if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Deletion prohibited"}}'
fi
```

Los hooks en Python pueden llamar directamente a APIs integradas (consulta las funciones `hook_*` en `Baize.py`).

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

- **Lista blanca de comandos**: Solo se permiten comandos comunes como `ls`, `cat`, `grep`, `git` y `python3`.
- **Detección de escape de rutas**: Todas las operaciones de archivos se restringen al directorio de trabajo actual y `/tmp`.
- **Bloqueo de comandos peligrosos**: Bloquea patrones como `rm -rf /`, fork bombs, `curl | sh` y `git push --force`.
- **Protección de archivos sensibles**: Prohíbe modificar `.env`, `.ssh/`, `id_rsa`, `*.pem`, etc.
- **Intercepción de inyección de scripts**: Detecta bypass como `python -c "os.system(...)"`.
- **Límites de recursos de proceso**: Limita CPU, memoria y número de procesos en Linux/macOS.
- **Redacción de privacidad (bidireccional reversible)**: Las PII se reemplazan por marcadores aleatorios en salida y se restauran en entrada; las escrituras en disco se redactan de forma independiente.
- **Resistencia a inyección de marcadores**: Tokens criptográficos aleatorios de 64 bits + neutralización en el lado de entrada + aislamiento de sesión.
- **Redacción de registros de auditoría**: `hook_audit_log` redacta antes de escribir, trunca y se niega a escribir si falla.

Si necesitas relajar las restricciones en proyectos de confianza, puedes modificar `ALLOWED_COMMANDS` y `FORBIDDEN_PATH_PATTERNS` en `Baize.py`.

# Redacción de privacidad (núcleo)

Baize incluye un mecanismo integrado de protección de privacidad **bidireccional reversible + redacción en disco** que cubre toda la ruta desde la entrada hasta el disco:

- **Salida**: Antes de enviar al LLM, las PII se reemplazan por marcadores imposibles de adivinar.
- **Entrada**: Los marcadores en las respuestas del LLM se restauran al texto original.
- **Escrituras en disco**: Los archivos de sesión, las transcripciones comprimidas y los registros de auditoría se **redactan de forma independiente** antes de escribirse en disco. No queda texto plano en disco.

**Desactivado por defecto**; actívalo cuando sea necesario.

## Dos formas de activarlo

### Método 1: lenguaje natural

Di directamente en la conversación:

```
>>> 降旨：Activar la redacción de privacidad
[Sistema] Redacción de privacidad activada (modo estándar).

>>> 降旨：Activar redacción estricta
[Sistema] Redacción de privacidad activada (modo estricto).

>>> 降旨：Desactivar la protección de privacidad
[Sistema] Redacción de privacidad desactivada.
```

### Método 2: comandos con barra

- `/privacy on` activa el modo estándar
- `/privacy strict` activa el modo estricto
- `/privacy off` lo desactiva
- `/privacy status` muestra estado, ID de sesión, número de reglas y estadísticas LRU/TTL
- `/privacy rules` lista todas las reglas (incluido su estado)
- `/privacy rule-off <name>` desactiva una regla
- `/privacy rule-on <name>` la reactiva
- `/privacy test <texto>` prueba el resultado de la redacción
- `/privacy clear` limpia el mapeo de marcadores y **rota el ID de sesión**

## Dos modos

**Estándar**: Números móviles de China continental, números de documento de identidad, números de tarjeta bancaria (validación Luhn), correos electrónicos, IPv4/IPv6, API keys de OpenAI/Anthropic/GitHub/AWS, Bearer tokens, bloques de clave privada, campos de contraseña, credenciales de URL.

**Estricto**: Todas las reglas estándar + nombres chinos, números QQ, IDs de WeChat, matrículas de China continental.

## Cómo funciona

Entrada del usuario (con PII reales) → los mensajes almacenan el texto original

↓ `sanitize_messages()`

Lo que se envía al LLM es `[[PHONE_1]]`, `[[EMAIL_1]]`

↓ Respuesta del LLM

Marcadores devueltos → `restore_message()`

Restaurados al texto original → escritura en disco / visualización / ejecución de herramientas

- **Redacción de privacidad (bidireccional reversible)**: Las PII se reemplazan por marcadores aleatorios en salida y se restauran en entrada; las escrituras en disco se redactan de forma independiente.
- **Resistencia a inyección de marcadores**: Tokens criptográficos aleatorios de 64 bits + neutralización en el lado de entrada + aislamiento de sesión.
- **Redacción de registros de auditoría**: `hook_audit_log` redacta antes de escribir, trunca y se niega a escribir si falla.

## Clasificación inteligente de parámetros de herramientas

**Redactados** (parámetros de texto plano que no participan en la ejecución real):

- `todo`, `ask_user_question`, `task_create`, `task_update`

**No redactados** (las rutas/comandos/URL se usan realmente):

- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep` (las rutas se usan para IO)
- `run_bash` / `background_run` (los comandos se ejecutan)
- `run_webfetch` / `web_search` (las URL se envían realmente a la red)
- `set_workspace` (la ruta se usa para `chdir`)
- `load_skills` (los nombres de habilidades son enumerados)
- `agent` (el contexto del subagente se redacta de forma independiente)
- `mcp_*` (semántica desconocida; se maneja de forma conservadora)

**Todos redactados al escribir en disco** (porque el contenido en disco no se reejecuta, prioridad a la seguridad).

## Redacción en disco

**Activada por defecto**, independiente de la redacción en memoria. Aunque se use `/privacy off` (sin redacción en memoria), las escrituras en disco siguen pasando al menos por las reglas estándar.

**Características clave**:

- La redacción en disco usa una **tabla de mapeo independiente y de un solo uso**. Los marcadores escritos en disco **no se pueden restaurar**, porque la tabla de mapeo se descarta.
- Si la redacción en disco **falla, Baize se niega a escribir texto plano** (sin degradación, sin omisión silenciosa).
- Si un archivo de sesión antiguo contiene texto plano, se redactará y reescribirá automáticamente la primera vez que se guarde.

**Cómo desactivarla** (no recomendado): Establece `PERSIST_REDACT_ENABLED = False` en `Baize.py`.

## Ejemplo

```
>>> 降旨：/privacy test Mi número de teléfono es 13812345678, correo a@b.com
Original: Mi número de teléfono es 13812345678, correo a@b.com
Redactado: Mi número de teléfono es [[PHONE_1]], correo [[EMAIL_1]]
Restaurado: Mi número de teléfono es 13812345678, correo a@b.com

>>> 降旨：/privacy status
[Redacción de privacidad]
Modo actual : Modo estándar (standard)
ID de sesión : 7d2f5e91
Reglas activas : 34 / 41
Marcadores activos : 2
Capacidad de mapeo : 2 / 2000
TTL : 86400 segundos
Evicciones LRU : 0
Evicciones TTL : 0
Llamadas de redacción: 3
Llamadas de restauración: 3

>>> 降旨：/privacy rules
[Lista de reglas de redacción de privacidad] 41 reglas en total
[Estándar + Estricto]
[✓] phone_cn Número móvil de China continental (standard,strict)
[✓] id_card_cn Número de documento de identidad de China continental (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
[Solo estricto]
[✓] name_cn Nombre chino (strict)
[✓] address_cn Dirección detallada china (strict)
...
Uso:
/privacy rule-off <name> desactivar una regla
/privacy rule-on <name> reactivar una regla
```

### Capturas de prueba

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

Baize se conecta a software empresarial de análisis de datos mediante **MCP (Model Context Protocol)**. El programa principal no requiere modificaciones: basta con registrar el servidor en `MCP/mcp_config.json`.

## Integración con SPSS

### Requisitos previos

- IBM SPSS Statistics instalado localmente (versiones 20–31; se recomienda Windows)
- SPSS con licencia y capaz de iniciarse normalmente

### Pasos de configuración

1. **Localizar el directorio de instalación de SPSS**: La ruta predeterminada suele ser `C:\Program Files\IBM\SPSS Statistics\` seguida del número de versión (p. ej. `31`).

2. **Establecer la variable de entorno** (en `.env` o en las variables de entorno del sistema):

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **Verificar el estado**:

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

4. **Registrarlo en `MCP/mcp_config.json`**:

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

Esto significa que `spss-studio-mcp` no encontró el motor de SPSS, pero `pyreadstat` + `pandas` funcionan. En este caso, entra en **modo archivo**:

- Puede leer `.sav`, inspeccionar metadatos, previsualizar datos y convertir CSV ↔ SAV
- No puede ejecutar estadísticas (prueba t, regresión, ANOVA, etc.)

Solución: Configura correctamente `SPSS_INSTALL_PATH` en `MCP/mcp_config.json`, o acepta la degradación a modo archivo.

## Integración con SQL

### Bases de datos compatibles

PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, Dameng, Kingbase, TiDB, OceanBase, etc. (basado en drivers de SQLAlchemy 2.0).

### Pasos de configuración

1. **Preparar una cuenta de base de datos de solo lectura** (muy recomendado):

```sql
CREATE USER baize_ro WITH PASSWORD 'xxx';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO baize_ro;
```

2. **Preparar la cadena de conexión**:

- PostgreSQL --> `postgresql+psycopg://user:pwd@host:5432/db`
- MySQL --> `mysql+pymysql://user:pwd@host:3306/db`
- SQL Server --> `mssql+pyodbc://user:pwd@host:1433/db?driver=ODBC+Driver+18+for+SQL+Server`
- Oracle --> `oracle+oracledb://user:pwd@host:1521/?service_name=ORCL`

3. **Registrarlo en `MCP/mcp_config.json`**:

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

### Barreras de seguridad integradas

`atengk-mcp-server-rdbms` proporciona múltiples capas de protección:

- **Guarda SELECT a nivel AST**: Usa `sqlglot` para analizar el árbol de sintaxis y bloquear físicamente operaciones de escritura como `DELETE/UPDATE/DROP/TRUNCATE`.
- **Inyección automática de LIMIT**: Las consultas sin número de filas especificado se fuerzan a añadir `LIMIT 100` para evitar que las consultas de tabla completa agoten la memoria.
- **Solo lectura por defecto**: Las operaciones de escritura deben autorizarse explícitamente mediante `--allow-dml` / `--allow-ddl`.
- **Intercepción de inyección SQL**: Rechaza sentencias maliciosas construidas por concatenación de cadenas a nivel AST.

### Configurar varias bases de datos a la vez

Si quieres conectarte a varias bases de datos simultáneamente, registra varios servidores:

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

Baize fusionará automáticamente todas sus herramientas en `MATERTOOLS`, y el LLM seleccionará la adecuada según la tarea.

# Estructura de directorios

```
    baize-agent/
    ├── pyproject.toml              # Configuración de empaquetado
    ├── requirements-data.txt       # Dependencias de acceso a datos (opcional)
    ├── requirements-data           # Dependencias de acceso
    ├── README.md
    ├── tests/                      # Pruebas (no se incluyen en el paquete)
    |   ├── __init__.py
    |   ├── test_history.py
    |   └── test_skill_loader.py
    ├── .env.example                # Ejemplo de variables de entorno
    ├── .gitignore
    └── agent/                      # Paquete principal
        ├── logo_*                  # Logotipo de la pantalla de inicio
        ├── LOGO和启动交互界面       # Imagen del logotipo de la pantalla de inicio
        ├── __init__.py             # Versión
        ├── Baize.py                # Programa principal y Agent Loop
        ├── config.py               # Carga de configuración multimotor
        ├── ui_theme.py             # Tema de renderizado de la CLI
        ├── utils.py                # Utilidades generales
        ├── logo.txt
        ├── skills/                 # Habilidades integradas
        ├── subagent/               # Subagentes integrados
        ├── core/                   # Lógica central (sin efectos secundarios, testeable unitariamente)
        |   ├── __init__.py
        |   ├── history.py          # Limpieza del historial de sesión / estimación de tokens / compresión
        |   └── privacy.py          # Redacción de privacidad: detección de PII / reemplazo por marcadores / restauración reversible
        ├── hooks/                  # Hooks integrados
        └── MCP/                    # Cliente y configuración MCP
            ├── __init__.py
            ├── mcp_client.py       # Cliente MCP
            └── mcp_config.json     # Configuración MCP
```

# Referencia de variables de entorno

- Variable: `DEEPSEEK_API_KEY` — Descripción: API key de DeepSeek — Valor por defecto: — (secreto)
- Variable: `DEEPSEEK_BASE_URL` — Descripción: URL del endpoint de DeepSeek — Valor por defecto: `https://api.deepseek.com`
- Variable: `OPENAI_API_KEY` — Descripción: API key compatible con OpenAI — Valor por defecto: — (secreto)
- Variable: `OPENAI_BASE_URL` — Descripción: URL del endpoint compatible con OpenAI — Valor por defecto: `https://api.openai.com/v1`
- Variable: `OLLAMA_BASE_URL` — Descripción: URL del servicio Ollama — Valor por defecto: `http://localhost:11434`

**Escribe las variables anteriores en `~/.baize/.env`; no es necesario modificar archivos de configuración del shell.**

- Variable de análisis de datos: `SPSS_INSTALL_PATH` — Descripción: Directorio de instalación de IBM SPSS Statistics — Valor por defecto: — (si no se establece, se degrada a modo archivo)
- Variable de análisis de datos: `DATABASE_URL` — Descripción: Cadena de conexión de base de datos para SQL MCP — Valor por defecto: — (la lee el servidor MCP)

**Escribe las variables anteriores en `MCP/mcp_config.json`.**

# Desarrollo

## Ejecutar pruebas

Este proyecto usa pytest. Antes de desarrollar, instala el paquete en modo editable con las dependencias de desarrollo:

    pip install -e ".[dev]"

Ejecutar todas las pruebas:

    python -m pytest tests/ -v

Ejecutar un solo archivo:

    python -m pytest tests/test_history.py -v

## Convenciones de estructura del código

- `agent/`: El paquete principal que se distribuye con el paquete. Toda la lógica de ejecución y los recursos (skills, subagent, hooks, MCP) viven aquí.
- `agent/core/`: Módulos de lógica pura sin efectos secundarios externos. **Deben poder probarse de forma independiente.** Añade aquí la nueva lógica de este tipo e incluye pruebas.
- `tests/`: Se corresponde uno a uno con los archivos fuente bajo `agent/`, con el nombre `test_<módulo>.py`.
- Cualquier función con dependencias externas (red, disco, estado global) debe inyectar dependencias mediante parámetros para que puedan sustituirse en las pruebas.

# Preguntas frecuentes

- P: ¿Dónde debo poner la API key?

R: En `~/.baize/.env`, no en el `.env` de la raíz del proyecto.

- P: ¿Necesito reinstalar tras cambiar de backend?

R: No. Solo cambia `active_provider` en `~/.baize/config.toml`.

- P: ¿Ollama local requiere API key?

R: No. Establece `active_provider = "ollama"` y deja `env_key` vacío.

- P: ¿Cómo cambio el directorio de trabajo?

R: En la conversación, simplemente di "cambia a /path/to/project", y Baize llamará a la herramienta `set_workspace`.

- P: ¿Qué ocurre si el contexto es demasiado largo?

R: Baize realiza automáticamente una compresión en dos niveles: primero trunca los resultados antiguos de herramientas y luego solicita un resumen al LLM. También puedes usar `/compact` manualmente.

- P: ¿Eliminará mis archivos por accidente?

R: La lista blanca de comandos predeterminada bloquea operaciones peligrosas como `rm -rf /`; antes de escribir archivos, muestra un diff y pide confirmación.

- P: ¿Cómo conecto Baize a SPSS?

R: 1. Instala `pip install -r requirements-data.txt`; 2. Establece la variable de entorno `SPSS_INSTALL_PATH` apuntando al directorio de instalación de SPSS; 3. Activa el servidor `spss` en `MCP/mcp_config.json`. Consulta la sección "Acceso a datos (SPSS / SQL)" para más detalles.

- P: ¿Qué hago con `SPSS batch: NOT FOUND`?

R: Significa que no se encontró el motor de SPSS. Comprueba si `SPSS_INSTALL_PATH` apunta correctamente al directorio que contiene `stats.exe`; si solo procesas archivos `.sav`, puedes ignorar esta advertencia (se degradará a modo archivo).

- P: ¿Qué cosas adicionales necesito instalar para conectarme a una base de datos SQL?

R: Instala `atengk-mcp-server-rdbms` en la capa Python (`pip install` se encarga). **Los usuarios de SQL Server también necesitan instalar Microsoft ODBC Driver 18 a nivel del sistema**, que no se puede instalar mediante pip.

- P: ¿Baize eliminará accidentalmente los datos de mi base de datos?

R: No. SQL MCP solo permite SELECT por defecto y bloquea todas las operaciones de escritura a nivel del árbol de sintaxis AST. Aun así, se recomienda encarecidamente crear una **cuenta de base de datos de solo lectura** para Baize como segunda salvaguarda.

- P: ¿Los datos de los resultados del análisis de SPSS se filtrarán al LLM?

R: Si la redacción de privacidad está activada (`/privacy on`), los resultados de las herramientas se redactan automáticamente para números de teléfono, correos electrónicos, documentos de identidad y otras PII antes de enviarse al LLM. **No obstante, se recomienda usar también una cuenta de base de datos de solo lectura + muestreo de datos** (consultar solo los campos necesarios) para reducir el riesgo.

- P: ¿Por qué Baize se vuelve más lento y usa más tokens en cada conversación tras añadir SPSS/SQL?

R: Porque las definiciones de herramientas expuestas por los servidores MCP se envían al LLM en cada turno de conversación. SPSS tiene más de 60 herramientas, lo que añade una sobrecarga fija de unos 6.000–12.000 tokens. Si tu flujo de trabajo habitual no implica SPSS, puedes poner su `enabled` en `false` y activarlo cuando lo necesites.

# Contribuir

Se aceptan Issues y PRs. Lee `CONTRIBUTOR.md` antes de enviar un PR.

**Gracias a todos los Contributors que envían PRs.**

- GitHub Contributors:
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# Licencia

MIT License

# Agradecimientos

- Este proyecto está alojado en AtomGit (China): https://atomgit.com/Com_Xu/Baize
- Gracias a AtomGit por incluir este proyecto en el programa de incubación G-star.
- Gracias a los contribuidores de PR, a los seguidores de Douyin y a los estudiantes que me siguen.
- Inspirado por excelentes herramientas de AI Coding como Claude Code y Codex.
- Construido sobre DeepSeek, OpenAI SDK y MCP.
- Gracias a todos los desarrolladores que recorren el camino del Vibe Coding juntos.

# ☕ Patrocinio

Si Baize te resulta útil, te invitamos a patrocinarlo y apoyarlo. El desarrollo independiente requiere mucho tiempo. El patrocinio no cambiará el calendario de actualizaciones del producto. ¡Gracias por tu apoyo!

<p align="center">
  <img src="image/support.jpg" alt="Código QR de WeChat" width="200" />
</p>

# Contacto

- Si te interesa Baize o quieres participar en la colaboración de código abierto, puedes contactarme a través de los siguientes canales.
- **Actualmente estoy buscando oportunidades laborales. Tengo experiencia en investigación de mercado e investigación de usuarios, y también entiendo algo sobre Agentes. Si mis capacidades se ajustan a sus necesidades, espero trabajar con usted (puestos objetivo: Operaciones de Producto de IA / Investigación de Usuarios / Investigación de Mercado).**

<p align="center">
  <img src="image/weixin.jpg" alt="Código QR de WeChat" width="200" />
</p>

<p align="center">Escanea el código QR de WeChat e indica "colaboración de código abierto de Baize" o "contratación empresarial".</p>

<p align="center">
  <img src="image/抖音.png" alt="Código QR de Douyin" width="200" />
</p>

<p align="center">Escanea el código QR de Douyin para seguir.</p>