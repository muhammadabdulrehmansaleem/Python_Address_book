import pymysql
class dbHandler:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.passwd=password
        self.database=db
    def create_table(self):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""create table users (User_id int auto_increment not null primary key,email varchar(100) not null unique,password varchar(30) not null unique);"""
            cursor.execute(query)
            connect.commit()
        except Exception as e:
            print(str(e))
        finally:
            if cursor!=None:
                cursor.close()
            if connect!=None:
                connect.close()
    def insert_contact(self,l1):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""insert into contacts values(%s,%s,%s,%s,%s,%s);"""
            values=(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5])
            cursor.execute(query,values)
            connect.commit()
        except Exception as e:
            print(str(e))
        finally:
            if cursor!=None:
                cursor.close()
            if connect!=None:
                connect.close()
    def show_contacts(self):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""select*from contacts"""
            cursor.execute(query)
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(str(e))
        finally:
            if cursor!=None:
                cursor.close()
            if connect!=None:
                connect.close()
    def delete_contact(self,name):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""delete from contacts where name=%s;"""
            values=(name)
            cursor.execute(query,values)
            connect.commit()
            print("User deleted ")
            return True
        except Exception as e:
            print(str(e))
            print("User not deleted")
            return False
        finally:
            if cursor!=None:
                cursor.close()
            if connect!=None:
                connect.close()
    def update_contact(self,id,l1):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""update contacts set id=%s,name=%s,mobileno=%s,city=%s,profession=%s,U_id=%s
            where id=%s;"""
            value=(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],id)
            cursor.execute(query,value)
            connect.commit()
            print("Query exe")
            return True
        except Exception as e:
            print(str(e))
            print("Not exe")
            return False
        finally:
            if cursor!=None:
                cursor.close()
            if connect!=None:
                connect.close()
    def get_contact_by_id(self,id):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""select * from contacts where id=%s;"""
            values=(id)
            cursor.execute(query,values)
            result=cursor.fetchall()
            l1=[]
            for i in range(0,6):
                l1.append(result[0][i])
            return l1
        except Exception as e:
            print(str(e))
            l1=[]
            return l1
        finally:
            if cursor!=None:
                cursor.close()
            if connect!=None:
                connect.close()
    def get_Contact_byName(self,name):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""select* from contacts where name=%s;"""
            values=(name)
            cursor.execute(query,values)
            result=cursor.fetchone()
            return result
        except Exception as e:
            print(str(e))
        finally:
            if cursor!=None:
                cursor.close()
            if connect!=None:
                connect.close()
    def insert_user(self,l1):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""insert into users values(%s,%s,%s);"""
            values=(l1[0],l1[1],l1[2])
            cursor.execute(query,values)
            connect.commit()
            print("User inserted")
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connect.close()
    def verify_user(self,l1):
        try:
            connect=pymysql.connect(host='localhost',user='root',passwd='1234566',database='addressbook')
            cursor=connect.cursor()
            query="""select password from users where email=%s;"""
            values=(l1[0])
            cursor.execute(query,values)
            result=cursor.fetchall()
            if result[0][0]==l1[1]:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connect.close()
db=dbHandler("localhost","root","1234566","addressbook")
# l1=[66,"abdulrehman","09876","shah","student",3]
# db.update_contact(43,l1)
# db.verify_user(l1)
db.get_contact_by_id(55)
# l1=[21,"bsef20m093@pucit.edu.pk","pak"]

# l1=db.get_Contact_byName("umar")
# print(l1)
# db.verify_user(l1)
# db.create_table()
# db.create_table()
# db.insert_contact(l1)
