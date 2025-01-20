import requests
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from config import API_URL, X_WHATSAPP_TOKEN, TITLE, DESCRIPTION

app = FastAPI(
    title=TITLE,
    description=DESCRIPTION
)


@app.get('/')
def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url='/docs')


@app.get("/tariffs")
def get_tariffs(currency='RUB', crm='lk'):
    """Получение тарифов из внешнего API."""
    headers = {'X-Whatsapp-Token': X_WHATSAPP_TOKEN}
    params = {'currency': currency, 'crm': crm}
    response = requests.get(url=API_URL, headers=headers, params=params)
    return response.json()
