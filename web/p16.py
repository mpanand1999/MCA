#Sort the dictionary in ascending and descending order.

# Sample dictionary
my_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4}
print("Original list:", my_dict,"\n")


# Sort in ascending order based on keys
asorted_dict = dict(sorted(my_dict.items()))
print("Ascending order:", asorted_dict,"\n")


# Sort in descending order based on keys
dsorted_dict = dict(sorted(my_dict.items(), reverse=True))
print("Descending order:", dsorted_dict,"\n")
