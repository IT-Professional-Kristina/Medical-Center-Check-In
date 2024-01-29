

def greet(username):
    result = (f"Hello")
    return result

username = input("what is your name?")
greet_result = greet(username)
print(greet_result)

result = (username) 
print(result  + "" ,  "Welcome to The Medical Center!")


Departments = {
    "Neurology":{
        "Doctors":["Dr. Rashad Wallace", "Dr. Shirley Templeton", "Dr.Bryson Taylor"],
        "Building": "Neuro Building C",
        "Suite": "Suite 303"},
    "Hematology":{
        "Doctors": ["Dr. Maureen Lansky", "Dr. Bethany Mauro", "Dr. Nelson Yancy"],
        "Building": "Hema Buidling B",
        "Suite": "Suite 203"}
               }
    
request = input("Please select a Department? Neurology or Hematology")
print(request)

if request in Departments:
    print(Departments[request])
else:
    print("Invalid Department selection. Please try again.")


Questionaire_message = input("Please read the Pre-screen Before Entering Office")
print(Questionaire_message)

question_statement = [
        {"Question 1": "Have you or anyone in your household been ill within the past week eg..Fever, Cough, Body Aches?"},
        {"Question 2": "Please have your Photo ID and Insurance Card ready for verification?"},
                    ]       
print(question_statement)

print(input("If you answered Yes, to Question 1 Please Make sure you are wearing a Mask! Thank you!"))

print(input("Make sure you have your Parking Ticket."))


            


