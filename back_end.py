from flask import Flask,redirect,url_for,render_template,request
import mysql.connector,random


app = Flask(__name__)
# global a
# a = random.randint(1,7)

global a
a = random.randint(1,6) 


@app.route("/")
def welcome_mainpage():
	
	#return render_template("sci_pro_html_part.html")
	return render_template("sci_pro_html_part.html" ,)


@app.route("/dice")
def dice():
	global a
	return render_template("dice.html" , data = a)
	

# @app.route('/back_end',methods = ['POST'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       print(user)
#       return redirect(url_for(''))
#    else:
#       return "Invalid Request"

# def roll_dice():
# 	a = random.randint(1,6)
# 	return render_template("dice.html" , data = a)
# @app.route("/Qes")
# def Qes():
# 	if a==1:
# 		return render_template("Q1.html")
# 	elif a==2:
# 		return render_template("Q2.html")
# 	elif a==3:
# 		return render_template("Q3.html")
# 	elif a==4:
# 		return render_template("Q4.html")
# 	elif a==5:
# 		return render_template("Q5.html")
# 	elif a==6:
# 		return render_template("Q6.html")
# 	else:
# 		pass
@app.route("/Q1")
def Q1():
	return render_template("Q1.html")

@app.route('/back_end',methods = ['POST'])
def login():
	if request.method == 'POST':
		user = request.form['ans1']
		print(user)
		return render_template("Q1.html",ans1 = data)
	else:
		return "Invalid Request"


@app.route("/Q2")
def Q2():
	 return render_template("Q2.html")


	

@app.route("/Q3")
def Q3():
	 return render_template("Q3.html")

@app.route("/Q4")
def Q4():
	 return render_template("Q4.html")

@app.route("/Q5")
def Q5():
	 return render_template("Q5.html")

@app.route("/Q6")
def Q6():
	 return render_template("Q6.html")





if __name__ == '__main__':
	app.run(debug = True) 





