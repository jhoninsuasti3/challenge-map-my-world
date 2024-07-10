from fastapi import FastAPI
from api.utils.custom_http_response import CustomHTTPException, http_exception_handler
from api.routers import categories, locations, recommendations  # Importa tus módulos de rutas aquí

app = FastAPI(
    title="API ordibi",
    description="Ordibi API",
    version="1.0.0"
)

# Manejador de excepciones personalizado
app.add_exception_handler(CustomHTTPException, http_exception_handler)

# Registra tus routers aquí
app.include_router(categories.router)
app.include_router(locations.router)
app.include_router(recommendations.router)

# Ruta principal de bienvenida
@app.get("/")
async def home():
    """
    Handler for the home route ("/") that returns a simple greeting message.

    Returns:
        str: A plain text message indicating the purpose of the application.
    """
    return "ordibi APIs"

