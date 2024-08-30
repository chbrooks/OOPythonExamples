
import argparse

# create a parser
if __name__=="__main__" :
    parser = argparse.ArgumentParser(description="A sample program")
    parser.add_argument("filename")
# let's add a -switch-style option. If this option is present,
# we'll store the corresponding name as 'true' in the object.
    parser.add_argument('-v', '--verbose', action="store_true")

    ## let's add a name/value pair = the value attached to --save will be stored
    ## in args.save. We've also added a custom help string.
    parser.add_argument("--save", type=str, help="Saves a specified pickle file at the file path.")

    ## parse the command line and return an object containing the arguments.
    args = parser.parse_args()
    print(args.filename)
    ## check to see if verbose is present.
    if args.verbose :
        print("verbose is turned on")
    if args.save :
        print(args.save)