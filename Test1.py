import matplotlib.pyplot as plt
import numpy as np

years = range(2013, 2022)
countries = ['중국', '미국', '대한민국', '일본']
data = {
    '중국': [216795.9, 225855.2, 243520.0, 253801.6, 265874.1, 283885.3, 303300.6, 328176.3, 350435.2],
    '미국': [138130.7, 148137.4, 152531.7, 149656.4, 155087.4, 162450.0, 172385.1, 174899.3, 171874.5, 168327.8],
    '대한민국': [2275.7, 2653.9, 3861.3, 3964.8, 4210.0, 4640.9, 5389.3, 5502.8, 5871.5, 6173.2],
    '일본': [17799.8, 19169.4, 20319.1, 21953.8, 21555.4, 23633.0, 24736.3, 26115.2, 26762.0, 28457.1]
}

plt.figure(figsize=(12, 6))

for country in countries:
    values = data[country]
    growth_rates = [(values[i] - values[i-1]) / values[i-1] * 100 for i in range(1, len(values))]
    plt.plot(years[:len(growth_rates)], growth_rates, label=country, marker='o')

plt.title('연간 재생 에너지 생산량 증감률')
plt.xlabel('년도')
plt.ylabel('증감률 (%)')
plt.legend()
plt.grid(True)
plt.show()
