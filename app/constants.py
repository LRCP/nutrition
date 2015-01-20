from collections import OrderedDict
#refer to page 9 of the USDA database
food_nutrient_dictionary = {
    "Calorie Information": OrderedDict(),
    "Carbohydrates": OrderedDict(),
    "Fats & Fatty Acids": OrderedDict(),
    "Protein & Amino Acids": OrderedDict(),
    "Vitamins": OrderedDict(),
    "Minerals": OrderedDict(),
    "Sterols": OrderedDict(),
    "Other": OrderedDict(),
}

food_nutrient_dictionary["Calorie Information"]["Energy_KCAL"] = 208
food_nutrient_dictionary["Carbohydrates"]["Carbohydrate, by difference"] = 205
food_nutrient_dictionary["Carbohydrates"]["Fiber, total dietary"] = 291
food_nutrient_dictionary["Carbohydrates"]["Starch"] = 209
food_nutrient_dictionary["Carbohydrates"]["Sugars, total"] = 269
food_nutrient_dictionary["Carbohydrates"]["Sucrose"] = 210
food_nutrient_dictionary["Carbohydrates"]["Glucose(dextrose)"] = 211
food_nutrient_dictionary["Carbohydrates"]["Fructose"] = 212
food_nutrient_dictionary["Carbohydrates"]["Lactose"] = 213
food_nutrient_dictionary["Carbohydrates"]["Maltose"] = 214
food_nutrient_dictionary["Carbohydrates"]["Galactose"] = 287

food_nutrient_dictionary["Fats & Fatty Acids"]["Total lipid (fat)"] = 204
food_nutrient_dictionary["Fats & Fatty Acids"]["Fatty acids, total saturated"] = 606
food_nutrient_dictionary["Fats & Fatty Acids"]["4:0 butanoic  butyric"] = 607
food_nutrient_dictionary["Fats & Fatty Acids"]["6:0 hexanoic  caproic "] = 608
food_nutrient_dictionary["Fats & Fatty Acids"]["8:0 octanoic  caprylic"] = 609
food_nutrient_dictionary["Fats & Fatty Acids"]["10:0 decanoic  capric"] =  610
food_nutrient_dictionary["Fats & Fatty Acids"]["12:0 dodecanoic  lauric"] = 611
food_nutrient_dictionary["Fats & Fatty Acids"]["13:0 tridecanoic"] = 696
food_nutrient_dictionary["Fats & Fatty Acids"]["14:0 tetradecanoic  myristic"] = 612
food_nutrient_dictionary["Fats & Fatty Acids"]["15:0 pentadecanoic"] = 652
food_nutrient_dictionary["Fats & Fatty Acids"]["16:0 hexadecanoic  palmitic"] = 613
food_nutrient_dictionary["Fats & Fatty Acids"]["17:0 heptadecanoic  margaric"] = 653
food_nutrient_dictionary["Fats & Fatty Acids"]["18:0 octadecanoic  stearic"] = 614
food_nutrient_dictionary["Fats & Fatty Acids"]["20:0 eicosanoic  arachidic"] = 615
food_nutrient_dictionary["Fats & Fatty Acids"]["22:0 docosanoic  behenic"] = 624
food_nutrient_dictionary["Fats & Fatty Acids"]["24:0 tetracosanoic  lignoceric"] = 654 #index 15

food_nutrient_dictionary["Fats & Fatty Acids"]["Fatty acids, total monounsaturated"] = 645
food_nutrient_dictionary["Fats & Fatty Acids"]["14:1 tetradecenoic  myristoleic"] = 625
food_nutrient_dictionary["Fats & Fatty Acids"]["15:1 pentadecenoic"] = 697
food_nutrient_dictionary["Fats & Fatty Acids"]["16:1 undifferentiated hexadecenoic"] = 626
food_nutrient_dictionary["Fats & Fatty Acids"]["16:1 cis  palmitoleic"] = 673
food_nutrient_dictionary["Fats & Fatty Acids"]["16:1 trans"] = 662
food_nutrient_dictionary["Fats & Fatty Acids"]["17:1 heptadecenoic"] = 687
food_nutrient_dictionary["Fats & Fatty Acids"]["18:1 undifferentiated octadecenoic  oleic"] = 617
food_nutrient_dictionary["Fats & Fatty Acids"]["18:1 cis  oleic"] = 674
food_nutrient_dictionary["Fats & Fatty Acids"]["18:1 trans"] = 663
food_nutrient_dictionary["Fats & Fatty Acids"]["18:1-11t(18:1t n-7)"] = 859
food_nutrient_dictionary["Fats & Fatty Acids"]["20:1 eicosenoic  gadoleic"] = 628
food_nutrient_dictionary["Fats & Fatty Acids"]["22:1 undifferentiated docosenoic"] = 630
food_nutrient_dictionary["Fats & Fatty Acids"]["22:1 cis  erucic"] = 676
food_nutrient_dictionary["Fats & Fatty Acids"]["22:1 trans"] = 664
food_nutrient_dictionary["Fats & Fatty Acids"]["24:1 cis cis-tetracosenoic  nervonic"] = 671 #index 31

food_nutrient_dictionary["Fats & Fatty Acids"]["Fatty acids, total polyunsaturated"] = 646
food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 undifferentiated octadecadienoic"] = 618
food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 trans not further defined"] = 665
food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 i (mixed isomers)"] = 666
food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 n-6 cis,cis  linoleic"] = 675
food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 trans,trans"] = 669
food_nutrient_dictionary["Fats & Fatty Acids"]["18:2 congugated linoleic acid(CLAs)"] = 670
food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 undifferentiated octadecatrienoic"] = 619
food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 n-3 cis,cis,cis (ALA)  linolenic alpha-linolenic"] = 851
food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 n-6 cis,cis,cis (GLA)  gamma-linolenic"] = 685
food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 trans (other isomers)"] = 856
food_nutrient_dictionary["Fats & Fatty Acids"]["18:3 i trans (mixed isomers)"] = 866
food_nutrient_dictionary["Fats & Fatty Acids"]["18:4 octadecatetraenoic  parinaric"] = 627
food_nutrient_dictionary["Fats & Fatty Acids"]["20:2 n-6 cis,cis eicosadienoic"] = 672
food_nutrient_dictionary["Fats & Fatty Acids"]["20:3 undifferentiated eicosadienoic"] = 689
food_nutrient_dictionary["Fats & Fatty Acids"]["20:3 n-3 eicosatrienoic acid (ETE)"] = 852
food_nutrient_dictionary["Fats & Fatty Acids"]["20:3 n-6 (DGLA) dihomo-gamma-linolenic acid"] = 853
food_nutrient_dictionary["Fats & Fatty Acids"]["20:4 undifferentiated arachidonic"] = 620
food_nutrient_dictionary["Fats & Fatty Acids"]["20:4 n-6 eicosatetraenoic (AA)  arachidonic"] = 855
food_nutrient_dictionary["Fats & Fatty Acids"]["20:5 n-3 eicosapentaenoic (EPA)  timnodonic"] = 629
food_nutrient_dictionary["Fats & Fatty Acids"]["21:5"] = 857
food_nutrient_dictionary["Fats & Fatty Acids"]["22:4"] = 858
food_nutrient_dictionary["Fats & Fatty Acids"]["22:5 n-3 docosapentaenoic (DPA)  clupanodonic"] = 631
food_nutrient_dictionary["Fats & Fatty Acids"]["22:6 n-3 docosahexaenoic (DHA)  cervonic"] = 621

food_nutrient_dictionary["Fats & Fatty Acids"]["Fatty acids, total trans"] = 605

food_nutrient_dictionary["Fats & Fatty Acids"]["Fatty acids, total trans-monoenoic"] = 693 

food_nutrient_dictionary["Fats & Fatty Acids"]["Fatty acids, total trans-polyenoic"] = 695 #index 58
#add another 2 lines for Omega-3 totals: linolenic(18:3), EPA (20:5), DHA(22:6))
#and omega-6: linoleic(18:2), arachidonic(20:4).
#linoleic acids are found in high concentrations in the oils of 
#safflower, sunflower, corn, soybean, peanut oil. Canola oil is 29% linoleic.
#and 12-16 carbon atoms: lauric acid, myristic acid and palmitic have the
#greatest effect on increasing LDL cholesterol levels. Foudn in animal products
#and tropical oils, including palm palm kernel and coconut.
food_nutrient_dictionary["Protein & Amino Acids"]["Protein"] = 203
food_nutrient_dictionary["Protein & Amino Acids"]["Adjusted Protein"] = 257
food_nutrient_dictionary["Protein & Amino Acids"]["Tryptophan"] = 501
food_nutrient_dictionary["Protein & Amino Acids"]["Threonine"] = 502
food_nutrient_dictionary["Protein & Amino Acids"]["Isoleucine"] = 503
food_nutrient_dictionary["Protein & Amino Acids"]["Leucine"] = 504
food_nutrient_dictionary["Protein & Amino Acids"]["Lysine"] = 505
food_nutrient_dictionary["Protein & Amino Acids"]["Methionine"] = 506
food_nutrient_dictionary["Protein & Amino Acids"]["Cystine"] = 597
food_nutrient_dictionary["Protein & Amino Acids"]["Phenylalanine"] = 508
food_nutrient_dictionary["Protein & Amino Acids"]["Tyrosine"] = 509
food_nutrient_dictionary["Protein & Amino Acids"]["Valine"] = 510
food_nutrient_dictionary["Protein & Amino Acids"]["Arginine"] = 511
food_nutrient_dictionary["Protein & Amino Acids"]["Histidine"] = 512
food_nutrient_dictionary["Protein & Amino Acids"]["Alanine"] = 513
food_nutrient_dictionary["Protein & Amino Acids"]["Aspartic acid"] = 514
food_nutrient_dictionary["Protein & Amino Acids"]["Glutamic acid"] = 515
food_nutrient_dictionary["Protein & Amino Acids"]["Glycine"] = 516
food_nutrient_dictionary["Protein & Amino Acids"]["Proline"] = 517
food_nutrient_dictionary["Protein & Amino Acids"]["Serine"] = 518
food_nutrient_dictionary["Protein & Amino Acids"]["Hydroxyproline"] = 521

food_nutrient_dictionary["Vitamins"]["Vitamin A, IU"] = 318
food_nutrient_dictionary["Vitamins"]["Vitamin A, RAE"] = 320
food_nutrient_dictionary["Vitamins"]["Retinol"] = 319
food_nutrient_dictionary["Vitamins"]["Carotene, beta"] = 321
food_nutrient_dictionary["Vitamins"]["Carotene, alpha"] = 322
food_nutrient_dictionary["Vitamins"]["Cryptoxanthin, beta"] = 334
food_nutrient_dictionary["Vitamins"]["Lycopene"] = 337
food_nutrient_dictionary["Vitamins"]["Lutein + Zeaxanthin"] = 338
food_nutrient_dictionary["Vitamins"]["Vitamin C, total ascorbic acid"] = 401
food_nutrient_dictionary["Vitamins"]["Vitamin D(D2 + D3)"] = 328
food_nutrient_dictionary["Vitamins"]["Vitamin D2(ergocalciforol)"] = 325
food_nutrient_dictionary["Vitamins"]["Vitamin D3(cholecalciferol)"] = 326
food_nutrient_dictionary["Vitamins"]["Vitamin D"] = 324
food_nutrient_dictionary["Vitamins"]["Vitamin E(alpha-tocopherol)"] = 323

food_nutrient_dictionary["Vitamins"]["Vitamin E, added"] = 573
food_nutrient_dictionary["Vitamins"]["Tocopherol, beta"] = 341
food_nutrient_dictionary["Vitamins"]["Tocopherol, gamma"] = 342
food_nutrient_dictionary["Vitamins"]["Tocopherol, delta"] = 343
food_nutrient_dictionary["Vitamins"]["Tocotrienol, alpha"] = 344
food_nutrient_dictionary["Vitamins"]["Tocotrienol, beta"] = 345
food_nutrient_dictionary["Vitamins"]["Tocotrienol, gamma"] = 346
food_nutrient_dictionary["Vitamins"]["Tocotrienol, delta"] = 347
food_nutrient_dictionary["Vitamins"]["Vitamin K (phylloquinone)"] = 430
food_nutrient_dictionary["Vitamins"]["Dihydrophylloquinone"] = 429
food_nutrient_dictionary["Vitamins"]["Menaquinone-4"] = 428
food_nutrient_dictionary["Vitamins"]["Vitamin B1(Thiamin)"] = 404
food_nutrient_dictionary["Vitamins"]["Vitamin B2(Riboflavin)"] = 405
food_nutrient_dictionary["Vitamins"]["Vitamin B3(Niacin)"] = 406
food_nutrient_dictionary["Vitamins"]["Vitamin B5(Pantothenic Acid)"] = 410 
food_nutrient_dictionary["Vitamins"]["Vitamin B-6(Pyridoxine)"] = 415
food_nutrient_dictionary["Vitamins"]["Folate, total"] = 417
food_nutrient_dictionary["Vitamins"]["Folic acid"] = 431
food_nutrient_dictionary["Vitamins"]["Folate, food"] = 432
food_nutrient_dictionary["Vitamins"]["Folate, DFE"] = 435
food_nutrient_dictionary["Vitamins"]["Vitamin B-12(Cobalamin)"] = 418
food_nutrient_dictionary["Vitamins"]["Vitamin B-12(Cobalamin), added"] = 578
food_nutrient_dictionary["Vitamins"]["Choline, total"] = 421
food_nutrient_dictionary["Vitamins"]["Betaine"] = 435

food_nutrient_dictionary["Minerals"]["Calcium, Ca"] = 301
food_nutrient_dictionary["Minerals"]["Iron, Fe"] = 303
food_nutrient_dictionary["Minerals"]["Magnesium, Mg"] = 304
food_nutrient_dictionary["Minerals"]["Phosphorus, P"] = 305
food_nutrient_dictionary["Minerals"]["Potassium, K"] = 306
food_nutrient_dictionary["Minerals"]["Sodium, Na"] = 307
food_nutrient_dictionary["Minerals"]["Zinc, Zn"] = 309
food_nutrient_dictionary["Minerals"]["Copper, Cu"] = 312
food_nutrient_dictionary["Minerals"]["Manganese, Mn"] = 315
food_nutrient_dictionary["Minerals"]["Selenium, Se"] = 317
food_nutrient_dictionary["Minerals"]["Flouride, F"] = 313

food_nutrient_dictionary["Sterols"]["Cholesterol"] = 601
food_nutrient_dictionary["Sterols"]["Phytosterols"] = 636
food_nutrient_dictionary["Sterols"]["Stigmasterol"] = 638
food_nutrient_dictionary["Sterols"]["Campesterol"] = 639
food_nutrient_dictionary["Sterols"]["Beta-sitosterol"] = 641

food_nutrient_dictionary["Other"]["Water"] = 255
food_nutrient_dictionary["Other"]["Alcohol, ethyl"] = 221
food_nutrient_dictionary["Other"]["Caffeine"] = 262
food_nutrient_dictionary["Other"]["Theobromine"] = 263
food_nutrient_dictionary["Other"]["Ash"] = 207

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
