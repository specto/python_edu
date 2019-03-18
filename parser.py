import re

ids = []
end_braces = []


entry_re = re.compile(r'@\w+{(.+),\n')

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
                ids.append(entry_re.sub(lambda m: m.group(1), line))
                in_brace = True
            if in_brace and brace_count == 0:
                end_braces.append('-')
                in_brace = False

print(len(ids) - len(set(ids)))

id_counts = {}
for name in ids:
    id_counts[name] = id_counts.get(name, 0) + 1

for name, count in id_counts.items():
    if count > 1:
        print(name, count)
# print(brace_count)
