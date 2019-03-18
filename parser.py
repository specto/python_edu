braces = []
end_braces = []

with open("library.bib", "r") as library_file:
    brace_count = 0
    in_brace = False
    for line in library_file:
        for char in line:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
            if not in_brace and brace_count == 1:
                braces.append('+')
                in_brace = True
            if in_brace and brace_count == 0:
                end_braces.append('-')
                in_brace = False

print(len(braces), len(end_braces))
# print(brace_count)
