import pandas as pd
import matplotlib.pyplot as plt

bill = {
    "Customer_a":{
        "Jan":200,
        "Feb":350,
        "Mar":310,
        "Apr":380
    },
    "Customer_b":{
        "Jan":430,
        "Feb":500,
        "Mar":250,
        "Apr":320
    },
    "Customer_c":{
        "Jan":450,
        "Feb":350,
        "Mar":150,
        "Apr":230
    },
    "Customer_d":{
        "Jan":300,
        "Feb":210,
        "Mar":500,
        "Apr":510
    }
}

df = pd.DataFrame(bill)
df = df.set_index([pd.Index(['Jan', 'Feb', 'Mar', 'Apr'])])
df.to_csv("pandas_and_matplotlib\\question_1\\bill.csv")

new_df = pd.read_csv("pandas_and_matplotlib\\question_1\\bill.csv",index_col=0)
print(new_df)

df.plot(kind="bar")
plt.show()