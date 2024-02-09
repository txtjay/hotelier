# onion= int(input("enter number of onions"))
# # tomato= input(int("enter number of tomato"))

# def onions():
#     onion= onion-1
#     print(onion)
#     return


# chicken_tikka= onions
# print(chicken_tikka)

# def onions():
#     global onion
#     onion= onion-1
#     return onion

# def chicken_tikka():
#     chicken_tikka1=onion

# while onion > 0:
#     print("onions left", onion)
#     onions()
#     choice= input("press o or t")
#     if choice == 'o':
#         chicken_tikka()
# __________________________________________________________________________________________________________________________________________


onion= int(input("onions"))
tomato= int(input("tomatos"))


# ___________________________________________________________________________________________________________________________________________

def onions():
    global onion
    buyonions= int(input("enter number of onions"))
    onion = buyonions+onion
    return onion

def tomatos():
    global tomato
    buytomatos= int(input("enter number of onions"))
    tomato = buytomatos+tomato
    return tomato


def chicken_tikka():
    global onion, tomato
    onion -= 1
    tomato -= 2
    return onion, tomato


def chicken():
    global onion, tomato
    onion -= 2
    tomato -= 3
    return onion, tomato

while onion > 0:
    print("onions left", onion)
    print("tomato left" , tomato)
    choice= input("press o or t or b")
    if choice == 'o':
        chicken_tikka()

    elif choice =='t':
        chicken()

    elif choice =='b':
        onions()
        tomatos()
