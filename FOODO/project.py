 #!/usr/bin/python
from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm import scoped_session


from flask import session as login_session
import random
import string
dataset={}
global ssession 
global waw
waw=True
ssession=True 

import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


APPLICATION_NAME = "FOODO"
ur=""
pas=""



engine = create_engine('sqlite:///r1estaurantmenu.db',
                poolclass=SingletonThreadPool)


Session = sessionmaker(bind=engine)
session = scoped_session(Session)


def re(username,password):
    file = open("accountfile.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()

def log(username,password):
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1] and username == "admin":
            return "a"
        elif username == login_info[0] and password == login_info[1] :
            return True
    return False

def cout():
    user=[""]*100
    i=0
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        user[i] = login_info[0] 
        i=i+1
    return user

def edit_user(username,password):
    i=0
    lines = open("accountfile.txt", 'r').readlines()
    for line in lines: # Read the lines
        login_info = line.split()
        if username == login_info[0]:
            login_info[1]=password
            line=login_info[0]+" "+login_info[1]
            lines[i] = line
            out = open("accountfile.txt", 'w')
#            out.seek(0)
            out.write(lines[i])
            out.close() # Split on the space, and store the results in a list of two strings
            return "user profile data changed "
        i=i+1
    return "user not founded or incoorect input"




@app.route('/categories/<int:category_id>/courses/JSON')
def coursesJSON(category_id):
   courses=session.query(Courses).filter_by(category_id=category_id).all()
   return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/JSON')
@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Categories).all()
    courses=session.query(Courses).all()
    return jsonify(categories=[r.serialize for r in categories])

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login1.html')
	else:
		#name = request.form['username']
		username = str(request.form['username'])
		password = str(request.form['password'])

		waw=log(username,password)

		data = session.query(User).filter(User.username.in_([username]), User.password.in_([password]) )
		
		if waw == True :   #is not None:
			ssession = False 
			return redirect(url_for('show_categories'))
		elif waw == "a" :   #is not None:
			ssession = "ad" 
			return redirect(url_for('admin'))
		else:
			return 'this user didnot on the website'
		#except:
			#return "Dont Login"

@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
	    #new_category=Categories(name=request.form['name'])
	    username=request.form['username']
	    password=request.form['password']
#	    dataset[username]=password
	    re(username,password)
#        new_user = User(username=request.form['username'], password=request.form['password'])
#	    session.add(new_user)
#	    session.commit()
	    return render_template('login1.html')
	return render_template('register.html')

@app.route("/logout/")
def logout():
	"""Logout Form"""
	ssession = True
	return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST'])
def home():
	""" Session control"""
	if not ssession == False:
		x="welcome to our home page"
		return render_template('index1.html',x=x)
	else:
		return redirect(url_for('show_categories'))

@app.route('/admin/', methods=['GET', 'POST'])
def admin():
	if not ssession == False:
		return render_template('index.html')

@app.route('/show_users', methods=['GET', 'POST'])

def show_users():
    x=cout()
    return render_template('users.html',x=x)
    
@app.route('/edit_users', methods=['GET', 'POST'])
def edit_users():
	if request.method == 'POST':
	    #new_category=Categories(name=request.form['name'])
	    username=str(request.form['username'])
	    password=str(request.form['password'])
	    x=edit_user(username,password)
	    return render_template('index1.html',x=x)
	x="please enter the correct data"
	return render_template('edituser.html',x=x)


    



@app.route('/categories/')
def show_categories():
	categories = session.query(Categories).all()
	courses=session.query(Courses).all()
	return render_template('categories.html', categories=categories,courses=courses)
	
@app.route('/categories/new/', methods=['GET', 'POST'])
def new_category():
	if not waw:
		return redirect('/login')
	if request.method == 'POST':
		new_category=Categories(name=request.form['name'])
		session.add(new_category)
		session.commit()
		flash('New Restaurant %s Successfully Created' % new_category.name)
		return redirect(url_for('show_categories'))
	else:
		return render_template('new_category.html')
	
@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def edit_category(category_id):
	if not waw:
		return redirect('/login')
	edited_category = session.query(Categories).filter_by(id=category_id).one()
	if request.method == 'POST':
		if request.form['name']:
			edited_category.name=request.form['name']
			session.add(edited_category)
			session.commit()
			flash('catefgory Successfully Edited %s' % edited_category.name)
			return redirect(url_for('show_categories'))
	else:
		return render_template('edit_category.html', category=edited_category)
	
@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def delete_category(category_id):
	if not waw:
		return redirect('/login')
	deleted_category = session.query(Categories).filter_by(id=category_id).one()
	if request.method == 'POST':
		session.delete(deleted_category)
		session.commit()
		flash('catefgory Successfully deleted %s' % deleted_category.name)
		return redirect(url_for('show_categories'))
	else:
		return render_template('delete_category.html', category=deleted_category)	


@app.route('/categories/<int:category_id>/courses/')
def show_courses(category_id):
	categories = session.query(Categories).all()
	courses=session.query(Courses).filter_by(category_id=category_id).all()
	return render_template('show_courses.html', courses=courses, categories=categories,category_id=category_id)


@app.route('/categories/<int:category_id>/courses/new', methods=['GET', 'POST'])
def new_course(category_id):
	if not waw:
		return redirect('/login')
	if request.method == 'POST':
		new_course = Courses(name=request.form['name'], description=request.form[
						'description'], link=request.form['link'],photo_url=request.form['photo_url'], category_id=category_id)
		session.add(new_course)
		session.commit()
		flash('course Successfully created %s' % new_course.name)
		return redirect(url_for('show_courses', category_id=category_id))
	else:
		return render_template('new_course.html', category_id=category_id)

@app.route('/categories/<int:category_id>/courses/<int:course_id>/edit/', methods=['GET', 'POST'])
def edit_course(category_id, course_id):
	if not waw:
		return redirect('/login')
	edited_course=session.query(Courses).filter_by(id=course_id).one()
	if request.method == 'POST':
		if request.form['name']:
			edited_course.name = request.form['name']
		if request.form['description']:
			edited_course.description = request.form['description']
		if request.form['link']:
			edited_course.link = request.form['link']
		if request.form['photo_url']:
			edited_course.photo_url = request.form['photo_url']
			
		session.add(edited_course)
		session.commit()
		flash('course Successfully edited %s' % edited_course.name)
		return redirect(url_for('show_courses', category_id=category_id))
	else:

		return render_template(
			'edit_course.html', category_id=category_id, course_id=course_id, course=edited_course)
	
@app.route('/categories/<int:category_id>/courses/<int:course_id>/delete/', methods=['GET', 'POST'])
def delete_course(category_id, course_id):
	if not waw:
		return redirect('/login')
	deleted_course=session.query(Courses).filter_by(id=course_id).one()
	if request.method == 'POST':
		session.delete(deleted_course)
		session.commit()
		flash('course Successfully deleted %s' % deleted_course.name)
		return redirect(url_for('show_courses', category_id=category_id))
	else:
		return render_template('delete_course.html',category_id=category_id,course=deleted_course)

@app.route('/categories/<int:category_id>/courses/<int:course_id>')
def course_details(category_id, course_id):
	course=session.query(Courses).filter_by(id=course_id).one()
	return render_template('course_details.html', category_id=category_id, course_id=course_id,course=course)


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)
