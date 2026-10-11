import random

quotes=[
    "Believe in yourself.",
    "Never give uo.",
    "small steps lead to big results",
    "Learn from mistakes",
    "Dream big and work hard",
    "Success comes with patience",
    "Every day is new beginning"
    "stay positive and keep learning"
]

print("==== QUOTE GENERATOR ====")

while True:
    input("\n Press enter to get a quote...")

    quote=random.choice(quotes)
    print("\n Your Quote:")
    print(quote)

    choice=input("\n Want another quote?(yes/no):").lower()

    if choice not in ["yes","y"]:
        print("keep believing in yourself.Goodbye!")

        break