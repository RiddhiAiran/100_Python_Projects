import random


# Who will Pay the Bill : Pick Randomly
friends = ["Avi","Prachi","Ritika","Neha","Muskan","Riddhi"]

#Solution 1
print(f"{random.choice(friends)} will pay the bill!")

#Solution 2
random_index = random.randint(0,5)
print(f"{friends[random_index]} will pay the bill!")