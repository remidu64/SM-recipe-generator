"""
Code by remidu64

Elektromania - Sky High is a good music CHANGE MY MIND
"""

print("To use the craft generator, simply write\nGenerateCraft(Output, Output Quantity, Crafting time, Ingredient1, Amount1, Ingredient2, Amount2, etc) \n\n"
      "The final script will be written in the Output.txt file and in the python console and you just need to copy\nand paste it on the top of the craftbot.json file\n\n"
      "To see the full list of items, open Survival Items.txt or go to https://scrapmechanictools.com/lua/Lists/Uuids/#block-and-part-uuids\nand search in the survival items category")

# Gotta define some characters cuz you cant do f"{}" whilst treating the {} as characters and not things for instruction
CBR = "{"  # Curly Bracket Right
CBL = "}"  # Curly Bracket Left
Q = "\""

ItemList = open("Crafting Recipe Generator assets and output/Survival Items.txt", "r") #Open the needed files

exec(ItemList.read()) #Define EVERY SINGLE ITEMS (Took me a few hours to make the file)


def GenerateCraft(OutputItem, OutputQuantity, CraftingTime, *IngredientsAndAmount): #Order for *IngredientsAndAmount: Ingredient1, Amount1, Ingredient2, Amount2, etc
    Output = open("Crafting Recipe Generator assets and output/Output.txt", "w")
    ingredients = ""
    amount = ""
    ingredientsList = []
    amountList = []
    finalstr = ""
    tempstr = ""

    for i in range(len(IngredientsAndAmount)): #Spaghetti code ahead
        if i % 2 == 0: #Ingredients are in even positions, Amounts are in odd positions
            ingredients += str(IngredientsAndAmount[i])
            ingredientsList.append(ingredients)
            ingredients = ""
        else:
            amount += str(IngredientsAndAmount[i])
            amountList.append(amount)
            ingredients = ""

    # Make the Output part
    finalstr = f"{CBR}\n" \
               f"   {Q}itemId{Q}: {Q}{OutputItem}{Q},\n" \
               f"   {Q}quantity{Q}: {OutputQuantity},\n" \
               f"   {Q}craftTime{Q}: {CraftingTime},\n" \
               f"   {Q}ingredientList{Q}: [\n"

    #Make the Input part
    for i in range(len(amount)):
        if not i+1 == len(amount):
            tempstr += \
                    f"       {CBR}\n" \
                    f"           {Q}quantity{Q}: {amount[i]},\n" \
                    f"           {Q}itemId{Q}: {Q}{ingredientsList[i]}{Q}\n" \
                    f"       {CBL},\n"
        else:
            tempstr += \
                f"       {CBR}\n" \
                f"           {Q}quantity{Q}: {amount[i]},\n" \
                f"           {Q}itemId{Q}: {Q}{ingredientsList[i]}{Q}\n" \
                f"       {CBL}\n"

    #Assemble the Inputs and Outputs together
    finalstr += f"{tempstr}\n" \
                f"      ]\n" \
                f"{CBL},"

    #Write everything to the Output.txt file (and print the result to the console cuz why not)
    print(finalstr)
    Output.write(finalstr)
    Output.close()