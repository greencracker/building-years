from flask_frozen import Freezer
from app import app, get_csv
freezer = Freezer(app)

# @freezer.register_generator
# def detail():
#     for row in get_csv():
#         yield {'row_id': row['id']}

if __name__ == '__main__':
	app.config.update(FREEZER_RELATIVE_URLS=True)
	freezer.freeze()