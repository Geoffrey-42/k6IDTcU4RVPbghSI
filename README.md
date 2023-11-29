# Sentiment analysis
This project helped businesses gain insights into customer satisfaction and identify areas for improvement.

## Objective
The goal of this project is to conduct sentiment analysis based on customer reviews. 

## Dataset
An excel sheet contains the results of a poll in which each column is the answer to a specify question, such as:

Was my order delivered delivered on time ? (score 1-5)

Contents of my order was as I expected (score 1-5) 

I paid a good price for my order (score 1-5) 

etc

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
