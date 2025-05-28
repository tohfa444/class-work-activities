def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city=="Spain":
        return 1000
    elif city=="Germany":
        return 1200
def trip_cost(city,nights,spanding_money):
    return hotel_cost(nights)+plane_ride_cost(city)+spanding_money
print("Total cost of trip is ",trip_cost("Spain",7,2000)) 