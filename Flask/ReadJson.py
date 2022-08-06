import json

f = open("JsonMockup.json")
data = json.load(f)
  
#print(data)
#print(type(data))
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
        