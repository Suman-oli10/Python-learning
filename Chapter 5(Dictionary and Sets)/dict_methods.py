marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
}
#print(marks.items())
#print(marks.keys())
print(marks.update({"Bob": 88}))
print(marks)
print(marks.get("Alice"))