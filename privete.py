def query():  return "SELECT * FROM priveteType"
def query1(id): return "SELECT * FROM priveteType WHERE id = ?", (id,)
def query2(id): return "SELECT * FROM priveteType WHERE id != ?", (id,)


    