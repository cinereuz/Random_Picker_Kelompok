# app.py

from flask import Flask, render_template, request
import random
from data import class_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_class = request.form.get('class')
        division_type = request.form.get('division_type')

        if selected_class in class_data and division_type in ['mixed', 'male', 'female']:
            students = class_data[selected_class][division_type]
            random.shuffle(students)

            num_students = len(students)
            num_groups = int(request.form.get('group_size'))

            group_size = num_students // num_groups
            remaining_students = num_students % num_groups

            groups = []
            start = 0
            for i in range(num_groups):
                end = start + group_size
                if remaining_students > 0:
                    end += 1
                    remaining_students -= 1
                group = students[start:end]
                groups.append(group)
                start = end

            return render_template('result.html', groups=groups)
    
    return render_template('index.html', classes=class_data.keys())

if __name__ == '__main__':
    app.run(debug=True)
