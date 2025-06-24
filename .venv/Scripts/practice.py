def fun():
    with open("23-06-2025.txt","r") as file:
          data = file.readlines()[1:] #it doesnt include first value ie temperatures

    #print(data)
    values = [float(item.strip('/n')) for item in data]
    print(values)
    average = sum(values) / len(values)
    return average

k = fun()
print(k)