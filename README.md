# iConversor

Una aplicación web minimalista que traduce texto reemplazando las vocales por la letra 'i'. Desarrollada con Python (servidor HTTP) y HTML/CSS/JavaScript (interfaz de usuario), demostrando una arquitectura cliente-servidor simple y efectiva.

## Características principales

🔄 Traducción instantánea de texto  
🌐 Servidor web Python nativo sin frameworks externos  
📱 Interfaz responsive con diseño moderno  
📊 Diagrama de arquitectura incluido  
🔌 Base para integración con Maya y Unreal Engine  

## Estructura del Proyecto

```
iConversor/
├── static/               # Archivos estáticos (Frontend)
│   ├── index.html        # Estructura HTML de la interfaz
│   ├── styles.css        # Estilos CSS de la aplicación
│   ├── app.js            # Lógica JavaScript del cliente
│   └── arquitectura.html # Diagrama explicativo de la arquitectura
├── src/                  # Código fuente Python (Backend)
│   └── traductor.py      # Servidor HTTP y lógica de traducción
├── iniciar_servidor.bat  # Script para iniciar el servidor en Windows
└── README.md             # Este archivo de documentación
```

## Requisitos

- Python 3.6 o superior
- Navegador web moderno (Chrome, Firefox, Edge, etc.)

## Cómo usar

1. Ejecuta el archivo `iniciar_servidor.bat` haciendo doble clic sobre él.
2. Se abrirá automáticamente tu navegador web predeterminado con la aplicación.
3. Introduce el texto que deseas traducir y pulsa el botón "Traducir".
4. El resultado aparecerá inmediatamente en el panel derecho.
5. Para ver el diagrama de arquitectura, haz clic en el enlace "Ver diagrama de arquitectura" en la parte inferior de la página.

## Funcionamiento Técnico

La aplicación sigue una arquitectura cliente-servidor simple:

### Backend (Python)

- El archivo `src/traductor.py` implementa:
  - Un servidor HTTP utilizando el módulo `http.server` de Python
  - Manejo de peticiones GET para servir archivos estáticos
  - Manejo de peticiones POST para procesar texto y devolverlo traducido
  - Configuración CORS para permitir peticiones desde cualquier origen

### Frontend (HTML/CSS/JavaScript)

- `static/index.html`: Define la estructura de la página
- `static/styles.css`: Implementa los estilos visuales
- `static/app.js`: Contiene la lógica del cliente para:
  - Capturar el texto introducido
  - Enviarlo al servidor mediante una petición AJAX
  - Recibir la respuesta y mostrarla en la interfaz

### Flujo de datos

1. El usuario escribe texto en el panel izquierdo
2. Al hacer clic en "Traducir", JavaScript captura el texto
3. Se envía una petición POST con los datos en formato JSON
4. El servidor recibe la petición, extrae el texto y lo traduce
5. El servidor devuelve la respuesta en formato JSON
6. JavaScript recibe la respuesta y muestra el resultado en el panel derecho

## Documentación de Código

Cada archivo contiene comentarios detallados explicando su funcionamiento:

- `traductor.py`: Incluye docstrings completos para cada clase y método
- `app.js`: Contiene comentarios explicando el flujo de ejecución
- `arquitectura.html`: Proporciona un diagrama visual de la arquitectura y flujo de datos

## Posibles Extensiones

Este proyecto puede servir como base para:

1. Implementar otros tipos de transformaciones de texto
2. Añadir más funcionalidades (historial de traducciones, exportar resultados)
3. Conectar con APIs externas o herramientas como Maya o Unreal Engine
4. Implementar autenticación de usuarios

## Detener el servidor

Para detener el servidor, cierra la ventana de comando que se abrió al ejecutar el archivo .bat o presiona Ctrl+C en dicha ventana. 