/**
 * app.js - Lógica del cliente para el Traductor de Vocales
 * -----------------------------------------------------
 * Este archivo contiene toda la lógica del lado del cliente para:
 * 1. Capturar el texto introducido por el usuario
 * 2. Enviarlo al servidor mediante una petición AJAX
 * 3. Recibir y mostrar la respuesta del servidor
 */

/**
 * Función principal para traducir el texto ingresado
 * 
 * Flujo de ejecución:
 * 1. Obtiene el texto del campo de entrada
 * 2. Valida que no esté vacío
 * 3. Muestra indicador de carga
 * 4. Envía petición POST al servidor con el texto
 * 5. Recibe la respuesta y actualiza la interfaz
 */
function traducir() {
    // Obtener el texto del campo de entrada
    const inputText = document.getElementById("inputText").value;
    
    // Validar que el texto no esté vacío
    if (!inputText.trim()) {
        alert("Por favor, introduce un texto para traducir");
        return;
    }
    
    // Mostrar indicador de carga y ocultar mensajes de error
    document.getElementById("loading").style.display = "block";
    document.getElementById("error").style.display = "none";
    
    // Preparar los datos para enviar al servidor (formato JSON)
    const data = { text: inputText };

    // Realizar petición POST al servidor (endpoint raíz '/')
    fetch("/", {
        method: "POST",                       // Método HTTP
        body: JSON.stringify(data),           // Convertir objeto a JSON
        headers: {
            "Content-Type": "application/json" // Tipo de contenido
        }
    })
    .then(response => {
        // Verificar si la respuesta del servidor es correcta
        if (!response.ok) {
            throw new Error("Error en la respuesta del servidor: " + response.status);
        }
        // Convertir la respuesta a JSON
        return response.json();
    })
    .then(data => {
        // Procesar datos recibidos del servidor
        
        // Ocultar indicador de carga
        document.getElementById("loading").style.display = "none";
        
        // Mostrar el texto traducido en el elemento de resultado
        document.getElementById("outputText").textContent = data.translated_text;
    })
    .catch(error => {
        // Manejar cualquier error que ocurra durante la petición
        console.error("Error:", error);
        
        // Ocultar indicador de carga y mostrar mensaje de error
        document.getElementById("loading").style.display = "none";
        document.getElementById("error").style.display = "block";
    });
}

/**
 * Inicializa los event listeners cuando se carga la página
 * 
 * Esta función configura:
 * - El evento de clic en el botón de traducir
 * - El evento de presionar Enter en el campo de texto
 */
function inicializarEventos() {
    // Configurar evento para traducir al presionar Enter 
    // (pero permitir saltos de línea con Shift+Enter)
    document.getElementById("inputText").addEventListener("keypress", function(event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();   // Prevenir el comportamiento por defecto
            traducir();               // Llamar a la función de traducción
        }
    });
    
    // Configurar evento de clic en el botón de traducir
    document.getElementById("translateBtn").addEventListener("click", traducir);
}

// Ejecutar la inicialización cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", inicializarEventos); 