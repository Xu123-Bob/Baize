<div align="center">

<img src="image/logopage02.png" alt="Logo de Baize" width="320" />

# Baize 白泽

**Conoce todas las cosas, acompaña tu programación segura.**

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
  <a href="image/抖音.png">
    <img src="https://img.shields.io/badge/抖音-扫码关注-FE2C55?style=flat-square&logo=douyin&logoColor=white" alt="抖音">
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

Bestia auspiciosa de la mitología china antigua, ahora reencarnada como asistente empresarial de análisis de datos y VibeCoding.

**Un CLI de Coding Agent de código abierto, con potente protección de privacidad e interacción multilingüe. Compatible con múltiples backends (DeepSeek / compatible con OpenAI / GLM / Qwen / Kimi / Ollama local), con llamada a herramientas, carga de skills, delegación a subagentes, compresión de contexto y sandbox de seguridad.**

----------

# Ventajas principales

## Protección de privacidad

- **Protección de privacidad bidireccional y reversible**: antes de enviar tu información sensible al LLM, se reemplaza por marcadores de posición; al recibir la respuesta, se restaura automáticamente. Todo el proceso es transparente para ti: el historial, los argumentos de herramientas y la respuesta final que ves siempre son el texto original, mientras que el LLM siempre ve marcadores como `[[PHONE_1]]` y `[[EMAIL_1]]`.
- **Múltiples formas de activar la protección de privacidad**: puedes activarla con lenguaje natural en la conversación o usar el comando más preciso `/privacy`.
- **Agente localizado**: este producto no tiene base de datos remota y se ejecuta completamente en local. No recopila información del usuario.

## Interacción multilingüe

- **Soporta nueve idiomas**: 中文, English, 日本語, 한국어, Español, Français, deutsch, русский, العربية.
- **Múltiples formas de cambiar idioma**: puedes decir directamente un idioma, por ejemplo `please speak with english`, para cambiar a inglés, o usar `/lang ja` para cambiar a japonés.

# Características

- **Soporte multi-backend**: DeepSeek, cualquier interfaz compatible con OpenAI (GLM / Qwen / Kimi / OpenAI), Ollama local, cambio con un clic.

- **Inicio sin configuración**: la primera ejecución genera automáticamente archivos de configuración; solo necesitas ingresar tu clave una vez.

- **Enmascaramiento de privacidad**: detecta y sustituye automáticamente teléfonos, correos, documentos de identidad, tarjetas bancarias, claves API y otra información personal antes de enviarla al LLM, restaurándola automáticamente en la respuesta. Soporta modos estándar / estricto, conmutables por lenguaje natural o `/privacy`.

- **Interacción multilingüe**: cambia libremente entre chino / inglés / japonés / coreano / español / francés / alemán / ruso / árabe. Basta con decir `English` o usar `/lang ja` y la IA piensa y responde en ese idioma.

- **Cadena de herramientas completa**: ejecución bash, lectura/escritura/edición de archivos, búsqueda glob/grep, búsqueda y scraping web, tareas en segundo plano, gestión de tareas y pendientes.

- **Sistema de Skills**: carga conocimiento de dominio (SKILL.md) bajo demanda, haciendo que la IA sea más profesional en escenarios específicos.

- **Subagentes**: delega tareas complejas a subagentes con contexto independiente, evitando contaminar la sesión principal.

- **Hooks**: hooks en Python o Shell, soportan intercepción antes/después de llamadas a herramientas, registro de auditoría, formateo automático y control de pruebas.

- **Protocolo MCP**: conecta servidores de herramientas externos (GitHub, Filesystem, etc.) a través del Model Context Protocol.

- **Compresión de contexto**: compresión en dos niveles (truncado de resultados de herramientas + resumen LLM), soporta conversaciones extremadamente largas.

- **Sandbox de seguridad**: lista blanca de comandos, detección de escape de rutas, bloqueo de comandos peligrosos, protección de archivos sensibles, bloqueo de inyección de scripts.

- **CLI con tema negro dorado**: ancho adaptativo en chino, resaltado de código, coloreado de Diff, plegado de pensamientos.

# Instalación

## Requisitos previos

- Python 3.10+ (necesita tomllib, incluido en 3.11+; para 3.10 instalar tomli)

- pip

## Instalar desde el código fuente

### Dos métodos de descarga

1. `pip install https://github.com/Xu123-Bob/Baize.git`

bash -- Presiona Win+R e ingresa cmd, luego escribe:

    baize

2. En la página del repositorio, haz clic en `<>Code` --> Download ZIP

(1) Después de descomprimir, entra al directorio de este archivo:

bash -- Presiona Win+R e ingresa cmd

    cd directorio_descomprimido

    pip install -r requirements.txt

    python -m Baize

Una vez completada la instalación, presiona Win+R, ingresa cmd, abre la interfaz CLI, escribe `baize` y ejecútalo.

(2) Descarga el ZIP e instala localmente: descomprime, entra al directorio y ejecuta:

bash -- Presiona Win+R e ingresa cmd

    pip install .

Una vez completada la instalación, presiona Win+R, ingresa cmd, abre la interfaz CLI, escribe `baize` y ejecútalo.

# Inicio rápido

1. Primera ejecución

bash

    baize

En la primera ejecución, Baize genera automáticamente dos archivos de configuración:

```
~/.baize/config.toml   # Configuración del backend (elige DeepSeek / OpenAI / Ollama)

~/.baize/.env          # Archivo de claves>
```

La ruta para usuarios de Windows es `C:\Users\tu_usuario\.baize\`.

2. Seleccionar backend

Abre `~/.baize/config.toml` y **modifica `active_provider`**:

toml
```
# Archivo de configuración de Bai Ze  
# Cambiar el proveedor activo para cambiar el backend  
# Valores opcionales: "deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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

3. Ingresar la clave

Edita `~/.baize/.env`,**si necesitas usar un LLM determinado, elimina el ` # ` situado delante de él, y añade ` # ` delante de los demás LLM para bloquear la salida de sus APIs. Después de introducir la Clave API, recuerda guardarla sin falta, solo tras guardarla será válido**:

env
```
# ============================================================
# Archivo de claves de Bai Ze
# ============================================================
# Solo introduce la clave del backend que deseas utilizar, el resto puede mantenerse comentado.
# El nombre de la variable debe coincidir con el campo env_key en config.toml.
#
# Ubicación：
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\Tu nombre de usuario\.baize\.env
# ============================================================

# ---------- DeepSeek（Backend predeterminado） ----------
# Obtener dirección:https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI o cualquier interfaz compatible con OpenAI (opcional) ----------
# Compatible con Groq, Tongyi, Moonshot, Zhipu, OpenAI, etc.  
# Nota: base_url se configura en [model_providers.xxx] de config.toml, no aquí
# OPENAI_API_KEY=

# ---------- Qwen（opcional） ----------
# Obtener dirección:https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot（opcional） ----------
# Obtener dirección:https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- GLM（opcional） ----------
# Obtener dirección:https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- Puerta de enlace personalizada（opcional） ----------
# CUSTOM_API_KEY=

# ---------- Ollama（modelo local, sin clave） ----------
# Solo asegúrese de que Ollama esté ejecutándose en localhost:11434, no es necesario configurarlo aquí
```

4. Reiniciar

bash

    baize

Cuando veas el logo negro dorado y el mensaje de bienvenida, el inicio fue exitoso.

# Ejemplos de uso

Después de iniciar, en el prompt `>>> 降旨：` describe tus necesidades en lenguaje natural:

```
>>>降旨：Escribe un script en Python para hacer scraping del Top250 de Douban y guárdalo como CSV

>>>降旨：Revisa todos los errores de tipo en los archivos Python bajo src/

>>>降旨：Busca todos los lugares en este repositorio que usan requests y cámbialos a httpx
```

## Interacción multilingüe

Baize admite **nueve idiomas**: 中文, English, 日本語, 한국어, Español, Français, deutsch, русский, العربية.

Dos formas de cambiar:

### Opción 1: habla directamente (detección automática)

Baize detecta el idioma de tu entrada y cambia automáticamente:

```
>>> 降旨：Hola, ¿puedes escribirme un script en Python?
[system] Idioma de entrada detectado: Español. Baize cambió a Español.
(responde en español)

>>> 降旨：Hello, write me a script
[system] Idioma de entrada detectado: English. Baize cambió a English.
(responde en inglés)
```

### Opción 2: comando manual

```
>>> 降旨：/lang                # Muestra el idioma actual y la lista disponible
[system] Idioma actual: 中文 (zh)
[system] Disponibles:
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français
    de    Deutsch
    ru    Русский
    ar    العربية

>>> 降旨：/lang English        # Cambiar por nombre de idioma
>>> 降旨：/lang ja             # Cambiar por código
>>> 降旨：/lang 西班牙语        # Nombres en chino también funcionan
```

Admite **nombre del idioma / código / nombre en chino / nombre nativo**. Para cambiar al inglés, cualquiera de `English`, `en`, `英语`, `英文` funciona.

## Interfaz CLI de Baize

<div align="center">
Pantalla de inicio de Baize CLI
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="Pantalla de inicio de Baize CLI" width="800" />
</p>

<div align="center">
Pantalla de ejecución de Baize CLI
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="Pantalla de ejecución de Baize CLI" width="800" />
</p>

## Comandos integrados

- `/exit`, `/quit` --> Salir de Baize
- `/clear` --> Limpiar historial de conversación, pendientes, registros de pensamiento y registros de herramientas
- `/compact` --> Compresión manual del contexto (usar cuando la conversación es demasiado larga)
- `/commit` --> Guardar la sesión actual y confirmar en Git (si estás en un repositorio Git)
- `/lang` → Muestra el idioma actual; `/lang en` cambia a inglés (acepta código o nombre)
- `/skills` --> Listar todas las skills disponibles
- `/skills reload` --> Recargar el directorio de skills del usuario
- `/unload` --> Descargar la skill activa actual
- `/show thought` --> Ver el registro completo de pensamientos
- `/show tool` --> Ver el registro de llamadas a herramientas
- `/show all` --> Ver todo el historial de la sesión
- `/nombre_skill` --> Cargar la skill especificada (soporta coincidencia difusa)
- `/privacy` --> Control de enmascaramiento de privacidad (ver "Enmascaramiento de privacidad" abajo)

# Modelo local Ollama (coste cero)

¿No quieres usar la API en la nube? Usa Ollama local:

bash

    #1. Instalar Ollama: https://ollama.com/download
    #2. Descargar modelo
    ollama pull qwen2.5:7b

    #3. Iniciar servicio Ollama
    ollama serve

    #4. Modificar ~/.baize/config.toml
    active_provider = "ollama"

    #5. Iniciar Baize
    baize

Modelos recomendados: `qwen2.5:7b` (fuerte en chino), `llama3.1:8b`, `deepseek-r1:7b`.

# Mecanismos de extensión

Baize soporta cuatro formas de extensión. Colócalas en el directorio de trabajo actual para que surtan efecto.

## Skills

Escribe conocimiento de dominio en `./skills/nombre_skill/SKILL.md`. La IA lo cargará automáticamente cuando encuentre tareas complejas.

markdown

    ---
    name: pandas-eda

    description: Mejores prácticas para análisis exploratorio de datos con pandas

    tags: data,python
    ---

    # Guía de Pandas EDA

    ## Pasos clave
    1. df.info() para ver tipos de campos y valores faltantes
    2. df.describe() descripción estadística
    ...

También puedes cargarlo manualmente en la conversación con `/pandas-eda`.

## Subagentes

Define subagentes especializados en `./subagent/nombre_rol/AGENT.md`. El agente principal puede delegar tareas mediante la herramienta `agent`.

markdown

    ---
    name: code-reviewer

    description: Revisor de código estricto
    ---

    Eres un revisor de código senior. Al revisar, prioriza:
    1. Condiciones de borde y manejo de excepciones
    2. Fugas de recursos
    3. Seguridad de concurrencia
    ...

## Hooks

Coloca en `./hooks/`:

- `PreToolUse-*.sh`
- `PostToolUse-*.sh`
- `Stop-*.sh`

Reciben entrada JSON y devuelven una decisión:

bash

    #!/bin/bash

    #PreToolUse-guard.sh

    read -r input

    if echo "$input" | grep -q "rm -rf"; then

    echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Prohibido eliminar"}}'

    fi

Los hooks de Python pueden llamar directamente a la API integrada (ver las funciones `hook_*` en `Baize.py`).

## Servidor MCP

Configura servidores de herramientas externos en `./MCP/mcp_config.json`:

json

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

# Diseño de seguridad

Baize activa por defecto los siguientes mecanismos de seguridad:

- **Lista blanca de comandos**: solo permite comandos comunes como `ls`, `cat`, `grep`, `git`, `python3`.
- **Detección de escape de rutas**: todas las operaciones de archivos se limitan al directorio de trabajo actual y `/tmp`.
- **Bloqueo de comandos peligrosos**: bloquea patrones como `rm -rf /`, fork bomb, `curl | sh`, `git push --force`.
- **Protección de archivos sensibles**: prohíbe modificar `.env`, `.ssh/`, `id_rsa`, `*.pem`, etc.
- **Bloqueo de inyección de scripts**: detecta bypasses como `python -c "os.system(...)"`.
- **Límites de recursos del proceso**: en Linux/macOS limita CPU, memoria y número de procesos.

Si necesitas relajar las restricciones en proyectos de confianza, modifica `ALLOWED_COMMANDS` y `FORBIDDEN_PATH_PATTERNS` en `Baize.py`.

# Enmascaramiento de privacidad

Baize incluye un mecanismo de enmascaramiento **bidireccional y reversible**. La información sensible se sustituye por marcadores de posición antes de enviarla al LLM y se restaura automáticamente en la respuesta — totalmente transparente para ti. Lo que ves (historial, argumentos de herramientas, respuesta final) siempre es el texto original; lo que ve el LLM son siempre marcadores como `[[PHONE_1]]`, `[[EMAIL_1]]`.

**Desactivado por defecto.** Actívalo cuando lo necesites.

## Dos formas de activarlo

### Opción 1: Lenguaje natural

```
>>>降旨：activa el enmascaramiento de privacidad
[system] Enmascaramiento de privacidad activado (modo estándar).

>>>降旨：activa el enmascaramiento estricto
[system] Enmascaramiento de privacidad activado (modo estricto).

>>>降旨：desactiva la protección de privacidad
[system] Enmascaramiento de privacidad desactivado.
```

### Opción 2: Comandos slash

- `/privacy on` Activar modo estándar
- `/privacy strict` Activar modo estricto (añade nombres, matrículas, QQ, WeChat)
- `/privacy off` Desactivar
- `/privacy status` Ver el estado actual y estadísticas
- `/privacy rules` Listar todas las reglas
- `/privacy test` <texto> Probar el enmascaramiento
- `/privacy clear` Limpiar el mapa de marcadores

## Dos niveles

**Estándar**: Teléfonos de China continental, documentos de identidad, tarjetas bancarias (validación Luhn), correos, IPv4/IPv6, claves API de OpenAI/Anthropic/GitHub/AWS, tokens Bearer, bloques de clave privada, campos de contraseña, credenciales en URL

**Estricto**: Todo lo de estándar + nombres chinos, números QQ, IDs de WeChat, matrículas de China continental

## Cómo funciona

Entrada del usuario (con PII real) → messages guarda el original

↓ sanitize_messages()

Lo que ve el LLM: [[PHONE_1]], [[EMAIL_1]]

↓ Respuesta del LLM

Marcadores → restore_message()

Restaurado al original → guardar / mostrar / ejecutar

**El mismo original reutiliza el mismo marcador**, por lo que un teléfono permanece como `[[PHONE_1]]` durante toda la sesión.

**Los argumentos de herramientas se clasifican por sensibilidad**: herramientas de solo texto como `todo`, `ask_user_question`, `task_*` sí enmascaran sus argumentos; herramientas de ruta/comando/URL como `run_read`, `run_bash`, `run_webfetch` no (de lo contrario fallarían al sustituirse la ruta).

**Los subagentes también están protegidos**: las tareas delegadas pasan por el mismo pipeline de enmascarar/restaurar.

## Ejemplo

```
>>>降旨：/privacy test Mi teléfono es 13812345678, correo a@b.com
Original: Mi teléfono es 13812345678, correo a@b.com
Enmascarado: Mi teléfono es [[PHONE_1]], correo [[EMAIL_1]]
Restaurado: Mi teléfono es 13812345678, correo a@b.com

>>>降旨：/privacy status
[Enmascaramiento de privacidad]
Modo actual : estándar
Reglas activas: 15 / 19
Marcadores : 2
Enmascaramientos: 3
Restauraciones: 3
```

# Estructura de directorios

```
baize-agent/
├── pyproject.toml              # Configuración de empaquetado
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
    ├── ui_theme.py             # Tema de renderizado CLI
    ├── utils.py                # Utilidades comunes
    ├── logo.txt
    ├── skills/                 # Skills integradas
    ├── subagent/               # Subagentes integrados
    ├── core/                   # Lógica central (sin efectos secundarios, testeable)
    |   ├── __init__.py
    |   ├── history.py          # Limpieza de historial / estimación de tokens / compresión
    |   └── privacy.py          # Enmascaramiento de privacidad: detección de PII 
    ├── hooks/                  # Hooks integrados
    └── MCP/                    # Cliente MCP y configuración
        ├── __init__.py
        ├── mcp_client.py
        └── mcp_config.json
```

# Referencia de variables de entorno

- Variable: `DEEPSEEK_API_KEY`  Descripción: API de DeepSeek  Valor por defecto: clave  —
- Variable: `DEEPSEEK_BASE_URL`  Descripción: Dirección de la interfaz de DeepSeek  Valor por defecto: `https://api.deepseek.com`
- Variable: `OPENAI_API_KEY`  Descripción: OpenAI  Valor por defecto: clave de interfaz compatible  —
- Variable: `OPENAI_BASE_URL`  Descripción: Dirección de interfaz compatible con OpenAI  Valor por defecto: `https://api.openai.com/v1`
- Variable: `OLLAMA_BASE_URL`  Descripción: Dirección del servicio Ollama  Valor por defecto: `http://localhost:11434`

Escribe las variables en `~/.baize/.env`, no es necesario modificar los archivos de configuración del shell.

# Desarrollo

## Ejecutar pruebas

Este proyecto usa pytest. Antes de desarrollar, instala el paquete en modo editable con las dependencias de desarrollo:

    pip install -e ".[dev]"

Ejecutar todas las pruebas:

    python -m pytest tests/ -v

Ejecutar solo un archivo:

    python -m pytest tests/test_history.py -v

## Convenciones de estructura de código

- `agent/`: paquete principal publicado con el paquete. Toda la lógica en tiempo de ejecución y recursos (skills, subagent, hooks, MCP) están aquí.
- `agent/core/`: módulos de lógica pura, sin efectos secundarios externos, **deben poder testearse individualmente**. Añade este tipo de lógica aquí con sus pruebas correspondientes.
- `tests/`: correspondencia uno a uno con los archivos fuente bajo `agent/`, nombrados `test_<módulo>.py`.
- Cualquier función con dependencias externas (red, disco, estado global) debe inyectar dependencias por parámetro para facilitar su reemplazo en pruebas.

# ❓ Preguntas frecuentes

- P: ¿Dónde debo poner la clave?

R: En `~/.baize/.env`, no en el `.env` del directorio raíz del proyecto.

- P: ¿Debo reinstalar si cambio de backend?

R: No. Solo modifica `active_provider` en `~/.baize/config.toml`.

- P: ¿Ollama local necesita clave?

R: No. Selecciona `active_provider = "ollama"`, deja `env_key` vacío.

- P: ¿Cómo cambio el directorio de trabajo?

R: En la conversación di directamente "cambiar a /path/to/project", Baize llamará a la herramienta `set_workspace`.

- P: ¿Qué pasa si el contexto es demasiado largo?

R: Baize comprime automáticamente en dos niveles: primero trunca resultados antiguos de herramientas, luego solicita al LLM que genere un resumen. También puedes usar `/compact` manualmente.

- P: ¿Podría borrar mis archivos por error?

R: La lista blanca de comandos por defecto bloquea operaciones peligrosas como `rm -rf /`; antes de escribir archivos muestra el Diff y solicita confirmación.

- P: ¿Cómo hago que Baize responda en inglés o japonés?

R: Solo di `English` o `日本語` y cambiará automáticamente. También puedes usar `/lang en` (o `/lang ja`). Todo el razonamiento y las respuestas siguientes usarán ese idioma. Para volver al chino, di `中文` o escribe `/lang zh`.

# 🤝 Contribuir

Se aceptan Issues y PRs. Se recomienda leer primero la función `agent_loop` en `Baize.py` para entender el bucle principal del Agente antes de extenderlo.

### Gracias a todos los Contribuidores que envían PR

- Github Contributor:
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# Licencia

MIT License

# Agradecimientos

- Este proyecto está alojado en AtomGit de China, enlace: https://atomgit.com/Com_Xu/Baize

- Gracias a AtomGit por incluir este proyecto en el programa de incubación G-star

- Gracias a los contribuidores de PR, a los seguidores de Douyin y a los estudiantes que me siguen

- Inspirado en excelentes herramientas de IA Coding como Claude Code, Codex

- Construido sobre DeepSeek, OpenAI SDK, MCP

- Gracias a todos los desarrolladores que acompañan en el camino del Vibe Coding

- El desarrollador se enfoca en la creatividad y las decisiones, Baize se encarga de lo trivial y la ejecución. Devuelve la programación a la intuición, haz que la creación fluya como un mito.

# ☕ Apoyo económico

Si Baize te resulta útil, agradezco tu apoyo económico. El desarrollo independiente también lleva mucho tiempo, el apoyo no cambia la planificación de actualizaciones del producto, ¡gracias por tu apoyo!

<p align="center">
  <img src="image/support.jpg" alt="Código QR de WeChat" width="200" />
</p>

# Contacto

- Si te interesa Baize o quieres participar en colaboración open source, puedes contactarme por:
- **Actualmente estoy buscando empleo. He trabajado en investigación de mercado e investigación de usuarios, y también tengo cierto conocimiento de Agentes. Si mis capacidades se ajustan a sus necesidades, me gustaría trabajar con ustedes (puestos de interés: Operaciones de producto de IA / Investigación de usuarios / Investigación de mercado)**

<p align="center">
  <img src="image/weixin.jpg" alt="Código QR de WeChat" width="200" />
</p>

<p align="center">Escanea con WeChat, indica colaboración open source de Baize o reclutamiento empresarial</p>

<p align="center">
  <img src="image/抖音.png" alt="Código QR de Douyin" width="200" />
</p>

<p align="center">Escanea con Douyin para seguir</p>