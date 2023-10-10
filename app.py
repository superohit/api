from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

employees = []

# appending pre data to showcase
employees.append({"name": "John", "position": "Software Engineer"})
employees.append({"name": "Rohan", "position": "Product Manager"})
employees.append({"name": "Mohan", "position": "Data Analyst"})

# GET method to render the HTML template
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', employees=employees)

# POST method to add employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    new_employee = {
        "name": request.form['name'],
        "position": request.form['position']
    }
    employees.append(new_employee)
    return render_template('index.html', employees=employees)

# DELETE method to remove employee
@app.route('/delete_employee/<int:employee_id>', methods=['GET'])
def delete_employee(employee_id):
    if employee_id < len(employees):
        employees.pop(employee_id)
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
