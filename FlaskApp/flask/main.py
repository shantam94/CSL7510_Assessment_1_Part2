from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employees',methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # connection = sql.connect(
        #                         host = '192.168.100.5',
        #                         user = 'shantam',
        #                         password = '123',
        #                         port = '3306',
        #                         auth_plugin = 'mysql_native_password',
        #                         database = 'DEMO_DB'
        #                         )
        # query = 'SELECT * from EMPLOYEES'

        # with connection.cursor() as cursor:
        #     cursor.execute(query)
        #     res = cursor.fetchall()
        #     final = []
        #     for row in res:
        #         record = {
        #             'name': row[0],
        #             'year_of_join' : row[1],
        #             'city' : row[2]
        #         }
        #         final.append(record)
        data = pd.read_csv('employees.csv')
        cols = ['FIRST_NAME', 'HIRE_DATE', 'EMAIL']
        data = data[cols]
        data = data.sample(10)
        data = data.T.to_dict().values()
        print(data)

    return render_template('employees.html', employees=data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)