
def bmiCalc(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)

    # Display BMI
    print("BMI = " + str(bmi))

    # Determine BMI classification
    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif bmi <= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1


def main():
    height = float(input("Enter your height (m): "))
    weight = float(input("Enter your weight (kg): "))

    bmiCalc(height=height, weight=weight)


if __name__ == "__main__":
    main()
