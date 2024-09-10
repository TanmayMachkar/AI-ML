import argparse

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("number1", help = "first number")
    # parser.add_argument("number2", help = "second number")
    # parser.add_argument("operation", help = "operation")
    
    # args = parser.parse_args()
    
    # print(args.number1)
    # print(args.number2)
    # print(args.operation)
    
    # n1 = int(args.number1)
    # n2 = int(args.number2)
    # result = None
    # if args.operation == "add":
    #     result = n1 + n2
    # elif args.operation == "sub":
    #     result = n1 - n2
        
    # print("Result: ", result)
    
    #Output:
    # python CommandLineArgumentProcessingUsingArgparse.py 4 5 add
    # 4
    # 5
    # add
    # Result:  9
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help = "first number") #-- => optional argument
    parser.add_argument("--number2", help = "second number")
    parser.add_argument("--operation", help = "operation", choices = ["add", "sub"]) #choices => restricts arguments to operation
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "sub":
        result = n1 - n2
    else:
        print("Unsupported operation")
        
    print("Result: ", result)
    
    #Output:
    # python CommandLineArgumentProcessingUsingArgparse.py --number1 4 --number2 5 --operation sub
    # 4
    # 5
    # sub
    # Result:  -1
    
    # python CommandLineArgumentProcessingUsingArgparse.py --number1 4 --number2 5
    # 4
    # 5
    # None
    # Unsupported operation
    # Result:  None