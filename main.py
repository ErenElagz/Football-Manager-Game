# Imports
import random
from prettytable import PrettyTable, SINGLE_BORDER

# RAW Python Colors
class Colors:
    #Text
    frontBlack   = '\033[30m'
    frontRed     = '\033[31m'
    frontGreen   = '\033[32m'
    frontYellow  = '\033[33m'
    frontBlue    = '\033[34m'
    frontMagenta = '\033[35m'
    frontCyan    = '\033[36m'
    frontWhite   = '\033[37m'
    frontReset   = '\033[39m'
    #Background
    backBlack    = '\033[40m'
    backRed      = '\033[41m'
    backGreen    = '\033[42m'
    backYellow   = '\033[43m'
    backBlue     = '\033[44m'
    backMagenta  = '\033[45m'
    backCyan     = '\033[46m'
    backWhite    = '\033[47m'
    backReset    = '\033[49m'
    #Styles
    bright       = '\033[1m'
    dim          = '\033[2m'
    normal       = '\033[22m'
    resetAll     = '\033[0m'

# Classes
class Team:
    def __init__(self, name, power, strategy, popularity):
        self.name = name
        self.power = power
        self.strategy = strategy
        self.popularity = popularity
        # For Goal
        self.goalConceded = 0
        self.goalScored = 0
        # For Scoreboard
        self.point = 0
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.winRate = 0

    def WinRate(self):
        self.winRate = round(100*(self.win/(self.win + self.draw + self.lose)), 2)
        self.winRate = "½ " + str(self.winRate)


    def TeamDetails(self):
        table = PrettyTable()
        table.field_names = ["Team Name", "Team Strategy", "Power", "Popularity", "Win Rate"]
        table.align["Team Name"] = "l"
        table.add_row([self.name, self.strategy.name, self.power, self.popularity, self.winRate])
        print(table)

    def ChangeStratedy(self):
        print("- - - - - - - - - - - -")
        print("\nPlease Choose Your Team Strategy")
        print("1: High Aggressive")
        print("2: Low Aggressive")
        print("3: Normal")
        print("4: Low Defensive")
        print("5: High Defensive")
        print("0: Stay Current Stratedy")
        print("- - - - - - - - - - - -\n")
        print(self.name)
        print("current stratedy: ",self.strategy.name)
        print("current power: ",self.power)    
        print("- - - - - - - - - - - -\n")  
        team_stratedy_number = int(input("Enter Number to Your Choosen Stratedy: "))

        if  team_stratedy_number == 0:
            pass
            
        elif team_stratedy_number == 1:           
            self.strategy = HighAggressive

        elif team_stratedy_number == 2:
            self.strategy = LowAggressive

        elif team_stratedy_number == 3:
            self.strategy = Normal

        elif team_stratedy_number == 4:
            self.strategy = LowDefensive

        elif team_stratedy_number == 5:
            self.strategy = HighDefensive

        else:
            print("Error.Please Try again. ") 

class Strategy:
    def __init__(self, name, HomeGoalExpection, HomeKeepExpection,AwayGoalExpection,AwayKeepExpection):
        self.name = name
        self.HomeGoalExpection = HomeGoalExpection
        self.HomeKeepExpection = HomeKeepExpection
        self.AwayGoalExpection = AwayGoalExpection
        self.AwayKeepExpection = AwayKeepExpection

# Variables
week = 0
myTeam = None
myStrategy = None

# Objects
HighAggressive = Strategy("High Aggressive", 8 ,2,1,1)
LowAggressive = Strategy("Low Aggressive", 7, 4,1,1)
Normal = Strategy("Normal", 4, 5, 5, 5)
LowDefensive = Strategy("Low Defensive", 4, 5, 4, 5)
HighDefensive = Strategy("High Defensive", 4, 9 ,1,1)
allStrategies = [HighAggressive, LowAggressive, Normal, LowDefensive, HighDefensive]
#
Arsenal = Team("Arsenal", 81, LowAggressive, 294000)
AstonVilla = Team("Aston Villa", 69, LowDefensive, 112000)
Bournemouth = Team("Bournemouth", 57, Normal, 97000)
Brentford = Team("Brentford", 54, HighDefensive, 110000)
Brighton = Team("Brighton", 63, Normal, 164000)
Burnley = Team("Burnley", 65, Normal, 127000)
Chelsea = Team("Chelsea", 84, LowAggressive, 260000)
CrystalPalace = Team("Crystal Palace", 54, LowAggressive, 187000)
Everton = Team("Everton", 74, Normal, 201000)
Fulham = Team("Fulham", 56, LowDefensive, 90000)
Liverpool = Team("Liverpool", 86, HighAggressive, 301000)
LutonTown = Team("Luton Town", 53, Normal, 54000)
ManchesterCity = Team("Manchester City", 91, HighAggressive, 280000)
ManchesterUnited = Team("Manchester United", 89, LowDefensive, 294000)
NewcastleUnited = Team("Newcastle United", 71, Normal, 176000)
NottinghamForest = Team("Nottingham Forest", 58, LowDefensive, 76000)
SheffieldUnited = Team("Sheffield United", 63, HighDefensive, 134000)
TottenhamHotspur = Team("Tottenham Hotspur", 83, Normal, 240000)
WestHamUnited = Team("West Ham United", 76, HighAggressive, 180000)
WolverhamptonWanderers = Team("Wolverhampton Wanderers", 75, LowDefensive, 99000)
allTeams = [Arsenal, AstonVilla, Bournemouth, Brentford, Brighton, Burnley, Chelsea, CrystalPalace, Everton, Fulham, Liverpool, LutonTown, ManchesterCity, ManchesterUnited, NewcastleUnited, NottinghamForest, SheffieldUnited,TottenhamHotspur,WestHamUnited,WolverhamptonWanderers]

# Match Function
def Match():
    #FixtureMaker
    print(">",week,". Week Results")
    table = PrettyTable()
    table.field_names= ["Home", " G ", " A ", "Away",]
    table.align["Home"] = "r"
    table.align["Away"] = "l"

    for i in allTeams:
        while len(allTeams) >= 1:
            for i in random.choices(allTeams):
                if  i.strategy == HighAggressive:
                    goal_home = int(int(i.power * random.randint(2,10))/100)
                    keep_home = int(int(i.power * random.randint(1,3))/100)

                elif i.strategy == LowAggressive:
                    goal_home = int(int(i.power * random.randint(2,8))/100)
                    keep_home = int(int(i.power * random.randint(1,4))/100)

                elif  i.strategy == Normal: 
                    goal_home = int(int(i.power * random.randint(3,6))/100)
                    keep_home = int(int(i.power * random.randint(2,4))/100)

                elif i.strategy == LowDefensive:
                    goal_home = int(int(i.power * random.randint(2,5))/100)
                    keep_home = int(int(i.power * random.randint(3,6))/100)

                elif i.strategy == HighDefensive:
                    goal_home = int(int(i.power * random.randint(2,5))/100)
                    keep_home = int(int(i.power * random.randint(2,7))/100)

                allTeams.remove(i)

                for a in random.choices(allTeams):
                    if  a.strategy == HighAggressive:
                        goal_away = int(int(i.power * random.randint(1,9))/100)
                        keep_away = int(int(i.power * random.randint(1,3))/100)

                    elif a.strategy == LowAggressive:
                        goal_away = int(int(a.power * random.randint(1,7))/100)
                        keep_away = int(int(a.power * random.randint(2,4))/100)

                    elif a.strategy == Normal: 
                        goal_away = int(int(a.power * random.randint(3,5))/100)
                        keep_away = int(int(a.power * random.randint(3,5))/100)

                    elif a.strategy == LowDefensive:
                        goal_away = int(int(a.power * random.randint(2,5))/100)
                        keep_away = int(int(a.power * random.randint(2,5))/100)

                    elif a.strategy == HighDefensive:
                        goal_away = int(int(a.power * random.randint(1,6))/100)
                        keep_away = int(int(a.power * random.randint(2,7))/100)

                    allTeams.remove(a)

                    goal_home = goal_home - keep_away
                    goal_away = goal_away - keep_home

                    if goal_home <=0:
                        goal_home = 0                    
                        
                    if goal_away <=0:
                        goal_away = 0

                    #MatchMaker
                    table.add_row([i.name,goal_home,goal_away,a.name],divider=True)

                    #GoalConceded
                    i.goalConceded = i.goalConceded + goal_away
                    a.goalConceded = a.goalConceded + goal_home
                    #GoalScored
                    i.goalScored = i.goalScored + goal_home
                    a.goalScored = a.goalScored + goal_away

                    #Win
                    if goal_home > goal_away:
                        #Point
                        i.point = i.point + 3
                        i.power = i.power + 0.5
                        a.power = a.power - 0.5
                        #MatchCounter
                        i.win   = i.win + 1
                        a.lose  = a.lose + 1
                        #HardMatchWin
                        if i.popularity <= 250000 and a.popularity >= 250000:
                            i.popularity = i.popularity + 20000
                            a.popularity = a.popularity - 12000
                        #EasyMatchWin
                        elif i.popularity >= 250000 and a.popularity <= 250000:
                            i.popularity = i.popularity + 7000
                            a.popularity = a.popularity - 5000
                        #Derby
                        elif i.popularity >= 250000 and a.popularity >= 250000:
                            i.popularity = i.popularity + 10000
                            a.popularity = a.popularity - 7000
                        #2LowTeamMatch    
                        else:
                            i.popularity = i.popularity + 12000
                            a.popularity = a.popularity - 10000                            
                    #Lose

                    elif goal_away > goal_home:
                        #Point
                        a.point = a.point + 3
                        i.power = i.power - 1
                        a.power = a.power + 1.5
                        #MatchCounter
                        a.win   = a.win  + 1
                        i.lose  = i.lose + 1
                        #HardMatchLose
                        if i.popularity <= 250000 and a.popularity >= 250000:
                            i.popularity = i.popularity - 7000
                            a.popularity = a.popularity + 7000
                        #EasyMatchLose
                        elif i.popularity >= 250000 and a.popularity <= 250000:
                            i.popularity = i.popularity - 10000
                            a.popularity = a.popularity + 15000
                        #Derby
                        elif i.popularity >= 250000 and a.popularity >= 250000:
                            i.popularity = i.popularity - 20000
                            a.popularity = a.popularity + 20000
                        #2LowTeamMatch    
                        else:
                            i.popularity = i.popularity - 10000
                            a.popularity = a.popularity + 12000     
                    #Draw

                    else:
                        #Point
                        i.point = i.point + 1
                        a.point = a.point + 1
                        i.power = i.power - 0.5
                        a.power = a.power + 0.5
                        #MatchCounter
                        i.draw  = i.draw  + 1
                        a.draw  = a.draw  + 1
                        #HardMatchDraw
                        if i.popularity <= 250000 and a.popularity >= 250000:
                            i.popularity = i.popularity + 10000
                            a.popularity = a.popularity - 7000
                        #EasyMatchDraw
                        elif i.popularity >= 250000 and a.popularity <= 250000:
                            i.popularity = i.popularity - 5000
                            a.popularity = a.popularity + 12000
                        #DerbyMatchDraw
                        elif i.popularity >= 250000 and a.popularity >= 250000:
                            i.popularity = i.popularity + 7000
                            a.popularity = a.popularity + 12000
                        #2LowTeamDraw
                        else:
                            i.popularity = i.popularity + 7000
                            a.popularity = a.popularity + 10000     
                    
    
    #AgainAddtoList
    for i in [Arsenal, AstonVilla, Bournemouth, Brentford, Brighton, Burnley, Chelsea, CrystalPalace, Everton, Fulham, Liverpool, LutonTown, ManchesterCity, ManchesterUnited, NewcastleUnited, NottinghamForest, SheffieldUnited,TottenhamHotspur,WestHamUnited,WolverhamptonWanderers]:
        allTeams.append(i)
    print(table)

# ScoreBoard Function
def ScoreBoard():
    for i in allTeams:
        i.WinRate()
    table = PrettyTable()
    table.field_names = ["#", "Name", "Goal Scored", "Goal Conceded", "W", "D", "L", "Power", "Strategy", "Win Rate", "Point", "Popularity"]
    table.align["Name"] = "l"
    sort = 1
    allTeams.sort(key = lambda x: (x.point, x.goalScored), reverse = True)
    for i in allTeams:
        table.add_row([sort, i.name, i.goalScored, i.goalConceded, i.win, i.draw, i.lose, i.power, i.strategy.name, i.winRate, i.point, i.popularity],divider=True)
        sort += 1
    table.set_style(SINGLE_BORDER)
    print(table)

# Choosing Team and Strategy
while True:
    table = PrettyTable()
    table.field_names = ["#", "Team", "Power", "Strategy", "Popularity"]
    table.align["Team"] = "l"
    sort = 1
    for i in allTeams:
        table.add_row([sort, i.name, i.power, i.strategy.name, i.popularity],divider=True)
        sort += 1
    table.set_style(SINGLE_BORDER)
    print(table)
    index = int(input("Choose Your Team. Enter the Team Number! "))    
    myTeam = allTeams[index-1]
    #
    table = PrettyTable()
    table.field_names = ["#", "Strategy", "Goal", "Keep"]
    table.align["Strategy"] = "l"
    sort = 1
    for i in allStrategies:
        table.add_row([sort, i.name, i.HomeGoalExpection, i.HomeKeepExpection],divider=True)
        sort += 1
    table.set_style(SINGLE_BORDER)
    print(table)
    index = int(input("Choose Your Strategy. Enter the Strategy Number! "))
    myTeam.strategy = allStrategies[index-1]
    myStrategy = allStrategies[index-1]
    break
    
# Main Loop
while True:
    print("\n-------------------------------------")
    print("           League Manager Game       ")
    print("-------------------------------------\n")
    print("> Team")
    print("---------------------")
    print("> 1: My Team")
    print("> 2: Strategy")
    print("---------------------")
    print("> League")
    print("---------------------")
    print("> 3: Fixture (Coming Soon...)")
    print("> 4: See the Scoreboard")
    print("> 5: Next Week >", week, ". Week")
    print("---------------------")
    print("> Statistics")
    print("---------------------")
    print("> 6: Most Strongest Teams")
    print("> 7: Most Popular Teams")
    print("---------------------")
    print("> 8: Info")
    print("> 0: Exit the Game\n")
    mainpagePage = int(input("Enter Number to Your Choosen Stratedy: "))

    # Exit
    if mainpagePage == 0:
        print("Exited the Game.\n")
        break

    # My Team
    elif mainpagePage == 1:
        myTeam.TeamDetails()

    # Strategy
    elif mainpagePage == 2:
        myTeam.ChangeStratedy()

    # Fixture
    elif mainpagePage == 3:
        print("Still working on it!")

    # See the Scoreboard
    elif mainpagePage == 4:
        ScoreBoard()

    # Next Week
    elif mainpagePage == 5:
        if week <= (2 * (len(allTeams)-1)):
            week += 1
            print("\n-------------------------------------")
            print("          ",week, ". Week Results    ")
            print("-------------------------------------\n")
            Match()

        elif week == (2 * (len(allTeams)-1)) + 1:
            print("\n----------------------------------------------")
            print("         The League is ended. Results!         ")
            print("----------------------------------------------\n")
            #
            ScoreBoard()
            print("Winners Teams!")
            print("1.", allTeams[0].name)
            print("2.", allTeams[1].name)
            print("3.", allTeams[2].name, "\n")
            print("---------------------------\n")
            print("Relegations Teams!")
            print("18.", allTeams[-3].name)
            print("19.", allTeams[-2].name)
            print("20.", allTeams[-1].name, "\n")

            if myTeam == allTeams[0]:
                print("> What the Hell. You are The Champion!")

            elif myTeam == allTeams[1]:
                print("> Congratulations. What a Team Spirit! You are Second! Keep Going...")

            elif myTeam == allTeams[2]:
                print("> Nice Team. You are Third! Keep Going... You deserved to join The Champions League...")

            elif myTeam == allTeams[-3]:
                print("> Sorry For That But You Elegated.")

            elif myTeam == allTeams[-2]:
                print("> Sorry For That But You Lost.")

            elif myTeam == allTeams[-1]:
                print("> Sorry For That But You are Terrible.")

            else:
                print("Nice Try. You are not bad. Try Again \n\n")

    # Most Strongest Teams
    elif mainpagePage == 6:
        for i in allTeams:
            i.WinRate()
        table = PrettyTable()
        table.field_names = ["#", "Name", "Goal Scored", "Goal Conceded", "W", "D", "L", "Power", "Strategy", "Win Rate", "Point", "Popularity"]
        table.align["Name"] = "l"
        sort = 1
        allTeams.sort(key = lambda x: x.power, reverse = True)
        for i in allTeams:
            table.add_row([sort, i.name, i.goalScored, i.goalConceded, i.win, i.draw, i.lose, i.power, i.strategy.name, i.winRate, i.point, i.popularity],divider=True)
            sort += 1
        table.set_style(SINGLE_BORDER)
        print(table)
    
    # Most Popular Teams
    elif mainpagePage == 7:
        for i in allTeams:
            i.WinRate()
        table = PrettyTable()
        table.field_names = ["#", "Name", "Goal Scored", "Goal Conceded", "W", "D", "L", "Power", "Strategy", "Win Rate", "Point", "Popularity"]
        table.align["Name"] = "l"
        sort = 1
        allTeams.sort(key = lambda x: x.popularity, reverse = True)
        for i in allTeams:
            table.add_row([sort, i.name, i.goalScored, i.goalConceded, i.win, i.draw, i.lose, i.power, i.strategy.name, i.winRate, i.point, i.popularity],divider=True)
            sort += 1
        table.set_style(SINGLE_BORDER)
        print(table)
    
    # Info
    elif mainpagePage == 8:
        print("Developer: ErenElagz")
        print("2023-2024 Premier League Text Based Football Manager Game.")
        print("Scoreboard, Teams, Strategies, Weekly Matches and more...")
        print("Have a Fun! Good Luck <3")

    # Error
    else:
        print("\nError. Please try again.")
