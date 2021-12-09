from flask import Flask, render_template, request, redirect, url_for, session
from flask.helpers import flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import bcrypt
from datetime import datetime

app = Flask(__name__)
#index
@app.route('/home')
def home():
    return render_template('home.html')


#Food pages
@app.route('/food')
def food():
    return render_template('food_all/food_page1.html')

@app.route('/food_page2')
def food_page2():
    return render_template('food_all/food_page2.html')

@app.route('/food_page3')
def food_page3():
    return render_template('food_all/food_page3.html')

@app.route('/food_page4')
def food_page4():
    return render_template('food_all/food_page4.html')

@app.route('/food_page5')
def food_page5():
    return render_template('food_all/food_page5.html')


#munu page

@app.route("/กระเพาอกไก่")
def menu_1():
    return render_template('food_all/food_menu/menu_1.html')

@app.route("/แกงจืดตำลึงหมูสับ")
def menu_2():
    return render_template('food_all/food_menu/menu_2.html')

@app.route("/ต้มข่าอกไก่")
def menu_3():
    return render_template('food_all/food_menu/menu_3.html')

@app.route("/แกงเหลืองสับปะรด")
def menu_4():
    return render_template('food_all/food_menu/menu_4.html')

@app.route("/ซุบหน่อไม้")
def menu_5():
    return render_template('food_all/food_menu/menu_5.html')

@app.route("/แกงเลียง")
def menu_6():
    return render_template('food_all/food_menu/menu_6.html')

@app.route("/ส้มตำผลไม้")
def menu_7():
    return render_template('food_all/food_menu/menu_7.html')

@app.route("/ห่อหมกปลาดอรี่")
def menu_8():
    return render_template('food_all/food_menu/menu_8.html')

@app.route("/น้ำพริกอ่องอกไก่")
def menu_9():
    return render_template('food_all/food_menu/menu_9.html')

@app.route("/อกไก่คั่วพริกแกง")
def menu_10():
    return render_template('food_all/food_menu/menu_10.html')





# Exercise 
@app.route('/exercise')
def excercise_page1():
    return render_template('exercise_all/exercise_page1.html')

@app.route('/exercise_page2')
def exercise_page2():
    return render_template('exercise_all/exercise_page2.html')

@app.route('/exercise_page3')
def exercise_page3():
    return render_template('exercise_all/exercise_page3.html')

# Exercise set
@app.route('/ออกกำลังกายต้นเเขน')
def exercise_set1():
    return render_template('exercise_all/exercise_set/exercise_set1.html')

@app.route('/ออกกำลังกายหน้าท้อง')
def exercise_set2():
    return render_template('exercise_all/exercise_set/exercise_set2.html')


@app.route('/ออกกำลังกายต้นขา')
def exercise_set3():
    return render_template('exercise_all/exercise_set/exercise_set3.html')



@app.route('/ออกกำลังกายต้นเเขน4')
def exercise_set4():
    return render_template('exercise_all/exercise_set/exercise_set4.html')



@app.route('/check_bmi' , methods=['POST','GET'])
def check():
    show_bmi = '0.00'
    message = 'กรอกข้อมูลของท่าน'
    if request.method=="POST" and "input-1" in request.form and 'input-2' in request.form:
        weight = float(request.form['input-1'])
        height = float(request.form['input-2'])
        show_bmi = weight/((height/100)*2)
        show_bmi = '%.2f' %show_bmi

        if float(show_bmi) >= 30:
            message = 'อ้วนระดับ2'
        elif float(show_bmi) >= 25.0 and float(show_bmi) < 30:
            message = 'อ้วนระดับ1'
        elif float(show_bmi) >= 23.0 and float(show_bmi) < 25:
            message = 'น้ำหนักเกิน'
        elif float(show_bmi) >= 18.5 and float(show_bmi) < 23:
            message = 'น้ำหนักตัวปกติ'
        elif float(show_bmi) < 18.5:
            message = 'น้ำหนักตัวน้อย'
        else:
            message = 'Erorr'
    return render_template('check_bmi.html', show_bmi=show_bmi , message=message)









if __name__=="__main__":
    app.run(debug=True)


