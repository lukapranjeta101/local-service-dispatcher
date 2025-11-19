def get_service_list(location, service_type):
    # MOCK DATA for now
    # Later you will pull from Google Places, Yelp, etc.
    return [
        {
            "id": "plumber1",
            "name": "Rapid Rooter Plumbing",
            "rating": 4.8,
            "price_level": "$$",
            "phone": "555-123-4567",
            "address": "123 Main St, Cleveland, OH",
            "availability": "Can arrive in 1-2 hours"
        },
        {
            "id": "plumber2",
            "name": "Mr Fix-It Plumbing",
            "rating": 4.5,
            "price_level": "$$",
            "phone": "555-555-9999",
            "address": "42 Elm St, Cleveland, OH",
            "availability": "Available today"
        }
    ]


def get_service_details(provider_id):
    # MOCK DETAILS
    return {
        "id": provider_id,
        "name": "Rapid Rooter Plumbing",
        "description": "24/7 plumbing repair and drain cleaning",
        "services": [
            "Drain cleaning",
            "Pipe repair",
            "Leak detection"
        ],
        "rating": 4.8,
        "phone": "555-123-4567",
        "address": "123 Main St, Cleveland",
        "availability": "1-2 hours"
    }
