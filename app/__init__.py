from flask_restx import Api
from app.main import app
from app.main.controllers.person import person

api = Api(
    app,
    version='0.1',
    title="EMR DATA API Server",
    description="Hwi's EMR DATA API Server!",
    terms_url="/",
    contact="songhwee1@naver.com",
)

api.add_namespace(person, '/person')