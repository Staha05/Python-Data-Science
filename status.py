import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os

a = input("آدرس فایل اکسل خود را وارد کنید: ")

if a.endswith(".xlsx"):
    if not os.path.exists(a):
        print("فایل وجود ندارد.")
        exit()
    
    address = pd.read_excel(a)
    
    b = input("نام ستون نمرات را وارد کنید: ")
    
    if b not in address.columns:
        print(f"ستون '{b}' در فایل اکسل وجود ندارد!")
        exit()
    else:   
        print(f"زمان: {datetime.datetime.now()}")
        
        score = address[b].dropna()
        score = score[(score >= 0) & (score <= 20)]
        
        mean_score = score.mean()
        min_score = score.min()
        max_score = score.max()
        percent = (mean_score * 100) / 20
        
        print(f"کمترین نمره: {min_score}")
        print(f"بیشترین نمره: {max_score}")
        
        print(f"میانگین نمره به عدد: {mean_score}")
        print(f"میانگین به درصد: {percent}%")
        
        score_sorted = score.sort_values()
        
        plt.figure()
        plt.bar(range(1, len(score_sorted)+1), score_sorted.values)
        plt.xlabel("Student number")
        plt.ylabel("Score")
        plt.title("GPA/Score chart")
        plt.show()
        
        plt.figure()
        plt.plot(range(1, len(score_sorted)+1), score_sorted.values)
        plt.xlabel('Student number')
        plt.ylabel('Score')
        plt.title('GPA/Score chart')
        plt.show()
        
        if percent < 50:
            level = "بسیار ضعیف"
        elif percent < 75:
            level = "ضعیف"
        elif percent < 85:
            level = "متوسط"
        elif percent < 90:
            level = "خوب"
        else:
            level = "عالی"
        print("سطح آموزش:", level)
    
        print("""
                    سطح آموزش در پنج وضعیت تقسیم می‌شود:
                    ۱- بسیار ضعیف
                    ۲- ضعیف
                    ۳- متوسط
                    ۴- خوب
                    ۵- عالی
                    * نکته *: نمرات/معدل بیشتر از 20 نمره و کمتر از 0 نمره را به صورت خودکار حذف می می شوند و داخل محاصبه نمی آیند و هیچ تأثیری بر روی نتایج بدست آمده ندارند
            """)
else:
    print("فایل واردشده اکسل نمی باشد")
    exit()