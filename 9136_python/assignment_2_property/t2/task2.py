# DO NOT DELETE THIS LINE
from haversine import haversine_distance

def process_properties(file_name: str) -> dict:
    raise NotImplementedError

def process_stations(file_name: str) -> dict:
    raise NotImplementedError

def nearest_station(properties: dict, stations: dict, prop_id: str) -> str:
    raise NotImplementedError

def main():
    """
    You need not touch this function, if your 
    code is correct, this function will work as intended 
    """
    # Process the properties
    properties_file = 'sample_properties.csv'
    properties = process_properties(properties_file)

    # Process the train stations
    stations_file = 'train_stations.csv'
    stations = process_stations(stations_file)

    # Check the validity of stations
    sample_prop = 'P10001'
    print(f"The nearest station for property {sample_prop} is {nearest_station(properties, stations, sample_prop)}")
    


if __name__ == '__main__':
    main()
