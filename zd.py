# To-do List

davalebebi = []

print("1. დავალების დამატება")
print("2. დავალების წაშლა")
print("3. დავალებების ნახვა")
print("4. დავალებების რაოდენობა")
print("5. გამოსვლა")
while True:
    user_answer = int(input("აირჩიე მოქმდება (რიცხვებით!): "))

    if user_answer == 1:
        radavamato = input("რა დავამატო?: ")
        davalebebi.append(radavamato)

    elif user_answer == 2:
        rawavshalo = input("რა წავშალო?: ")
        davalebebi.remove(rawavshalo)
    
    elif user_answer == 3:
        print("ეს არის შენი To-do ლისტი")
        print(davalebebi)

    elif user_answer == 4:
        dl = len(davalebebi)
        print(f"ესაა შენი დავალებების რაოდენობა - '{dl}'")

    elif user_answer == 5: 
        break

