import mysql.connector as mc
# conne = mc.connect(user='raj',password ='hello12345@',host ='52.66.212.209',port = '3306')
conne = mc.connect(user='govi',password ='hello@123',host ='localhost',port = '3306',database='jaykumar')

if conne.is_connected():
    print('you are connected')
else:
    print('sorry unable to connect')

mycur = conne.cursor()
query = "create table student (stud_id int, student_name varchar(25),student_class varchar(10))"
query2 = "INSERT INTO student (stud_id,student_name,student_class) values(%s,%s,%s)"
while True:
    id = int(input('student id : '))
    if id ==0:
        break
    name = input('enter your name : ')
    room = input('enter your class : ')
    record = (id,name,room)
    

# %(key)s,%(key)s

try:
    mycur.execute(query2,record)
    conne.commit()

except:
    conne.rollback()
    print('unable to insert')

# records = mycur.fetchall()
# for record in records:
#     print(record)

mycur.close()
conne.close()