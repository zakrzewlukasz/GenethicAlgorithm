
import random
import boto3

# A simple app to populate a DynamoDB table with location data for the Genetic Algorithm 

dynamodb = boto3.resource('dynamodb')

DELIVERY_STOPS_TABLE = 'ga-blog-stack-DeliveryStops'
table = dynamodb.Table(DELIVERY_STOPS_TABLE)

def write_delivery_stops(stops_set_id, stops):
    item = {
        'StopsSetID': stops_set_id,
        'Locations': stops
    }
    table.put_item(Item=item)

def build_list_of_stops():
    stops = []
    coords_used = set()
    coords_used.add("0+0")  # don't allow a stop at (0,0) since that's the warehouse

    NUM_STOPS = 100
    MIN_X = -15
    MAX_X = 15
    MIN_Y = -15
    MAX_Y = 15

    for _ in range(NUM_STOPS):
        key = ""
        while True:
            x_coord = random.randint(MIN_X, MAX_X)
            y_coord = random.randint(MIN_Y, MAX_Y)
            key = str(x_coord) + "+" + str(y_coord)
            if key not in coords_used:
                break
        coords_used.add(key)

        stop = {'X': x_coord, 'Y': y_coord}
        stops.append(stop)

    return stops

if __name__ == "__main__":
    stops = build_list_of_stops()
    print(stops)
    write_delivery_stops(0, stops)
