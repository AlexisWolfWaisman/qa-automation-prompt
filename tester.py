from name_checker_api_tests import NameCheckerAPI
from Database_handler import  Db_connection

def run_diagnose():
    name_checker = NameCheckerAPI()
    name_checker.diagnose_system_errors()

def uptime_checker(p_totalTime):
    from datetime import datetime
    dataB = Db_connection()  
    counting_by_records =  (dataB.count_OK_records() / dataB.count_records()) * 100
    records = dataB.select_uptime_analisis()
    records = [(record[0],record[1].split()[-1]) for record in records]    
    records = [(record[0],datetime.strptime(record[1], "%H:%M:%S")) for record in records]
    intervals = [ (records[i][1] - records[i-1][1]).seconds for i in range(1,len(records)) if records[i-1][0] == 200]
    counting_by_time = sum(intervals)/p_totalTime * 100
    return counting_by_records,counting_by_time
    

def test_uptimePerfo():
    totalTime = 60
    db_conn = Db_connection()
    name_checker = NameCheckerAPI()
    db_conn.reset_table()
    name_checker.populate_database(totalTime)
    uptimeByrecords,uptimeBySeconds = uptime_checker(totalTime)
    print(f"uptime per total number of records  : {uptimeByrecords} %")
    print(f"System active time: {uptimeBySeconds} seconds out of {totalTime} seconds")    

if __name__ == "__main__":
    #first of all we will check the uptime performance
    test_uptimePerfo()
    # After that we will try to find the pattern
    NameCheckerAPI().diagnose_system_errors()
    
    
