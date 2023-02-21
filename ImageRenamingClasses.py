class BinaryNameAssigner:
    def __init__(self, array):
        self.array = array

    def assign(self):
        # create an empty list to store assigned names
        assigned_names = []  
        # iterate over each element of the array
        for i in range(len(self.array)):  
            # prompt the user for a name
            name = input(f"Enter name for part occurance {i+1}: ")
            # add the name to the list of assigned names
            assigned_names.append(name)  
        # return the list of assigned names    
        return assigned_names

#array = [0, 1, 0, 1, 1, 0]
#bna = BinaryNameAssigner(array)  # create a BinaryNameAssigner object with the array
#assigned_names = bna.assign()  # call the assign method to assign names to each occurrence
#print(assigned_names)  # print the list of assigned names