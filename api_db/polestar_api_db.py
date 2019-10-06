import os
import sqlite3
import pandas as pd

positions_data_path = "positions.csv"
column_names = ["imo_number","timestamp","latitude","longitude"]
positions_data = pd.read_csv(positions_data_path,header=None,names=column_names)
ship_data = [
 {'imo_number':9632179,'ship_name':'Mathilde Maersk'},
 {'imo_number':9247455,'ship_name':'Australian Spirit'},
 {'imo_number':9595321,'ship_name':'MSC Preziosa'}
]

#Remove existing table
if os.path.exists('polestar.db'):
    os.remove('polestar.db')

#Create a new database
conn = sqlite3.connect("polestar.db",check_same_thread=False)

#Loading ships-imo details in the ships table
conn.execute('CREATE TABLE ships (imo_number INTEGER, ship_name VARCHAR(256))')

for i in range(len(ship_data)):
    conn.execute('INSERT INTO ships VALUES (?,?)', (ship_data[i].get('imo_number'),ship_data[i].get('ship_name')))


#Loading data/csv to the positions table
positions_data.to_sql('positions1',conn, dtype={
 'imo_number':'INTEGER',
 'timestamp':'DATETIME',
 'latitude':'VARCHAR(256)',
 'longitude':'VARCHAR(256)'
})



#Queries to fetch data
def getShips(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def getPositions(query,imoNumber):
    print("QUery :"+query)
    print(type(imoNumber))
    cur = conn.cursor()
    cur.execute(query,imoNumber)
    rows = cur.fetchall()
    return rows
