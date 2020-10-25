name = input("enter your name ")
# hiren devda         also writte this way (equalent)  normal way to count
 # name.count("h")  , name.count(name[0]) =1
 # name.count("i")  , name.count(name[1]) =1
 # name.count("r")  , name.count(name[2]) =1
 # name.count("e")  , name.count(name[3]) =2
 # name.count("n")  , name.count(name[4]) =1
 # name.count("d")  , name.count(name[5]) =2
 # name.count("e")  , name.count(name[6]) =2
 # name.count("v")  , name.count(name[7]) =1
 # name.count("d")  , name.count(name[8]) =2
 # name.count("a")  , name.count(name[9]) =1

 # output
 # name[0] = h : 1
 # i : 1
 # r : 1
 # e : 2 
 # n : 1
 # d : 2
 # e : 2 (again repeat e show 2 times) aam karis toh) sigal ne be var batav se 
 # v : 1
 # d : 2 (again repeat thase aa) mate use kar su temporary variable temp_var = ""
 # a : 1
temp_var = ""
i = 0 #(work as indexing)
while i < len(name):   #(name of len - 1 = 9 coz start with zero)
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")  # i = 0 (also incresing value of i) # name[i] is charecter (example ;- (f"hello {name}") hello is charecter
    i+=1   
 

 # temporary variable
 # temp_var = "e" ( loop repeat chale se jo temp_var mai char e che toh again count nhi kare
 # before we use in keyword now we use not in
 #if name[i] not in temp_var:
 # now store variable like temp_var = "e" but we store temp_var += name[i]
