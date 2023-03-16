import time

def speedtyping_test():
    
    # Setting the text for user to type in order to calculate speed.
    text = "This codeclause code in python development internship."
    print("Type the above text fast and as accurately as possible:\n")
    print(text + "\n")
    
    # Starting the timer form the first word entered.
    start_time = time.time()
    
    # Getting user input for the text
    user_input = input("Type the text here: ")
    
    # Ending the timer after user writes the text.
    end_time = time.time()
    
    # Calculate the elapsed time between start and end.
    elapsed_time = end_time - start_time
    
    # Calculate the accuracy of user's writing.
    num_correct = 0
    for i in range(min(len(text), len(user_input))):
        if text[i] == user_input[i]:
            num_correct += 1
    accuracy = num_correct / len(text) * 100
    
    # Printing the results
    print("\nTime elapsed: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))

speedtyping_test()
