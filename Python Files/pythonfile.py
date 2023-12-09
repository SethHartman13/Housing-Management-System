import json
import os

def main():
    output_json = dict()
    
    
    while (room_input := input("Room Name? ")) != "":
        
        if room_input not in output_json.keys():
        
            tier_input = 1
            output_json[room_input] = {}
            
            while input(f"Do you want to make a tier for tier {tier_input}? ").lower() in "yes" or tier_input == 1:
                output_json[room_input][f"{tier_input}"] = {}
                
                if (tier_name := input("Tier name? ")) != "":
                    output_json[room_input][str(tier_input)]["TierName"] = tier_name
                    
                else:
                    pass
                
                if (description := input("Description? ")) != "":
                    output_json[room_input][str(tier_input)]["Description"] = description
                    
                else:
                    pass
                
                if (size := input("Size? ")) != "":
                    output_json[room_input][str(tier_input)]["Size"] = size
                    
                else:
                    pass
                
                while_loop = True
                
                while while_loop:
                    if (build_cost := input("Build Cost? ")) != "":
                        try:
                            output_json[room_input][str(tier_input)]["BuildCost"] = round(float(build_cost), 2)
                            while_loop = False
                            
                        except Exception as error:
                            print("Please enter in a float")
                            print(error)
                            
                    else:
                        while_loop = False
                    
                # while_loop = True
                
                # while while_loop:
                #     if (build_time := input("Build Time (in seconds)? ")) != "":
                #         try:
                #             output_json[room_input][str(tier_input)]["BuildTime"] = int(build_time)
                #             while_loop = False
                            
                #         except:
                #             print("Please enter in an integer")
                            
                #     else:
                #         while_loop = False
                        
                while_loop = True
                
                while while_loop:
                    if (upkeep_cost := input("Upkeep Cost? ")) != "":
                        try:
                            output_json[room_input][str(tier_input)]["UpkeepCost"] = round(float(upkeep_cost), 2)
                            while_loop = False
                            
                        except:
                            print("Please enter in a float")
                            
                    else:
                        while_loop = False
                        
                del while_loop
                
                if (requirements := input("Requirements? ")) != "":
                    output_json[room_input][str(tier_input)]["Requirements"] = requirements
                    
                else:
                    pass
                
                if (img_url := input("Image URL? ")) != "":
                    output_json[room_input][str(tier_input)]["URL"] = img_url
                    
                else:
                    pass
                
                if (color_hex := input("Color Hex? ")) != "":
                    output_json[room_input][str(tier_input)]["Color"] = color_hex
                    
                else:
                    pass
                
                if (benefits := input("Benefits? ")) != "":
                    output_json[room_input][str(tier_input)]["Benefits"] = benefits
                    
                else:
                    pass                    
                
                tier_input += 1
                
                print("")                  
                      
        else:
            print("Room already exists")
    
    while True:
        try:
            with open(f"{input('JSON name? ').replace(' ', '_')}.json", "x+") as json_file:
                json.dump(output_json, json_file, indent=4)
                
            break
        
        except Exception as error:
            print(error)
        
    print("JSON Generated")
    print(f"Characters (compact): {len(json.dumps(output_json))}")
    print(f"Characters (expanded): {len(json.dumps(output_json, indent=4))}")
    
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
