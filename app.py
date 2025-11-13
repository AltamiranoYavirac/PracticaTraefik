from flask import Flask

# 1. Inicializa la aplicación Flask
app = Flask(__name__)

# 2. Define la ruta para la página principal ("/")
@app.route('/')
def pagina_principal():
    
    # 3. Define el contenido HTML como un string de Python
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Página Principal</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                display: grid;
                place-items: center;
                min-height: 100vh;
                background-color: #f4f4f4;
                margin: 0;
            }
            .content {
                text-align: center;
                border: 1px solid #ddd;
                padding: 2rem 4rem;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            h1 { color: #2c3e50; }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>¡Bienvenido a mi Página Principal!</h1>
            <p>Este HTML se está sirviendo directamente desde Flask.</p>
        </div>
    </body>
    </html>
    """
    
    # 4. Retorna el HTML
    return html_content

# 5. Inicia el servidor si este script es ejecutado directamente
if __name__ == '__main__':
    # debug=True hace que el servidor se reinicie automáticamente con los cambios
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)