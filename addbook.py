def addbook():
  bn=input("Enter BOOK Name:")
  c=input("Enter BOOK Code:")
  t=input("Total Subject:")
  s=input("Enter Subject:")
  data=input(bn,c,t,s)
  sql='insert into books values(%s,%s,%s,%s)'
  c=con.cursor()
  c.execute(sql,data)
  con.commit() 
  print(">---------------------------------------------")
  print("Data Entered Successfully")
  main()
