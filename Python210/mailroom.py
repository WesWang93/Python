#=========================================================================================
#Name: Mailroom OO
#Author: Wesley Wang
#Date: 5/14/2018
#=========================================================================================
import sys
from datetime import date

class Donor:
    def __init__(self, name, donations = None):
        self._name = name
        if donations is None:
            self._donations = []
        else:
            self._donations = donations

    def __str__(self):
        return f"{self._name} donated ${sum(self._donations):,.2f}"

    def __repr__(self):
        return f"{self._name} donated ${sum(self._donations):,.2f}"
        
    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations

    @property
    def total(self):
        return sum(self._donations)
    
    @property
    def num_donation(self):
        return len(self._donations)

    @property
    def avg_donation(self):
        return sum(self._donations)/len(self._donations)

    def new_donation(self, donation):
        self._donations.append(donation)

    def __eq__(self, other):
        return sum(self._donations) == sum(other._donations)

    def __ne__(self, other):
        return not sum(self._donations) == sum(other._donations)

    def __lt__(self, other):
        return sum(self._donations) < sum(other._donations)

    def __gt__(self, other):
        return not sum(self._donations) < sum(other._donations)

    def __le__(self, other):
        return sum(self._donations) >= sum(other._donations)

    def __ge__(self, other):
        return not sum(self._donations) >= sum(other._donations)

class DonorDB():
    def __init__(self):
        self._donors = {}

    @property
    def donors(self):
        return self._donors
    
    def add_donor(self, donor):
        self._donors[donor.name] = donor

    def generate_donor_list(self):
        output = "-"*20 + "\nList of Donors:\n" + "-"*20
        for donor in sorted(self._donors):
            output += "\n" + donor
        output += "\n" + "-"*20
        return output

    def build_report(self):
        donors = self._donors
        header = ["Donor Name","Total Given", "Num Gifts","Average Gifts"]
        report = ""
        report += "-"*75
        report += f"\n{header[0]:30}| {header[1]:15}| {header[2]:10}| {header[3]:20}\n"
        report += "-"*75
        for donor in sorted(donors):
            report += f"\n{donors[donor].name:30}${donors[donor].total:>15,.2f}{donors[donor].num_donation:>13}{donors[donor].avg_donation:>15,.2f}"
        report += "\n" + "-"*75
        return report


def default_donors():
    donorA = Donor("Donor A", [10000,5000,3000])
    donorB = Donor("Donor B", [500,1200])
    donorC = Donor("Donor C", [100])
    db.add_donor(donorA)
    db.add_donor(donorB)
    db.add_donor(donorC)

def thank_letter(donor, amount):
    letter = "-"*80 + f"""\nDear {donor},\n\n\tWe have received you donation of ${amount:,.2f}.
        \n\n\tWe greatly appreciate your generous contribution.
        \n\n\tThis donation is meaningful and crucial to our organization's misson.
        \n\nSincerely,\n\nWesley Wang\n""" + "-"*80
    return letter

def thank_you():
    # Ask for user input
    response = input("Please enter donor's full name, or type 'list' to check all donors: ").title()
    if response.lower() == "list":
        print(db.generate_donor_list())
        thank_you()

    while True:
        try:
            amount = float(input("Please enter donation amount for " + response + ":"))
            break
        except:
            print("\nPlease enter a dollar amount!!\n")
            continue

    donors = db.donors
    for donor in donors:
        if response.lower() == donors[donor].name.lower():
            donors[donor].new_donation(amount)
            print(thank_letter(donors[donor].name, amount))
            print("Return to main menu!!")
            mainloop()
    db.add_donor(Donor(response, [amount]))
    print(thank_letter(response, amount))


def report():
    print(db.build_report())


def send_letters():
    donors = db.donors
    for donor in donors:
        letters = open(donors[donor].name.replace(" ", "_") + "_Donation_Letter_" + str(date.today()) + ".txt", "w")
        letters.write(thank_letter(donors[donor].name, donors[donor].donations[-1]))
        letters.close()
    print("\nLetters to all donors' previous donations printed !!\n")


def quit():
    print("You have successfully quit Mailroom")
    sys.exit()

menu = {"1":["Send a Thank you", thank_you]
    , "2":["Create a Report", report]
    , "3":["Send Letters to Everyone", send_letters]
    , "4":["Quit", quit]}


def mainloop():
    print("\nWelcome to the Mailroom\n")

    while True:
        for key, value in menu.items():
            print("[" + key + "] "+ value[0])
        response = input("What do you want to do?\t")
        print(response, " was chosen")

        if response not in menu:
            print("Not a Valid Response --- Type 1, 2, 3, or 4")
        else:
            menu[response][1]()


if __name__ == "__main__":
    db = DonorDB()
    default_donors()
    mainloop()