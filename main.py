import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
from flask_mysqldb import MySQL
from pymysql.cursors import Cursor
from datetime import datetime



app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="comment"
)


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

@app.route("/ต้มยำเห็ดน้ำใส")
def menu_11():
    return render_template('food_all/food_menu/menu_11.html')

@app.route("/ผัดถั่วงอกเต้าหู้")
def menu_12():
    return render_template('food_all/food_menu/menu_12.html')

@app.route("/แกงจืดมะระยัดไส้")
def menu_13():
    return render_template('food_all/food_menu/menu_13.html')

@app.route("/ต้มเลือดหมู")
def menu_14():
    return render_template('food_all/food_menu/menu_14.html')

@app.route("/สลัดโรล")
def menu_15():
    return render_template('food_all/food_menu/menu_15.html')

@app.route("/ยำวุ้นเส้น")
def menu_16():
    return render_template('food_all/food_menu/menu_16.html')

@app.route("/ยำถั่วพู")
def menu_17():
    return render_template('food_all/food_menu/menu_17.html')

@app.route("/ยำปลากระป๋อง")
def menu_18():
    return render_template('food_all/food_menu/menu_18.html')

@app.route("/ส้มตำไทย")
def menu_19():
    return render_template('food_all/food_menu/menu_19.html')

@app.route("/ปลาแซลมอนย่างซอสเทอริยากิ")
def menu_20():
    return render_template('food_all/food_menu/menu_20.html')

@app.route("/แกงเขียวหวานอกไก่")
def menu_21():
    return render_template('food_all/food_menu/menu_21.html')

@app.route("/Gnocchi with Tomato Sauce")
def menu_22():
    return render_template('food_all/food_menu/menu_22.html')

@app.route("/Tuna Corn Salad")
def menu_23():
    return render_template('food_all/food_menu/menu_23.html')

@app.route("/ข้าวไข่ข้นข้าวโพด")
def menu_24():
    return render_template('food_all/food_menu/menu_24.html')
    
@app.route("/Chicken Panzanella Salad")
def menu_25():
    return render_template('food_all/food_menu/menu_25.html')

@app.route("/มะเขือเทศผัดไข่")
def menu_26():
    return render_template('food_all/food_menu/menu_26.html')

@app.route("/แซนวิชไข่ต้มไส้ทะลัก")
def menu_27():
    return render_template('food_all/food_menu/menu_27.html')

@app.route("/Sour Banked Salmon")
def menu_28():
    return render_template('food_all/food_menu/menu_28.html')

@app.route("/ไข่อบอะโวคาโด")
def menu_29():
    return render_template('food_all/food_menu/menu_29.html')

@app.route("/เปาะเปี๊ยะลาบลุยสวน")
def menu_30():
    return render_template('food_all/food_menu/menu_30.html')

@app.route("/สลัดปลาแซลมอนย่าง")
def menu_31():
    return render_template('food_all/food_menu/menu_31.html')

@app.route("/Salad Cottage Cheese")
def menu_32():
    return render_template('food_all/food_menu/menu_32.html')

@app.route("/couscous salad with tofu")
def menu_33():
    return render_template('food_all/food_menu/menu_33.html')

@app.route("/Acai Bowl")
def menu_34():
    return render_template('food_all/food_menu/menu_34.html')

@app.route("/Pink Smoothie")
def menu_35():
    return render_template('food_all/food_menu/menu_35.html')

@app.route("/อกไก่ผัดมันฝรั่ง")
def menu_36():
    return render_template('food_all/food_menu/menu_36.html')

@app.route("/แซนด์วิชไข่คน")
def menu_37():
    return render_template('food_all/food_menu/menu_37.html')

@app.route("/ข้าวคลุกกะปิ")
def menu_38():
    return render_template('food_all/food_menu/menu_38.html')

@app.route("/ไก่ย่างน้ำจิ้มแจ่ว")
def menu_39():
    return render_template('food_all/food_menu/menu_39.html')

@app.route("/ปลานิลย่าง")
def menu_40():
    return render_template('food_all/food_menu/menu_40.html')

@app.route("/คั่วกลิ้ง")
def menu_41():
    return render_template('food_all/food_menu/menu_41.html')

@app.route("/สปาเกตตีซอสมะเขือเทศ")
def menu_42():
    return render_template('food_all/food_menu/menu_42.html')

@app.route("/สปาเกตตีคาโบนารา")
def menu_43():
    return render_template('food_all/food_menu/menu_43.html')

@app.route("/ไข่เจียวใส่ผักวอเตอร์เครส")
def menu_44():
    return render_template('food_all/food_menu/menu_44.html')

@app.route("/ไข่ตุ๋นคลีน")
def menu_45():
    return render_template('food_all/food_menu/menu_46.html')

@app.route("/ยำไข่ต้มคลีน")
def menu_46():
    return render_template('food_all/food_menu/menu_46.html')

@app.route("/ไข่เจียวฟักทองคลีน")
def menu_47():
    return render_template('food_all/food_menu/menu_47.html')

@app.route("/ไข่ซูเฟล่")
def menu_48():
    return render_template('food_all/food_menu/menu_48.html')








# Exercise 
@app.route('/exercise')
def exercise_page1():
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



@app.route('/ออกกำลังกายกล้ามเนื้อหน้าอก')
def exercise_set4():
    return render_template('exercise_all/exercise_set/exercise_set4.html')

@app.route('/ออกกำลังกายกล้ามเนื้อหลัง')
def exercise_set5():
    return render_template('exercise_all/exercise_set/exercise_set5.html')

@app.route('/ออกกำลังกายกล้ามเเขน')
def exercise_set6():
    return render_template('exercise_all/exercise_set/exercise_set6.html')

@app.route('/ออกกำลังกายเเบบคาร์ดิโอ')
def exercise_set7():
    return render_template('exercise_all/exercise_set/exercise_set7.html')

@app.route('/โยคะ')
def exercise_set8():
    return render_template('exercise_all/exercise_set/exercise_set8.html')

@app.route('/ว่ายน้ำ')
def exercise_set9():
    return render_template('exercise_all/exercise_set/exercise_set9.html')









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


# search menu เสร็จแล้วนะ by Lotto
@app.route('/Food_search', methods=['POST', 'GET'])
def search():
    text_search = ''
    if request.method=="POST" and "search" in request.form:
        search = request.form["search"]
    else:
        text_search = 'กรุณาใส่ชื่ออาหาร' 
        return render_template('Erorr.html',search=text_search)
    
    if search == "กระเพราอกไก่" or search == "กระเพรา":
        return redirect(url_for('menu_1'))
    elif search == "แกงจืดตำลึงหมูสับ" or search == "ตำลึงหมูสับ":
        return redirect(url_for('menu_2'))
    elif search == "ต้มข่าอกไก่":
        return redirect(url_for('menu_3'))
    elif search == "แกงเหลือง":
        return redirect(url_for('menu_4'))
    elif search == "ซุบหน่อไม้":
        return redirect(url_for('menu_5'))
    elif search == "แกงเลียง":
        return redirect(url_for('menu_6'))
    elif search == "ส้มตำผลไม้":
        return redirect(url_for('menu_7'))
    elif search == "ห่อหมกปลาดอรี่":
        return redirect(url_for('menu_8'))
    elif search == "น้ำพริกอ่องอกไก่":
        return redirect(url_for('menu_9'))
    elif search == "อกไก่คั่วพริกแกง":
        return redirect(url_for('menu_10'))
    elif search == "ต้มยำเห็ดน้ำใส":
        return redirect(url_for('menu_11'))
    elif search == "ผัดถั่วงอกเต้าหู้":
        return redirect(url_for('menu_12'))
    elif search == "แกงจืดมะระยัดไส้":
        return redirect(url_for('menu_13'))
    elif search == "ต้มเลือดหมู":
        return redirect(url_for('menu_14'))
    elif search == "สลัดโรล":
        return redirect(url_for('menu_15'))
    elif search == "ยำวุ้นเส้น":
        return redirect(url_for('menu_16'))
    elif search == "ยำถั่วพู":
        return redirect(url_for('menu_17'))
    elif search == "ยำปลากระป๋อง":
        return redirect(url_for('menu_18'))
    elif search == "ส้มตำไทย":
        return redirect(url_for('menu_19'))
    elif search == "ปลาแซลมอนย่างซอสเทอริยากิ":
        return redirect(url_for('menu_20'))
    elif search == "แกงเขียวหวานอกไก่":
        return redirect(url_for('menu_21'))
    elif search == "Gnocchi with Tomato Sauce":
        return redirect(url_for('menu_22'))
    elif search == "Tuna Corn Salad":
        return redirect(url_for('menu_23'))
    elif search == "ข้าวไข่ข้นข้าวโพด":
        return redirect(url_for('menu_24'))
    elif search == "Chicken Panzanella Salad":
        return redirect(url_for('menu_25'))
    elif search == "มะเขือเทศผัดไข่":
        return redirect(url_for('menu_26'))
    elif search == "แซนวิชไข่ต้มไส้ทะลัก":
        return redirect(url_for('menu_27'))
    elif search == "Sour Banked Salmon":
        return redirect(url_for('menu_28'))
    elif search == "ไข่อบอะโวคาโด":
        return redirect(url_for('menu_29'))
    elif search == "เปาะเปี๊ยะลาบลุยสวน":
        return redirect(url_for('menu_30'))
    elif search == "สลัดปลาแซลมอนย่าง":
        return redirect(url_for('menu_31'))
    elif search == "Salad Cottage Cheese":
        return redirect(url_for('menu_32'))
    elif search == "couscous salad with tofu":
        return redirect(url_for('menu_33'))
    elif search == "Acai Bowl":
        return redirect(url_for('menu_34'))
    elif search == "Pink Smoothie":
        return redirect(url_for('menu_35'))
    elif search == "อกไก่ผัดมันฝรั่ง":
        return redirect(url_for('menu_36'))
    elif search == "แซนวิชไข่คน":
        return redirect(url_for('menu_37'))
    elif search == "ข้าวคลุกกะปิ":
        return redirect(url_for('menu_38'))
    elif search == "ไก่ย่างน้ำจิ้มแจ่ว":
        return redirect(url_for('menu_39'))
    elif search == "ปลานิลย่าง":
        return redirect(url_for('menu_40'))
    elif search == "คั่วกลิ้ง":
        return redirect(url_for('menu_41'))
    elif search == "สปาเกตตีซอสมะเขือเทศ":
        return redirect(url_for('menu_42'))
    elif search == "สปาเกตตีคาโบนารา":
        return redirect(url_for('menu_43'))
    elif search == "ไข่เจียวใส่ผักวอเตอร์เครส":
        return redirect(url_for('menu_44'))
    elif search == "ไข่ตุ๋นคลีน":
        return redirect(url_for('menu_45'))
    elif search == "ยำไข่ต้มคลีน":
        return redirect(url_for('menu_46'))
    elif search == "ไข่เจียวฟักทองคลีน":
        return redirect(url_for('menu_47'))
    elif search == "ไข่ซูเฟล่":
        return redirect(url_for('menu_48'))
    elif search == 'อกไก่' or search == 'ไก่' or 'ไก่' in search:
        return redirect(url_for('search_1'))
    elif search == 'สลัด' or search == 'salad' or 'สลัด' in search:
        return redirect(url_for('search_2'))
    elif 'ปลา' in search or 'แซวม่อน' in search:
        return redirect(url_for('search_3'))
    else:
        text_search = "ไม่พบเมนู " + search
        return render_template('Erorr.html',search=text_search)


@app.route('/เมนูไก่')
def search_1():
    return render_template('food_all/food_search1.html')

@app.route('/เมนูสลัด')
def search_2():
    return render_template('food_all/food_search2.html')

@app.route('/เมนูปลา')
def search_3():
    return render_template('food_all/food_search3.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/comment', methods=['POST','GET']) # page1
def comment():
    if request.method=="POST":
        name = request.form['name']
        text = request.form['text']
        date = datetime.today()
        time = str(date.strftime("%d/%m/%Y %H:%M"))
        with db.cursor() as cursor:
            sql = "Insert into `comment` (`time`,`name`,`text`) values(%s,%s,%s)"
            cursor.execute(sql,(time,name,text))
            db.commit()
        return redirect(url_for('food'))
    
    
@app.route('/comment1', methods=['POST','GET']) # page2
def comment1():
    if request.method=="POST":
        name = request.form['name']
        text = request.form['text']
        date = datetime.today()
        time = str(date.strftime("%d/%m/%Y %H:%M"))
        with db.cursor() as cursor:
            sql = "Insert into `comment` (`time`,`name`,`text`) values(%s,%s,%s)"
            cursor.execute(sql,(time,name,text))
            db.commit()
        return redirect(url_for('food_page2'))


@app.route('/comment2', methods=['POST','GET']) # page2
def comment2():
    if request.method=="POST":
        name = request.form['name']
        text = request.form['text']
        date = datetime.today()
        time = str(date.strftime("%d/%m/%Y %H:%M"))
        with db.cursor() as cursor:
            sql = "Insert into `comment` (`time`,`name`,`text`) values(%s,%s,%s)"
            cursor.execute(sql,(time,name,text))
            db.commit()
        return redirect(url_for('food_page3'))
    
    
@app.route('/comment3', methods=['POST','GET']) # page2
def comment3():
    if request.method=="POST":
        name = request.form['name']
        text = request.form['text']
        date = datetime.today()
        time = str(date.strftime("%d/%m/%Y %H:%M"))
        with db.cursor() as cursor:
            sql = "Insert into `comment` (`time`,`name`,`text`) values(%s,%s,%s)"
            cursor.execute(sql,(time,name,text))
            db.commit()
        return redirect(url_for('food_page4'))
    

    
    

if __name__=="__main__":
    app.run(debug=True)


