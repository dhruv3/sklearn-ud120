#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))
print(len(enron_data['GLISAN JR BEN F']))

count = 0
for key, value in enron_data.iteritems():
    if value["poi"] == 1:
        count += 1
print(count)

print(enron_data['PRENTICE JAMES'])

print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

quant_salary = 0
known_email = 0
for key, value in enron_data.iteritems():
    if value["salary"] != 'NaN':
        quant_salary += 1
    if value["email_address"] != 'NaN':
        known_email += 1

print(quant_salary)
print(known_email)

empty_total_payments = 0.0
total_poi = 0
for key, value in enron_data.iteritems():
    if value["total_payments"] == 'NaN':
        empty_total_payments += 1
    if value["poi"] == True:
        total_poi += 1

print(empty_total_payments)
