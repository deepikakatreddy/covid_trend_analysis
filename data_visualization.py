import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(country_data, country):
    plt.figure(figsize=(18, 16))

    plt.subplot(2, 2, 1)
    plt.plot(country_data['date'], country_data['total_cases'], label='Total Cases', marker='o')
    plt.plot(country_data['date'], country_data['total_deaths'], label='Total Deaths', marker='x')
    plt.fill_between(country_data['date'], country_data['total_cases'], country_data['total_deaths'], color='skyblue', alpha=0.4)
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Total Cases and Deaths over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.bar(country_data['date'], country_data['daily_new_cases'], label='Daily New Cases', color='blue', alpha=0.7)
    plt.bar(country_data['date'], country_data['daily_new_deaths'], label='Daily New Deaths', color='red', alpha=0.7)
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Daily New Cases and Deaths')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 3)
    labels = ['Total Cases', 'Total Deaths', 'Total Vaccinations']
    sizes = [country_data['total_cases'].iloc[-1], country_data['total_deaths'].iloc[-1], country_data['total_vaccinations'].iloc[-1]]
    colors = ['gold', 'lightskyblue', 'lightcoral']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Distribution of Total Cases, Deaths, and Vaccinations')

    plt.subplot(2, 2, 4)
    plt.plot(country_data['date'], country_data['total_vaccinations'], label='Total Vaccinations', marker='o', color='green')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Total Vaccinations over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(country_data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(country_data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    plt.show()
