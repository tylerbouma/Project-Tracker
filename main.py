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
        # Check if this project name already exists
        check_project(self.name, self.csvName)
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
        # Get the project details
        self.gather_details()
        # Write the user input to a csv file keeping track of projects
        with open(self.csvName, 'a', newline='') as csvFile:
            fieldNames = ['project_name', 'project_timeline', 'project_hours', 'project_desc']
            # Use dictwriter to create a dict for each row for easier editing
            pWriter = csv.DictWriter(csvFile, fieldnames=fieldNames)
            print(self.name)
            pWriter.writerow({'project_name': self.name, 'project_timeline': self.length, 'project_hours': self.hours,'project_desc': self.desc})

def check_project(projName, csvName):
    # Open the csv given and check if the project already exists
    with open(csvName, newline='') as csvFile:
        preader = csv.DictReader(csvFile)
        for row in preader:
            print(row['project_name'])
            


def edit_proj():
    # Find the project line and edit it

    print("edit")

def main():
    # Present the user with options of what to do
    print("Welcome! What would you like to do?")
    print("1) Create a new project")
    print("2) Edit a project")
    print("3) Delete a project")
    print("4) Exit")

    toDoChoice = input(": ")
    print(toDoChoice)
    if int(toDoChoice) == 1:
        while 1:
            # Create projects until user is done
            p = Project()
            p.write_to_csv()
            
            anotherProject = input("Create another project? [Y|N]: ")
            if anotherProject.upper() in ['N', 'NO']:
                break
    elif int(toDoChoice) == 2:
        print("You want to edit a project")
    elif int(toDoChoice) == 3:
        print("You want to delete a project")
    elif int(toDoChoice) == 4:
        quit()
    else:
        print("That is not a valid choice")

if __name__ == "__main__":
    main()









