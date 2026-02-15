questions = [
    [
        "What is the capital of India?",
        "Mumbai", "Delhi", "Chennai", "Kolkata",
        "none", "Delhi"
    ],
    
    [
        "Which language is mainly used for Data Science?",
        "Python", "HTML", "CSS", "PHP",
        "none", "Python"
    ],
    [
        "Who is known as the Father of the Nation in India?",
        "Subhas Chandra Bose", "Jawaharlal Nehru", "Mahatma Gandhi", "Bhagat Singh",
        "none", "Mahatma Gandhi"
    ],
    [
        "What does CPU stand for?",
        "Central Processing Unit", "Computer Power Unit", "Central Program Unit", "Control Processing Unit",
        "none", "Central Processing Unit"
    ],
    [
        "Which planet is known as the Red Planet?",
        "Earth", "Venus", "Jupiter", "Mars",
        "none", "Mars"
    ]
]

levels = [1000, 2000, 3000, 4000, 10000]
money = 0

for i in range(len(questions)):
    question = questions[i]

    print("\n--------------------------------")
    print(f"Question for Rs. {levels[i]}")
    print(question[0])
    print(f"1. {question[1]}      2. {question[2]}")
    print(f"3. {question[3]}      4. {question[4]}")

    reply = int(input("Enter your answer (1-4): "))

    selected_option = question[reply]   # 1-4 maps to options

    if selected_option == question[6]:
        print(f"✅ Correct Answer! You won Rs. {levels[i]}")
        money = levels[i]
    else:
        print("❌ Wrong Answer!")
        break

print("\n================================")
print(f"🎉 Game Over! Total money won: Rs. {money}")
