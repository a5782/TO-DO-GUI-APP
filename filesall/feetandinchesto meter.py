feet_inches = input("enter a feet and  inches :")


def convert(feet_inches):
    k = feet_inches.split(" ")
    feet = float(k[0])
    inches = float(k[1])
    meters = feet*0.3048 + inches *0.0254
    return f"{feet} feet, {inches} inches is equal to {meters} meters"


print(convert(feet_inches))
