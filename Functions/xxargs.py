# haven learnt how to pass in variable number of argument,
# it is possible to pass in a variable number of key args
# this is achieved with double asterix ** before the parameter

def my_car(**car):
    # this will print the whole car list (properties)
    # this is is in surrounded by curly brackets...they are known as topples
    print(car)

    #  to access a particular property use a bracket notation and the property key
    # example
    print(car["model"])
    print(car["engine"])
    # these two lines above will print the value of the keys


my_car(brand="Lexus", model="E350", color="darkred", engine="v6")
