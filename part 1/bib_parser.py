import re


# Prepare to capture target_id in text like "@WORD{target_id,
entry_id_regex = re.compile(r'@\w+{(.+),\n')


# Parse a bib file and extract the ids of all the entries
ids = []
with open("library.bib", "r") as library_file:
    # Isolate top level items surrounded by { and }
    # by tracking opening and closing braces
    brace_depth = 0
    is_between_braces = False
    for line in library_file:  # Walk over every line
        for char in line:  # Walk over every character on the line
            if char == '{':
                brace_depth += 1
            elif char == '}':
                brace_depth -= 1
            if not is_between_braces and brace_depth == 1:
                # Find the id
                target_id = entry_id_regex.sub(lambda m: m.group(1), line)
                # Collect the id in array
                ids.append(target_id)
                # Start tracking our entry
                is_between_braces = True
            if is_between_braces and brace_depth == 0:
                # Back to top level our entry must be ending
                is_between_braces = False

print("Total duplicates in library:", len(ids) - len(set(ids)))

# Create a dictionary collection
id_counts = {}
# Fill the dictionary with counter for every id
for name in ids:
    id_counts[name] = id_counts.get(name, 0) + 1

# Display all repeated items
for name, count in id_counts.items():
    if count > 1:
        print(name, count)

# Do you think this is a corrupted bib file?
if brace_depth > 0:
    print("Your bib file seems corrupted")
