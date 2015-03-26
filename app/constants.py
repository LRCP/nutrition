from collections import OrderedDict
import copy
#refer to page 9 of the USDA database
# food_nutrient_dictionary = {
#     "Calorie Information": OrderedDict(),
#     "Carbohydrates": OrderedDict(),
#     "Fats & Fatty Acids": OrderedDict(),
#     "Protein & Amino Acids": OrderedDict(),
#     "Vitamins": OrderedDict(),
#     "Minerals": OrderedDict(),
#     "Sterols": OrderedDict(),
#     "Other": OrderedDict(),
# }
food_nutrient_dictionary_new = {
    "Calorie Information": OrderedDict(),
    "Carbohydrates": OrderedDict(),
    "Fats & Fatty Acids": OrderedDict(),
    "Protein & Amino Acids": OrderedDict(),
    "Vitamins": OrderedDict(),
    "Minerals": OrderedDict(),
    "Sterols": OrderedDict(),
    "Other": OrderedDict(),
}

food_nutrient_dictionary_new["Calorie Information"]["Energy_KCAL"] = (208, OrderedDict())
#First Level
food_nutrient_dictionary_new["Carbohydrates"]["Carbohydrate, by difference"] = (205, OrderedDict())
#Second Level
food_nutrient_dictionary_new["Carbohydrates"]["Fiber"] = (291, OrderedDict())
food_nutrient_dictionary_new["Carbohydrates"]["Starch"] = (209, OrderedDict())
food_nutrient_dictionary_new["Carbohydrates"]["Sugars"] = (269, OrderedDict())
#Third Level
food_nutrient_dictionary_new["Carbohydrates"]["Sugars"][1]["Fructose"] = 212
food_nutrient_dictionary_new["Carbohydrates"]["Sugars"][1]["Galactose"] = 287
food_nutrient_dictionary_new["Carbohydrates"]["Sugars"][1]["Sucrose"] = 210
food_nutrient_dictionary_new["Carbohydrates"]["Sugars"][1]["Glucose(dextrose)"] = 211
food_nutrient_dictionary_new["Carbohydrates"]["Sugars"][1]["Lactose"] = 213
food_nutrient_dictionary_new["Carbohydrates"]["Sugars"][1]["Maltose"] = 214

#Level 1
# food_nutrient_dictionary["Fats & Fatty Acids"]["Total lipid (fat)"] = 204
# #Level 2
# food_nutrient_dictionary["Fats & Fatty Acids"]["Saturated"] = 606
# food_nutrient_dictionary["Fats & Fatty Acids"]["Monounsaturated"] = 645
# food_nutrient_dictionary["Fats & Fatty Acids"]["Polyunsaturated"] = 646


# food_nutrient_dictionary["Fats & Fatty Acids"]["Trans"] = 605
# food_nutrient_dictionary["Fats & Fatty Acids"]["Trans-Monoenoic"] = 693 
# food_nutrient_dictionary["Fats & Fatty Acids"]["Trans-Polyenoic"] = 695 #index 58
# #Level 2
# #Polyunsaturated Omega 3/DHA, EPA's
# food_nutrient_dictionary["Fats & Fatty Acids"]["22:6 n-3 docosahexaenoic (DHA)  cervonic"] = 621
# food_nutrient_dictionary["Fats & Fatty Acids"]["20:5 n-3 eicosapentaenoic (EPA)  timnodonic"] = 629
# #Polyunsaturated Omega-3/ALA
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 n-3 cis,cis,cis (ALA)  linolenic alpha-linolenic"] = 851
# #Level 2 Polyunsaturated Omega-6

# food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 n-6 cis,cis (LA)  linoleic"] = 675
# food_nutrient_dictionary["Fats & Fatty Acids"]["20:4 n-6 eicosatetraenoic (AA)  arachidonic"] = 855
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 n-6 cis,cis,cis (GLA)  gamma-linolenic"] = 685
# #Level 2
# #Monounsaturated Fats Omega-9:
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:1 undifferentiated octadecenoic  oleic"] = 617
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:1 cis  oleic"] = 674
# food_nutrient_dictionary["Fats & Fatty Acids"]["20:1 eicosenoic  gadoleic"] = 628
# food_nutrient_dictionary["Fats & Fatty Acids"]["22:1 undifferentiated docosenoic"] = 630
# food_nutrient_dictionary["Fats & Fatty Acids"]["22:1 cis  erucic"] = 676
# food_nutrient_dictionary["Fats & Fatty Acids"]["24:1 cis cis-tetracosenoic  nervonic"] = 671 #index 31


# #Level 3 More Polyunsaturated Omega 3's:

# food_nutrient_dictionary["Fats & Fatty Acids"]["20:3 n-3 eicosatrienoic acid (ETE)"] = 852
# food_nutrient_dictionary["Fats & Fatty Acids"]["22:5 n-3 docosapentaenoic (DPA)  clupanodonic"] = 631




# #Level 3 Polyunsaturated Other Omega-6


# food_nutrient_dictionary["Fats & Fatty Acids"]["20:2 n-6 cis,cis eicosadienoic"] = 672
# food_nutrient_dictionary["Fats & Fatty Acids"]["20:3 n-6 (DGLA) dihomo-gamma-linolenic acid"] = 853
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 undifferentiated octadecadienoic"] = 618
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 trans not further defined"] = 665
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 i (mixed isomers)"] = 666
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 trans,trans"] = 669
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 congugated linoleic acid(CLAs)"] = 670
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 trans (other isomers)"] = 856
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 i trans (mixed isomers)"] = 866






# #Level 3
# #Monounsaturated Fats Omega-9 Other:
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:1 trans"] = 663
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:1-11t(18:1t n-7)"] = 859
# food_nutrient_dictionary["Fats & Fatty Acids"]["22:1 trans"] = 664


# #Saturated Fats
# #Level 4
# food_nutrient_dictionary["Fats & Fatty Acids"]["4:0 butanoic  butyric"] = 607
# food_nutrient_dictionary["Fats & Fatty Acids"]["6:0 hexanoic  caproic "] = 608
# food_nutrient_dictionary["Fats & Fatty Acids"]["8:0 octanoic  caprylic"] = 609
# food_nutrient_dictionary["Fats & Fatty Acids"]["10:0 decanoic  capric"] =  610
# food_nutrient_dictionary["Fats & Fatty Acids"]["12:0 dodecanoic  lauric"] = 611
# food_nutrient_dictionary["Fats & Fatty Acids"]["13:0 tridecanoic"] = 696
# food_nutrient_dictionary["Fats & Fatty Acids"]["14:0 tetradecanoic  myristic"] = 612
# food_nutrient_dictionary["Fats & Fatty Acids"]["15:0 pentadecanoic"] = 652
# food_nutrient_dictionary["Fats & Fatty Acids"]["16:0 hexadecanoic  palmitic"] = 613
# food_nutrient_dictionary["Fats & Fatty Acids"]["17:0 heptadecanoic  margaric"] = 653
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:0 octadecanoic  stearic"] = 614
# food_nutrient_dictionary["Fats & Fatty Acids"]["20:0 eicosanoic  arachidic"] = 615
# food_nutrient_dictionary["Fats & Fatty Acids"]["22:0 docosanoic  behenic"] = 624
# food_nutrient_dictionary["Fats & Fatty Acids"]["24:0 tetracosanoic  lignoceric"] = 654 #index 15



# # Level 4 Monounsaturated fats
# food_nutrient_dictionary["Fats & Fatty Acids"]["14:1 tetradecenoic  myristoleic"] = 625
# food_nutrient_dictionary["Fats & Fatty Acids"]["15:1 pentadecenoic"] = 697
# food_nutrient_dictionary["Fats & Fatty Acids"]["16:1 undifferentiated hexadecenoic palmitoleic"] = 626
# food_nutrient_dictionary["Fats & Fatty Acids"]["16:1 cis  palmitoleic"] = 673
# food_nutrient_dictionary["Fats & Fatty Acids"]["16:1 trans"] = 662
# food_nutrient_dictionary["Fats & Fatty Acids"]["17:1 heptadecenoic"] = 687



# #Level 4 More Polyunsaturated fats
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 undifferentiated octadecatrienoic"] = 619
# food_nutrient_dictionary["Fats & Fatty Acids"]["18:4 octadecatetraenoic  parinaric"] = 627
# food_nutrient_dictionary["Fats & Fatty Acids"]["20:3 undifferentiated eicosadienoic"] = 689
# food_nutrient_dictionary["Fats & Fatty Acids"]["20:4 undifferentiated arachidonic"] = 620
# food_nutrient_dictionary["Fats & Fatty Acids"]["21:5"] = 857


# food_nutrient_dictionary["Fats & Fatty Acids"]["22:4"] = 858




# #add another 2 lines for Omega-3 totals: linolenic(18:3), EPA (20:5), DHA(22:6))
# #and omega-6: linoleic(18:2), arachidonic(20:4).
#Level 1
food_nutrient_dictionary_new["Protein & Amino Acids"]["Protein"] = (203, OrderedDict())
#food_nutrient_dictionary["Protein & Amino Acids"]["Adjusted Protein"] = 257
# 9 essential aminio acids
#Level 2
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"] = (None, OrderedDict())
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Histidine"] = 512
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Isoleucine"] = 503
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Leucine"] = 504
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Lysine"] = 505
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Methionine"] = 506
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Phenylalanine"] = 508
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Threonine"] = 502
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Tryptophan"] = 501
food_nutrient_dictionary_new["Protein & Amino Acids"]["Essential"][1]["Valine"] = 510

#Conditional Amino Acids are only esssential in times of illness and stress:
#is there one for glutamine,ornithine?
food_nutrient_dictionary_new["Protein & Amino Acids"]["Conditional"] = (None, OrderedDict())
food_nutrient_dictionary_new["Protein & Amino Acids"]["Conditional"][1]["Arginine"] = 511
food_nutrient_dictionary_new["Protein & Amino Acids"]["Conditional"][1]["Cystine"] = 507
#where is glutamine?
food_nutrient_dictionary_new["Protein & Amino Acids"]["Conditional"][1]["Glycine"] = 516
food_nutrient_dictionary_new["Protein & Amino Acids"]["Conditional"][1]["Hydroxyproline"] = 521
food_nutrient_dictionary_new["Protein & Amino Acids"]["Conditional"][1]["Proline"] = 517

food_nutrient_dictionary_new["Protein & Amino Acids"]["Conditional"][1]["Tyrosine"] = 509


# Nonessential amino acids but should be consumed:
#are there listings for asparagine?
#Level 3
food_nutrient_dictionary_new["Protein & Amino Acids"]["Nonessential"] = (None, OrderedDict())
food_nutrient_dictionary_new["Protein & Amino Acids"]["Nonessential"][1]["Alanine"] = 513
food_nutrient_dictionary_new["Protein & Amino Acids"]["Nonessential"][1]["Aspartic acid"] = 514
#where is asparagine?
food_nutrient_dictionary_new["Protein & Amino Acids"]["Nonessential"][1]["Glutamic acid"] = 515
food_nutrient_dictionary_new["Protein & Amino Acids"]["Nonessential"][1]["Serine"] = 518





     

#Level 1
food_nutrient_dictionary_new["Vitamins"]["A, RAE"] = (320, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["A, RAE"][1]["Vitamin A, IU"] = 318
food_nutrient_dictionary_new["Vitamins"]["A, RAE"][1]["Retinol"] = 319
food_nutrient_dictionary_new["Vitamins"]["A, RAE"][1]["Carotene, beta"] = 321
food_nutrient_dictionary_new["Vitamins"]["A, RAE"][1]["Carotene, alpha"] = 322
food_nutrient_dictionary_new["Vitamins"]["A, RAE"][1]["Cryptoxanthin, beta"] = 334
#Level 2 Other carotenoids
food_nutrient_dictionary_new["Vitamins"]["Carotenoids"] = (None, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["Carotenoids"][1]["Lycopene"] = 337
food_nutrient_dictionary_new["Vitamins"]["Carotenoids"][1]["Lutein + Zeaxanthin"] = 338

food_nutrient_dictionary_new["Vitamins"]["B1 (Thiamin)"] = (404, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["B2 (Riboflavin)"] = (405, OrderedDict())
#mg Niacin equivalents = mg niacin + (mg tryptophan / 60).
food_nutrient_dictionary_new["Vitamins"]["B3 (Niacin)"] = (406, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["B5 (Pantothenic Acid)"] = (410, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["B6 (Pyridoxine)"] = (415, OrderedDict())

#food_nutrient_dictionary_new["Vitamins"]

food_nutrient_dictionary_new["Vitamins"]["B9 Folate Total"] = (417, OrderedDict())
#food_nutrient_dictionary_new["Vitamins"]["Folate"] = (None, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["B9 Folate Total"][1]["Folate, DFE"] = 435
food_nutrient_dictionary_new["Vitamins"]["B9 Folate Total"][1]["Folate, food"] = 432

food_nutrient_dictionary_new["Vitamins"]["B9 Folate Total"][1]["Folic acid"] = 431

food_nutrient_dictionary_new["Vitamins"]["B12 (Cobalamin)"] = (None, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["B12 (Cobalamin)"][1]["B12 (Cobalamin)"] = 418
food_nutrient_dictionary_new["Vitamins"]["B12 (Cobalamin)"][1]["B12 (Cobalamin), added"] = 578
food_nutrient_dictionary_new["Vitamins"]["C, (ascorbic acid)"] = (401, OrderedDict())
#Level 1
food_nutrient_dictionary_new["Vitamins"]["D (D2 + D3)"] = (None, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["D (D2 + D3)"][1]["D (D2 + D3)"] = 328
food_nutrient_dictionary_new["Vitamins"]["D (D2 + D3)"][1]["D"] = 324
food_nutrient_dictionary_new["Vitamins"]["D (D2 + D3)"][1]["Vitamin D3(cholecalciferol)"] = 326


food_nutrient_dictionary_new["Vitamins"]["D (D2 + D3)"][1]["D2 (Ergocalciforol)"] = 325


food_nutrient_dictionary_new["Vitamins"]["Vitamin E"] = (None, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["Alpha-Tocopherol"] = (None, OrderedDict())


food_nutrient_dictionary_new["Vitamins"]["Alpha-Tocopherol"][1]["E (Alpha-Tocopherol)"] = 323
food_nutrient_dictionary_new["Vitamins"]["Alpha-Tocopherol"][1]["E, added"] = 573


food_nutrient_dictionary_new["Vitamins"]["Alpha-Tocopherol"][1]["Tocopherol, beta"] = 341
food_nutrient_dictionary_new["Vitamins"]["Alpha-Tocopherol"][1]["Tocopherol, gamma"] = 342
food_nutrient_dictionary_new["Vitamins"]["Alpha-Tocopherol"][1]["Tocopherol, delta"] = 343

food_nutrient_dictionary_new["Vitamins"]["E Tocotrienol"] = (None, OrderedDict())

food_nutrient_dictionary_new["Vitamins"]["E Tocotrienol"][1]["E Tocotrienol, alpha"] = 344
food_nutrient_dictionary_new["Vitamins"]["E Tocotrienol"][1]["E Tocotrienol, beta"] = 345
food_nutrient_dictionary_new["Vitamins"]["E Tocotrienol"][1]["E Tocotrienol, gamma"] = 346
food_nutrient_dictionary_new["Vitamins"]["E Tocotrienol"][1]["E Tocotrienol, delta"] = 347



food_nutrient_dictionary_new["Vitamins"]["Choline"] = (421, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["Betaine"] = (454, OrderedDict())

# food_nutrient_dictionary_new["Vitamins"]["Folate"] = (None, OrderedDict())
# food_nutrient_dictionary_new["Vitamins"]["Folate, DFE"] = (435, OrderedDict())
# food_nutrient_dictionary_new["Vitamins"][1]["Folate, food"] = 432

# food_nutrient_dictionary_new["Vitamins"][1]["Folic acid"] = 431

#1 DFE = 1 ug food folate = 0.6 ug folic acid from fortified food or .5 ug supplement on empty stomach
food_nutrient_dictionary_new["Vitamins"]["Vitamin K"] = (None, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["Vitamin K (Phylloquinone)"] = (430, OrderedDict())
food_nutrient_dictionary_new["Vitamins"]["Vitamin K (Phylloquinone)"][1]["Vitamin K Dihydrophylloquinone"] = 429
food_nutrient_dictionary_new["Vitamins"]["Vitamin K (Phylloquinone)"][1]["Vitamin K Menaquinone-4"] = 428

#In plant foods, where individual carotenoids are not reported, 1 RAE = IU /20
#In animal products, where individual caratenoids are not reported, 1 RAE = IU / 3.33
#Level 1
# 1 IU retinol = 0.3 mcg RAE
# 1 IU beta-carotene from dietary supplements = 0.15 mcg RAE
# 1 IU beta-carotene from food = 0.05 mcg RAE
# 1 IU alpha-carotene or beta-cryptoxanthin = 0.025 mcg RAE


#1 RAE of Vitamin A = 1 mcg retinol, 12 mcg B-carotene, 24 mcg a carotene or 24 umcgB-cryptoxanthin
#Level 2
# food_nutrient_dictionary["Vitamins"]["Vitamin A, IU"] = 318
# food_nutrient_dictionary["Vitamins"]["Retinol"] = 319
# food_nutrient_dictionary["Vitamins"]["Carotene, beta"] = 321
# food_nutrient_dictionary["Vitamins"]["Carotene, alpha"] = 322
# food_nutrient_dictionary["Vitamins"]["Cryptoxanthin, beta"] = 334
# #Level 2 Other carotenoids
# food_nutrient_dictionary["Vitamins"]["Lycopene"] = 337
# food_nutrient_dictionary["Vitamins"]["Lutein + Zeaxanthin"] = 338

# #Level 1

# #1 mcg Vitamin D =  Vitamin D1 + Vitamin D3
# food_nutrient_dictionary["Vitamins"]["Vitamin D"] = 324
# #1 IU Vitamin D = (Vitamin D2+ Vitamin D3) x 40


# #Level 2
# food_nutrient_dictionary["Vitamins"]["Vitamin D2(ergocalciforol)"] = 325
# food_nutrient_dictionary["Vitamins"]["Vitamin D3(cholecalciferol)"] = 326



# #Level 1



# #Level 2
# food_nutrient_dictionary["Vitamins"]["Tocopherol, beta"] = 341
# food_nutrient_dictionary["Vitamins"]["Tocopherol, gamma"] = 342
# food_nutrient_dictionary["Vitamins"]["Tocopherol, delta"] = 343

# food_nutrient_dictionary["Vitamins"]["Tocotrienol, alpha"] = 344
# food_nutrient_dictionary["Vitamins"]["Tocotrienol, beta"] = 345
# food_nutrient_dictionary["Vitamins"]["Tocotrienol, gamma"] = 346
# food_nutrient_dictionary["Vitamins"]["Tocotrienol, delta"] = 347

# #Level 1

# #Level 1
# food_nutrient_dictionary["Vitamins"]["Dihydrophylloquinone"] = 429
# food_nutrient_dictionary["Vitamins"]["Menaquinone-4"] = 428
# # Level 1

# food_nutrient_dictionary["Vitamins"]["Folate, DFE"] = 435
# food_nutrient_dictionary["Vitamins"]["Folate, food"] = 432

# #1 DFE = 1 ug food folate = 0.6 ug folic acid from fortified food or .5 ug supplement on empty stomach
# food_nutrient_dictionary["Vitamins"]["Folic acid"] = 431


# #Vitamin B-12 = 418 + 578


food_nutrient_dictionary_new["Minerals"]["Calcium"] = (301, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Iron"] = (303, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Magnesium"] = (304, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Phosphorus"] = (305, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Potassium"] = (306, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Sodium"] = (307, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Zinc"] = (309, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Copper"] = (312, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Manganese"] = (315, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Selenium"] = (317, OrderedDict())
food_nutrient_dictionary_new["Minerals"]["Flouride"] = (313, OrderedDict())

#Level 1
food_nutrient_dictionary_new["Sterols"]["Cholesterol"] = (601, OrderedDict())
food_nutrient_dictionary_new["Sterols"]["Phytosterols"] = (636, OrderedDict())
#Level 2
food_nutrient_dictionary_new["Sterols"]["Phytosterols"][1]["Stigmasterol"] = 638
food_nutrient_dictionary_new["Sterols"]["Phytosterols"][1]["Campesterol"] = 639
food_nutrient_dictionary_new["Sterols"]["Phytosterols"][1]["Beta-sitosterol"] = 641
#Level 1
food_nutrient_dictionary_new["Other"]["Water"] = (255, OrderedDict())
food_nutrient_dictionary_new["Other"]["Water"][1]["Alcohol, ethyl"] = 221
food_nutrient_dictionary_new["Other"]["Water"][1]["Caffeine"] = 262
food_nutrient_dictionary_new["Other"]["Water"][1]["Theobromine"] = 263
food_nutrient_dictionary_new["Other"]["Water"][1]["Ash"] = 207


# food_nutrient_dictionary_new = {
#     "Fats & Fatty Acids": OrderedDict(),
# }

food_nutrient_dictionary_new["Fats & Fatty Acids"]["Total lipid (fat)"] = (204, OrderedDict())
#Level 2
#Create a nested Ordered Dictionary within the first Ordered Dictionary of Saturated Fats.
#We do so by having it be the second argument to the key Saturated.
#To reach the first Saturated fat is actually the second in the list of Saturated,
#the first or 0 index being the 606.
#The ndb no of the satuated fats is the first item of the tuple.
#The subitems of the saturated fats in the OrderedDict is the second part of the tuple.
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"] = (606, OrderedDict())
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["4:0 butanoic  butyric"] = 607
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["6:0 hexanoic  caproic "] = 608
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["8:0 octanoic  caprylic"] = 609
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["10:0 decanoic  capric"] =  610
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["12:0 dodecanoic  lauric"] = 611
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["13:0 tridecanoic"] = 696
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["14:0 tetradecanoic  myristic"] = 612
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["15:0 pentadecanoic"] = 652
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["16:0 hexadecanoic  palmitic"] = 613
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["17:0 heptadecanoic  margaric"] = 653
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["18:0 octadecanoic  stearic"] = 614
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["20:0 eicosanoic  arachidic"] = 615
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["22:0 docosanoic  behenic"] = 624
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Saturated"][1]["24:0 tetracosanoic  lignoceric"] = 654

food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"] = (645, OrderedDict())
#Omega-9
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["18:1 undifferentiated octadecenoic  oleic"] = 617
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["18:1 cis  oleic"] = 674
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["20:1 eicosenoic  gadoleic"] = 628
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["22:1 undifferentiated docosenoic"] = 630
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["22:1 cis  erucic"] = 676
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["24:1 cis cis-tetracosenoic  nervonic"] = 671
#Other Monounsaturated Fats
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["14:1 tetradecenoic  myristoleic"] = 625
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["15:1 pentadecenoic"] = 697
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["16:1 undifferentiated hexadecenoic palmitoleic"] = 626
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["16:1 cis  palmitoleic"] = 673
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["16:1 trans"] = 662
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["17:1 heptadecenoic"] = 687

#Other Omega-9's
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["18:1 trans"] = 663
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["18:1-11t(18:1t n-7)"] = 859
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Monounsaturated"][1]["22:1 trans"] = 664


food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"] = (646, OrderedDict())
#Omega-3's
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["22:6 n-3 docosahexaenoic (DHA)  cervonic"] = 621
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["20:5 n-3 eicosapentaenoic (EPA)  timnodonic"] = 629
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:3 n-3 cis,cis,cis (ALA)  linolenic alpha-linolenic"] = 851
#Other Omega-3's
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["20:3 n-3 eicosatrienoic acid (ETE)"] = 852
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["22:5 n-3 docosapentaenoic (DPA)  clupanodonic"] = 631

food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:3 n-3 cis,cis,cis (ALA)  linolenic alpha-linolenic"] = 851
#Omega-6's
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:2 n-6 cis,cis (LA)  linoleic"] = 675
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["20:4 n-6 eicosatetraenoic (AA)  arachidonic"] = 855
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:3 n-6 cis,cis,cis (GLA)  gamma-linolenic"] = 685
#Other Omega-6
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["20:2 n-6 cis,cis eicosadienoic"] = 672
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["20:3 n-6 (DGLA) dihomo-gamma-linolenic acid"] = 853
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:2 undifferentiated octadecadienoic"] = 618
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:2 trans not further defined"] = 665
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:2 i (mixed isomers)"] = 666
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:2 trans,trans"] = 669
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:2 congugated linoleic acid(CLAs)"] = 670
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:3 trans (other isomers)"] = 856
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:3 i trans (mixed isomers)"] = 866
#Other Polyunsaturated fats
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:3 undifferentiated octadecatrienoic"] = 619
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["18:4 octadecatetraenoic  parinaric"] = 627
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["20:3 undifferentiated eicosadienoic"] = 689
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["20:4 undifferentiated arachidonic"] = 620
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["21:5"] = 857
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Polyunsaturated"][1]["22:4"] = 858


food_nutrient_dictionary_new["Fats & Fatty Acids"]["Trans"] = (605, OrderedDict())
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Trans"][1]["Trans-Monoenoic"] = 693
food_nutrient_dictionary_new["Fats & Fatty Acids"]["Trans"][1]["Trans-Polyenoic"] = 695





food_groups_dictionary = OrderedDict()
food_groups_dictionary["American Indian/Alaska Native Foods"] = 3500
food_groups_dictionary["Baby Foods"] = 300
food_groups_dictionary["Baked Products"] = 1800
food_groups_dictionary["Beef Products"] = 1300
food_groups_dictionary["Beverages"] = 1400
food_groups_dictionary["Breakfast Cereals"] = 800 
food_groups_dictionary["Cereal Grains and Pasta"] = 2000
food_groups_dictionary["Dairy and Egg Products"] = 100
food_groups_dictionary["Fast Foods"] = 2100
food_groups_dictionary["Fats and Oils"] = 400
food_groups_dictionary["Finfish and Shellfish Products"] = 1500
food_groups_dictionary["Fruit and Fruit Juices"] = 900
food_groups_dictionary["Lamb, Veal, and Game Products"] = 1700
food_groups_dictionary["Legumes and Legume Products"] = 1600
food_groups_dictionary["Meals, Entrees, and Side Dishes"] = 2200
food_groups_dictionary["Nut and Seed Products"] = 1200
food_groups_dictionary["Pork Products"] = 1000
food_groups_dictionary["Poultry Products"] = 0500
food_groups_dictionary["Restaurant Foods"] = 3600
food_groups_dictionary["Sausages and Luncheon Meats"] = 700
food_groups_dictionary["Snacks"] = 2500
food_groups_dictionary["Soups, Sauces, and Gravies"] = 600
food_groups_dictionary["Spices and Herbs"] = 200
food_groups_dictionary["Sweets"] = 1900
food_groups_dictionary["Vegetables and Vegetable Products"] = 1100
