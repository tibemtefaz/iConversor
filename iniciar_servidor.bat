@echo off

:: Puerto en el que deseas ejecutar el servidor
set PUERTO=8000

:: Verifica si hay un proceso en ejecución en el puerto especificado y lo detiene
for /f "tokens=5" %%a in ('netstat -aon ^| findstr /c":%PUERTO%" ^| find "LISTENING"') do (
    echo Cerrando el servidor en el puerto %PUERTO%...
    taskkill /F /PID %%a > nul
)

:: Ruta al directorio donde se encuentran tus archivos
set DIRECTORIO=%~dp0

:: Navega al directorio
cd /d %DIRECTORIO% || exit /b

:: Inicia el servidor web en segundo plano
echo Iniciando el servidor de traducción...
start /B python src/traductor.py

:: Espera un segundo para asegurarse de que el servidor esté en funcionamiento
timeout /t 1 /nobreak > nul

:: Abre el navegador web predeterminado para acceder al servidor
start http://localhost:%PUERTO%/

echo Servidor iniciado correctamente en http://localhost:%PUERTO%/
echo Presiona Ctrl+C en la ventana del servidor para detenerlo cuando termines.
