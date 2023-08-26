import matplotlib.pyplot as plt

data = [22, 18, 9, 8, 7, 6]
name_language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']

for i in range(len(data)):
    plt.bar(i, height=data[i], color=colors[i])

plt.minorticks_on()
plt.grid(which='major', color='red')
plt.grid(which='minor', color='black', linestyle=':')

plt.xticks([i for i in range(len(name_language))], name_language)
plt.xlabel('Языки программирования')
plt.ylabel('Популярность')
plt.title('Популярность языков программирования')

plt.show()