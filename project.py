#project for creating a database to send the result automatically to the students mail or phone.
with open("data.csv") as file :
  a=file.read()
  a=a.splitlines()
  temp_data=[]

  for _ in a:
    temp_data.append(_.split(","))
  a=temp_data.copy()

  for _ in a:
    print(_)

 
