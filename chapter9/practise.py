# f = open("poem.txt")
# content = f.read()
# if ("twinkle" in content):
#     print("twinkle is present")
# else:
#     print("twinkle is not present")
    
# print("📄 File content:\n", content)
# f.close()

import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)  # generate a random score

    # Read the existing high score
    try:
        with open("myscore.txt", "r") as f:
            myscore = f.read()
            myscore = int(myscore) if myscore else 0
    except FileNotFoundError:
        myscore = 0  # If file doesn't exist, default highscore is 0

    print(f"Your Score: {score}")

    # Compare and update if current score is higher
    if score > myscore:
        print("🎉 New High Score!")
        with open("myscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"💡 High Score remains: {myscore}")

    return score

game()
