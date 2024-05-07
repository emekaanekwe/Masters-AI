# return csv in the order of prop id full address, 
property_string = "prop_id, streetnumber streetname streettype suburb statecode postcode, bedrooms, bathrooms, parking_spaces, latitude, longitude, floor_number, land_area, floor_area, price, property_features"

property_data = {}    
split_property_string = property_string.split(",")
def extract_information(property_string: str) -> dict:
    property_data = property_string

    for entries in split_property_string:
        if entries != "":
            if entries == "prop_id":
                property_data[entries] = ""
            elif entries == "prop_type":
                property_data[entries] = ""
            elif entries == "suburb":
                property_data[entries] = ""
            elif entries == "full_address":
                property_data[entries] = ""
            elif entries == "latitude":
                property_data[entries] = 0.0
            elif entries == "longitude":
                property_data[entries] = 0.0
            elif entries == "property_features":
                property_data[entries] = []
            elif entries == "":
                pass
            else:
                property_data[entries] = None
        else:
            continue        
    return property_data

def add_feature(property_dict: dict, feature: str) -> None:
    property_dict = property_string.values("property_features")
    if feature in property_dict:
        property_dict.append(feature)
    else:
        pass       
    
    
def remove_feature(property_dict: dict, feature: str) -> None:    
    property_dict = property_string.values("property_features")
    if feature in property_dict:
        property_dict.remove(feature)
    else:
        pass
    
    
def main():
    sample_string = "P10001,3 Antrim Place Langwarrin VIC 3910,4,2,2,-38.16655678,145.1838435,,608,257,870000,dishwasher;central heating"
    property_dict = extract_information(sample_string)
    print(f"The first property is at {property_dict['full_address']} and is valued at ${property_dict['price']}")

    sample_string_2 = "P10002,G01/7 Rugby Road Hughesdale VIC 3166,2,1,1,-37.89342337,145.0862616,1,,125,645000,dishwasher;air conditioning;balcony"
    property_dict_2 = extract_information(sample_string_2)

    print(f"The second property is in {property_dict_2['suburb']} and is located on floor {property_dict_2['floor_number']}")

    add_feature(property_dict, 'electric hot water')
    print(f"Property {property_dict['prop_id']} has the following features: {property_dict['property_features']}")

if __name__ == '__main__':
    main()