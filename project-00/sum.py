
""" 
Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.

Print the total sum with an appropriate message. """

num1: str = input("enter any number: ")
num2:str = input("enter any number: ")
num_1:int= int(num1)
num_2:int= int(num2)
sum:int= (num_1 + num_2)
print(f"the sum of two numbers is: {sum}")


print("***************************************************")
print("another way using python file to call the function")

def main():
   
    first_numb = input("Enter first number: ")
    second_numb = input("Enter second number: ")
    
    first_number = int(first_numb)
    second_number = int(second_numb)
 

    sum_result = first_number + second_number

    print(f"The sum of two integers is: {sum_result}")

if __name__ == '__main__': 
  main()



