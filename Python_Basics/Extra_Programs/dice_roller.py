import random

dice_faces = [1,2,3,4,5,6]

print(random.choice(dice_faces))

# or 

role = random.randint(0,5)
print(dice_faces[role])