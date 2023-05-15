import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# design Recipe:
# 1) add two times together if seconds are equal to 60 or higher, then add to minutes and then do the same
# for minutes and add to hours
# 2) def time_add(T1:data.Time, T2:data.Time):
# 3) template of function
#     - get the values for time in the first value
#     - get the values for time in the second value
#     - add hours from both variables together
#     - add minutes from both variables together
#     - add seconds from both variables together
#     - if seconds is over 60 double divide it by 60 and add to minutes
#     - if minutes is over 60 double divide it by 60 and add to hours
# 4) test case:          def test_time_add_2(self):
#                            F_time = data.Time(5, 13, 50)
#                            S_time = data.Time(6, 20, 50)
#                            Total = Lab5.time_add(F_time, S_time)
#                            assert Total == (11, 34, 40)
# 5)

def time_add(T1:data.Time, T2:data.Time):
    T_hours = T1.hour + T2.hour
    T_minutes= T1.minute + T2.minute
    T_seconds = T1.second + T2.second
    if T_seconds >= 60:
        T_minutes += T_seconds // 60
        T_seconds = T_seconds % 60
    if T_minutes >= 60:
        T_hours += T_minutes // 60
        T_minutes = T_minutes % 60
    return (T_hours, T_minutes, T_seconds)

# Part 4
# design Recipe:
# 1) return true if input list is in descending order
# 2) def is_descending(List:list[float]):
# 3) template of function
#     - check if the list is empty and if so return none
#     - check if the next value in the list is greater than the previous one
#     - if so return false
#     - if the entire list is descending than return true
# 4) test case:           def test_is_descending_1(self):
#                             nums = [4, 3, 2, 1]
#                             Out_put = Lab5.is_descending(nums)
#                             assert Out_put == True
# 5)

def is_descending(List:list[float]):
    if len(List) == 0:
        return None
    for x in range(1, len(List)):
        if List[x] >= List[x-1]:
            return False
        return True




# Part 5
# design Recipe:
# 1)  returns index of the largest value in the input list that appears between the two provided indexes.
# 2) def largest_between(lst: list[int], lower: int, upper: int):
# 3) template of function
#     - if lower is greater than upper or lower is less than 0 or upper is greater than or equal to the
# length of the list then return None
#     - create max value and make it 0
#     - create max index which is set to none
#     - get the range made by lower and upper
#     - if the current value in the list is greater than the max_value then it becomes the new max value
#     - the index of that number is made the max_index
# 4) test case: def test_largest_between_1(self):
#                   numbers = [5, 2, 6, 3, 9, 1, 8, 4, 7, 0]
#                   lower = 3
#                   upper = 8
#                   expected = 7
#                   result = Lab5.largest_between(numbers, lower, upper)
#                   self.assertEqual(result, expected)
# 5)


def largest_between(lst: list[int], lower: int, upper: int):
    if lower > upper or lower < 0 or upper >= len(lst) or len(lst) == 0:
        return None
    max_value = lst[0]
    max_index = 0
    for i in range(lower, upper + 1):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i
    return max_index

# Part 6
# design Recipe:
# 1) get the index of the point in the list that is the farthest away from the point (0,0)
# 2) def furthest_from_origin(L:list[data.Point]):
# 3) template of function
#     - if length of the list is 0 return none
#     - make index equal to none and max_distance equal to 0
#     - cycle through each point of the list and get its distances
#     - if the distance is bigger than the current one make max_distance equal to it
#     - also make the index equal to its location
#     - return index
# 4) test case:     def test_furthest_from_origin_1(self):
#                    points = [data.Point(0, 0), data.Point(1, 1), data.Point(2, 2), data.Point(3, 3), data.Point(4, 4)]
#                       assert Lab5.furthest_from_origin(points) == 4
# 5)

def furthest_from_origin(L:list[data.Point]):
    if len(L) == 0:
        return None
    index = None
    max_distance = -1
    for i in range(len(L)):
        point = L[i]
        distance = (point.x ** 2 + point.y ** 2) ** 0.5
        if distance > max_distance:
            max_distance = distance
            index = i
    return index
