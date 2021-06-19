def test_function():
    return 1, "asd", {"name": "John", "id": 20}

res = test_function()
print type(res) # tuple

# Numbers of return value doesn't match
# item1, item2 = test_function()
# print type(item1), item1
# print type(item2), item2

item1, item2, item3 = test_function()
print type(item1), item1
print type(item2), item2
print type(item3), item3