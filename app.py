from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask('__main__') # Flask Bağlantısı

try:  # MongoDb'ye bağlanma ve koleksiyona erişme
    conn = MongoClient()
    db = conn.employees
    employees = db.employees
    print("Successfull connection!")
except ConnectionError:
    print("Db connection failed!")



@app.route('/', methods=['GET'])
def WelcomePage():
    return "Welcome!"     

@app.route('/get_data', methods=['GET','POST'])
def GetData():
    if request.method == 'POST': #html üzerinden gönderilen post isteklerini alıyor.
        employees.insert_one({'name': request.form['name'].capitalize().strip(), 
                              'email': request.form['email'].lower().strip(), 
                              'phonenumber' : request.form['phonenumber'].strip(), 
                              'birthdate' : request.form['birthdate'], 
                              'workdate' : request.form['workdate']})
    return render_template('getdata.html') #verileri girmek için oluşturulan arayüzü ekrana yazdırıyor.
    
    
@app.route('/show_data', methods=['GET'])
def ShowData():
    return render_template('showdata.html', data = employees.find())  #verileri göstermek için oluşturulan arayüzü ekrana yazdırıyor.

if __name__ == '__main__':
    app.run(debug=True)
