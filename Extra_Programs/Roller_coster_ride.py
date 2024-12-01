def Roller_Coster_ride():
    print("Welcome to the Rollercoster! ")
    height = int(input("What's Your Height (in cms) : "))
    Bill = 0
    if height >= 120:
        print("You can ride the Rollercoster.")
        age = int(input("What's Your Age : "))
        if age < 12:
            Bill += 5
            print("child Tickets Are : $5.")
        elif age >= 12 and age < 18:
            Bill += 7
            print("Youth Tickets Are : $7.")
        elif age >= 18:
            Bill += 12
            print("child Tickets Are : $12.")
        elif age >= 45 and age <= 55:
            print("Everything is going to be okay! Have a Free Ride on us.")
        else:
            print("Not Valid Input")
        Pic = input("Do you want to have a photo take? Type y for Yes and n for No. ").lower()
        if Pic == 'y':
            Bill += 3
        print(f"The Total Bill is : {Bill}")
    else:
        print("Sorry, You have to grow taller before you ride.")
        
Roller_Coster_ride()
