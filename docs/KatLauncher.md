# Integración de Chunk en KatLauncher

Estudio: **KatStudios**. Plataforma disponible: Windows x64.

URL fija del manifiesto:

`https://raw.githubusercontent.com/kikerayo/Chunk-KatStudios/main/updates/stable.json`

## Contrato JSON (schema_version = 1)

- `game_id`: `chunk`.
- `version`: versión visible, con 2–4 componentes numéricos.
- `build`: entero de compilación. Comparar primero versión numérica y después build; puede haber hotfixes con la misma versión.
- `studio`: `KatStudios`.
- `channel`: `stable`.
- `release_url`: página pública de la release.
- `platforms.windows-x64.url`: descarga HTTPS del ZIP completo de esa release.
- `platforms.windows-x64.sha256`: hash hexadecimal SHA-256 del ZIP.
- `platforms.windows-x64.size`: bytes exactos del ZIP.
- `platforms.windows-x64.archive_root`: `Chunk_Publica`.
- `platforms.windows-x64.executable`: `Chunk_Publica.exe`.

## Instalar y abrir

1. Descargar y verificar tamaño + SHA-256 antes de extraer.
2. Rechazar rutas absolutas, enlaces simbólicos, unidades, `..` y archivos duplicados en el ZIP.
3. Extraer `Chunk_Publica` en una carpeta dedicada del launcher.
4. Ejecutar `Chunk_Publica.exe` con esa carpeta como directorio de trabajo.
5. Leer `chunk-release.json` en esa carpeta para detectar versión/build instalada.

## Actualizar sin perder datos

No reemplazar instalaciones mientras Chunk está abierto. Conservar `mundos`, `personalizacion`, `mods`, archivos de configuración y cualquier dato del usuario. El actualizador de Chunk administra únicamente el ejecutable, `_internal/` y la documentación/metadatos que distribuye la release; conserva una copia para revertir errores durante la copia.

Si KatLauncher administra las actualizaciones, puede guardar `{"repo":"kikerayo/Chunk-KatStudios","automaticas":false}` en `actualizaciones.json` de la instalación para evitar que ambos actualicen a la vez. Esta preferencia también es editable dentro del juego.

Descarga cómoda para una primera instalación: `https://github.com/kikerayo/Chunk-KatStudios/releases/latest/download/Chunk-Windows-x64.zip`. Para actualizar y comprobar integridad usar siempre el ZIP exacto y el hash del manifiesto.
