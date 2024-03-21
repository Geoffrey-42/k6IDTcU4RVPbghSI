# Sentiment analysis
This project helped businesses gain insights into customer satisfaction and identify areas for improvement.

## Objective
The goal of this project is to conduct sentiment analysis based on customer reviews. 

## Dataset
An excel sheet contains the results of a poll in which each column is the answer to a specify question:

Y: Binary target variable; 0 meaning an unsatisfied and 1 meaning a satisfied customer
X1: Was my order was delivered on time ? (score 1-5)
X2: Contents of my order was as I expected (score 1-5)
X3: I ordered everything I wanted to order (score 1-5)
X4: I paid a good price for my order (score 1-5)
X5: I am satisfied with my courier (score 1-5)
X6: The app makes ordering easy for me (score 1-5)

## Methodology
This sentiment analysis problem was treated as a logistic regression problem in which the input is the client's feedback and the output is a binary variable determining whether the client was satisfied.

Logistic regression and decision trees were fitted to the labeled data.

Feature extraction was performed to determine which questions were most relevant to determine customer satisfaction.

## Results
The feature extraction process reduced the number of relevant questions from 6 to 2.
The models resulted in 73% accuracy to predict customer satisfaction.

## Conclusion
This sentiment analysis permitted to summarize customer's feedback and predict whether they were satisfied based on their answers.
The relevant criteria for customer satisfaction were identified.
