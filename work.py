def nested_dict(input, parent_key = '', seperator = ' '):
    output = []

    for key, value in input.items():
        new_key = f"{parent_key} {seperator} {key}" if parent_key else key

        if isinstance(value,dict):
            output.extend(nested_dict(value, new_key, seperator))

        else:
            output.append(f"{new_key} {seperator} {value}")


    return output

input = {"country":{"India":{"state":"Punjab"}},"china":"wuhan"}
final_output = nested_dict(input, seperator = " -> ")
print({"region": final_output})