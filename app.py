from flask import Flask, redirect, render_template, request
import data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if '_create' in request.form:
            name = request.form.get('text')
            data.create_list_item(name)
        elif '_complete' in request.form:
            print(request.form)
            formKeys = list(request.form.keys())
            formKeys.remove('_complete')
            data.toggle_list_item(formKeys[0])
        return redirect('/')
    items = data.get_list_items()
    print(items)
    completed_items = [item for item in items if item[2] == 0]
    incomplete_items = [item for item in items if item[2] == 1]
    return render_template('index.html', completed_items=completed_items, incomplete_items=incomplete_items)

if __name__ == '__main__':
    data.init()
    app.run(debug=True, host="0.0.0.0")
