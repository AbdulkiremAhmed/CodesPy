idmins = ["Huder","Nasur","Mohammed","Abdulkirem","Remah","Hagur","Nugwa","Ahmed"]
print(idmins)
yourname = str(input("please, input your name : ")).strip().capitalize()

if yourname in idmins:

   print(f"Hello {yourname} , welcom back!")
  
   status = str(input("what aer you doing ,\"update or delete\" ?")).capitalize()
   
   if status == "Update":
   
      newname = str(input("please, input a new name ! ")).capitalize()
      
      idmins[idmins.index(yourname)] = newname
      print(idmins)
      
      print(f"done update the name idmin  of {yourname} to {newname}")
      
   elif status == "Delete":
      idmins.remove(yourname)
      print(idmins)
      
      print(f"done delete the name idmin  of {yourname}")
else:
   
   print(f"excuse me {yourname} , you are not idmin")
   
   q = str(input("do you want to be idmin ? : \"yes or no\" : " )).strip()
   
   if q == "yes" or q == "Yes":
   
      idmins.append(yourname)
      
      print(idmins)
      
   elif q == "no" or q == "No":
   
      print(f"\'{yourname}\' you\'r can out")
   else : 
      print ("your input thing rong")
