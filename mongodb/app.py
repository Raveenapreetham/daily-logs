from business import collection

def insert_user_info():
    user_info={'username': 'rav',
               ' email': 'raveena@gmail.com',
               'password': 12345,
               'dept':'cs',
               'year':2025,
               },{'sub':'python',
                  'start_date':'21 june 2022',
                  'end_date':'22 may 2025',
                  'reg_no':21522267623,
                  },{'dob':11/8/2005,
                     'age':21,
                     'father_name':'saran'
                          }

    if user_info:
        collection.insert_many(user_info)
        print('user info insert successfully',
              'msg', user_info)
def main():
        insert_user_info()

if __name__ =='__main__':
     main()
