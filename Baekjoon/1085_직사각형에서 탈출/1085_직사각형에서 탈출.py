x, y, w, h = map(int, input().split())
diff_list = [abs(x-w), abs(y-h), x, y]
print(min(diff_list))