import math
import csv
import random
import matplotlib.pyplot as plt


####################################### Setup #######################################

for_times = 100

path = './Datasets/data1.csv'

####################################### End of Setup #######################################

####################################### Vector Functions #######################################


def add(vector_a, vector_b):
    result = []
    
    for (i, j) in zip(vector_a, vector_b):
        result.append(i+j)
    
    return tuple(result)

def sub(vector, B):
    
    return add(vector, scal(B, -1))

def scal(vector, scaler):
    result = []
    
    for i in vector:
        result.append(scaler*i)
    
    return tuple(result)

def cord(vector):
    result = 0
    
    for i in vector:
        result = result + i*i
    
    return result

def zero(vector):   
    result = []
    
    for i in vector:
        result.append(0)
    
    return tuple(result)

# random function for centers of clusters
def random_point():
    point = []
    
    for (l, r) in bound:
        point.append(random.random()*(r-l) + l)
    
    return tuple(point)


####################################### End of Vector Functions #######################################

####################################### Csv Reader #######################################


points = []
dims = []
bound = []

with open(path, 'r') as f:
    csv_reader = csv.DictReader(f)
    frstln = True
    for row in csv_reader:
        if frstln:
            frstln = False
            for dim in row:
                dims.append(dim)
        point = [float(row[dim]) for dim in dims]
        point = tuple(point)
        points.append(point)

        

for i in range(len(dims)):
    max_tmp = None
    min_tmp = None

    for point in points:
        
        if max_tmp is None:
            max_tmp = point[i]
            min_tmp = point[i]
        
        else :
            min_tmp = min(min_tmp, point[i])
            max_tmp = max(max_tmp, point[i])
        
    bound.append((min_tmp, max_tmp))


####################################### End of Csv Reader  #######################################

####################################### C-means Function #######################################


centroids = []

def C_means(c, m):
    
    for i in range(c):
        centroids.append(random_point())
    
    # Debug
    # print(centroids)

    for n in range(for_times):

        u = []
        
        for i in range(len(points)):
            point  = points[i]
            row = []

            for j in range(c):
                
                centroid = centroids[j]
                sum = 0
                first = cord(sub(point, centroid))
                
                for ocentroid in centroids:
                    second = cord(sub(point, ocentroid))
                    sum = sum + (first/second) ** (1/(m-1))

                tmp_u = 1/sum
                row.append(uij)
            
            u.append(row)
        
        # change centers
        for i in range(c):
            centroid = centroids[i]
            
            cur = zero(centroid)
            sum = 0
            
            for j in range(len(points)):
                point = points[j]
                cur = add(cur, scal(point, u[j][i]**m))
                sum += u[j][i]**m
            cur = scal(cur, 1/sum)
            
            centroids[i] = cur
        
        # cost function
        cost = 0
        for i in range(len(points)):
            point = points[i]
            
            for j in range(c):
                centroid = centroids[j]
                cost += u[i][j]**m * cord(sub(point, centroid))
        
    return centroids, cost, u


####################################### End of C-means Function #######################################

####################################### Part1  #######################################


# cs = [1, 2, 3, 4, 5, 6, 7, 8]
# m = 2

# costs = []

# for c in cs:

#     tmp1, cost, tmp2 = C_means(c, m)
#     costs.append(cost)
    

# plt.plot(cs, costs)
# plt.xlabel('Cs')
# plt.ylabel('Costs')
# plt.show()


####################################### End of Part1 #######################################

####################################### Part2  #######################################


# c = 3
# ms = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# costs = []


# for m in ms:

#     tmp1, cost, tmp2 = C_means(c, m)
#     costs.append(cost)
    
# plt.plot(ms, costs)
# plt.xlabel('Ms')
# plt.ylabel('Costs')
# plt.show()


####################################### End of Part2 #######################################

####################################### Part3  #######################################


c = 3
ms = [2, 3, 4, 5, 6]
tmp = []
x = []
y = []
center_x = []
center_y = []

for m in ms:
    centroids, cost, u  = C_means(c, m)
    tmp.append((m, centroids, u))

for i in points:
    x.append(i[0])
    y.append(i[1])        
    
for m, centroids, u in tmp:
    
    for i in centroids:
        center_x.append(i[0]) 
        center_y.append(i[1]) 

    colors = []
    
    for i, point in enumerate(points):
        
        col = 0
        all = 0
        max_v, id = -1, -1
        
        for j in range(c):
            col += u[i][j]**m * (j*50/c)
            all += u[i][j]**m
            if u[i][j] > max_v:
                max_v, id = u[i][j], j
        col = col / all
        colors.append(col)

    plt.scatter(x, y, c=colors, cmap='viridis')
    plt.colorbar()
    plt.show()



####################################### End of Part3 #######################################

####################################### Part4  #######################################


# c = 4
# ms = [4]
# tmp = []
# x = []
# y = []
# center_x = []
# center_y = []

# for m in ms:
#     centroids, cost, u  = C_means(c, m)
#     tmp.append((m, centroids, u))

# for i in points:
#     x.append(i[0])
#     y.append(i[1])        
    
# for m, centroids, u in tmp:
    
#     for i in centroids:
#         center_x.append(i[0]) 
#         center_y.append(i[1]) 

#     colors = []
    
#     for i, point in enumerate(points):
#         max_v, id = -1, -1
        
#         for j in range(c):
#             if u[i][j] > max_v:
#                 max_v, id = u[i][j], j

#         colors.append(id*100/c)

#     plt.scatter(x, y, c=colors, cmap='viridis')
#     # for centers
#     plt.scatter(center_x, center_y, color='red', marker='o')
    
#     plt.colorbar()
#     plt.show()



####################################### End of Part4 #######################################
