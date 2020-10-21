from app import *
import sqlite3

con = sqlite3.connect("students.db")


@server.route("/", methods=["GET", "POST"])
@server.route("/Home", methods=["GET", "POST"])
def Index(search_info=""):
	con = sqlite3.connect("students.db")
	cur = con.cursor()
	if search_info == "":
		cur.execute("SELECT * from student_data")
	else:
		cur.execute("SELECT * from student_data where id_number=:id", {"id": search_info})
	#student_list = cur.fetchall()
	return render_template("index.html", student_list=cur.fetchall())

@server.route("/add", methods=["GET", "POST"])
def Add():
	return render_template("addform.html")

@server.route("/savedetails", methods=["GET", "POST"])
def Savedetails():
	msg = "msg"
	if request.method == "POST":
		con = sqlite3.connect("students.db")
		cur = con.cursor()
		id_number = request.form["id_number"]
		print(id_number)
		first_name = request.form["first_name"]
		last_name = request.form["last_name"]
		course = request.form["course"]
		cur.execute("INSERT into student_data(id_number, first_name, last_name, course) values (?,?,?,?)" , (id_number, first_name, last_name, course))
		con.commit()
		return render_template("success.html")

@server.route("/delete/<id>")
def Delete(id):
	con = sqlite3.connect("students.db")
	cur = con.cursor()
	cur.execute("DELETE from student_data where id_number=:id", {"id": id})
	con.commit()
	return Index()

@server.route("/edit/<id>/<first>/<last>/<course>")
def Edit(id, first, last, course):
	return render_template("edit.html", ID=id, First=first, Last=last, Course=course)

@server.route("/editinfo", methods=["GET", "POST"])
def EditInfo():
	con = sqlite3.connect("students.db")
	cur = con.cursor()
	cur.execute("UPDATE student_data set id_number=:id, first_name=:first, last_name=:last, course=:course where id_number=:old_id_number", {"id": request.form["id_number"], "first": request.form["first_name"], "last": request.form["last_name"], "course": request.form["course"], "old_id_number": request.form["old_id_number"]} )
	con.commit()
	return Index()

@server.route("/search", methods=["POST"])
def Search():
	return Index(request.form["id_number_search"])
