
def people():
    import random
    lastName = ["West" , "Guzman" , "Tate" , "Macguire" , "Smith" , "Turner" , "Diaz" , "Pablo" , "Martin" , "Mayfield" , "Jackson" , "Franklin" , "Hernandez" , "Brooks" , "Pedroza" , "King" , "Sung" , "White" , "Waterson" , "Mendez"]
    firstName = ["Kanye" , "Agatha" , "Juan" , "Andrew" , "Imani" , "Louie" , "Marco" , "Chapo" , "Enrique" , "Carl" , "Ronaldo" , "Chicharito" ,  "Escobar" , "Emerson" , "Edward" , "Derik" , "Imani" ,"Aj" , "Walter" , "shakira"]
    email = ["fakeemail@gmail.com" , "fakeemail2@gmail.com" , "fakeemail3@gmail.com" , "notFake@gmail.com" , "Myfake@gmail.com" , "FakeFake@gmail.com" , "TotallyNotReal@gmail.com" , "MyEmailisFalse@gmail.com" , "EmailIsFake@gmail.com" , "1234@gmail.com" , "Wakeup@gmail.com" , "12fakemail@gmail.com" , "fakeemail13@gmail.com"  ,"fakeemail14@gmail.com" , "Ye4prez@gmail.com" , "fakeemail16@gmail.com" , "heisenberg@gmail.com" , "NotElchapo@gmail.com" , "RealestBot@gmail.com" , "email@gmail.com"]
    zip = [10001 , 10069,  10420 , 111111 , 100121 , 974374 , 972991 , 123262 , 962745 , 174294 , 954324 , 999999 , 916493 , 1284337 , 129436, 916438 , 853273 , 846502 , 928441 , 638956]
    city = ["Dallas" , "Fort Worth", "Chicago" , "Miami" , "Portland" , "Clevland" , "Houston" , "Laredo" , "El paso" , "Arlington" , "San Antonio" , "New York" , "San Diego" , "Las Vegas" , "Philadelphia" , "Boston" , "Seattle" , "Austin" , "Portland" , "Albuquerque"]
    address = [7263 , 1673 , 7423 , 8462 , 1456 , 9643 , 1234 , 4321 , 6284 , 8362 , 5237 , 1424 , 4532 , 8362 , 6381 , 8365 , 8253 , 3424 , 6262 , 9911]
    phone = [4628374615 , 1847362986 , 1984563782 , 9724652915 , 6342871592 , 99351628462 , 9118374536 , 8453917352 , 1936582537 , 9037562718 , 1746235294 , 8374650192 , 1234567899, 7254918427 , 1243657891, 9876543211 , 8461942683 , 1844638296 , 2648154832 , 1746294528]
    x = 0
    while x!=5:
        print(lastName[random.randint(0,19)] , firstName[random.randint(0,19)], email[random.randint(0,19)] , zip[random.randint(0,19)] , city[random.randint(0,19)] , address[random.randint(0,19)] , phone[random.randint(0,19)])
        x=x+1

