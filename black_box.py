# This is the introductory black box file for the project


from themeclass import *
import sys, csv
import pprint


"""
It becomes necessary to understand how a base ratio becomes connected to a clause.
For the purposes of this explanation, we define a clause as follows:
    A clause is a a list of terms that do not include addition or subtraction operators.
"""



class Clause(object):
    # assumption: name is a string, terms is a list of terms ... e.g. ['a', '*', 'b', '/', 'c']
    def __init__(self, name, terms, base_ratio):
        self.name = name
        self.terms = terms

    # returns a dictionary of the table of terms
    # this implementation assumes that the ratios are stored exactly as this format: numerator/denominator
    # this implementation also assumes that the ratios contain a maximum of two terms per clause
    def get_table_terms(self):
        num_operators = 0

        for term in self.terms:
            if term == "*" or term == "/":
                num_operators += 1

        return_dict = {}

        if num_operators == 0:
            rand_int = random.randint(1,100)
            return_dict = {base_ratio.get_name() : rand_int}
        elif num_operators == 1:
            if self.terms[1] == "*":
                return_dict[base_ratio.get_numerator().get_name()] = random.randint(1,100)
                return_dict["1/" + base_ratio.get_denominator().get_name()] = random.randint(1,100)
            else:
                return_dict[base_ratio.get_numerator().get_name()] = random.randint(1, 100)
                return_dict[base_ratio.get_denominator().get_name()] = random.randint(1, 100)
        else:
            print("MORE THAN 1 OPERATOR NOT CURRENTLY SUPPORTED!")

        return return_dict


# sample_input =  "a*b+c+e/f+g/h-j"

sample_input = "a/b+c/d+e/f-k/j-z/y"

# base_ratio = car_theme.get_random_ratio()
base_ratio = car_theme.get_random_ratio()

term_list = []
clause_list = []
identifier = 0
for char in sample_input:
    if char == '+' or char == '-':
        if len(term_list) > 0:
            new_clause = Clause(identifier, term_list, "BASE RATIO")
            clause_list.append(new_clause)
            identifier += 1
            term_list = []
        clause_list.append(char)
    else:
        term_list.append(char)
new_clause = Clause(identifier, term_list, "BASE RATIO")
clause_list.append(new_clause)

# generate table of data

table_headers = []
table = []
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
max_row_len = 0

for term in clause_list:
    if type(term) is Clause:
        clause_dict = term.get_table_terms()
        new_table_row = []
        for header in clause_dict:
            if header not in table_headers:
                table_headers.append(header)
        for header in table_headers:
            if header in clause_dict:
                new_table_row.append(clause_dict[header])
            else:
                new_table_row.append('X')
        table.append(new_table_row)

        if len(new_table_row) > max_row_len:
            max_row_len = len(new_table_row)

# fix the table
for i in range(0,len(table)):
    while (len(table[i]) < max_row_len):
        table[i].append('X')




# name = car_theme.get_random_name()
name = car_theme.get_random_name()
# Print the start of the problem

if len(clause_list) > 1:
    print("A set of " + name + "s have the following properties:")

# print the table of data
table_head = ""
table_headers.insert(0,name)
for header in table_headers:
    table_head += header
    table_head += '\t'
print(table_head)

row_string = ""
for row in table:
    row.insert(0,labels[0])
    labels.pop(0)

    for element in row:
        row_string += str(element) + '\t\t'
    print(row_string)
    row_string = ""

# use stack overflow solution:
table.insert(0,table_headers)


index = 0
positive_term_names = []
negative_term_names = []

positive_term_names.append(table[index][0])
index += 1

for term in clause_list:
    if type(term) is not Clause:
        if term == '+':
            positive_term_names.append(table[index][0])
        else:
            negative_term_names.append(table[index][0])
        index += 1

# print(positive_term_names)
# print(negative_term_names)

question = "Using the table of information above, write a program to "
if len(positive_term_names) >= 1 and len(negative_term_names) >= 1:
    question += "compute the sum of the " + base_ratio.get_name() + " of the " + name + "s "
    for term in positive_term_names:
        question += term + ", "
    question += "minus the sum of the " + base_ratio.get_name() + " of the " + name + "s "
    for term in negative_term_names:
        question += term + ", "
elif len(positive_term_names) >= 1:
    question += "compute the sum of the " + base_ratio.get_name() + " of the " + name + "s "


question += "."

print(question)









# for row in table:
#     for column in row:
#         print



























# sample parse input






# # sample parse input
# input = "a*b+c*d+e"
# tree = []
#
# last_op = ""
# last_term = ""
#
# # basic parser found below, takes input and puts it into the 'tree'
# for i in range(0, len(input)):
#     term = input[i]
#
#     # if we receieve a term
#     if term >= 'a' and term <= 'z':
#         if last_term == '' and last_op == '':
#             last_term = term
#         elif last_term != '' and last_op != '':
#             tree.append((last_term, term, last_op))
#             last_term = ''
#             last_op = ''
#         else:
#             print("ERROR LINE 170?")
#     # if we receive an op
#     else:
#         if last_term == '' and last_op == '':
#             tree.append(term)
#         elif last_term != '' and last_op == '':
#             last_op = term
#         else:
#             print("ERROR LINE 178?")
# if last_term != "":
#     tree.append((last_term))

\