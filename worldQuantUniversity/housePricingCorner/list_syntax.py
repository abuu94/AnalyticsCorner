print('Notes on Syntax')

house_0_list = [115910.26, 128, 4]
print("house_0_list type:", type(house_0_list))
print("house_0_list length:", len(house_0_list))
house_0_list


# house per meter sqr
house_0_price_m2 = house_0_list[0] / house_0_list[1]
house_0_price_m2

# append house_0_price_m2 to house_0_list
house_0_list.append(house_0_price_m2)

#nested list and for loop
houses_nested_list = [[115910.26, 128.0, 4.0],[48718.17, 210.0, 3.0],[28977.56, 58.0, 2.0],[36932.27, 79.0, 3.0],[83903.51, 111.0, 3.0],]
for house in houses_nested_list:
  price_m2=house[0]/house[1]
  house.append(price_m2)
houses_nested_list

