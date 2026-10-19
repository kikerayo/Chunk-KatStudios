# Chunk 1.0.3 — Crónicas de los Siete (build 2026101903)

- Historia completa del bibliotecario y Pausa > Historia: origen del Player, nombres de los siete, reglas alteradas, Infernales, oscuros, confianza y dimensión de papa.
- Después de vencer al dragón, clic derecho en el bloque azul de Comunicación bajo un templo del Aether > Desafiar a los Siete Estelares. Siete fases consecutivas: Jared, Craf, Joky, Doshhy, Pluto, Helso y Transto. Sus cuerpos toman tu skin morada. Esquiva el círculo rojo anunciado; solo reciben golpes y flechas cuando se acuestan. Salir del área o morir pausa el combate; guarda la vida/fase y continúa al volver. No destruye construcciones.
- Ayuda infernal: clic derecho con mano vacía a un oscuro y entrega 3 lingotes de hierro + 2 chuletas cocinadas en tres días diferentes. Estas tareas de abastecimiento son la forma jugable de ayudar a los refugios, no un tributo de los dioses. Ya aliados, los oscuros se apartan por tu olor y ocasionalmente regalan comida o minerales.
- Los oscuros llevan un bloque rojo visible en el pecho. Sobreviven a las caídas del Aether y regresan al refugio; el rayo infernal afecta a los Templarios claros.
- Tras ganar, los claros tiemblan; después de tres días se calman gradualmente y a los seis confían en ti. Buscan recursos naturales cercanos o cultivos maduros, los recogen para ti y esperan si tu inventario está lleno. Puedes encargar un casco con cinco lingotes: lo fabrican y entregan tras 45 segundos. No extraen bloques colocados por el jugador. Trabajan en zonas cargadas; no simulan tareas fuera de ellas.
- Tras ganar, habla con mano vacía con un oscuro: puedes dejarlo con los Infernales o curarlo con manzana dorada normal + lágrima de Ghast. La cura quita su bloque rojo. La decisión de dejarlo protegido permite volver a curarlo después.
- Relación opcional: después de seis días de confianza, habla con mano vacía con el mismo guardián en tres días diferentes y acepta ser pareja. Personaje hombre: Templaria; personaje mujer: Templario. Abrazo/beso con gesto y corazón. No se fuerza una relación al ganar.
- Campaña, salud de la fase, amistad, encargos, curas y relación persisten al guardar, cargar y cambiar de dimensión. LAN: decisiones y conversaciones de campaña en la PC anfitriona; invitados ven las fases y participan en la batalla con daño validado por el anfitrión. Ambos equipos deben actualizar.
- Se conservan las texturas existentes, inventarios, mundo y mecánicas independientes, incluido B frente a la invocación por estatua. No hay modelos ni assets externos nuevos: los cuerpos usan skins locales; los indicadores se dibujan en el juego.

Las donaciones, receta de cura, duración de confianza y detalles del combate son una adaptación jugable del lore de Oliver. Los Infernales son amigables y no exigen servidumbre. El bloque rojo es soporte vital; el azul transmite profecías Estelares.


---

# Corrección visual 1.0.3 · build 2026101902

Botones con colores y bordes propios de Minecraft en todos los paneles, independientes del tema del escritorio. Paleta explícita y estilo Fusion; pestañas, listas, campos y botones predeterminados conservan el contraste. Debug dibuja tierra también dentro de las páginas desplazables. Se evita que el selector genérico QWidget imponga fondo transparente a los botones. Verificado nativamente con esquemas claro y oscuro y con los botones del menú principal y de los diálogos.


---

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
