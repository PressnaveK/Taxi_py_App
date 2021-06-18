import sqlite3
conn = sqlite3.connect('TBS.db')
c = conn.cursor()
class Administrator:
    def __init__(self,Username,Password,First_Name,Last_Name):
        self.Username = Username
        self.Password = Password
        self.First_Name = First_Name
        self.Last_Name = Last_Name

#admin1 = Administrator('Pressnave','1234','Kiruparaj','Pressnave')

Name = 'Shivan'
c.execute('INSERT INTO Administrator VALUES(?,?,?,?)',(Name,'1234','Ganam','Mangalan') )
#UserNm = 'Pressnave'
c.execute('SELECT * FROM Administrator where Username = :User',{'User': UserNm})
#K = c.fetchone()
#print(K[1])
conn.commit()
conn.close()