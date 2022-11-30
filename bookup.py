def bookup(co,u):
  a="'select TOTAL from books where BCODE =%s"
  data=(co,)
  c=con.cursor()
  c.execute(a,data)
  myresult=c.fetchone()
  t=myresult[0]+u
  sql="update books set TOTAL %s where BCODE =%s"
  d=(t,co)
  c.execute(sql,d)
  con.commit()
  main()
