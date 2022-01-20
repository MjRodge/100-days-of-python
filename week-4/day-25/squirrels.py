import pandas

squirrels = pandas.read_csv("squirrel-data.csv")

grey_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
red_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

data_dict = {
    "fur colour": ["grey", "red", "black"],
    "count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")