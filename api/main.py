from fastapi import FastAPI
from api.utils.custom_http_response import CustomHTTPException, http_exception_handler
from api.routers import categories, locations, location_category_reviewed, recommendation

app = FastAPI(
    title="API orbidi",
    description="Orbidi API",
    version="1.0.0"
)

# Manejador de excepciones personalizado
app.add_exception_handler(CustomHTTPException, http_exception_handler)

# Registro de routers
app.include_router(categories.router)
app.include_router(locations.router)
app.include_router(location_category_reviewed.router)
app.include_router(recommendation.router)

# Ruta principal de bienvenida
@app.get("/")
async def home():
    """
    Handler for the home route ("/") that returns a simple greeting message.

    Returns:
        str: A plain text message indicating the purpose of the application.
    """
    return "orbidi APIs"

