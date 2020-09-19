
########################################################################
## Get and print a random cocktail receipe from www.thecocktaildb.com ##
########################################################################

import requests
import json
from PIL import Image

def PerformApiRequest(RequestURL):

  Response = requests.get(RequestURL)
  ResponseBody = Response.json()

  return ResponseBody



def PrintCockTailInfo(ResponseBody):

  # ParseJSON = json.loads(ResponseBody)
  # PrettyPrintJSON = json.dumps(ResponseBody, indent=2)
  
  CocktailName = "Name: " + ResponseBody["drinks"][0]["strDrink"]
  Alcoholic = "Is Alcoholic: " + ResponseBody["drinks"][0]["strAlcoholic"]
  Glass = "Glass: " + ResponseBody["drinks"][0]["strGlass"]
  ImgURL = "Image: " + ResponseBody["drinks"][0]["strDrinkThumb"]
  Instructions = "Instructions: " + ResponseBody["drinks"][0]["strInstructions"]


  print('\n')
  print(CocktailName)
  print(Alcoholic)
  print(Glass)
  print(ImgURL)
  
  MeasureList = []
  IngredientsList = []

  print("------------")
  print("Ingredients:")
  for key in ResponseBody["drinks"][0]:

    if "strMeasure" in key and ResponseBody["drinks"][0][key]!= None:
      MeasureList.append(ResponseBody["drinks"][0][key])

    if "strIngredient" in key and ResponseBody["drinks"][0][key]!= None:
      IngredientsList.append(ResponseBody["drinks"][0][key])
  
  i = 0
  while i < len(IngredientsList):
    print(MeasureList[i] + IngredientsList[i])
    i+=1
  print("------------")

  print(Instructions)





def main():
  # Random Cocktails URL
  BaseURL = "https://www.thecocktaildb.com"
  EndPoint = "/api/json/v1/1/random.php"
  Response1 = PerformApiRequest(BaseURL+EndPoint)

  PrintCockTailInfo(Response1)

  print('\n' + "Execution over...")


main()