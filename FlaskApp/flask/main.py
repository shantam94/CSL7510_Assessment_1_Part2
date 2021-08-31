from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employees',methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        data = pd.read_csv('employees.csv')
        cols = ['FIRST_NAME', 'HIRE_DATE', 'EMAIL']
        data = data[cols]
        data = data.sample(10)
        data = data.T.to_dict().values()
        print(data)

    return render_template('employees.html', employees=data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
