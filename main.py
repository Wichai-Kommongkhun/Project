from flask import Flask, render_template, request, redirect, url_for, session
from flask.helpers import flash



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


# search menu ยังทำไม่เสร็จ
@app.route('/Food_search', methods=['POST', 'GET'])
def search():
    text_search = ''
    if request.method=="POST" and "search" in request.form:
        search = request.form["search"]
    else:
        text_search = 'กรุณาใส่ชื่ออาหาร' 
        return render_template('Erorr.html',search=text_search)
    
    if search == "กระเพราอกไก่" or search == "กระเพรา":
        return render_template('food_all/food_menu/menu_1.html')
    elif search == "แกงจืดตำลึงหมูสับ" or search == "ตำลึงหมูสับ":
        return render_template('food_all/food_menu/menu_2.html')
    elif search == "ต้มข่าอกไก่":
        return render_template('food_all/food_menu/menu_3.html')
    elif search == "แกงเหลือง":
        return render_template('food_all/food_menu/menu_4.html')
    elif search == "ซุบหน่อไม้":
        return render_template('food_all/food_menu/menu_5.html')
    elif search == "แกงเลียง":
        return render_template('food_all/food_menu/menu_6.html')
    elif search == "ส้มตำผลไม้":
        return render_template('food_all/food_menu/menu_7.html')
    elif search == "ห่อหมกปลาดอรี่":
        return render_template('food_all/food_menu/menu_8.html')
    elif search == "น้ำพริกอ่องอกไก่":
        return render_template('food_all/food_menu/menu_9.html')
    elif search == "อกไก่คั่วพริกแกง":
        return render_template('food_all/food_menu/menu_10.html')
    elif search == "ต้มยำเห็ดน้ำใส":
        return render_template('food_all/food_menu/menu_11.html')
    elif search == "ผัดถั่วงอกเต้าหู้":
        return render_template('food_all/food_menu/menu_12.html')
    elif search == "แกงจืดมะระยัดไส้":
        return render_template('food_all/food_menu/menu_13.html')
    elif search == "ต้มเลือดหมู":
        return render_template('food_all/food_menu/menu_14.html')
    elif search == "สลัดโรล":
        return render_template('food_all/food_menu/menu_15.html')
    elif search == "ยำวุ้นเส้น":
        return render_template('food_all/food_menu/menu_16.html')
    elif search == "ยำถั่วพู":
        return render_template('food_all/food_menu/menu_17.html')
    elif search == "ยำปลากระป๋อง":
        return render_template('food_all/food_menu/menu_18.html')
    elif search == "ส้มตำไทย":
        return render_template('food_all/food_menu/menu_19.html')
    elif search == "ปลาแซลมอนย่างซอสเทอริยากิ":
        return render_template('food_all/food_menu/menu_20.html')
    else:
        text_search = "ไม่พบเมนู " + search
        return render_template('Erorr.html',search=text_search)

if __name__=="__main__":
    app.run(debug=True)


