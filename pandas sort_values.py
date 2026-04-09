import pandas as pd
data = {

    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Tablet"],

    "Category": ["Electronics", "Electronics", "Electronics", "Gadgets", "Electronics", "Gadgets"],

    "Price": [50000, 20000, 52000, 15000, 21000, 16000],

    "Quantity": [2, 5, 1, 3, 4, 2]

}
df = pd.DataFrame(data)
# print(df)
# print(df["Product"])
# print(df["Price"])
# expensive=df[df["Price"]>20000]
# print(expensive)
# cate=df[(df["Category"]=="Electronics") & df["Price"]>20000]
# print(cate)

# df_sort_Price=df.sort_values(by="Price",ascending=False)
# print(df_sort_Price)
# df_sort_Quantity=df.sort_values(by="Quantity",ascending=False)
# print(df_sort_Quantity)
#print(df.sort_values(by=["Category","Price"],ascending=[True,False]))


df["Total_sell"]=df["Price"]*df["Quantity"]
Category_sell=df.groupby("Category")["Total_sell"].sum()
print(Category_sell)

avg_price=df.groupby("Product")["Price"].mean()
print(avg_price)

