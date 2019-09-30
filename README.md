# Ft_linear_regression

Implementation of a linear regression in python
Here we predict the price of a car based on a mileage, it was a good introduction to ML.

Here I used a simple normalization and the gradient descent algorythm

# Usage

```$> python3 linear_regression.py```   
The programme prompt you for a mileage and gives you an estimation.  

```$> 240000```  
Since we didn't train the programme yet the value is 0.

```$> python3 training.py data.csv```
The machine learn from our data file "data.csv".

```$> python3 linear_regression.py```  
We relaunch the predictive programme and enter the mileage value again.

```$> 240000```    
The programme is giving you a value related to what he learned with the linear regression.

You can now compare the output with the associated value from the data file:  
```$> cat data.csv```

The treshold between the data in the file and the output is totally normal as you may know.
Indeed the Linear regression algorythm is suposed to give a realist value for each mileage you would input. 
if the output was the exact value of the data file, it would be a case of overfitting.
