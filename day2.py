 #list --> [], dic-->{}, tuple-->()
 #firstName-->pascalcase, first_name_of-->snakecase,

 #_set
my_set ={"suprekshya","suprekshya","karki"}

#
is_raining = True

if is_raining:
    print("carry an umbrella")
else:
    print("Dont carry umbrella") 

    #temperature = 23 
    # t>30-->hot weather
    # t>20-->normal weather
    # t>0-->cold weather 

    # the gap is called intendation
     
temperature = 20
if temperature>30:
    print("hot weather")

elif temperature>20: 
    print("normal weather")  

else:
    print("cold weather")

#loop( loop ko lagi for in use garinxa)
days = ["sunday","monday","tuesday"]
for hi in days:
    print(hi)

    #function
    def sayHello(name):
        print(f"Hello{name}")

    sayHello("suprekshya")




    #days = ["sun","mon","tue","wed"]
    #make a function that prints each day by looping using for in

def print_days(days):
    for day in days:
        print(day)
days = ["sun", "mon", "tue", "wed"]
print_days(days)