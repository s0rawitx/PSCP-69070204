'''dadad'''
def main():
    '''pizza'''
    member=int(input())
    atleast=int(input())
    piece=int(input())
    require=member*atleast
    pizza=require/piece
    if pizza != int(pizza):
        pizza=int(pizza)+1
    remain=(pizza*piece)-require
    print(require)
    print(int(pizza))
    print(int(remain))
main()
