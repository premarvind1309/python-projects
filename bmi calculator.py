#bmi = weight/(height)**2

times = int(input("enter no of users"))
for i in range(times):
    name= input("enter your name:")
    print(name)
    weight =  float(input("enter your weight"))
    height = float(input("enter your height"))
    if(weight >0 and height > 0):
        bmi = weight/(height)**2
        print(bmi)

        if(bmi< 18.5):
            print("UnderWeight")
        elif(bmi >= 18.5 and bmi <=24.9):
            print("Normal weight")
        elif(bmi>=25 and bmi <=29.9):
            print("Over weight")

        elif(bmi>=30):
            print("Obesity")
    else:
        print("invalid inputs")
