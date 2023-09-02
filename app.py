from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return render_template('index.html')


@app.route('/<string:page_num>')
def direct_page(page_num):  # put application's code here
    return render_template(page_num)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        database2(data)
        return redirect('/thank_you.html')
    else:
        return 'something went wrong please try again'


def database(data):
    name = data['Your Name']
    email = data['Your Email']
    subject = data['Subject']
    message = data['Message']

    with open('database.txt', 'a') as data_base:
        data_base.write(f'\n Name = {name}\n Email = {email}\n Subject = {subject}\n Message = {message}\n')


def database2(data):
    name = data['Your Name']
    email = data['Your Email']
    subject = data['Subject']
    message = data['Message']

    with open('database.csv', mode='a', newline='') as data_base2:
        csv_file = csv.writer(data_base2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([name, email, subject, message])


if __name__ == '__main__':
    app.run()
