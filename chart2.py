import matplotlib.pyplot as plt

indices = [0, 3, 7]
titles = ["競争の価値の割合が100%の場合", "競争と協調の価値の割合が50:50の場合", "物質が満たされるにつれ、価値が競争から協調に移行する場合"]
max_y = 150000
fig, axs = plt.subplots(1, 3, figsize=(20, 5))  # Adjust the figure size if necessary

for i, index in enumerate(indices):
    axs[i].plot(total_creativities_all_x2[index][0], linestyle=':', color="grey", label='社会の総価値')
    axs[i].plot(labours_all_x2[index][0], linestyle='--', color="grey", label='物質的価値')
    axs[i].plot(total_productions_all_x2[index][0], linestyle='-', color="black", label='総合的価値')
    axs[i].set_ylim([0, max_y])  # Set y-axis limits to be the same across all subplots
    axs[i].set_yticks([])  # Remove y-axis labels
    axs[i].set_xticks([])  # Remove x-axis labels
    axs[i].set_xlabel("→→  時間の経過  →→", fontsize=12)  # Set x-axis label
    axs[i].set_ylabel("価値の総量", fontsize=12)  # Set y-axis label
    axs[i].legend()  # Add legend
#     axs[i].set_title(titles[i])  # Set title

# Save the figure as a PDF
plt.savefig("chart1.png",bbox_inches='tight', dpi=300)

# Show the plot
plt.show()