while True:
    print("Press q to quit")
    a =input("Enter a number:")
    if a=='q':
        break
    try:
        print("Typing..")
        a=int(a)
        if a>6:
            print("You entered a number greater than 6")
    
    # except ValueError as e:
    #     # print(e)
    #     print(f"Your input1 resulted in an error: {e}")

    except ZeroDivisionError as e:
        # print(e)
        print(f"Your input2 resulted in an error: {e}")

    # except Exception as e:
    #     # print(e)
    #     print(f"Your input3 resulted in an error: {e}")

    except :
        # print(e)#throw an error because e is not defined..
        print("Another Exception..")

print("Thanks for playing this game..")                
      
