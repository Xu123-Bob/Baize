<div align="center">

<img src="image/logopage02.png" alt="Logo de Baize" width="320" />

# Baize 白泽

**Conoce todas las cosas, acompaña tu programación intuitiva.**

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

Baize —— La bestia auspiciosa de la mitología china antigua que conocía todas las cosas, ahora reencarnada como asistente de Vibe Coding.

**Un CLI de Agente de Programación con IA de código abierto, alternativa a Claude Code CLI. Compatible con múltiples backends (DeepSeek / compatible con OpenAI / GLM / Qwen / Kimi / Ollama local), con capacidades completas de llamada a herramientas, carga de skills, delegación a subagentes, compresión de contexto y sandbox de seguridad. Programa en pareja con IA directamente desde la terminal.**

----------


# Características

- **Soporte multi-backend**: DeepSeek, cualquier interfaz compatible con OpenAI (GLM / Qwen / Kimi / OpenAI), Ollama local, cambio con un clic.

- **Inicio sin configuración**: la primera ejecución genera automáticamente archivos de configuración; solo necesitas ingresar tu clave una vez.

- **Cadena de herramientas completa**: ejecución bash, lectura/escritura/edición de archivos, búsqueda glob/grep, búsqueda y scraping web, tareas en segundo plano, gestión de tareas y pendientes.

- **Sistema de Skills**: carga conocimiento de dominio (SKILL.md) bajo demanda, haciendo que la IA sea más profesional en escenarios específicos.

- **Subagentes (Subagents)**: delega tareas complejas a subagentes con contexto independiente, evitando contaminar la sesión principal.

- **Hooks**: hooks en Python o Shell, soportan intercepción antes/después de llamadas a herramientas, registro de auditoría, formateo automático, control de pruebas.

- **Protocolo MCP**: conecta servidores de herramientas externos (GitHub, Filesystem, etc.) a través del Model Context Protocol.

- **Compresión de contexto**: compresión en dos niveles (truncado de resultados de herramientas + resumen LLM), soporta conversaciones extremadamente largas.

- **Sandbox de seguridad**: lista blanca de comandos, detección de escape de rutas, bloqueo de comandos peligrosos, protección de archivos sensibles, bloqueo de inyección de scripts.

- **Interacción multilingüe**: Cambia libremente entre chino / inglés / japonés / coreano / español / francés. Basta con decir `English` o usar `/lang ja` y la IA piensa y responde en ese idioma.

- **CLI con tema negro dorado**: ancho adaptativo en chino, resaltado de código, coloreado de Diff, plegado de pensamientos.

# Instalación

## Requisitos previos

- Python 3.10+ (necesita tomllib, incluido en 3.11+; para 3.10 instalar tomli)

- pip

## Instalar desde el código fuente
### Dos métodos de descarga
1. pip install https://github.com/Xu123-Bob/Baize.git

bash --win+R escribe cmd

    baize

2. <>Code --> Download ZIP

(1) Después de descomprimir, entra al directorio de este archivo:

bash --win+R escribe cmd

    cd directorio_descomprimido # si ya abriste cmd con win+R en el directorio de este archivo, este paso no es necesario

    pip install -r requirements.txt    

    python -m Baize             

Una vez completada la descarga, pulsa win+R, escribe cmd, abre la interfaz CLI e ingresa baize para ejecutarlo.

(2) Descarga el ZIP e instala localmente, descomprime y entra al directorio, ejecuta:

bash --win+R escribe cmd

    pip install .

Una vez completada la descarga, pulsa win+R, escribe cmd, abre la interfaz CLI e ingresa baize para ejecutarlo.

# Inicio rápido
1. Primera ejecución

bash

    baize

En la primera ejecución, Baize genera automáticamente dos archivos de configuración:

text

    ~/.baize/config.toml   # Configuración del backend (elige DeepSeek / OpenAI / Ollama)

    ~/.baize/.env          # Archivo de claves>

La ruta para usuarios de Windows es C:\Users\tu_usuario\.baize\.


2. Seleccionar backend

Abre ~/.baize/config.toml y modifica active_provider:

toml

    active_provider = "deepseek"    # o "openai" / "ollama"

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
    model = "qwen2.5:7b">


3. Ingresar la clave

Edita ~/.baize/.env:

env

    #Obligatorio para backend DeepSeek

    DEEPSEEK_API_KEY=sk-tu_clave


    #Obligatorio para interfaz compatible con OpenAI (GLM / Qwen / Kimi / OpenAI)

    #OPENAI_API_KEY=tu_clave

    #Ollama local no requiere clave


4. Reiniciar

bash

    baize

Cuando veas el logo negro dorado y el mensaje de bienvenida, el inicio fue exitoso.


# Ejemplos de uso

Después de iniciar, en el prompt >>> 降旨: describe tus necesidades en lenguaje natural:

text

    >>>降旨：Escribe un script en Python para hacer scraping del Top250 de Douban y guárdalo como CSV

    >>>降旨：Revisa todos los errores de tipo en los archivos Python bajo src/

    >>>降旨：Busca todos los lugares en este repositorio que usan requests y cámbialos a httpx

## Interacción multilingüe

Baize admite **seis idiomas**: 中文, English, 日本語, 한국어, Español, Français.

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
[system] Idioma actual: Español (es)
[system] Disponibles:
    zh    中文
    en    English
    ja    日本語
    ko    한국어
    es    Español ←
    fr    Français

>>> 降旨：/lang English        # Cambiar por nombre de idioma
>>> 降旨：/lang ko             # Cambiar por código
>>> 降旨：/lang 西班牙语        # Nombres en chino también funcionan
```

Admite **nombre del idioma / código / nombre nativo**. Para cambiar al inglés, cualquiera de `English`, `en`, `英语`, `英文` funciona.


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
- /exit, /quit --> Salir de Baize
- /clear	--> Limpiar historial de conversación, pendientes, registros de pensamiento y registros de herramientas
- /compact	--> Compresión manual del contexto (usar cuando la conversación es demasiado larga)
- /commit	--> Guardar la sesión actual y confirmar en Git (si estás en un repositorio Git)
- /lang → Muestra el idioma actual; /lang en cambia a inglés (acepta código o nombre)
- /skills	--> Listar todas las skills disponibles
- /skills reload	--> Recargar el directorio de skills del usuario
- /unload	--> Descargar la skill activa actual
- /show thought	--> Ver el registro completo de pensamientos
- /show tool	--> Ver el registro de llamadas a herramientas
- /show all	--> Ver todo el historial de la sesión
- /nombre_skill	--> Cargar la skill especificada (soporta coincidencia difusa)


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

Modelos recomendados: qwen2.5:7b (fuerte en chino), llama3.1:8b, deepseek-r1:7b.


# Mecanismos de extensión

Baize soporta cuatro formas de extensión, todas funcionan colocándolas en el directorio de trabajo actual.

## Skills
Escribe conocimiento de dominio en ./skills/nombre_skill/SKILL.md, la IA lo cargará automáticamente cuando encuentre tareas complejas.

markdown

    ---
    name: pandas-eda

    description: Mejores prácticas para análisis exploratorio de datos con pandas

    tags: data,python
    ---

    #Guía de Pandas EDA

    ##Pasos clave
    1. df.info() para ver tipos de campos y valores faltantes
    2. df.describe() descripción estadística
    ...
    También puedes cargarlo manualmente en la conversación con /pandas-eda.


## Subagentes (Subagents)

Define subagentes especializados en ./subagent/nombre_rol/AGENT.md, el agente principal puede delegar tareas mediante la herramienta agent.

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

Coloca en ./hooks/ los archivos 
- PreToolUse-*.sh
- PostToolUse-*.sh
- Stop-*.sh
que reciben entrada JSON y devuelven una decisión:

bash

    #!/bin/bash

    #PreToolUse-guard.sh

    read -r input

    if echo "$input" | grep -q "rm -rf"; then

    echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Prohibido eliminar"}}'

    fi

Los hooks de Python pueden llamar directamente a la API integrada (ver las funciones hook_* en Baize.py).


## Servidor MCP

Configura servidores de herramientas externos en ./MCP/mcp_config.json:

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

- **Lista blanca de comandos**: solo permite comandos comunes como ls, cat, grep, git, python3.

- **Detección de escape de rutas**: todas las operaciones de archivos se limitan al directorio de trabajo actual y /tmp.

- **Bloqueo de comandos peligrosos**: bloquea patrones como rm -rf /, fork bomb, curl | sh, git push --force.

- **Protección de archivos sensibles**: prohíbe modificar .env, .ssh/, id_rsa, *.pem, etc.

- **Bloqueo de inyección de scripts**: detecta bypasses como python -c "os.system(...)".

- **Límites de recursos del proceso**: en Linux/macOS limita CPU, memoria y número de procesos.

Si necesitas relajar las restricciones en proyectos de confianza, modifica ALLOWED_COMMANDS y FORBIDDEN_PATH_PATTERNS en Baize.py.


# Estructura de directorios
text

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
        |   └── history.py          # Limpieza de historial / estimación de tokens / compresión
        ├── hooks/                  # Hooks integrados
        └── MCP/                    # Cliente MCP y configuración
            ├── __init__.py
            ├── mcp_client.py
            └── mcp_config.json


# Referencia de variables de entorno
		
- Variable: DEEPSEEK_API_KEY  Descripción: API de DeepSeek  Valor por defecto: clave	—

- Variable: DEEPSEEK_BASE_URL  Descripción: Dirección de la interfaz de DeepSeek  Valor por defecto: https://api.deepseek.com

- Variable: OPENAI_API_KEY  Descripción: OpenAI  Valor por defecto: clave de interfaz compatible	—

- Variable: OPENAI_BASE_URL	 Descripción: Dirección de interfaz compatible con OpenAI	 Valor por defecto: https://api.openai.com/v1

- Variable: OLLAMA_BASE_URL	 Descripción: Dirección del servicio Ollama	 Valor por defecto: http://localhost:11434

Escribe las variables en ~/.baize/.env, no es necesario modificar los archivos de configuración del shell.


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

R: En ~/.baize/.env, no en el .env del directorio raíz del proyecto.

- P: ¿Debo reinstalar si cambio de backend?

R: No. Solo modifica active_provider en ~/.baize/config.toml.

- P: ¿Ollama local necesita clave?

R: No. Selecciona active_provider = "ollama", deja env_key vacío.

- P: ¿Cómo cambio el directorio de trabajo?

R: En la conversación di directamente "cambiar a /path/to/project", Baize llamará a la herramienta set_workspace.

- P: ¿Qué pasa si el contexto es demasiado largo?

R: Baize comprime automáticamente en dos niveles: primero trunca resultados antiguos de herramientas, luego solicita al LLM que genere un resumen. También puedes usar /compact manualmente.

- P: ¿Podría borrar mis archivos por error?

R: La lista blanca de comandos por defecto bloquea operaciones peligrosas como rm -rf /; antes de escribir archivos muestra el Diff y solicita confirmación.

# 🤝 Contribuir
Se aceptan Issues y PRs. Se recomienda leer primero la función agent_loop en Baize.py para entender el bucle principal del Agente antes de extenderlo.
### Gracias a todos los Contribuidores que envían PR
- Github Contributor：
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