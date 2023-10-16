
import pandas as pd
import urllib3
import certifi
import xmltodict
from bs4 import BeautifulSoup
import os

## Initilize all lists that will be used to sort the recipes
sorted_recipes = []
## Fruit related lists
fruit = []
apple = []
banana = []
blueberry = []
cherry = []
cranberry = []
lemon = []
orange = []
peach = []
pineapple = []
pumpkin = []
raspberry = []
strawberry = []
tomato = []

## Vegetable related lists
vegetable = []
artichoke = []
asparagus = []
bean = []
broccoli = []
carrot = []
cauliflower = []
corn = []
eggplant = []
lettuce = []
potato = []
spinach = []
zucchini = []

## Dairy related lists
dairy = []
alfredo = []
brie = []
cheddar = []
cheese = []
gruyere = []
mozzarella = []
parmesan = []
ricotta = []
yogurt = []

## Meat related lists
meat = []
bacon = []
beef = []
chicken = []
crab = []
fish = []
meatballs = []
pork = []
roast = []
sausage = []
seafood = []
shrimp = []
steak = []

## Desserts and sweets related lists
dessert = []
cake = []
cannoli = []
cheesecake = []
creamPuffs = []
custard = []
danish = []
fudge = []
iceCream = []
mousse = []
pastry = []
pie = []
pudding = []
tart = []
tiramisu = []
trifle = []
truffle = []

cookie = []
biscotti = []
shortbread = []
gingerbread = []
ladyfinger = []

bars = []

brownies = []
blondies = []

## Pasta, noodle, dumpling related lists
pasta = []
dumpling = []
gnocchi = []
## Lasagna and lasagne to be under same list
lasagna = []
lasagne = []
macaroni = []
noodle = []
pierogi = []
ravioli = []
risotto = []
spaghetti = []
tortellini = []
wonton = []

## Drink related lists
drink = []

## Bread related lists
bread = []
babka = []
brioche = []
rolls = []
pita = []
naan = []
## Biscuits as well as scones
biscuit = []
bagel = []
pizza = []
focaccia = []
breadsticks = []
flatbread = []
pretzel = []


tortilla = []
wraps = []

## Breakfast food related lists
breakfast = []
cinnamonRoll = []
## Donuts includes sopapilla and beignets
donuts = []
granola = []
muffins = []
oatmeal = []
pancake = []
waffles = []

## Misc lists

flavors = []
eggs = []
nuts = []
miscFood = []

databaseExists = ()
## Begin the program by asking the user if they would like to re-initialize the database, if a database.csv
## file already exists. 
def mainloop():
    ## This will occur if someone clicks on the sitemapimport.py instead of the recipedatabase.py, if they want to redo the database instead of through the recipedatabase.py
    df = pd.DataFrame([])
    ## By asking before recreating the database each time the program runs, it will reduce the amount of time
    ## the program takes to load.
    ## The program checks to see if the file exists currently.
    if os.path.exists('database.csv'):
        global databaseExists
        databaseExists = ("true")
        userInput = input("Recipe database already exists. Would you like to re-initialize the database? Y/N: ")
        ## Y will delete the database.csv file
        if userInput == "y":
            os.remove('database.csv')
            createLoop()
        ## N will instead exit the program 
        if userInput == 'n':
            print("Database will stay the same.")
            exit()
        ## If answer is neither Y or N, the program will not recognize the input and ask for the user to
        ## reinput their answer.
        else:
            print("Answer inputted was not 'Y' or 'N'. Please try again.")
    ## If there is not a database.csv file, the program will call the loop to create it. 
    elif():            
        databaseExists = ("false")
        createLoop()


## Start the program by collecting recipes from internet
def createLoop():
    if os.path.exists('database.csv'):
        os.remove('database.csv')
    ## Make new database.csv
    with open('database.csv', 'a', newline='') as file:
        ## Send an HTTPS request for the sitemap to retrieve the urls
        https = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
        ## Certifi is used to allow the use of https requests, which we want to do for security reasons
        url = ['https://glutenfreeonashoestring.com/post-sitemap.xml', 'https://glutenfreeonashoestring.com/post-sitemap2.xml', 'https://www.letthemeatgfcake.com/post-sitemap.xml']
        for url in url:
            response = https.request('GET', url)
        ## Convert the XMLs to dictonary
            sitemap = xmltodict.parse(response.data)
            sitemap_df = pd.DataFrame.from_dict(sitemap['urlset']['url'])
            ## Exports the data into a CSV file
            sitemap_df.to_csv('database.csv', mode='a', index=False)

            listMaker()
## listMaker sorts the given csv file into just the urls to sort
def listMaker():
    ## Opens the CSV file for reading
    import csv
    with open('database.csv', 'r') as csv_file:
        ## Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        ## Initalize an empty list to store the sorted data
        ## Read and process each line in the CSV file
        for row in csv_reader:
            column_to_sort = row[0]
            ## Adds the recipes to the initalized list
            sorted_recipes.append(column_to_sort)
            fruitLoop()

## Create a loop to tag recipes that include fruit ingredients
## in the URL
def fruitLoop():
   
    ## Reads each line for keywords
    for item in sorted_recipes:
        ## Assigns variable to the URL being read
        link = item
       
        ## Assigns a master list (Fruit) that will assign all fruit words found to be added to the Fruit list
        
        fruitwords = ["fruit", "apple", "banana", "blueberry", "cherry", "cranberry", "lemon", "orange", "peach", "pineapple", "pumpkin", "raspberry", "strawberry", "tomato"]
        
        ## These lists define the word to be searched for each list
        appleWord = ("apple")
        bananaWord = ("banana")
        blueberryWord  = ("blueberry")
        cherryWord = ("cherry")
        cranberryWord = ("cranberry")
        lemonWord = ("lemon")
        orangeWord = ("orange")
        peachWord = ("peach")
        pineappleWord = ("pineapple")
        pumpkinWord = ("pumpkin")
        raspberryWord = ("raspberry")
        strawberryWord = ("strawberry")
        tomatoWord = ("tomato")

        ## Tests each link to see if the word is in the fruitwords list
        for i in fruitwords:
            if i in link:
                fruit.append(link)

        ## Sorts all recipes into respective ingredient lists
        if appleWord in link and not pineappleWord in link:
            apple.append(link)

        if bananaWord in link:
            banana.append(link)
        
        if blueberryWord in link:
            blueberry.append(link)

        if cherryWord in link:
            cherry.append(link)
        
        if cranberryWord in link:
            cranberry.append(link)
        
        if lemonWord in link:
            lemon.append(link)

        if orangeWord in link:
            orange.append(link)

        if peachWord in link:
            peach.append(link)

        if pineappleWord in link:
            pineapple.append(link)
        
        if pumpkinWord in link:
            pumpkin.append(link)

        if raspberryWord in link:
            raspberry.append(link)

        if strawberryWord in link:
            strawberry.append(link)
        
        if tomatoWord in link:
            tomato.append(link)
    ## Once the program has gone through all and sorted all URLs into related lists, 
    ## it will go on to the next ingredient type loop
    vegLoop()
    
def vegLoop():
    ## This list will follow the same logic as the fruitLoop and will define all vegetable related items
    for item in sorted_recipes:
        link = item

        vegWords = ["veggie", "vegetable", "artichoke", "asparagus", "bean", "broccoli", "carrot", "cauliflower", "corn", "eggplant", "lettuce", "potato", "spinach", "zucchini"]

        artichokeWord = ("artichoke")
        asparagusWord = ("asparagus")
        beanWord = ("bean")
        broccoliWord = ("broccoli")
        carrotWord = ("carrot")
        cauliflowerWord = ("cauliflower")
        cornWord = ("corn")
        eggplantWord = ("eggplant")
        lettuceWord = ("lettuce")
        potatoWord = ("potato")
        spinachWord = ("spinach")
        zucchiniWord = ("spinach")

        for i in vegWords:
            if i in link:
                vegetable.append(link)

        if artichokeWord in link:
            artichoke.append(link)

        if asparagusWord in link:
            asparagus.append(link)

        if beanWord in link:
            bean.append(link)
            
        if broccoliWord in link:
            broccoli.append(link)
            
        if carrotWord in link:
            carrot.append(link)
            
        if cauliflowerWord in link:
            cauliflower.append(link)

        if cornWord in link  and not "popcorn" in link:
            corn.append(link)

        if eggplantWord in link:
            eggplant.append(link)
            
        if lettuceWord in link:
            lettuce.append(link)

        if potatoWord in link:
            potato.append(link)

        if spinachWord in link:
            spinach.append(link)

        if zucchiniWord in link:
            zucchini.append(link)
    ## Calls the next loop
    dairyLoop()

def dairyLoop():
    ## This list loop will sort all dairy/cheese related items
    for item in sorted_recipes:
        link = item
    
        dairyWords = ["milk", "ice-cream", "brie", "cheddar", "cheese", "gruyere", "mozzarella", "parm", "parmesan", "ricotta", "yogurt"]

        cheeseWords = ["brie", "cheddar", "cheese", "gruyere", "mozzarella", "parm", "parmesan", "ricotta"]

        parmesanWords = ["parm", "parmesan"]
         
        iceCreamWords = ("ice-cream")
        brieWords = ("brie")
        cheddarWords = ("cheddar")
        gruyereWords = ("gruyere")
        mozzarellaWords = ("mozzarella")
        ricottaWords = ("ricotta")
        yogurtWords = ("yogurt")

        for i in dairyWords:
            if i in link:
                dairy.append(link)

        for i in cheeseWords:
            if i in link:
                cheese.append(link)

        for i in parmesanWords:
            if i in link:
                parmesan.append(link)

        if iceCreamWords in link:
            iceCream.append(link)

        if brieWords in link:
            brie.append(link)

        if cheddarWords in link:
            cheddar.append(link)

        if gruyereWords in link:
            gruyere.append(link)
            
        if mozzarellaWords in link:
            mozzarella.append(link)
            
        if ricottaWords in link:
            ricotta.append(link)
            
        if yogurtWords in link:
            yogurt.append(link)
    ## Calls the next loop
    meatLoop()
    
def meatLoop():
    ## This loop will sort all meat/seafood related items
    for item in sorted_recipes:
        link = item

        meatWords = ["bacon", "beef", "chicken", "crab", "fish", "meatball", "pork", "roast", "sausage", "seafood", "shrimp", "steak"]

        seafoodWords = ["crab", "fish", "seafood", "shrimp"]

        baconWords = ("bacon")
        beefWords = ("beef")
        chickenWords = ("chicken")
        crabWords = ("crab")
        fishWords = ("fish")
        meatballWords = ("meatball")
        porkWords = ("pork")
        roastWords = ("roast")
        sausageWords = ("sausage")
        shrimpWords = ("shrimp")
        steakWords = ("steak")

        for i in meatWords:
            if i in link:
                meat.append(link)

        for i in seafoodWords:
            if i in link:
                seafood.append(link)
            
        if baconWords in link:
            bacon.append(link)

        if beefWords in link:
            beef.append(link)
            
        if chickenWords in link:
            chicken.append(link)

        if crabWords in link:
            crab.append(link)

        if fishWords in link:
            fish.append(link)

        if meatballWords in link:
            meatballs.append(link)

        if porkWords in link:
            pork.append(link)

        if roastWords in link and not "roasted" in link:
            roast.append(link)

        if sausageWords in link:
            sausage.append(link)

        if shrimpWords in link:
            shrimp.append(link)

        if steakWords in link:
            steak.append(link)
    ## Calls the next loop
    dessertLoop()

def dessertLoop():
    ## This loop will sort all dessert/sweets related items
    for item in sorted_recipes:
        link = item

        dessertWords = ["dessert", "cake", "cannoli", "cheesecake", "cream-puff", "custard", "fudge", "danish", "ice-cream", "mousse", "pastry", "pie", "pudding", "tart", "tiramisu", "trifle", "truffle", "cookie", "biscotti", "shortbread", "gingerbread", "ladyfinger", "bar", "square", "brownie", "blondie"]

        cookieWords = ["cookie", "biscotti", "shortbread", "gingerbread", "ladyfinger", "oreo"]

        barWords = ["bar", "square"]

        brownieWords = ["brownie", "blondie"]

        cakeWords = ("cake")
        cannoliWords = ("cannoli")
        cheesecakeWords = ("cheesecake")
        creamPuffsWords = ("cream-puff")
        custardWords = ("custard")
        danishWords = ("danish")
        fudgeWords = ("fudge")
        mousseWords = ("mousse")
        pastryWords = ("pastry")
        pieWords = ("pie")
        puddingWords = ("pudding")
        tartWords = ("tart")
        tiramisuWords = ("tiramisu")
        trifleWords = ("trifle")
        truffleWords = ("truffle")
        biscottiWords = ("biscotti")
        shortbreadWords = ("shortbread")
        gingerbreadWords = ("gingerbread")
        ladyfingerWords = ("ladyfinger")
        blondieWords = ("blondie")

        for i in dessertWords:
            if i in link:
                dessert.append(link)

        for i in cookieWords:
            if i in link:
                cookie.append(link)

        for i in barWords:
            if i in link:
                bars.append(link)
        
        for i in brownieWords:
            if i in link:
                brownies.append(link)
        
        if cakeWords in link:
            cake.append(link)

        if cannoliWords in link:
            cannoli.append(link)
        
        if cheesecakeWords in link:
            cheesecake.append(link)

        if creamPuffsWords in link:
            creamPuffs.append(link)

        if custardWords in link:
            custard.append(link)
        
        if danishWords in link:
            danish.append(link)

        if fudgeWords in link:
            fudge.append(link)
        
        if mousseWords in link:
            mousse.append(link)
        
        if pastryWords in link:
            pastry.append(link)
        
        if pieWords in link:
            pie.append(link)
        
        if puddingWords in link:
            pudding.append(link)
        
        if tartWords in link:
            tart.append(link)

        if tiramisuWords in link:
            tiramisu.append(link)
        
        if trifleWords in link:
            trifle.append(link)
        
        if truffleWords in link:
            truffle.append(link)
        
        if biscottiWords in link:
            biscotti.append(link)
        
        if shortbreadWords in link:
            shortbread.append(link)
        
        if gingerbreadWords in link:
            gingerbread.append(link)
        
        if ladyfingerWords in link:
            ladyfinger.append(link)
        
        if blondieWords in link:
            blondies.append(link)
    ## Calls the next loop
    pastaLoop()

def pastaLoop():
    ## This loop will sort all pasta/noodle related items
    for item in sorted_recipes:
        link = item

        pastaWords = ["pasta", "dumpling", "gnocchi", "lasagna", "lasagne", "macaroni", "noodle", "pierogi", "ravioli", "risotto", "spaghetti", "tortellini", "wonton"]

        lasagnaWords = ["lasagna", "lasagne"]

        dumplingWords = ["dumpling, pierogi, tortellini, wonton"]

        gnocchiWords = ("gnocchi")
        noodleWords = ("noodle")
        pierogiWords = ("pierogi")
        ravioliWords = ("ravioli")
        risottoWords = ("risotto")
        tortelliniWords = ("tortellini")            
        wontonWords = ("wonton")
    
        for i in pastaWords:
            if i in link:
                pasta.append(link)

        for i in dumplingWords:
            if i in link:
                dumpling.append(link)
    
        for i in lasagnaWords:
            if i in link:
                lasagna.append(link)
        
        if gnocchiWords in link:
            gnocchi.append(link)
        
        if noodleWords in link:
            noodle.append(link)
        
        if pierogiWords in link:
            pierogi.append(link)
        
        if ravioliWords in link:
            ravioli.append(link)

        if risottoWords in link:
            risotto.append(link)
        
        if tortelliniWords in link:
            tortellini.append(link)

        if wontonWords in link:
            wonton.append(link)
    ## Calls the next loop
    drinkLoop()

def drinkLoop():
    ## This list will sort all drink related items into a single drink list
    for item in sorted_recipes:
        link = item

        drinkWords = ["drink", "smoothie", "soda", "eggnog", "coffee", "tea", "lemonade", "shake"]

        for i in drinkWords:
            if i in link:
                drink.append(link)
    ## Calls the next loop
    breadLoop()

def breadLoop():
    ## This list will sort all bread and dough related items
    for item in sorted_recipes:
        link = item

        breadWords = ["bread", "babka", "brioche", "rolls", "pita", "naan", "biscuit", "scone", "bagel", "pizza", "breakstick", "flatbread", "pretzel", "tortilla", "wrap", "focaccia", "dough"]

        biscuitWords = ["biscuit", "scone"]
        
        tortillaWords = ["tortilla", "wrap"]

        babkaWords = ("babka")
        briocheWords = ("brioche")
        rollWords = ("roll")
        pitaWords = ("pita")
        naanWords = ("naan")
        bagelWords = ("bagel")
        pizzaWords = ("pizza")
        focacciaWords = ("focaccia")
        breadstickWords = ("breadstick")
        flatbreadWords = ("flatbread")
        pretzelWords = ("pretzel")

        for i in breadWords:
            if i in link:
                bread.append(link)
        
        for i in biscuitWords:
            if i in link:
                biscuit.append(link)
        
        for i in tortillaWords:
            if i in link:
                tortilla.append(link)

        if babkaWords in link:
            babka.append(link)
        
        if briocheWords in link:
            brioche.append(link)
        
        if rollWords in link:
            rolls.append(link)
        
        if pitaWords in link:
            pita.append(link)
        
        if naanWords in link:
            naan.append(link)

        if bagelWords in link:
            bagel.append(link)

        if pizzaWords in link:
            pizza.append(link)
        
        if focacciaWords in link:
            focaccia.append(link)
        
        if breadstickWords in link:
            breadsticks.append(link)

        if flatbreadWords in link:
            flatbread.append(link)
        
        if pretzelWords in link:
            pretzel.append(link)
    ## Calls next loop
    breakfastLoop()

def breakfastLoop():
    for item in sorted_recipes:
        link = item

        breakfastWords = ["cinnamon-roll", "donut", "bagel", "granola", "doughnut", "muffin", "oatmeal", "pancake", "waffle"]

        donutWords = ["donut", "doughnut"]

        cinnamonRollWords = ("cinnamon-roll")
        granolaWords = ("granola")
        muffinWords = ("muffin")
        oatmealWords = ("oatmeal")
        pancakeWords = ("pancake")
        waffleWords = ("waffle")

        for i in breakfastWords:
            if i in link:
                breakfast.append(link)
        
        for i in donutWords:
            if i in link:
                donuts.append(link)
            
        if cinnamonRollWords in link:
            cinnamonRoll.append(link)

        if granolaWords in link:
            granola.append(link)

        if muffinWords in link:
            muffins.append(link)

        if oatmealWords in link:
            oatmeal.append(link)
        
        if pancakeWords in link:
            pancake.append(link)
        
        if waffleWords in link:
            waffles.append(link)
    miscLoop()

def miscLoop():
    for item in sorted_recipes:
        link = item

        flavorWords = ["chocolate", "caramel", "cinnamon", "coconut", "mint", "peanut-butter", "vanilla"]

        eggWords = ["egg", "omelette", "quiche"]

        foodWords = ["burrito", "taco", "sandwich", "cracker", "gravy", "rice"]

        nutWords = ["nut", "almond", "pecan", "peanut", "peanut", "walnut", "hazelnut"]

        for i in flavorWords:
            if i in link:
                flavors.append(link)
        
        for i in eggWords:
            if i in link and not 'eggplant' in link:
                eggs.append(link)

        for i in foodWords:
            if i in link:
                miscFood.append(link)
        
        for i in nutWords:
            if i in link:
                nuts.append(link)
    
## Begin loop



## Remove any duplicates in the list
fruit = list(set(fruit))
apple = list(set(apple))
banana = list(set(banana))
blueberry = list(set(blueberry))
cherry = list(set(cherry))
cranberry = list(set(cranberry))
lemon = list(set(lemon))
orange = list(set(orange))
peach = list(set(peach))
pineapple = list(set(pineapple))
pumpkin = list(set(pumpkin))
raspberry = list(set(raspberry))
strawberry = list(set(strawberry))
tomato = list(set(tomato))

vegetable = list(set(vegetable))
artichoke = list(set(artichoke))
bean = list(set(bean))
broccoli = list(set(broccoli))
carrot = list(set(carrot))
cauliflower = list(set(cauliflower))
corn = list(set(corn))
eggplant = list(set(eggplant))
lettuce = list(set(lettuce))
potato = list(set(potato))
spinach = list(set(spinach))
zucchini = list(set(zucchini))

dairy = list(set(dairy))
cheese = list(set(cheese))
parmesan = list(set(parmesan))
iceCream = list(set(iceCream))
brie = list(set(brie))
cheddar = list(set(cheddar))
gruyere = list(set(gruyere))
mozzarella = list(set(mozzarella))
ricotta = list(set(ricotta))
yogurt = list(set(yogurt))

meat = list(set(meat))
seafood = list(set(seafood))
bacon = list(set(bacon))
beef = list(set(beef))
chicken = list(set(chicken))
crab = list(set(crab))
fish = list(set(fish))
meatballs = list(set(meatballs))
pork = list(set(pork))
roast = list(set(roast))
sausage = list(set(sausage))
shrimp = list(set(shrimp))
steak = list(set(steak))

dessert = list(set(dessert))
cookie = list(set(cookie))
bars = list(set(bars))
brownies = list(set(brownies))
cake = list(set(cake))
cannoli = list(set(cannoli))
cheesecake = list(set(cheesecake))
creamPuffs = list(set(creamPuffs))
custard = list(set(custard))
danish = list(set(danish))
fudge = list(set(fudge))
mousse = list(set(mousse))
pastry = list(set(pastry))
pie = list(set(pie))
pudding = list(set(pudding))
tart = list(set(tart))
tiramisu = list(set(tiramisu))
trifle = list(set(trifle))
truffle = list(set(truffle))
biscotti = list(set(biscotti))
shortbread = list(set(shortbread))
gingerbread = list(set(gingerbread))
ladyfinger = list(set(ladyfinger))
blondies = list(set(blondies))

pasta = list(set(pasta))
dumpling = list(set(dumpling))
lasagna = list(set(lasagna))
gnocchi = list(set(gnocchi))
noodle = list(set(noodle))
pierogi = list(set(pierogi))
ravioli = list(set(ravioli))
risotto = list(set(risotto))
tortellini = list(set(tortellini))
wonton = list(set(wonton))

drink = list(set(drink))

bread = list(set(bread))
biscuit = list(set(biscuit))
tortilla = list(set(tortilla))
babka = list(set(babka))
brioche = list(set(brioche))
rolls = list(set(rolls))
pita = list(set(pita))
naan = list(set(naan))
bagel = list(set(bagel))
pizza = list(set(pizza))
focaccia = list(set(focaccia))
breadsticks = list(set(breadsticks))
flatbread = list(set(flatbread))
pretzel = list(set(pretzel))

breakfast = list(set(breakfast))
donuts = list(set(donuts))
cinnamonRoll = list(set(cinnamonRoll))
granola = list(set(granola))
muffins = list(set(muffins))
oatmeal = list(set(oatmeal))
pancake = list(set(pancake))
waffles = list(set(waffles))

flavors = list(set(flavors))
eggs = list(set(eggs))
miscFood = list(set(miscFood))
nuts = list(set(nuts))
