# Import module to handle PostgreSQL connections
import psycopg2
import dbconfig as cfg

# Establish a connection to the database by creating a cursor objest
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal

class actorDAO:
    db=""
    def connectToDB(self):
        self.db = psycopg2.connect(
            host=cfg.sql['host'], 
            port=cfg.sql['port'], 
            database=cfg.sql['database'], 
            user=cfg.sql['user'], 
            password=cfg.sql['password']
        )

    def __init__(self): 
        self.connectToDB()

    def getCursor(self):
        if not self.db.isolation_level:
            self.connectToDB()
        return self.db.cursor()

    def columnsName(self, test):
        cursor = self.getCursor()
        sql = 'SELECT column_name FROM information_schema.columns WHERE table_name = %s'
        values = (test,)
        cursor.execute(sql, values)
        columns = cursor.fetchall()
        # columns = [e for item in columns for e in item]
        return [e for item in columns for e in item]

    def getAll(self):
        cursor = self.getCursor()
        # sql = 'SELECT * FROM test'
        sql = '''
                SELECT a.id, a.actorname, date(a.actordob)::text as actordob , a.actorgender, c.countryname as countryname
                FROM actor a
                    LEFT JOIN country c 
	                    ON a.actorcountryid = c.id
                ORDER by a.id
                ;'''
        cursor.execute(sql)
        results = cursor.fetchall()
        columns = self.columnsName('actor')
        columnsCountry = self.columnsName('country')
        # results = [{columns[i]: item[i]} for item in results for i in range(len(item))]
        # a = []
        # for item in results:
        #     a.append({columns:item for columns,item in zip(columns,item)})

        return [{columns:item for columns,item in zip(columns,item)} for item in results]

    def findByID(self, id):
        country = '%' + country + '%'
        cursor = self.getCursor()
        sql="SELECT * FROM countries WHERE country ILIKE %s"
        values = (country,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def createActor(self, actor):
        cursor = self.getCursor()
        sql = 'INSERT INTO actor (actorName, actordob, actorgender, actorcountryid) VALUES (%s, %s, %s, %s)'
        values = [actor[item] for item in actor ]
        print(values)
        cursor.execute(sql, values)
        self.db.commit()
        return 'Record has been added - {actor}'

    def createTest(self, test):
        cursor = self.getCursor()
        sql = 'INSERT INTO test(fname, lname, age) VALUES (%s, %s, %s)'
        values = [test[item] for item in test]
        cursor.execute(sql, values)
        # result = cursor.fetchone()
        self.db.commit()
        return 'Record has been added'

    def findByNameTest(self, id):
        cursor = self.getCursor()
        sql="SELECT * FROM test WHERE id = %s"
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if (result == None):
            return {}
        columns = self.columnsName('test')
        return {columns:result for columns,result in zip(columns,result)}

    def findActorById(self, id):
        cursor = self.getCursor()
        sql = '''
                SELECT a.id, a.actorname, date(a.actordob)::text as actordob , a.actorgender, c.countryname as actorcountryname
                FROM actor a
                    LEFT JOIN country c 
	                    ON a.actorcountryid = c.id
                WHERE a.id = %s
                ;'''
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if (result == None):
            return {}
        columns = self.columnsName('actor')
        return {columns:result for columns,result in zip(columns,result)}

    def getCountries(self):
        cursor = self.getCursor()
        sql="SELECT * FROM country"
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result == None):
            return {}
        columns = self.columnsName('country')
        return [{columns:item for columns,item in zip(columns,item)} for item in result]

    def findCountryById(self, id):
        cursor = self.getCursor()
        sql="SELECT * FROM country WHERE countryid = %s"
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if (result == None):
            return {}
        columns = self.columnsName('country')
        return {columns:result for columns,result in zip(columns,result)}

    def findCountryByName(self, name):
        cursor = self.getCursor()
        sql="SELECT id FROM country WHERE countryname ILIKE %s"
        values = [ name ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if (result == None):
            return {}
        # columns = self.columnsName('country')
        # return {columns:result for columns,result in zip(columns,result)}
        return result[0]

    def updateTest(self, test):
        cursor = self.getCursor()
        sql = 'UPDATE test SET fname = %s, lname = %s, age = %s WHERE id = %s'
        values = [test[item] for item in test]
        values = values[1:] + [values[0]]
        print(values)
        cursor.execute(sql, values)
        self.db.commit()
        return f'Record has been updated - {test}'

    def updateActor(self, actor):

        values = [actor[item] for item in actor]
        country = values[-1]
        countryid = self.findCountryByName(country)
        values[-1] = countryid
        values = values[1:] + [values[0]]

        cursor = self.getCursor()
        # sql = 'UPDATE test SET fname = %s, lname = %s, age = %s WHERE id = %s'
        sql = '''
                UPDATE actor as a
                SET
                    actorname = %s,
                    actordob = %s,
                    actorgender = %s,
                    actorcountryid = %s
                FROM country as c
                WHERE a.id = %s 
                    AND a.actorcountryid = c.id;
                '''
        # sql = 'UPDATE actor a SET actorname = %s, actordob = %s, actorgender = %s, actorcountryid = %s FROM country c WHERE a.id = %s AND a.actorcountryid = c.id;'
        
        cursor.execute(sql, values)
        self.db.commit()
        return f'Record has been updated - {actor}'


    def deleteActor(self, id):
        cursor = self.getCursor()
        sql="DELETE FROM actor WHERE id = %s"
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        return f'Record with id : {id} has been deleted {values}'

actorDAO = actorDAO()

# conn = psycopg2.connect("dbname=db port=5432 user=usog password=usog")

# conn = psycopg2.connect(host="localhost", port=5432, database="db", user="usog", password="usog")

# Create a cursor object

# c = conn.cursor()
# sql = "SELECT country, population FROM countries WHERE population > %s ORDER BY population DESC"
# values = (100000000,)
# c.execute(sql,values)
# result = c.fetchall()
# for row in result:
#     # print(row)
#     s = ''
#     for item in row:
#         s += str(item) + ' : '
#     print(s)
#     #     print(item)


# the transaction is not completed until...
# db.commit()

# Close a cursor and connection so the server can allocate 
# bandwith to other requests
# c.close()
# conn.close()


# class StudentDAO:
#     db=""
#     def __init__(self): 
#         self.db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         #user="datarep",  # this is the user name on my mac
#         #passwd="password" # for my mac
#         database="datarepresentation"
#         )
#     def create(self, values):
#         cursor = self.db.cursor()
#         sql="insert into student (name, age) values (%s,%s)"
#         cursor.execute(sql, values)

#         self.db.commit()
#         return cursor.lastrowid

#     def getAll(self):
#         cursor = self.db.cursor()
#         sql="select * from student"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         return result

#     def findByID(self, id):
#         cursor = self.db.cursor()
#         sql="select * from student where id = %s"
#         values = (id,)

#         cursor.execute(sql, values)
#         result = cursor.fetchone()
#         return result
#     def update(self, values):
#         cursor = self.db.cursor()
#         sql="update student set name= %s, age=%s  where id = %s"
#         cursor.execute(sql, values)
#         self.db.commit()
#     def delete(self, id):
#         cursor = self.db.cursor()
#         sql="delete from student where id = %s"
#         values = (id,)

#         cursor.execute(sql, values)

#         self.db.commit()
#         print("delete done")

# studentDAO = StudentDAO()