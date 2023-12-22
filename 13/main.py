with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\13\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\13\\test.txt") as f:
#     lines = f.readlines()

mirrors = []
mirror = []
for line in lines:
    if line != "\n":
        mirror.append(line.replace("\n", ""))
    else:
        mirrors.append(mirror)
        mirror = []
mirrors.append(mirror)

# Ass function that doesn't work
def check_mirror(mirror, smudge):
    smudge_mirror = mirror
    smudge_found = smudge
    for i in range(len(smudge_mirror)):
        if i - 1 >= 0:

            error = (sum(1 for a, b in zip(smudge_mirror[i-1], smudge_mirror[i]) if a != b), [a for a, b in zip(smudge_mirror[i-1], smudge_mirror[i]) if a != b])
            if error[0] == 1 and not smudge_found:
                smudge_mirror[i-1] = smudge_mirror[i]
                return 1, smudge_mirror, True
            
            if smudge_mirror[i-1] == smudge_mirror[i]:
                true_mirror = True
                u, d = i-2, i+1
                while u >= 0 and d < len(smudge_mirror):

                    if not smudge_found:
                        count = sum(1 for a, b in zip(smudge_mirror[u], smudge_mirror[d]) if a != b)
                        if count == 1:
                            smudge_mirror[u] = smudge_mirror[d]
                            smudge_found = True

                    true_mirror = smudge_mirror[u] == smudge_mirror[d]
                    if not true_mirror: break
                    u -= 1
                    d += 1
                if true_mirror: return i, smudge_mirror, smudge_found
    return 0, smudge_mirror, smudge_found

# Stolen from github that does work
def find_reflected_rows(grid, smudges=0):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        # Checking if there is exactly a certain amount of smudges (a difference between
        # corresponding elements) between the rows `above` and `below`. It does this by iterating over
        # each pair of corresponding elements in `above` and `below` and counting the number of
        # differences. If the count is equal to smudges, it means there is exactly that amount of smudges
        if (
            sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                # x, y are the rows
                for x, y in zip(above, below)
            )
            == smudges
        ):
            return r

    return 0

notes = 0
new_notes = 0
for mirror in mirrors:
    notes += find_reflected_rows(mirror, 0) * 100
    new_notes += find_reflected_rows(mirror, 1) * 100

    notes += find_reflected_rows(list(zip(*mirror)), 0)
    new_notes += find_reflected_rows(list(zip(*mirror)), 1)


print(notes)
print(new_notes)