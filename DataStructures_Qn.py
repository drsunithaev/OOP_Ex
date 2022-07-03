"""#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element avaible in list
7 . Try to extract all the value element form dict available in list
"""
import logging
import log.log_file

class DataStructures_Class :
    def __init__(self, data):
        self.data = data



    def extract_values(self):
        """extract values from the dictionary"""
        try:
            logging.info("extracting values from the dictionary")
            values_dict = []
            if type(self.data) == dict:
                values_dict = self.data.values()
            elif type(self.data) == list:
                for i in self.data:
                    if type(i) == dict:
                        values_dict.append(i.values())
            logging.info(f"keys --> {values_dict}")
            return values_dict
        except Exception as e:
            logging.exception(e)

    def extract_keys(self):
        """extract keys from the dictionary"""
        try:
            logging.info("extracting keys from the dictionary")
            keys_dict = []
            if type(self.data) == dict:
                keys_dict = self.data.keys()
            elif type(self.data) == list:
                for i in self.data:
                    if type(i) == dict:
                        keys_dict.append(i.keys())
            logging.info(f"keys --> {keys_dict}")
            return keys_dict
        except Exception as e:
            logging.exception(e)

    def extract_list(self):
        """extract list data"""
        try:
            logging.info("extracting list from data")
            list_items = []
            for i in self.data :
                if type(i) == list :
                    logging.info(f"list --> {i}")
                    list_items.append(i)
            return list_items
        except Exception as e:
            logging.exception(e)

    def extract_dict(self):
        """extract dictionary data"""
        try:
            logging.info("extracting dictionary from data")
            dict_items = []
            for i in self.data :
                if type(i) == dict :
                    logging.info(f"Dictionary --> {i}")
                    dict_items.append(i)
            return dict_items
        except Exception as e:
            logging.exception(e)

    def extract_tuple(self):
        """extract tuple data"""
        try:
            logging.info("extracting tuple from data")
            tuple_items = []
            for i in self.data :
                if type(i) == tuple :
                    logging.info(f"Tuples --> {i}")
                    tuple_items.append(i)
            return tuple_items
        except Exception as e:
            logging.exception(e)

    def extract_list_odd(self):
        """extract odd numbers from list"""
        try:
            logging.info("extracting odd numbers from lists")
            q8 = self.extract_list()
            odd_num = []
            for i in q8:
                for j in i:
                    if type(j) == int:
                        if (j % 2) != 0:
                            odd_num.append(j)
            logging.info(f"odd numbers {odd_num}")
            return odd_num
        except Exception as e:
            logging.exception(e)

    def extract_string(self,s):
        """extract string from data"""
        try:
            q9 = []
            for i in self.data:
                if type(i) == list:
                    for j in i:
                        if type(j) == str:
                            if j == s:
                                q9.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str:
                            if k == s:
                                q9.append(k)
                        if type(v) == str:
                            if v == s:
                                q9.append(v)
            logging.info(f"extracted {q9}")
            return q9
        except Exception as e:
            logging.exception(e)

    def occurrences_all(self) :
        """
        Number of occurrences of all data
        """
        try :
            logging.info("Number of occurrences of all data")
            q10 = {}
            q10_l = []
            for i in self.data:
                if type(i) == dict:
                    for k, v in i.items():
                        q10_l.append(k)
                        q10_l.append(v)
                elif type(i) == list or type(i)==tuple or type(i)==set:
                    for j in i:
                        q10_l.append(j)
                else:
                    q10_l.append(i)
            for i in set(q10_l):
                c = q10_l.count(i)
                q10[i] = c
            logging.info(f"Counts {q10}")
            return q10
        except Exception as e:
            logging.exception(e)


    def extract_numeric(self):
        """
        extract all numeric data
        """
        try :
            logging.info("extract all numeric data")
            q6 = []
            for i in self.data:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == float:
                            q6.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(k) == float:
                            q6.append(k)
                        if type(v) == int or type(v) == float:
                            q6.append(v)
            logging.info(f"Extracted values --> {q6}")
            return q6
        except Exception as e:
            logging.exception(e)

    def sum_numeric(self):
        """SUm of numeric data"""
        try:
            logging.info("Summing up numerical data")
            numerics = self.extract_numeric()
            total = sum(numerics)
            logging.info(f" Sum = {total}")
            return total
        except Exception as e:
            logging.exception(e)

    def reverse_list(self):
        """reverse the list"""
        try:
            logging.info("Try to reverse the data")
            if type(self.data) == list:
                return self.data[-1::-1]
            else:
                logging.info("Data is not a list. Not possible to reverse now")
        except Exception as e:
            logging.exception(e)
