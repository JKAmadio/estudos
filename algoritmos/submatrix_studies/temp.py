import numpy as np

full_matrix = np.array([
    [1,0,0,1],
    [1,0,0,1],
    [1,0,0,1]
])

submatrix = np.array([
    [1,0,1],
    [1,0,0],
    [1,0,1]
])

all_variants = []
all_variants.append(submatrix)
all_variants.append(np.fliplr(submatrix))
all_variants.append(np.flipud(submatrix))
all_variants.append(np.rot90(submatrix))
all_variants.append(np.rot90(np.rot90(submatrix)))
all_variants.append(np.rot90(np.rot90(np.rot90(submatrix))))

print(all_variants)
unique_variants = []
unique_variants.append(submatrix)
# breakpoint()
for variant in all_variants:
    i = 0
    counter = 0
    for i in range(len(unique_variants)):
        if not (np.all(unique_variants[i] == variant)):
            counter += 1
    if (counter == len(unique_variants)):
        unique_variants.append(variant) 

print(unique_variants)

