import matplotlib.pyplot as plt


def bar(bargraph):
    # bar graph
    xtitle = "Category"
    ytitle = "Expense"
    fig = plt.figure(figsize=(5, 5))
    axes = fig.add_subplot(1, 1, 1)
    fig.set_facecolor("whitesmoke")
    axes.set_facecolor("lavender")

    axes.bar(range(len(bargraph)), [N[1] for N in bargraph], tick_label=[N[0] for N in bargraph], width=0.4, alpha=0.7, label='Names', linewidth=0.3, edgecolor="black", facecolor="hotpink")
    plt.xlabel(xtitle, fontdict={'family': 'Arial', 'color': 'Black', 'weight': 'bold', 'size': 12, 'style': 'normal'})
    plt.ylabel(ytitle, fontdict={'family': 'Arial', 'color': 'Black', 'weight': 'bold', 'size': 12, 'style': 'normal'})
    plt.axis = 'equal'
    plt.title("EXPENSES ACCORDING TO CATEGORIES", fontdict={'family': 'Arial', 'color': 'Black', 'weight': 'bold', 'size': 20, 'style': 'normal'})
    plt.style.use('Solarize_Light2')
    plt.xticks(rotation=90)
    return fig


# pie chart
def pie(piegraph):
    colors = ['orange', 'lightcoral', 'turquoise', 'pink', 'gold', 'thistle', 'palegreen', 'moccasin', 'darkkhaki']
    fig = plt.figure(figsize=(5, 5))
    fig.set_facecolor("lavender")
    plt.title("EXPENSES ACCORDING TO CATEGORIES", fontdict={'family': 'Arial', 'color': 'Black', 'weight': 'bold', 'size': 20, 'style': 'normal'})
    plt.pie([N[1] for N in piegraph], labels=[N[0] for N in piegraph], colors=colors, startangle=90, autopct='%0.0f%%', radius=0.8, pctdistance=0.8)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=2)

    l = plt.legend(labels=[N[0] for N in piegraph], title="CATEGORY", loc="upper right", bbox_to_anchor=(1.3, 1), ncol=1, shadow=True, labelcolor="black", frameon=True, borderpad=0.5, title_fontsize=15)
    l.get_frame().set_edgecolor('black')
    l.get_frame().set_facecolor('white')
    plt.style.use('Solarize_Light2')

    plt.tight_layout()
    return fig
