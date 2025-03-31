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


#print(areas[1])
#print(areas[-1])
#print(areas[5])
#print(downstairs)
#print(upstairs)
#print(house[-1][1])



import numpy as np

#------------------
### NumPy practice:
#------------------

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2

#print(bmi)
#print(bmi[1])
#print(bmi > 23)
#print(bmi[bmi > 23])

python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

#print(python_list + python_list)
#print(numpy_array + numpy_array)


x = np.array([3, 4, True, False, "5.2"])
#print(x)



### N Dimensional Array / 2D NumPy Arrays:
np_height2 = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight2 = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

#print(type(np_height2))
#print(type(np_weight2))


np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

#print(np_2d)
#print(np_2d.shape)
#print(np_2d[0])
#print(np_2d[0][2])
#print(np_2d[0, 2])
#print(np_2d[:, 1:3])
#print(np_2d[1, :])
#print(np_2d[1:,2:])


np_heights = np.array([[1.60,1.75],[1.56,1.70],[1.49,1.68]])
#print(np.mean(np_heights[:,0]))


costs = np.column_stack(([3, 2, 1, 3],
                         [7, 6, 6, 5]))
mean_costs = np.mean(costs[:, 0])
#print(mean_costs)


r_height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
r_weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((r_height, r_weight))

#print(np.mean(np_city[:, 0]))
#print(np.median(np_city[:, 0]))
#print(np.corrcoef(np_city[:, 0], np_city[:, 1]))
#print(np.std(np_city[:, 0]))