from fixtures.mydb import MyDB

import pytest

@pytest.fixture(scope="module")
def cur():
    print("Setting Up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("Closing DB")
# def setup_module(module): #initiate connection
#     global conn
#     global cur
#     db = MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#
# def teardown_module(module): #close connection
#     cur.close()
#     conn.close()

def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789

