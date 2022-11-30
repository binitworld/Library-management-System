def issueb():
  n=input("enter Name: ")
  r=input("'Enter Reg No: ")
  co=input("Enter Book Code: ")
  d=input("Enter Date: ")
  a="insert into issue values(%s,%s,%s,%s)"
  data=(n,r,co,d)
  c=con.cursor()
  c.execute(a,data)
  con.commit()
  print(">----------------------------------------<")
  print("Book issued to : ",n)
  bookup(co,-1)
