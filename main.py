import random
from abc import ABC, abstractmethod

teams        = ["Arsenal","Aston_Villa","Brentford","Brighto","Burnley","Chelsea","Crystal_Palace","Everton","Leeds_United","Leicester_City","Liverpool","Manchester_City","Manchester_United","Newcastle_United","Norwich_City","Southampton","Tottenham_Hotspur","Watford","West_Ham_United","Wolverhampton_Wanderers"]
strategies   = ["Aggressive","Low Aggressive","Normal","Low Defensive","Defensive"]
week_counter = 1

#SportClass
class Sport(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def Print(self):
        print("Leaguee Name: ",self.name)

#LeagueClass
class League(Sport):
    def __init__(self,name):
        super().__init__(name)
        self.name =name

    def Print(self):
        print("Leaguee Name: ",self.name)

    def RenameLeague(self):
        self.name = input("Rename The League: ")

#TeamsClass
class Teams():
    #Primary
    def __init__(self,text,name,power,team_strategy,team_strategy_object,point,goal_scored,goal_conceded,win,lose,draw,win_rate,popularity):        
        self.name                 = name
        self.text                 = text
        self.power                = power
        self.point                = point  
        self.popularity           = popularity
        #Strategy
        self.team_strategy        = team_strategy
        self.team_strategy_object = team_strategy_object
        #For Goal and Scoreboard
        self.goal_conceded        = goal_conceded
        self.goal_scored          = goal_scored
        #For Scoreboard
        self.win                  = win
        self.lose                 = lose
        self.draw                 = draw
        self.win_rate             = win_rate

    #WinRateFunc
    def WinRate(self):
        self.win_rate = round(100*(self.win/(self.win + self.lose + self.draw)),2)  
        self.win_rate = ("% "+str(self.win_rate)) 

    #PrintTeamDetails
    def PrintTeam(self):
        print("- - - - - - - - - - - - - -")
        print("Name    :  ",self.name)
        print("Power   :  ",self.power)
        print("Stratedy:  ",self.team_strategy) 
        print("Popularity:",self.popularity)
        print("- - - - - - - - - - - - - -")

    #ChangeTeamStrategy
    def ChangeStratedy(self):
        print("- - - - - - - - - - - -")
        print("\nPlease Choose Your Team Strategy")
        print("1: Aggressive")
        print("2: Low Aggressive")
        print("3: Normal")
        print("4: Low Defensive")
        print("5: Defensive")
        print("0: Stay Current Stratedy")
        print("- - - - - - - - - - - -\n")
        print(self.name)
        print("current stratedy: ",self.team_strategy)
        print("current power: ",self.power)    
        print("- - - - - - - - - - - -\n")  
        team_stratedy_number = int(input("Enter Number to Your Choosen Stratedy: "))

        if  team_stratedy_number == 0:
            pass
            
        elif team_stratedy_number == 1:           
            self.team_strategy = "Aggressive" 
            self.team_strategy_object = Aggressive

        elif team_stratedy_number == 2:
            self.team_strategy = "Low Aggressive" 
            self.team_strategy_object = Low_Aggressive

        elif team_stratedy_number == 3:
            self.team_strategy = "Normal" 
            self.team_strategy_object = Normal

        elif team_stratedy_number == 4:
            self.team_strategy = "Low Defensive" 
            self.team_strategy_object = Low_Defensive

        elif team_stratedy_number == 5:
            self.team_strategy = "Defensive" 
            self.team_strategy_object = Defensive

        else:
            print("Error.Please Try again. ") 

    #ChangeTeamPower
    def ChangePower(self):
        print("team name:     ",self.name)
        print("current skill: ",self.team_strategy)
        print("current power: ",self.power)
        self.power = int(input("Power(0/100): "))
        if 0 <= self.power <= 100:
            pass

        else:
            print("\n\n- - - - - - - - -")
            self.power = input("Only Between 0/100 ")
        print("- - - - - - - - - - - - - - -")

    #PrintAllTeamsInTheClass
    def PrintAllTeams():
        for i in all_teams_objects:
            print("\n- - - - - - - -")
            print("Team Name:",i.name)
            print("TeamStrategy:",i.team_strategy)
            print("TeamPower:",i.power)
            print("Popularity:",i.popularity)
            print("- - - - - - - -\n")

#StratedyClass
class Stratedy():
    def __init__(self,name):
        self.name = name

    #PrintStrategy
    def PrintScreen(self):
        print(self.name)
    
#MatchFunction
def Match():
    #FixtureMaker
    print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
    for i in all_teams_objects:
        while len(all_teams_objects) >= 1:
            for i in random.choices(all_teams_objects):
                if  i.team_strategy_object == Aggressive:
                    goal_home = random.randint(1,7)
                    keep_home = random.randint(1,4)

                elif i.team_strategy_object == Low_Aggressive:
                    goal_home = random.randint(1,6)
                    keep_home = random.randint(0,3)

                elif  i.team_strategy_object == Normal: 
                    goal_home = random.randint(1,5)
                    keep_home = random.randint(1,4)

                elif i.team_strategy_object == Low_Defensive:
                    goal_home = random.randint(2,5)
                    keep_home = random.randint(1,5)

                elif i.team_strategy_object == Defensive:
                    goal_home = random.randint(1,4)
                    keep_home = random.randint(2,6)

                all_teams_objects.remove(i)

                for a in random.choices(all_teams_objects):
                    if  a.team_strategy_object == Aggressive:
                        goal_away = random.randint(1,6)
                        keep_away = random.randint(0,4)

                    elif a.team_strategy_object == Low_Aggressive:
                        goal_away = random.randint(1,5)
                        keep_away = random.randint(0,3)

                    elif a.team_strategy_object == Normal: 
                        goal_away = random.randint(1,5)
                        keep_away = random.randint(0,5)

                    elif a.team_strategy_object == Low_Defensive:
                        goal_away = random.randint(1,4)
                        keep_away = random.randint(1,4)

                    elif a.team_strategy_object == Defensive:
                        goal_away = random.randint(1,4)
                        keep_away = random.randint(2,5)

                    all_teams_objects.remove(a)

                    goal_home = goal_home - keep_away
                    goal_away = goal_away - keep_home

                    if goal_home <=0:
                        goal_home = 0                    
                        
                    if goal_away <=0:
                        goal_away = 0

                    #MatchMaker
                    print("-",i.text,goal_home," - ",goal_away,a.name)
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - ")

                    #GoalConceded
                    i.goal_conceded = i.goal_conceded + goal_away
                    a.goal_conceded = a.goal_conceded + goal_home
                    #GoalScored
                    i.goal_scored = i.goal_scored + goal_home
                    a.goal_scored = a.goal_scored + goal_away
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
                        if i.popularity <= 300000 and a.popularity >= 300000:
                            i.popularity = i.popularity + 20000
                            a.popularity = a.popularity - 12000
                        #EasyMatchWin
                        elif i.popularity >= 300000 and a.popularity <= 300000:
                            i.popularity = i.popularity + 7000
                            a.popularity = a.popularity - 5000
                        #Derby
                        elif i.popularity >= 300000 and a.popularity >= 300000:
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
                        if i.popularity <= 300000 and a.popularity >= 300000:
                            i.popularity = i.popularity - 7000
                            a.popularity = a.popularity + 7000
                        #EasyMatchLose
                        elif i.popularity >= 300000 and a.popularity <= 300000:
                            i.popularity = i.popularity - 10000
                            a.popularity = a.popularity + 15000
                        #Derby
                        elif i.popularity >= 300000 and a.popularity >= 300000:
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
                        if i.popularity <= 300000 and a.popularity >= 300000:
                            i.popularity = i.popularity + 10000
                            a.popularity = a.popularity - 7000
                        #EasyMatchDraw
                        elif i.popularity >= 300000 and a.popularity <= 300000:
                            i.popularity = i.popularity - 5000
                            a.popularity = a.popularity + 12000
                        #DerbyMatchDraw
                        elif i.popularity >= 300000 and a.popularity >= 300000:
                            i.popularity = i.popularity + 7000
                            a.popularity = a.popularity + 12000
                        #2LowTeamDraw
                        else:
                            i.popularity = i.popularity + 7000
                            a.popularity = a.popularity + 10000     

                    #all_teams_objects.sort(key=lambda x: x.point, reverse = True)
                    break
    
    #AgainAddtoList
    for i in [Arsenal,Aston_Villa,Brentford,Brighto,Burnley,Chelsea,Crystal_Palace,Everton,Leeds_United,Leicester_City,Liverpool,Manchester_City,Manchester_United,Newcastle_United,Norwich_City,Southampton,Tottenham_Hotspur,Watford,West_Ham_United,Wolverhampton_Wanderers]:
        all_teams_objects.append(i)

#League OBject Created
league = League("Premier League")

#All Teams is Created
Arsenal                 = Teams("Arsenal               ","Arsenal",80.0,"Aggressive"              ,0,0,0,0,0,0,0,0,430000)
Aston_Villa             = Teams("Aston_Villa           ","Aston_Villa",55.0,"Normal"              ,0,0,0,0,0,0,0,0,190000)
Brentford               = Teams("Brentford             ","Brentford",53.0,"Defensive"             ,0,0,0,0,0,0,0,0,210000)
Brighto                 = Teams("Brighto               ","Brighto",53.0,"Normal"                  ,0,0,0,0,0,0,0,0,170000)
Burnley                 = Teams("Burnley               ","Burnley",57.0,"Low Defensive"           ,0,0,0,0,0,0,0,0,150000)
Chelsea                 = Teams("Chelsea               ","Chelsea",78.0,"Aggressive"              ,0,0,0,0,0,0,0,0,400000)
Crystal_Palace          = Teams("Crystal_Palace        ","Crystal_Palace",61.0,"Normal"           ,0,0,0,0,0,0,0,0,250000)
Everton                 = Teams("Everton               ","Everton",72.0,"Low Defensive"           ,0,0,0,0,0,0,0,0,320000)
Leeds_United            = Teams("Leeds_United          ","Leeds_United",56.0,"Defensive"          ,0,0,0,0,0,0,0,0,270000)
Leicester_City          = Teams("Leicester_City        ","Leicester_City",70.0,"Normal"           ,0,0,0,0,0,0,0,0,390000)
Liverpool               = Teams("Liverpool             ","Liverpool",82.0,"Low Aggressive"        ,0,0,0,0,0,0,0,0,420000)
Manchester_City         = Teams("Manchester_City       ","Manchester_City",79.0,"Aggressive"      ,0,0,0,0,0,0,0,0,410000)
Manchester_United       = Teams("Manchester_United     ","Manchester_United",81.0,"Low Aggressive",0,0,0,0,0,0,0,0,450000)
Newcastle_United        = Teams("Newcastle_United      ","Newcastle_United",66.0,"Low Defensive"  ,0,0,0,0,0,0,0,0,350000)
Norwich_City            = Teams("Norwich_City          ","Norwich_City",64.0,"Defensive"          ,0,0,0,0,0,0,0,0,260000)
Southampton             = Teams("Southampton           ","Southampton",55.0,"Normal"              ,0,0,0,0,0,0,0,0,270000)
Tottenham_Hotspur       = Teams("Tottenham_Hotspur     ","Tottenham_Hotspur",74.0,"Low Aggressive",0,0,0,0,0,0,0,0,420000)
Watford                 = Teams("Watford               ","Watford",62.0,"Normal"                  ,0,0,0,0,0,0,0,0,290000)
West_Ham_United         = Teams("West_Ham_United       ","West_Ham_United",68.0,"Normal"          ,0,0,0,0,0,0,0,0,310000)
Wolverhampton_Wanderers = Teams("Wolverhampton         ","Wolverhampton",56.0,"Low Defensive"     ,0,0,0,0,0,0,0,0,220000)

#All Stratedy is Created
Aggressive              = Stratedy("Aggressive")
Low_Aggressive          = Stratedy("Low Aggressive")
Normal                  = Stratedy("Normal")
Low_Defensive           = Stratedy("Low Defensive")
Defensive               = Stratedy("Defensive")

#Object Lists
all_teams_objects = [Arsenal,Aston_Villa,Brentford,Brighto,Burnley,Chelsea,Crystal_Palace,Everton,Leeds_United,Leicester_City,Liverpool,Manchester_City,Manchester_United,Newcastle_United,Norwich_City,Southampton,Tottenham_Hotspur,Watford,West_Ham_United,Wolverhampton_Wanderers]
all_skill_objects = [Aggressive,Low_Aggressive,Normal,Low_Defensive,Defensive]

#LandingPageLoop
while True:
    league.Print()
    print("Welcome to Football Manager Game for",league.name)

    # Team Select
    print("-----------------------------------------------")
    for i in teams:
        print("-",i)
    print("-----------------------------------------------")    
    my_team = input("Choose a team from the list above: ") 

    if my_team in teams:
        for i in strategies:
            print("-",i)
        my_strategy = input("Choose a team from the list above: ") 

        if my_strategy in strategies:
            print("\nNice Chooses. Let's Play.\n")
            break
        else:
            print("Error.")
    else:
        print("Error.")

#My Team Details Added to The MyTeam Variable
for i in all_teams_objects:
    if my_team in i.name:
        our_team = i
for i in all_skill_objects:
    if my_strategy in i.name:
        our_strategy = i
        our_team.team_strategy = my_strategy

#Teams and Strategies is united
for i in all_teams_objects:         
    if i.team_strategy == "Aggressive" :
        i.team_strategy_object = Aggressive

    elif i.team_strategy == "Low Aggressive":
        i.team_strategy_object = Low_Aggressive

    elif i.team_strategy == "Normal":
        i.team_strategy_object = Normal   

    elif i.team_strategy == "Low Defensive":
        i.team_strategy_object = Low_Defensive

    elif i.team_strategy == "Defensive":
        i.team_strategy_object = Defensive
       
#MainPageLoop
while True:
    #MainPage
    print("========================================================")
    print("===============",league.name,"MainPage","===============")
    print("1: Team")
    print("2: League")
    print("3: Options")
    print("0: Exit\n")
    mainpage_page = int(input("Choose Any Page Number: "))

    #Exit
    if  mainpage_page  == 0:
        break

    #TeamPage
    elif mainpage_page == 1:
        print("\n------------------------------------")
        print("--------------- Team ---------------")
        print("1: My Team")        
        print("2: Change Stratedy")
        print("3: League Teams")
        print("0: Back to MainPage\n")
        team_page = int(input("Choose Any Page Number: "))

        while True:
            #BackToMainPage 
            if team_page  ==  0 :
                break
            
            #My Team
            elif team_page == 1 :
                our_team.PrintTeam()
                break

            #Change Stratedy
            elif team_page == 2 :
                our_team.ChangeStratedy()
                break

            #Other Teams
            elif team_page == 3 :
                Teams.PrintAllTeams()
                break
            
            #Error
            else :
                print("Error. Please try again.")

    #MatchPage
    elif mainpage_page == 2:
        print("\n-------------------------------------")
        print("--------------- League ---------------")
        print("1: Go to Next Week","(Week-"+str(week_counter)+")")
        print("2: See the ScoreBoard")
        print("3: Fast Change Strategy") 
        print("0: Back To The Menu\n")
        league_page = int(input("Choose Any Page Number: "))

        while True:
            #BackToMainPage
            if league_page == 0 :
                break

            #NextWeekPage
            elif league_page == 1 :
                if week_counter <= 38:
                    week_counter = week_counter + 1  
                    #WeekResults
                    print("\n-----------",str(week_counter),". Week Results -----------")
                    Match()
                    break           
                    
                elif week_counter == 39 :
                    print("\n----------------------------------------------")
                    print("-   The League is ended. Go to Scoreboard    -")
                    print("----------------------------------------------\n")

                    all_teams_objects.sort(key=lambda x: x.point, reverse = True)
                    print("Winners Teams!")
                    print("1.",all_teams_objects[0].name)
                    print("2.",all_teams_objects[1].name)
                    print("3.",all_teams_objects[2].name,"\n")

                    print("Relegations Teams!")
                    print("18.",all_teams_objects[17].name)
                    print("19.",all_teams_objects[18].name)
                    print("20.",all_teams_objects[19].name,"\n")

                    if our_team == all_teams_objects[0]:
                        print("What the Hell. You are Best! Keep Going... ")
                        print("Now. We will be best in The Champions League (Coming Soon)")
                    
                    elif our_team == all_teams_objects[1]:
                        print("Congratulations.What a Team Spirit!  You are Second! You deserved to join The Champions League...")

                    elif our_team == all_teams_objects[2]:
                        print("Nice Team . You are Third! Keep Going...You deserved to join The Champions League...")         

                    elif our_team == all_teams_objects[17]:
                        print("Sorry For That But You Lost.")   
                                        
                    elif our_team == all_teams_objects[18]:
                        print("Sorry For That But You Lost.")   

                    elif our_team == all_teams_objects[19]:
                        print("Sorry For That But You are Trash.")   

                    else:
                        print("Hey! You are not bad.Try Again \n\n")                    
                    break

            #Scoreboard                        
            elif league_page == 2 :
                for i in all_teams_objects:
                    i.WinRate()
                    
                    all_teams_objects.sort(key=lambda x: x.point, reverse = True)
                sort = 1
                
                print("  |              Name               |  Point  |  Goal Scored  |  Goal Conceded  |   W   |   D   |   L   |  WinRate  |    Popularity    |  Power  |    Current Stratedy   |")
                print("  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                for i in all_teams_objects:
                    print("  ",sort,"- ",i.text,"        ",i.point,"          ",i.goal_scored,"           ",i.goal_conceded,"           ",i.win,"    ",i.draw,"    ",i.lose,"    ",i.win_rate,"     ",i.popularity,"     ",i.power,"     ",i.team_strategy)
                    print(" -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  ")
                    sort = sort+1
                break

            #FastChangeStrategy
            elif league_page == 3:
                our_team.ChangeStratedy()
                break

            #Error
            else:
                print("Error. Please try again .")
                break                      
    
    #OptionsPage
    elif mainpage_page == 3:
        print("\n------------------------------------")
        print("------------- Options --------------")
        print("1- Choose Team Power")
        print("2- Change Team Stratedy")
        print("3: Rename the League")
        print("0- Back to MainPage\n")
        options_page = int(input("Choose Any Page Number: "))

        while True:
            #BackToMainPage
            if options_page == 0:
                break

            #Change Team Power
            elif options_page == 1:
                    print("\n\n------------------------------------------------")
                    for i in [Arsenal,Aston_Villa,Brentford,Brighto,Burnley,Chelsea,Crystal_Palace,Everton,Leeds_United,Leicester_City,Liverpool,Manchester_City,Manchester_United,Newcastle_United,Norwich_City,Southampton,Tottenham_Hotspur,Watford,West_Ham_United,Wolverhampton_Wanderers]:
                        i.ChangePower()
                    print("------------------------------------\n\n")
                    break
            
            #Change Team Stratedy
            elif options_page == 2:
                    print("\n\n---------------------------------------------------")
                    for i in [Arsenal,Aston_Villa,Brentford,Brighto,Burnley,Chelsea,Crystal_Palace,Everton,Leeds_United,Leicester_City,Liverpool,Manchester_City,Manchester_United,Newcastle_United,Norwich_City,Southampton,Tottenham_Hotspur,Watford,West_Ham_United,Wolverhampton_Wanderers]:
                        i.ChangeStratedy()
                    print("------------------------------------\n\n")
                    break

            elif options_page == 3:
                league.name = input("Enter The New League Name: ")
                break

            #Error
            else:
                print("Error. Please try again.")
                break
    #Error
    else:
        print("Error. Please try again .")
        break
