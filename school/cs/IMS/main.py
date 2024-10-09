import pandas as pd
import csv

location:str = "/home/dylan/Documents/_code/school/cs/IMS/Database.csv"


data = []

def add_data():
  stock:str = input("What is your stock name: ")
  quantity:int = int(input(f"What is the quantity of {stock}: "))
  dp:float = float(input("What is the danger percentage: "))
  if(dp >= 100):
    dp = 99
  
  data.append({"stock" : stock, "quantity" : quantity, "danger_percentage": dp})
  
  with open(location, 'w', newline='') as csvfile:
      fieldnames = ['stock', 'quantity', 'danger_percentage']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(data)


def read_database():
  data = pd.read_csv(location)
  df = pd.DataFrame(data, columns=["product_name"])
  print(data)

def main():
  read_database()

if(__name__=="__main__"):
  main()
  
  
  
