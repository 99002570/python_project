import csv 
thelist=[]


class donor:
    def __init__(self,name,phone,mail,group,amount):
        self.name=name;
        self.phone=phone;
        self.mail=mail;
        self.group=group;
        self.amount=amount;



class blooddb(donor):
    def __init__(self,name,phone,mail,group,amount):
        donor.__init__(self,name,phone,mail,group,amount)


    def search_donor(self,phone):
        flag=0;
        for lines in thelist:
            A,B,C,D,E,F=lines;
            if(B==phone):
                print("Record Found:\n");
                print(lines);
                flag=1;
                return "Found"
        if(flag!=1):
            print("Record not found.")
            return "Not Found"
        



    def read_data(self,thelist):
        file=open('Blooddata.csv', mode ='r');
        csvFile=csv.reader(file);
        for lines in csvFile:
            thelist.append(lines);

    def write_data(self,thelist):
        file1=open('Blooddata.txt','w');
        for lines in thelist:
            A,B,C,D,E,F=lines;
            file1.write("Name:")
            file1.write(A);
            file1.write("\n");
            file1.write("Phone Num:")
            file1.write(B);
            file1.write("\n");
            file1.write("Mail ID:")
            file1.write(C);
            file1.write("\n");
            file1.write("Blood Group:")
            file1.write(D);
            file1.write("\n");
            file1.write("Amount:")
            file1.write(E);
            file1.write("\n");
            file1.write("\n");
            file1.write("\n");

            print("Name:")
            print(A);
            print("\n");
            print("Phone Num:")
            print(B);
            print("\n");
            print("Mail ID:")
            print(C);
            print("\n");
            print("Blood Group:")
            print(D);
            print("\n");
            print("Amount:")
            print(E);
            print("\n");
            print("\n");
            print("\n");





