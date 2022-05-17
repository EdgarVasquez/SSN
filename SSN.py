if __name__ == '__main__':
    print("Write your SSN Code")
    SSNCODE = input()
    if len(SSNCODE.replace("-", "")) == 9:
        number = SSNCODE.split("-")
        if len(number[0]) == 3:
            if int(number[0]) != 000 and int(number[0]) != 666:
                if int(number[0]) > 999 or int(number[0]) < 900:
                    if len(number[1]) == 2:
                        if int(number[1]) > 00 and int(number[1]) < 100:
                            if len(number[2]) == 4:
                                if int(number[2]) > 0000 and  int(number[2]) < 10000:
                                    print("SSN CODE VALIDATED")
                                else:
                                    print("the last part must be between 0001 and 9999")

                            else:
                                print("The len of the last part must be 4 digits")

                        else:
                            print("The second part must be betweeen 01 and 99")

                    else:
                        print("The len of the second part must be 2 digits")


                else:
                    print("The First part can't be between 900 and 999")

            else:
                print("The first part can't be 000 or 666")
        else:
            print("The len of the first part must be 3 digits")
    else:
        print("The SSN Code len must be 9 digits ")

