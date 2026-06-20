from flask import Flask, render_template, request, redirect
import boto3

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Students')

@app.route('/')
def home():
    response = table.scan()
    students = response.get('Items', [])
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    rollno = request.form['rollno']

    table.put_item(
        Item={
            'RollNo': rollno,
            'Name': name
        }
    )

    return redirect('/')

@app.route('/delete/<rollno>')
def delete_student(rollno):

    table.delete_item(
        Key={
            'RollNo': rollno
        }
    )

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)