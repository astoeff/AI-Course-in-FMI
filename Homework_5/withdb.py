import csv
import MySQLdb
mydb = mysql.connector.connect(
  database="covid19"
)
mycursor = mydb.cursor()

dataframe = csv.reader(file('total_cases.csv'))
print(dataframe)

for row in dataframe:
     mycursor.execute('INSERT INTO covid_per_day_per_country (date, World, Afghanistan, Albania, Algeria, Andorra") VALUES("%s", "%s", "%s", "%s", "%s", "%s")', row)
mydb.commit()
cursor.close()
