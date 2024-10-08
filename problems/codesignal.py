# question 3

# def text_editor(operations):
#     text = []  # To store the text at the current cursor position
#     stack = []  # To store the undo operations
#     res = []  # To store the state of the text after each command
    
#     for command in operations:
        
#         if command.startswith("INSERT"):
#             # Extract the text to be inserted
#             _, insert_text = command.split(" ", 1)
#             text.extend(insert_text)  # Append the text to the end
#             stack.append(("INSERT", insert_text))  # Record the operation for undo
#         elif command == "BACKSPACE":
#             if text:
#                 removed_char = text.pop()  # Remove the last character
#                 stack.append(("BACKSPACE", removed_char))  # Record the operation for undo
#         elif command == "UNDO":
#             if stack:
#                 last_command, value = stack.pop()
#                 if last_command == "INSERT":
#                     # Undo the insert by removing the same number of characters
#                     for _ in range(len(value)):
#                         text.pop()
#                 elif last_command == "BACKSPACE":
#                     # Undo the backspace by re-adding the removed character
#                     text.append(value)
        
#         # Append the current state of the text to the result
#         res.append("".join(text)) 
    
#     return res

def text_editor(operations):
    res = []
    stack = [] # save the states of successful backspace and insert changes
    for operation in operations:
        op = operation.split(" ")
        op_type = op[0]
        if op_type == "INSERT":
            if res:
                res.append(res[-1] + op[1]) 
                stack.append(res[-1])
            else:
                res.append(op[1])
                stack.append(res[-1])
        elif op_type == "BACKSPACE":
            if res:
                old_text = res[-1]
                res.append(old_text[0:len(old_text) - 1]) 
                stack.append(res[-1])
        else:
            # undo it
            if stack:
                stack.pop(-1)
                if stack:
                    res.append(stack[-1]) # popping twice is wrong
                else:
                    res.append("")
        print(stack, "\n", res)
    return res
        
operations = ["INSERT hello", "INSERT world", "BACKSPACE", "BACKSPACE", "UNDO", "INSERT !", "UNDO"]
result = text_editor(operations)
print(result)

# question 4
def solve(houses, queries):
    res = []
    for query in queries:
        houses.remove(query)
        prev = houses[0]
        segments = 1
        for i in range(len(houses)):
            if prev + 1 == houses[i] or prev == houses[0]:
                prev = houses[i]
                continue
            else:
                segments += 1
                print(houses[i], segments)
        res.append(segments)
    return res

example_houses = [1, 2, 3, 6, 7, 9]
example_queries = [6, 7, 2, 1]

print(solve(example_houses, example_queries))