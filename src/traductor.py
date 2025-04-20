"""
Servidor HTTP para la aplicación "Traductor de Vocales a 'i'"
=============================================================

Este módulo implementa un servidor HTTP simple que:
1. Sirve archivos estáticos (HTML, CSS, JavaScript)
2. Procesa peticiones para traducir texto (reemplazando vocales por 'i')

El servidor escucha en el puerto 8000 por defecto y responde a:
- GET: Para servir los archivos estáticos
- POST: Para recibir texto, traducirlo y devolver el resultado en formato JSON
- OPTIONS: Para habilitar CORS (Cross-Origin Resource Sharing)

Autor: Pablo
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import sys

class RequestHandler(BaseHTTPRequestHandler):
    """
    Controlador de peticiones HTTP.
    Maneja las peticiones GET, POST y OPTIONS.
    """
    
    def do_OPTIONS(self):
        """
        Maneja peticiones OPTIONS para permitir CORS.
        Esto es necesario para que el navegador permita peticiones desde diferentes dominios.
        """
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "http://localhost:8000")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        """
        Maneja las peticiones GET para servir archivos estáticos.
        
        El flujo de esta función es:
        1. Si la URL es "/", sirve index.html
        2. Construye la ruta del archivo solicitado
        3. Verifica si el archivo existe
        4. Determina el tipo de contenido según la extensión
        5. Envía el archivo como respuesta
        """
        try:
            # Si la URL es la raíz, entregar index.html
            if self.path == '/':
                self.path = '/index.html'
                
            # Determinar la ruta del archivo estático
            # Nota: __file__ es la ubicación del archivo actual (traductor.py)
            # os.path.dirname obtiene el directorio padre (primero src/, luego el raíz)
            file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                    "static", 
                                    self.path.lstrip('/'))
            
            # Verificar si el archivo existe
            if not os.path.isfile(file_path):
                self.send_error(404, 'Archivo no encontrado')
                return
                
            # Determinar el tipo de contenido según la extensión
            content_type = 'text/html'  # Por defecto
            if self.path.endswith('.css'):
                content_type = 'text/css'
            elif self.path.endswith('.js'):
                content_type = 'application/javascript'
            
            # Enviar respuesta HTTP 200 (OK)
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            
            # Leer y enviar el archivo como bytes
            with open(file_path, 'rb') as file:
                self.wfile.write(file.read())
                
        except Exception as e:
            # En caso de error, enviar código 500
            self.send_error(500, str(e))

    def do_POST(self):
        """
        Procesa una petición POST para traducir texto.
        
        El flujo de esta función es:
        1. Leer los datos JSON enviados en la petición
        2. Extraer el texto a traducir
        3. Llamar a la función que implementa la traducción
        4. Devolver el resultado en formato JSON
        """
        try:
            print("Petición POST recibida")
            
            # Obtener la longitud del contenido de la petición
            content_length = int(self.headers['Content-Length'])
            
            # Leer los datos de la petición
            post_data = self.rfile.read(content_length)
            
            # Convertir de JSON a diccionario Python
            data = json.loads(post_data.decode('utf-8'))
            
            # Extraer el texto a traducir
            text = data['text']
            print("Texto recibido: " + text)
            
            # Traducir el texto (reemplazar vocales por 'i')
            translated_text = self._traducir_texto(text)
            print("Texto traducido: " + translated_text)
            
            # Preparar respuesta
            response = {'translated_text': translated_text}
            
            # Enviar respuesta HTTP 200 (OK)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            
            # Configurar CORS para permitir la comunicación
            self.send_header("Access-Control-Allow-Origin", "http://localhost:8000")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()
            
            # Enviar el JSON con el resultado
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
        except Exception as e:
            # En caso de error, enviar código 500
            self.send_error(500, str(e))
    
    def _traducir_texto(self, texto):
        """
        Reemplaza todas las vocales del texto por la letra 'i'.
        
        Args:
            texto (str): El texto a traducir
            
        Returns:
            str: El texto con las vocales reemplazadas por 'i'
        """
        return texto.replace('a', 'i').replace('e', 'i').replace('o', 'i').replace('u', 'i')

def iniciar_servidor(puerto=8000):
    """
    Inicia el servidor HTTP en el puerto especificado.
    
    Args:
        puerto (int): Puerto en el que escuchará el servidor (por defecto 8000)
    """
    try:
        # Configurar dirección del servidor ('' significa todas las interfaces)
        server_address = ('', puerto)
        
        # Crear instancia del servidor HTTP
        httpd = HTTPServer(server_address, RequestHandler)
        
        # Mostrar información de inicio
        print(f'Iniciando servidor HTTP en el puerto {puerto}...')
        print(f'Accede a http://localhost:{puerto}/ en tu navegador')
        
        # Iniciar el servidor (bucle infinito)
        httpd.serve_forever()
    
    except KeyboardInterrupt:
        # Manejar la interrupción con Ctrl+C
        print("\nServidor detenido")
        httpd.server_close()
        sys.exit(0)
    
    except Exception as e:
        # Manejar otros errores
        print(f"Error al iniciar el servidor: {e}")
        sys.exit(1)

# Punto de entrada principal
if __name__ == '__main__':
    iniciar_servidor() 