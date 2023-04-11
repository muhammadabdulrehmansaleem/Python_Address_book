from flask import Flask,render_template,request,make_response,session
from flask_session import Session
from controller import insert_record,get_record,get_byname,register_user,verify_login,delete_contact_record,get_info,update_contact_info
app=Flask(__name__)
app.config.from_object('config')
app.secret_key=app.config["SECRET_KEY"]
Session(app)
@app.route('/')
def home_contact():
    return render_template("create_contact.html")
@app.route('/show',methods=["POST"])
def register_contact():
    name=request.form['cname']
    id=request.form['Id']
    city=request.form['city']
    phone=request.form['PH#']
    profess=request.form['Profession']
    uid=request.form['u_id']
    l1=[id,name,city,phone,profess,uid]
    insert_record(l1)
    l1=get_record()
    l2=[]
    for i in range(0,len(l1)):
        dic={}
        dic.update(id=l1[i][0])
        dic.update(name=l1[i][1])
        dic.update(phN=l1[i][2])
        dic.update(city=l1[i][3])
        dic.update(prof=l1[i][4])
        dic.update(u_id=l1[i][5])
        l2.append(dic)
    # return render_template("data.html", l2 = l2)
    respose=make_response(render_template('data.html',l2=l2))
    respose.set_cookie('uname',name)
    respose.set_cookie('uid',id)
    respose.set_cookie('ucity',city)
    respose.set_cookie('uphn',phone)
    respose.set_cookie('uprofess',profess)
    return respose

@app.route('/byname')
def getName():
    # n2=request.cookies.get('uname')
    # id2=request.cookies.get('uid')
    # ucity=request.cookies.get('ucity')
    # uphone=request.cookies.get('uphn')
    # uprofess=request.cookies.get('uprofess')

    # return render_template("hello.html",n2=n2,id2=id2,ucity=ucity)
    return render_template("hello.html")
@app.route('/byname2',methods=["POST"])
def get_by_name():
    name=request.form['serching']
    l1=get_byname(name)
    if len(l1)==0:
        str3="No record against this name found"
        return render_template("data.html",str3=str3)
    else:
        l2=[]
        dic={}
        dic.update(id=l1[0])
        dic.update(name=l1[1])
        dic.update(phN=l1[2])
        dic.update(city=l1[3])
        dic.update(prof=l1[4])
        dic.update(u_id=l1[5])
        l2.append(dic)
        return render_template("data.html",l2=l2)
       
@app.route('/serch')
def search_byname():
    l1=get_record()
    l2=[]
    for i in range(0,len(l1)):
        dic={}
        dic.update(id=l1[i][0])
        dic.update(name=l1[i][1])
        dic.update(phN=l1[i][2])
        dic.update(city=l1[i][3])
        dic.update(prof=l1[i][4])
        dic.update(u_id=l1[i][5])
        l2.append(dic)
    return render_template("data.html", l2 = l2)
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/man',methods=["POST"])
def signup_credentials():
    id=request.form['id']
    email=request.form['email']
    password=request.form['password']
    if len(password)<8:
        str="Password length minimum 8 characters"
        return render_template("signup.html",str=str)
    l1=[id,email,password]
    status=register_user(l1)
    if status==True:
        str="User registerd successfully"
        return render_template('login.html',str=str)
    else:
        str2="User with same email or password already exists"
        return render_template('signup.html',str2=str2)
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/linfo',methods=['POST'])
def login_credentials():
    email=request.form['email']
    password=request.form['password']
    l1=[email,password]
    session['email']=email
    session['password']=password
    status=verify_login(l1)

    if status==True:
        str="User successfully log-in"
        return render_template("menue.html",str=str)
    else:
        str="user does not loged in"
        return render_template("login.html",str=str)
@app.route('/delf')
def show_del_page():
    l1=get_record()
    l2=[]
    for i in range(0,len(l1)):
        dic={}
        dic.update(id=l1[i][0])
        dic.update(name=l1[i][1])
        dic.update(phN=l1[i][2])
        dic.update(city=l1[i][3])
        dic.update(prof=l1[i][4])
        dic.update(u_id=l1[i][5])
        l2.append(dic)
    return render_template('delete.html',l2=l2)
@app.route('/del',methods=['POST'])
def del_contact():
    name=request.form['name']
    status=delete_contact_record(name)
    if status==True:
        str="Contact successfully deleted"
        return render_template('menue.html',str=str)
    else:
        str="Contact can't be deleted"
        return render_template('menue.html',str=str)
@app.route('/update')
def show_update_page():
    l1=get_record()
    l2=[]
    for i in range(0,len(l1)):
        dic={}
        dic.update(id=l1[i][0])
        dic.update(name=l1[i][1])
        dic.update(phN=l1[i][2])
        dic.update(city=l1[i][3])
        dic.update(prof=l1[i][4])
        dic.update(u_id=l1[i][5])
        l2.append(dic)
    name=request.cookies.get('uname')
    return render_template('update.html',l2=l2,msg=name)
@app.route('/update_rec',methods=['POST'])
def update():
    to_be_update=request.form['updated_id']
    l1=get_info(to_be_update)
    uname=l1[1]
    uid=l1[0]
    ucity=l1[3]
    uphone=l1[2]
    uprofess=l1[4]
    u_id=l1[5]
    response=make_response(render_template('update2.html',uname=uname,uid=uid,ucity=ucity,uphone=uphone,uprofess=uprofess,u_id=u_id))
    response.set_cookie('to_be_update',to_be_update)
    return response
@app.route('/update2',methods=['POST'])
def update2():
    name=request.form['cname']
    id=request.form['Id']
    city=request.form['city']
    phone=request.form['PH#']
    profess=request.form['Profession']
    uid=request.form['u_id']
    l1=[id,name,city,phone,profess,uid]
    to_be_update=request.cookies.get('to_be_update')
    status=update_contact_info(to_be_update,l1)
    if status==True:
        str="The contact is updates"
        return render_template('menue.html',str=str)
    else:
        str="Contact not updated"
        return render_template('menue.html',str=str)
if __name__ == '__main__':
    app.run()