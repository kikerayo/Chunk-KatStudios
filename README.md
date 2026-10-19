# Chunk — KatStudios

Juego indie de bloques creado por **KatStudios**. Nuestro objetivo: escuchar a la comunidad y construir el juego juntos.

- [Descargar Chunk para Windows](https://github.com/kikerayo/Chunk-KatStudios/releases/latest/download/Chunk-Windows-x64.zip)
- [Última release](https://github.com/kikerayo/Chunk-KatStudios/releases/latest)
- [Manifiesto de actualizaciones](https://raw.githubusercontent.com/kikerayo/Chunk-KatStudios/main/updates/stable.json)
- [Integración con KatLauncher](docs/KatLauncher.md)

Extrae el ZIP y abre `Chunk_Publica/Chunk_Publica.exe`. Chunk consulta este repositorio, verifica SHA-256 y prepara las actualizaciones en segundo plano. Las aplica al cerrar, conservando mundos, configuración, personalización y mods. Puedes desactivarlas en **Actualizaciones** dentro del menú principal. La primera instalación de una versión antigua requiere instalar la build con actualizador una vez.

## Publicar una actualización

1. Cambia `VERSION` y/o aumenta `BUILD` en `chunk_updates.py` antes de compilar. La compilación debe crecer también en hotfixes que mantengan la misma versión visible.
2. Compila el juego y genera el ZIP público completo, con `chunk-release.json` en su raíz `Chunk_Publica`.
3. Ejecuta `python tools/publish.py ruta/al/Chunk_Publica.zip` usando tu sesión de GitHub en Git o `GITHUB_TOKEN`. El script comprueba el contenido, publica la release, calcula SHA-256 y actualiza el manifiesto al final.

No se publican la edición privada, mundos personales ni credenciales. Este repositorio distribuye builds públicas y metadatos; no implica una licencia de código abierto para el juego o sus recursos.

Chunk es un proyecto independiente, no oficial ni afiliado a Mojang o Microsoft. Los derechos correspondientes a Minecraft y sus recursos pertenecen a sus titulares. Este proyecto no busca insultar ni hacer quedar mal a Mojang; se creó por diversión.
