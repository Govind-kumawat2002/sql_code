
import csv
import mysql.connector as mc
conne = mc.connect(user='govi',password ='hello@123',host ='localhost',port = '3306',database ='laptop')
mycur = conne.cursor()
# query1 = "create table lap (brand varchar(20), processor_brand varchar(20), processor_name varchar(20), processor_gnrtn varchar(20), ram_gb varchar(20), ram_type varchar(20), ssd varchar(20),   hdd varchar(20),  os varchar(20),  os_bit varchar(20), graphic_card_gb varchar(20), weight  varchar(20), warranty varchar(20), Touchscreen varchar(20), msoffice varchar(20), Price int,rating varchar(20), NumberofRatings int, NumberofReviews varchar(20))"
# query2 = "INSERT INTO lp value('lp2')"
# columns = (brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,weight,warranty,Touchscreen,msoffice,Price,rating,Number of Ratings,Number of Reviews)
query = 'INSERT INTO lap  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
with open('laptopPrice.csv','r') as file:
    csv_reader = csv.reader(file)
    temp = 0
    for row in csv_reader:
        if temp == 0:
            temp +=1
            continue
        if temp > 0:
            try:
                
                mycur.execute(query,tuple(row))
                conne.commit()
            
                # print(tuple(row))
            except Exception as e:
                conne.rollback()
                print(e)



mycur.close()
conne.close()




      


    
