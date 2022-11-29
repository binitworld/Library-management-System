def submit():
  n=input("Enter Name: ")
  r=input("Enter Reg No: ")
  co=input("Enter Book Code: ")
  a="insert into submit values(%s,%s,%s,%s)"
  data=(n,r,co,d)
  c=con.cursor()
  c.execute(a,data)
  con.commit()
  print(">--------------------------------------------")
  print("Book Submitted from: ",n)
  bookup(co,1)