name = input("Enter you name ")

print(f"Good Afternoon {name}")

#problem2

letter = ''' Dear <|Name|>
            You are Selected 
            <|Date|> '''

print(letter.replace("<|Name|>", "Rahul".replace("<|Date|>", "10/10/2024")))