# Select the required elements
selected_elements = [average_motivations_all_x[i] for i in [0,1,2,4,5,6]]
# Sum up the selected elements
sum_elements = [sum(x) for x in selected_elements]

# Create the plot
plt.figure(figsize=(10,5))
plt.plot(x_values, sum_elements, marker='.', linestyle='-', color="black")

# Set the x and y axis labels
plt.xlabel("←競争的価値　  --------------------------------------　協調的価値→", fontsize=13, labelpad=20)
plt.ylabel("社会全体のモチベーションの総量", fontsize=13)

# Adjust x and y axis ticks
plt.xticks(x_values, ["100:0", "80:20", "60:40", "40:60", "20:80", "0:100"], fontsize=13)
plt.yticks([])

# Set the title
# plt.title("競争的価値と協調的価値の割合とモチベーション総量との関係", fontsize=14)

# Save the figure as a pdf
plt.savefig("chart3.png", bbox_inches='tight', dpi=300)

# Show the plot
plt.show()

