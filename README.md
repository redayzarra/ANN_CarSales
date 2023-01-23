# Car Sales - Regression Neural Network

## Overview
This project utilizes an **artificial neural network to perform a regression task**, which means the model will predict a value based on the features. In this case, the model will have **eight features to predict the purchasing amount** for each customer. This project showcases a *step-by-step implementation* of the model as well as *in-depth notes* to customize the model further for higher accuracy.

The model is trained on this [dataset](https://github.com/redayzarra/ml-carsales-project/blob/master/Car_Purchasing_Data.csv) and divided into training and testing sets. Despite the dataset having eight variables, or columns, the model is only trained on five. This is due to some of the variables having little to no significance to the model’s performance. For example, the customer’s name and email hold little value to their purchasing power. In addition, the model has achieved incredible accuracy results which I was able to calculate by comparing the predicted values and the true values (which have also been added as columns).

The model can be used to predict the purchasing power of customers looking to purchase cars. This can be incredibly useful to businesses looking to serve their customers’ needs by targeting their advertising and marketing efforts towards those who have the highest predicted purchasing power, and by adjusting prices and offers to appeal to those with lower purchasing power. The model can also be used to identify potential high-value customers and prioritize their sales efforts accordingly. Additionally, the model can be used to predict trends in customer purchasing power and adjust business strategies accordingly.

<div align="center" padding-bottom = 100px>

<img src="https://user-images.githubusercontent.com/113388793/214177495-67b1bd8f-acae-4dc9-94fe-4f994ce65556.png" >

Training vs. Validation Loss



<img src="https://user-images.githubusercontent.com/113388793/214177729-ed8e1aef-32a4-47bd-bb90-a3dec91f5635.PNG" >

Model Accuracy Metrics
</div>



## Project Website

If you would like to find out more about the project, please checkout: [Car Sales Regression Project](https://www.redaysblog.com/projects/car-sales)

## Installing the libraries

This project uses several important libraries such as Pandas, NumPy, Matplotlib, and more. You can install them all by running the following commands with pip:

```bash 
pip install pandas
pip install numpy

python -m pip install -U matplotlib
pip install seaborn

pip install -U scikit-learn
pip install tensorflow

```

If you are not able to install the necessary libraries, I recommend you **use Jupyter Notebook with Anaconda**. I have a .ipynb file for the project as well.


## Configurations

This project utilizes a CSV file for loading the dataset. If you have a CSV file full of text that you would like to use, please feel free to use this code to load your dataset in to the file:

```python
dataset = pd.read_csv('YOUR-DATA.csv')
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
