original_list = [1, 3, 6, 78, 35, 55, 88, 120, 12, 24, 35, 24, 88, 120, 155]
duplicate_values = []
seen = set()
for value in original_list:
    if original_list.count(value) > 1 and value not in seen:
        duplicate_values.append(value)
        seen.add(value)
print(duplicate_values)
