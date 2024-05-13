# Create a function that given a list which represents street lights given as a parameter(l_street),
# determine if an outage has occurred. 
# A street with a total number of "F" greater than or equal to 2 returns "Outage",
# anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]
# Example Output: "Outage"

given_list = [ 'T', 'F', 'F', 'F' ]
def street_lights(l_street):
    for index in l_street:
        if index >= 2:
            return "Outage"
        else:
            return "Power"
print(street_lights(given_list))


# Additional Solution 
# def check_outage(l_street):
#     f_count = l_street.count('F')
#     if f_count >= 2:
#         return "Outage"
#     else:
#         return "Power"
# print(check_outage(['T', 'F']))