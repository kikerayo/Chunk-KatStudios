# Chunk 1.0.3 — Cultivos, oficios y caos en el Aether

- Semillas de calabaza y sandía, patatas, frutos y patatas asadas. Plantación, ocho etapas, agua, iluminación, polvo de hueso, recetas y cosecha. Los tallos producen frutos en terreno libre adyacente; no crean dos frutos mientras el anterior siga junto al tallo. Semillas en hierba, granjeros y cofres de aldeas nuevas.
- Pasto por manchas deterministas sin las franjas del patrón antiguo. Las hojas pueden sustituir hierba, evitando huecos junto a los árboles. No modifica bloques construidos por el jugador ni regenera aldeas sobre casas.
- 13 oficios con sus puestos: atril, compostador, mesa de flechas, herrería, cartografía, afiladora, telar, barril, soporte de pociones, cortapiedras, caldero, alto horno y ahumador. Aldeanos a ocho bloques reclaman un puesto libre y guardan su oficio al comerciar. Los nuevos puestos dan oficio; no incluyen todavía todos los procesos especializados de Minecraft (alquimia, patrones de estandartes, etc.).
- Partículas celestes acotadas alrededor de portales del Aether cercanos.
- Invocar un Wither en el Aether inicia una escena orbital de 5,2 segundos con siete haces, trueno y barras de cine. Esc la omite. Oculta HUD/manos y restaura el control. Cargar un Wither guardado no repite la escena. Challenge: **Desatando el caos en la paz**. La escena y el avance se comparten en LAN.
- Pausa → Logros: Avances y Challenges obtenidos, progreso por mundo y compatibilidad con avances ya guardados.
- Fondo de tierra en pausa y paneles generales, incluido debug; conserva las láminas originales de inventarios y las texturas existentes.
- Opciones → Resource packs: selector Disponibles / Seleccionados, prioridad, ZIP o carpeta Java, arrastrar y soltar, alerta experimental al importar y selección persistente. La primera textura de animaciones se importa; las animaciones especiales del motor conservan su comportamiento. Admite rutas block/item y los nombres plurales antiguos. Preserva los recursos originales; un pack parcial usa el respaldo integrado.
- **Compatibilidad experimental limitada a PNG de bloques e ítems del catálogo mapeado.** No interpreta modelos/blockstates JSON, shaders, fuentes, sonidos personalizados ni animaciones arbitrarias. Texturas hasta 64 px; se ajustan al límite de la GPU. Reinicia el juego para aplicar o quitar packs. Bedrock .mcpack no está soportado. Los modelos fijos especiales pueden conservar su textura original.

## Dimensión secreta de papa
Da una patata con clic derecho a un Templario claro y neutral del Aether. Te empuja al borde; una papa amortigua el descenso y atraviesas la capa del vacío. Esc omite la escena y entra directamente. El mundo secreto usa cielo turquesa, relieves, bosques y roca de papa. La imagen del usuario es el fondo de carga intacto.

Cosecha un bloque de papa: entrega entre 1 y 500 papas fritas y una patata. Las pilas se limitan a 64; el exceso queda como objetos recogibles. Patata + papas fritas en cualquier orden fabrica una **papa llave**. Úsala con clic derecho sobre un bloque de papa para volver al Aether. Hay una mesa de fabricación en la llegada. El avance se guarda, la posición de regreso es segura y guardar durante la escena no almacena al jugador bajo el mundo. En LAN, las dimensiones siguen siendo compartidas: un invitado puede activar el recorrido o usar la llave.

La textura de papas fritas del usuario se conserva byte por byte; el blanco exterior se oculta solo al dibujarla para evitar un recuadro en mano. Las imágenes previas se conservan. Nuevos IDs 222–224 y bloque 149, sin renumeraciones.

## Validación 1.0.3
Pruebas nativas Qt/OpenGL de plantación, crecimiento, cosecha, colisiones, recetas, oficios, persistencia JSON, partículas acotadas, cámara/cancelación y paneles. Pack Java real de prueba de 64 px aplicado a atlas e iconos; aviso experimental probado al cancelar y aceptar. Dos instancias por TCP local: nuevos cultivos, oficios, cinematic y challenge, además de regresiones de construcción, minería, hornos, portales y Templarios. 30 pulsaciones B siguen creando un solo Wither; la estatua conserva su invocación independiente. También se probaron la entrega real al Templario, repetición rápida, guardado durante la caída, entrada/salida, persistencia de la dimensión, premios exactos 1/500 y exceso con inventario lleno. El generador de chunks usa la nueva dimensión real, también en LAN. Los 504 archivos originales de texturas se compararon byte a byte contra 1.0.2.

## Referencias
- Formato de recursos Java: https://www.minecraft.net/en-us/article/minecraft-java-edition-1-19-3
- Cultivo de tallos y frutos: https://minecraft.wiki/w/Tutorial:Pumpkin_and_Melon_farming
