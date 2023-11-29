test_data = (1, 2, 3)

if isinstance(test_data, int):
    print("Integer!")
elif isinstance(test_data, float):
    print("Float!")
elif isinstance(test_data, str):
    print("String!")
elif isinstance(test_data, dict):
    print("Dictionary!")
else:
    print("Something Else!")
