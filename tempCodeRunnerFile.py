mport os
import csv

def write_into_csv(info_list):
    with open('student_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","E-Mail ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input("enter student information for student #{} in the following format(Name Age Contact_Number E-Mail_ID): ".format(student_num))

        # split() returns list of all the words in the string 
        student_info_list = student_info.split(' ')

        print("\nEntered information: \nName: {}\nAge: {}\nContact Number: {}\nE-Mail ID: {}"\
              .format(student_info_list[0],student_info_list