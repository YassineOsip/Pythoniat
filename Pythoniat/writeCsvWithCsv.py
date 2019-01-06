import csv

with open('test.csv' , "w" , newline="" ) as fp :
    a = csv.writer(fp)
    data = [['stock ' , "sales"] ,
           ["100" , "322"],
            ["100", "322"],
            ["100", "322"]]
    a.writerows(data)

