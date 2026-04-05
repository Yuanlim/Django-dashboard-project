import pycountry
import phonenumbers

for c in pycountry.countries:
    try:
        # Valid region 
        print(c.name, c.alpha_2, phonenumbers.country_code_for_valid_region(c.alpha_2))
        
        
    except:
        # Not valid
        print(f"Skipped: {c.name}, {c.alpha_2}")