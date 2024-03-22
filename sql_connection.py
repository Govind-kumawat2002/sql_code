import mysql.connector as mc
# conne = mc.connect(user='raj',password ='hello12345@',host ='52.66.212.209',port = '3306')
conne = mc.connect(user='govi',password ='hello@123',host ='localhost',port = '3306',database ='Lp_db')

if conne.is_connected():
    print('you are connected')
else:
    print('sorry unable to connect')

mycur = conne.cursor()
query = "select * from TABLE_NAME"
try:
    mycur.execute(query)
except:
    print("byy")

# records = mycur.fetchall()      # [(),(),()]   <--
# mycur.fetchmany(25)
# mycur.fetchone()
row = mycur.fetchone()   # ()

while row is not None:    # True  is not true   ,<-- False
    print(row)
    row = mycur.fetchone()

mycur.close()
conne.close()    
