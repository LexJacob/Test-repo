#to call items from a different file use import Functions

import Functions


def main():
    print(Functions.concat('str', 'ing'))

    #list
    myFirstList = [1, 2, 3, 4, 5, 6]

    #dictionary          
    myFirstDictionary = {
        #key      :  value
        "day one" : "Monday", 
        "day two" : "Tuesday", 
        "day three" : "Wednesday"
        }
    
    print(myFirstDictionary["day three"])

if __name__ == "__main__":
    main()