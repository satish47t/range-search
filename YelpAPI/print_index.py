def print_index():
    file = open("commands.txt", "w")
    
    for i in range (0, 50):
        j = i * 20 + 3
        str1 = "sample_1.py --term=\"dinner\" --location=\"San Jose, CA\" --offset=\"" + str(j) + "\" #G:\\Fall15\\Asynchronous\\Project\\YelpAPI\\San Jose\\output_" + str(i) + ".txt\n"
        file.write(str1)
    
print_index()