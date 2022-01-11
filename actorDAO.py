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


    # returns a list of the columns for a given table
    def columnsName(self, test):
        cursor = self.getCursor()
        sql = 'SELECT column_name FROM information_schema.columns WHERE table_name = %s'
        values = (test,)
        cursor.execute(sql, values)
        columns = cursor.fetchall()
        # columns = [e for item in columns for e in item]
        return [e for item in columns for e in item]


    # returns all actors and associated country name by left joining a country table based on country id 
    def getAll(self):
        cursor = self.getCursor()
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
        # columnsCountry = self.columnsName('country')

        return [{columns:item for columns,item in zip(columns,item)} for item in results]


    # inserts a new record into the table 
    def createActor(self, actor):

        # replaces the country name with country id to execute the insert statement
        values = [actor[item] for item in actor]
        country = values[-1]
        countryid = self.findCountryByName(country)
        values[-1] = countryid

        cursor = self.getCursor()
        sql = 'INSERT INTO actor (actorName, actordob, actorgender, actorcountryid) VALUES (%s, %s, %s, %s)'

        cursor.execute(sql, values)
        self.db.commit()
        return 'Record has been added - {actor}'


    # returns actor associated with a given id
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


    # returns record(s) with a given searching text - case insensitive due to ILIKE statement
    def findActorByText(self, text):
        # defines the searching pattern to match all the records containing a given text 
        text = '%' + text + '%'
        cursor = self.getCursor()
        sql = '''
                SELECT a.id, a.actorname, date(a.actordob)::text as actordob , a.actorgender, c.countryname as actorcountryname
                FROM actor a
                    LEFT JOIN country c 
	                    ON a.actorcountryid = c.id
                WHERE a.actorname ILIKE %s
                ORDER BY a.id ASC
                ;'''
        values = [ text ]
        cursor.execute(sql, values)
        result = cursor.fetchall()
        if (result == None):
            return {}
        columns = self.columnsName('actor')
        return [{columns:item for columns,item in zip(columns,item)} for item in result]


    # returns all countries
    def getCountries(self):
        cursor = self.getCursor()
        sql="SELECT * FROM country"
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result == None):
            return {}
        columns = self.columnsName('country')
        return [{columns:item for columns,item in zip(columns,item)} for item in result]


    # returns country associated with a given id
    def findCountryById(self, id):
        cursor = self.getCursor()
        sql="SELECT * FROM country WHERE id = %s"
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if (result == None):
            return {}
        columns = self.columnsName('country')
        return {columns:result for columns,result in zip(columns,result)}


    # returns country with a given country name - case insensitive due to ILIKE statement
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
        return str(result[0])


    # updates the record 
    def updateActor(self, actor):

        # replaces the country name with country id to execute the update statement
        values = [actor[item] for item in actor]
        country = values[-1]
        countryid = self.findCountryByName(country)
        values[-1] = countryid
        values = values[1:] + [values[0]]

        cursor = self.getCursor()
        
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
        
        cursor.execute(sql, values)
        self.db.commit()
        return f'Record has been updated - {actor}'


    # deletes the record from table
    def deleteActor(self, id):
        cursor = self.getCursor()
        sql="DELETE FROM actor WHERE id = %s"
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        return f'Record with id : {id} has been deleted {values}'

actorDAO = actorDAO()