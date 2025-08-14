# # # LISTS: ACCESS AND CHANGE # # #

# Step 1:

colors = ["red", "green", "blue"]
print("Step 1.0: first color: ", colors[0])

colors[1] = "yellow"
print("Step 1.1: changed color of index 1: ", colors)

colors.extend(["green", "purple", "red"])
print("Step 1.2: added new colors: ", colors)


# Step 2:

primary_colors = colors[:3]
print("Step 2.1: stored in primary_colors:", primary_colors)

warm_colors = colors[-2:]
print("Step 2.2: stored in warm_colors:", warm_colors)

cold_colors = colors[2:4]
print("Step 2.3: stored in cold_colors:", cold_colors)


# Step 3:

warm_colors.extend(primary_colors)
print("Step 3.1: mixed_colors: ", warm_colors)

for i in range(len(colors)):
    color = colors[i]
    if color not in ["red", "purple"]:
        print("Step 3.2: index of not warm color: ", color, i)

colors[1] = "orange"
colors[2] = "pink"
colors[3] = "brown"
print("Step 3.3: Final warm color list: ", colors)