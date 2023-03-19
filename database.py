import mysql.connector as sql

class Database:
    def __init__(self):
        self.myDB = None
        self.query = None


    def connect(self, host, user:str, pwd:str, db:str):
        try:
            self.myDB = sql.connect(
                host = host,
                user = user,
                password = pwd
            )

            self.query = self.myDB.cursor()
            self.query.execute("SHOW DATABASES")
            dbs = []
            for i in self.query:
                dbs.append(i[0])

            if db not in dbs:
                self.query.execute(f"CREATE DATABASE {db}")
            self.myDB.database = db

            return ("Success", "Connected to the database successlully!")
        except sql.Error as error:
            return ("Error", error)
        


    def initTables(self, authTable:str, resultTable:str, quizTable:str):
        try:
            self.query.execute("SHOW TABLES")

            allTables = []
            for i in self.query:
                allTables.append(i[0])
            

            if authTable not in allTables:
                self.query.execute(f"CREATE TABLE {authTable} (id INT(5) NOT NULL AUTO_INCREMENT, name VARCHAR(50) NULL, password VARCHAR(50) NULL, type VARCHAR(10) NOT NULL DEFAULT 'user', attempted INT(1) NOT NULL DEFAULT 0, createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, updatedAt TIMESTAMP on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id), UNIQUE (name(50)))")


            if resultTable not in allTables:
                self.query.execute(f"CREATE TABLE {resultTable} (id INT(5) NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, answers JSON NOT NULL, grade VARCHAR(2) NOT NULL, score VARCHAR(10) NOT NULL, percent VARCHAR(20) NOT NULL, createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, updatedAt TIMESTAMP on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id), UNIQUE (name(50)))")


            if quizTable not in allTables:
                self.query.execute(f"CREATE TABLE {quizTable} (id INT(5) NOT NULL AUTO_INCREMENT, qname VARCHAR(255) NULL, option1 VARCHAR(255) NULL, option2 VARCHAR(255) NULL, option3 VARCHAR(255) NULL, option4 VARCHAR(255) NULL, answer VARCHAR(255) NULL, createdAt TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, updatedAt TIMESTAMP on update CURRENT_TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id))")

            return ("Success", "Initailization Completed!")
        
        except sql.Error as error:
            return ("Error", error)



    def insertIntoAuthTable(self, tableName:str, values:tuple, admin:bool=False):
        try:
            self.query.execute(f"INSERT INTO {tableName} (name, password) VALUES (%s, %s)", values) if not admin else self.query.execute(f"INSERT INTO {tableName} (name, password, type) VALUES (%s, %s, %s)", (values[0], values[1], "admin"))
            self.myDB.commit()

            return ("Success", "1 record inserted, ID:" + str(self.query.lastrowid))

        except sql.Error as error:
            return ("Error", (error.errno, error.msg))


    def getFromAuthTable(self, tbName:str, name:str, pwd:str):
        try:
            self.query.execute(f"SELECT name, type FROM {tbName} WHERE name = %s AND password = %s", (name, pwd))
            res = self.query.fetchall()
            return ("Success", res[0]) if len(res) == 1 else ("Warn", "Invalid credentials!")
        
        except sql.Error as error:
            return ("Error", error)
        

    def fetchUsers(self, tbName:str, name:str=None):
        try:
            if name is None:
                self.query.execute(f"SELECT name, answers, grade, score, percent FROM {tbName}")
            else:
                self.query.execute(f"SELECT name, answers, grade, score, percent FROM {tbName} WHERE name = %s", (name,))
            data = self.query.fetchall()

            if len(data) == 0:
                return ("Warn", "No User record found who have attempted the quiz.")
            return ("Success", data)

        except sql.Error as error:
            return ("Error", error)
        
    
    def fetchQuests(self, tbName:str):
        try:
            self.query.execute(f"SELECT qname, option1, option2, option3, option4, answer FROM {tbName}")
            data = self.query.fetchall()
            return ("Success", data)

        except sql.Error as error:
            return ("Error", error)
        

    def saveQuests(self, tbName:str, values:tuple, multiple:bool=False):
        try:
            if multiple:
                self.query.executemany(f"INSERT INTO {tbName} (qname, option1, option2, option3, option4, answer) VALUES (%s, %s, %s, %s, %s, %s)", values)
            else:
                self.query.execute(f"INSERT INTO {tbName} (qname, option1, option2, option3, option4, answer) VALUES (%s, %s, %s, %s, %s, %s)", values)
            
            self.myDB.commit()
            return ("Success", "Total Record inserted: " + str(self.query.rowcount))

        except sql.Error as error:
            return ("Error", error)
        

    def delQuestByName(self, tbName:str, qname:str):
        try:
            self.query.execute(f"DELETE FROM {tbName} WHERE qname = %s", (qname,))
            self.myDB.commit()
            return ("Success", "Total Record deleted: " + str(self.query.rowcount))

        except sql.Error as error:
            return ("Error", error)
        

    def insertIntoResultTable(self, tbName:str, values):
        try:
            self.query.execute(f"INSERT INTO {tbName} (name, answers, grade, score, percent) VALUES (%s, %s, %s, %s, %s)", values)
            self.myDB.commit()
            return ("Success", "Total Record inserted: " + str(self.query.rowcount))

        except sql.Error as error:
            return ("Error", error)


    
    def disconnect(self):
        self.query.close()
        self.myDB.close()
        self.myDB.disconnect()

