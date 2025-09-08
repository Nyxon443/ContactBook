def add_contact():
  name = input("enter contact name: ")
  phone = input("enter phone number: ")
  #the contact.txt is automatically created "a" manually appends in the file
  with open("contacts.txt" , "a") as file: 
      file.write(f"{name} , {phone}\n")
    print ("contact successfully added !!")
    
