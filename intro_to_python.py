hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = ["hallway",hall,"kitchen",kit,"living room",liv,"bedroom",bed,"bathroom",bath]
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

downstairs = areas[0:6]
upstairs = areas[6:]

x = ["a", "b", "c", "d"]


print(areas[1])
print(areas[-1])
print(areas[5])
print(downstairs)
print(upstairs)
print(house[-1][1])