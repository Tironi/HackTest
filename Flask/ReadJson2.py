
data = {
  "array": [
    {
      "id": "5",
      "param": [{ "1": "Samsung galaxy s6", "2": "Nokia lumia 1520" }]
    },
    { "id": "8" },
    { "id": "9" },
    { "id": "11" },
    {
      "id": "4",
      "param": [
        {
          "1": {
            "name": "Matteo Vedovati",
            "country": "Italy",
            "city": "Piazzatorre",
            "card": "mastercard",
            "month": "12",
            "year": "2022"
          },
          "2": {
            "name": "Matteo Vedovati",
            "country": "Italy",
            "city": "Piazzatorre",
            "card": "mastercard",
            "month": "12",
            "year": "2022"
          }
        }
      ]
    }
  ]
}

  
flag = False
for value in data.values():
    for mini in value:

        for elem in mini.values():
            #print(elem)
            if(flag == True):
                #print(elem)
                xi = json.dumps(elem)
                #print(xi)
                x = xi.split(",")
                print(x)
                print(len(x))
                flag = False
                
            if(elem == "5"):
                #print(elem)
                flag = True
               

            #count = count +1
        