#ap program
#NO CODE IS RUN HERE,IT IS TELLING US WHAT WE WILL DO LATER
#HERE WE WILL DEFINE OUR FUNCTIONS
#THIS PRINT THE MAIN MENU AND PROMPTS FOR A CHOICE

def menu():
   #print what options you have
   print "'welcome to ap.py"
   print "your options are:"
   print ""
   print "1)a+(n-1)*d"
   print "2)11/2*{2*a+(n-1)*d}"
   print "3)Quit ap.py"
   print ""
   return input("choose your option:")

#THIS ap1 GIVEN
def ap1(a,d,n):
    print a,"+","(",n,"-",1,")","*",d,"=",a+(n-1)*d
#THIS ap2 GIVEN
def ap2(a,d,n):
    print "11/2","*","{","2","*",a,"+","(",n,"-","1",")","*",d,"}","=",11/2*{2*a+(n-1)*d}
#NOW THE PROGRAM REALLY STARTS,AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
  choice = menu()
  if choice == 1:
      ap1(input("a:"),input("d:"),input("n:"))
  elif choice == 2:
      ap2(input("a:"),input("d:"),input("n:"))
  elif choice == 3:
      loop = 0
print "thank u for using studyphysics.py!"
print "made by Ro706"

#NOW THE PROGRAM REALLY FINISHES
