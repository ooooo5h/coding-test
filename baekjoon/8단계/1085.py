x,y,w,h = map(int, input().split())

a = [h-y, y, x, w-x]
# t = h - y
# b = y
# l = x
# r = w - x

print(min(a))