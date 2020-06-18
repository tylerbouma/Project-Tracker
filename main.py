import csv
import os
import re

class Project:
    def __init__(self):
        # Use a default csv unless specified
        self.csvName = 'default_projects.csv'
        self.name = ''
        self.length = ''
        self.hours = ''
        self.desc = ''

    def gather_details(self):
        # Gather user input information about this project
        self.name = input("Project name: ")
        while 1:
            # Loop until a valid entry is made
            self.length = input("Project length (in days): ")
            try:
                float(self.length)
                break
            except ValueError:
                print("This is not an integer or decimal, try again.")

        while 1:
            # Loop until a valid entry is made
            self.hours = input("Hours used: ")
            try:
                float(self.hours)
                break
            except:
                print("This is not an integer or decimal, try again.")

    def check_if_exists(self, csvName):
        if os.path.exists(csvName):
            self.csvName = csvName
        else:
            # Ask if the user wants to use the default csv or create a new one
            useDefCsv = input("The csv file you selected does not exist, do you want to create it? [Y|N]: ")
            if useDefCsv.upper() in ['N', 'NO']:
                print("Exiting")
            else:
                self.csvName = csvName
    
    def write_to_csv(self):
        while 1:
            # Get the csv file name from the user
            userCsv = input(f"Enter csv file to use or press Enter to use default '{self.csvName}': ")
            # Only check for the file if the user enters a string and references a csv file
            if re.split("\.", userCsv)[-1] == 'csv':
                # Check if the csv exists
                self.check_if_exists(userCsv)
                break
            elif userCsv == "":
                # They pressed <Enter>
                break
            else:
                print("Please use a .csv file")
        # Write the user input to a csv file keeping track of projects
        with open(self.csvName, 'a', newline='') as csvFile:
            pWriter = csv.writer(csvFile, delimiter='|')
            pWriter.writerow([self.name, self.length, self.hours, self.desc])




def main():
    while 1:
        # Create projects until user is done
        p = Project()
        p.gather_details()
        p.write_to_csv()
        
        anotherProject = input("Create another project? [Y|N]: ")
        if anotherProject.upper() in ['N', 'NO']:
            break

if __name__ == "__main__":
    main()









