from core.settings import database_url
import db.models.models

models = ['aerich.models', 'db.models']


TORTOISE_ORM = {
    'connections': {'default': database_url},
    'apps': {
        'models': {
            'models': models,
            'default_connection': 'default',
        },
    },
}