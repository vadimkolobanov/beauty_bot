from services.sql import DataBase

db = DataBase("db.sqlite3")

specialist_types = [
    {'ru': 'визажист', 'en': 'visagiste'},
    {'ru': 'парикмахер', 'en': 'barber'},
    {'ru': 'мастер маникюра', 'en': 'manicurist'},
    {'ru': 'косметолог', 'en': 'cosmetologist'},
    {'ru': 'мастер татуажа', 'en': 'tattoo_master'},
    {'ru': 'модель', 'en': 'model'},
    {'ru': 'стилист', 'en': 'stylist'},
    {'ru': 'перманентный макияж', 'en': 'permanent_makeup'},
    {'ru': 'лейшмейкер', 'en': 'lashmaker'},
    {'ru': 'бровист', 'en': 'eyebrower'},
    {'ru': 'дипиляция', 'en': 'depilation'}
]

