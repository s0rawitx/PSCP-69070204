start,end=input().split()
weight=float(input())
startPrice={"BKK" : {"CNX" : 10,"PKT" : 25},
            "CNX" :{"UBP" : 15 },
            "UBP" : {"BKK" : 20,"PKT" : 40},
            "PKT" : {"CNX" : 30}}

weightPrice={"BKK" : {"CNX" : 30,"PKT" : 50},
            "CNX" :{"UBP" : 40 },
            "UBP" : {"BKK" : 40,"PKT" : 70},
            "PKT" : {"CNX" : 60}}

try:
    total=startPrice[start][end]+(weightPrice[start][end]*weight)
    print(f"{total:.2f}")
except KeyError:
    print("Error")
