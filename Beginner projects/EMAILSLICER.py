"""email slicer"""

#email name request
#split the mail using the @, the 1th part username 2th - be saves as domain
#splice domain using .


def main():
    print("welcome to the program to organise your string")
    print("")
    a_input = input("Input your email: ")
    (username, domain) = a_input.split("@")
    (domain,extension) = domain.split(".")
    #put here domain-country based dependencies
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
while True:
    main()
