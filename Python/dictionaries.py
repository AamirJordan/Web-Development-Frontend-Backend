my_stuff = {"key1":"value","key2":"value2"}
print(my_stuff)

my_stuff = {"key1":"value","key2":"value2"}
print(my_stuff["key2"])

my_stuff = {"key1":123,"key2":"value2","key3":{"123":[1,2,3]}}
print(my_stuff)

my_stuff = {"key1":123,"key2":"value2","key3":{"123":[1,2,'grabMe']}}
print(my_stuff["key3"]["123"][2])

my_stuff = {"key1":123,"key2":"value2","key3":{"123":[1,2,'grabMe']}}
print(my_stuff["key3"]["123"][2].upper())







my_stuff = {"lunch":"pizza","breakfast":"eggs"}
print(my_stuff)


my_stuff = {"lunch":"pizza","breakfast":"eggs"}
print(my_stuff["lunch"])


my_stuff = {"lunch":"pizza","breakfast":"eggs"}
my_stuff["lunch"] = "burger"
print(my_stuff["lunch"])
print(my_stuff)


my_stuff = {"lunch":"pizza","breakfast":"eggs"}
my_stuff["lunch"] = "burger"
my_stuff["dinner"] = "chowmein"
print(my_stuff)
print(my_stuff["dinner"])
