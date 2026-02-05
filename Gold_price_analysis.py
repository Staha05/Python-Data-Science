import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\lenovo\\Desktop\\Dataset\\GoldPrice.csv")

print("تعداد داده ها:", len(df))
print("ستون ها:", df.columns.tolist())
print("\nنمونه داده ها:")
print(df.head())

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

plt.figure(figsize=(10, 4))
plt.plot(df['Date'], df['Price'], color='gold')
plt.title('Gold Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.hist(df['Chg%'], bins=20, color='blue', edgecolor='black')
plt.title('Daily Price Changes')
plt.xlabel('Percentage Change')
plt.ylabel('Number of Days')
plt.show()

print("\nآمار ساده:")
print("میانگین قیمت:", df['Price'].mean().round(2))
print("بیشترین قیمت:", df['Price'].max())
print("کمترین قیمت:", df['Price'].min())
print("میانگین تغییر روزانه:", df['Chg%'].mean().round(3), "%")

positive_days = (df['Chg%'] > 0).sum()
negative_days = (df['Chg%'] < 0).sum()
print(f"\nروزهای مثبت: {positive_days}")
print(f"روزهای منفی: {negative_days}")
print(f"درصد روزهای مثبت: {(positive_days/len(df)*100):.1f}%")