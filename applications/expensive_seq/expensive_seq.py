expensive_dict = {}


def expensive_seq(x, y, z):
    key = (x,y,z)
    if key in expensive_dict:
        return expensive_dict[key]
    elif x <= 0:
        total = y + z
        expensive_dict[key] = total
        return total
    elif x > 0:
        total = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        expensive_dict[key] = total
        return total



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
