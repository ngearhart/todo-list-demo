from flask import Flask, redirect, render_template, request
import data
import logging
# from flask_bootstrap import Bootstrap

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
# Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if '_create' in request.form:
            name = request.form.get('text')
            data.create_list_item(name)
        elif '_complete' in request.form:
            formKeys = list(request.form.keys())
            formKeys.remove('_complete')
            formKeys = [int(key) for key in formKeys]
            # FormKeys now holds all of the "checked" items
            items = data.get_list_items()
            for item in items:
                if item[0] in formKeys and item[2] == 0:
                    logger.info(f'Toggling {item[1]}')
                    data.toggle_list_item(item[0])
                elif item[0] not in formKeys and item[2] == 1:
                    logger.info(f'Toggling {item[1]}')
                    data.toggle_list_item(item[0])
        return redirect('/')
    items = data.get_list_items()
    logger.info(items)
    completed_items = [item for item in items if item[2] == 1]
    incomplete_items = [item for item in items if item[2] == 0]
    return render_template('index.html', completed_items=completed_items, incomplete_items=incomplete_items)

if __name__ == '__main__':
    data.init()
    app.run(debug=True)
