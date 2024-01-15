from random import choice

# this is mean calculator no a expectaton calculator,
# for expectaton,only need 6 step

sums = 0
count = 0

while True:
    x = input("Roll for ?: ")
    x = int(x)

    for _ in range(x):
        e = choice([x for x in range(1, 7)])
        sums += e
        count += 1
        print(f"µ: {sums/count:.5f} got: {e}")

    if x == 0:
        break
