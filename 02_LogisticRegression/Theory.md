## What is Logistic Regression?
It’s a classification algorithm, that is used where the response variable is categorical. The idea of Logistic Regression is to find a relationship between features and probability of particular outcome.
E.g. When we have to predict if a student passes or fails in an exam when the number of hours spent studying is given as a feature, the response variable has two values, pass and fail.
This type of a problem is referred to as Binomial Logistic Regression, where the response variable has two values 0 and 1 or pass and fail or true and false. Multinomial Logistic Regression deals with situations where the response variable can have three or more possible values.
## Why Logistic, not Linear?
With binary classification, let ‘x’ be some feature and ‘y’ be the output which can be either 0 or 1. 
The probability that the output is 1 given its input can be represented as:

![image](https://github.com/NicolaChiesa/ML-Training/assets/89846244/ffa1bea5-4dda-4bc7-8abf-6c580fb59d93)


If we predict the probability via linear regression, we can state it as:


![image](https://github.com/NicolaChiesa/ML-Training/assets/89846244/ec99ebbf-e1ae-411d-a994-f1c5af8858d2)

Linear regression model can generate the predicted probability as any number ranging from negative to positive infinity, whereas probability of an outcome can only lie between 0< P(x)<1.

![image](https://github.com/NicolaChiesa/ML-Training/assets/89846244/1c3e48b1-f24b-4f67-89d9-689972c2892b)![image](https://github.com/NicolaChiesa/ML-Training/assets/89846244/4168f115-aa52-446c-b8d2-909f1edab85c)
## Logit Function
Logistic regression can be expressed as:

![image](https://github.com/NicolaChiesa/ML-Training/assets/89846244/305a7cd1-bf9e-4d0b-9559-2c4c01d4d12e)


where, the left hand side is called the logit or log-odds function, and p(x)/(1-p(x)) is called odds.
The odds signifies the ratio of probability of success to probability of failure. Therefore, in Logistic Regression, linear combination of inputs are mapped to the log(odds) - the output being equal to 1.

## Estimation of Regression Coefficients
Unlike linear regression model, that uses Ordinary Least Square for parameter estimation, we use Maximum Likelihood Estimation. 
There can be infinite sets of regression coefficients. The maximum likelihood estimate is that set of regression coefficients for which the probability of getting the data we have observed is maximum. 
If we have binary data, the probability of each outcome is simply π if it was a success, and 1−π otherwise. Therefore we have the likelihood function:


## Linear regression vs logistic regression
Both linear and logistic regression are among the most popular models within data science, and open-source tools, like Python and R, make the computation for them quick and easy.

Linear regression models are used to identify the relationship between a continuous dependent variable and one or more independent variables. When there is only one independent variable and one dependent variable, it is known as simple linear regression, but as the number of independent variables increases, it is referred to as multiple linear regression. For each type of linear regression, it seeks to plot a line of best fit through a set of data points, which is typically calculated using the least squares method.

Similar to linear regression, logistic regression is also used to estimate the relationship between a dependent variable and one or more independent variables, but it is used to make a prediction about a categorical variable versus a continuous one. A categorical variable can be true or false, yes or no, 1 or 0, et cetera. The unit of measure also differs from linear regression as it produces a probability, but the logit function transforms the S-curve into straight line.  

While both models are used in regression analysis to make predictions about future outcomes, linear regression is typically easier to understand. Linear regression also does not require as large of a sample size as logistic regression needs an adequate sample to represent values across all the response categories. Without a larger, representative sample, the model may not have sufficient statistical power to detect a significant effect.

## Use cases of logistic regression
Logistic regression is commonly used for prediction and classification problems. Some of these use cases include:

Fraud detection: Logistic regression models can help teams identify data anomalies, which are predictive of fraud. Certain behaviors or characteristics may have a higher association with fraudulent activities, which is particularly helpful to banking and other financial institutions in protecting their clients. SaaS-based companies have also started to adopt these practices to eliminate fake user accounts from their datasets when conducting data analysis around business performance.
Disease prediction: In medicine, this analytics approach can be used to predict the likelihood of disease or illness for a given population. Healthcare organizations can set up preventative care for individuals that show higher propensity for specific illnesses.
Churn prediction: Specific behaviors may be indicative of churn in different functions of an organization. For example, human resources and management teams may want to know if there are high performers within the company who are at risk of leaving the organization; this type of insight can prompt conversations to understand problem areas within the company, such as culture or compensation. Alternatively, the sales organization may want to learn which of their clients are at risk of taking their business elsewhere. This can prompt teams to set up a retention strategy to avoid lost revenue.
