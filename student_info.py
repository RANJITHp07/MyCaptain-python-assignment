 #to get student information
import csv
def write_into_csv(infolist):
    with open(studentinfo.csv,'a',newline="")as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","Email-ID"])
            writer.writerow(infolist)
if __name__ =='__main__':
    condition=True
    student_num=1
    while(condition):
          studentInfo=input("enter the studenti #{} information(Name,Age,Contact Number,e-mail ID):".format(student_num))
          studentInfoList=studentInfo.split(' ')
          print("\nThe entered information is -\nName:{}\nAge:{}\nContact number:{}\nE-mail ID:{}".format(studentInfoList[0],studentInfoList[1],studentInfoList[2],studentInfoList[3]))
          choiceCheck=input("Entered information is correct(yes/no):")
          if(choiceCheck=="yes"):
              write_into_csv(studentInfoList)
              condition_check=input("Do you want to enter another students data(y/n):")
              if(condition_check=="y"):
                  condition=True
                  student_num=student_num+1
              else:
                  condition=False    
          elif(choiceCheck=="no"):
              print("Re-enter the value")
