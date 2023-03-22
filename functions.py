# Functions
#define function
def function_name():
    print(2+2)


# call function
function_name()

# with parameters
def function_2(parameter):
    print(parameter + 2)


function_2(5)

def function_3(num_1=5, num_2=9):
    print(num_1 * num_2)


function_3()
function_3(2)
function_3(6, 8)
print(function_3()) # None because value isn't being returned

# with return
def function_4(num_1=7, num_2=8):
    return num_1 * num_2

function_4()
print(function_4())
print(function_4() + 44)
