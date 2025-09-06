import net

query = "SELECT * FROM usuarios"
net.mycursor.execute(query)
result = net.mycursor.fetchall()

print(result)

for row in result:
    print(f"User: {row[1]}, Password: {row[2]}")


net.mydb.close()
