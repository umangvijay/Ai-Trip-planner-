"""
Festival Data - Seasonal and Country-wise recommendations
Simple database for the trip planner prototype
"""

SEASONAL_FESTIVALS = {
    "spring": {
        "march": [
            {"name": "Holi Festival", "country": "India", "description": "Festival of Colors", "budget_range": "budget-friendly"},
            {"name": "Cherry Blossom Festival", "country": "Japan", "description": "Beautiful pink sakura blooms", "budget_range": "moderate"},
            {"name": "St. Patrick's Day", "country": "Ireland", "description": "Irish cultural celebration", "budget_range": "moderate"},
            {"name": "Las Fallas", "country": "Spain", "description": "Fire festival in Valencia", "budget_range": "moderate"}
        ],
        "april": [
            {"name": "Songkran", "country": "Thailand", "description": "Water Festival", "budget_range": "budget-friendly"},
            {"name": "Tulip Festival", "country": "Netherlands", "description": "Colorful tulip displays", "budget_range": "moderate"},
            {"name": "Easter Celebrations", "country": "Greece", "description": "Orthodox Easter traditions", "budget_range": "moderate"},
            {"name": "Queen's Birthday", "country": "UK", "description": "Royal celebrations in London", "budget_range": "expensive"}
        ],
        "may": [
            {"name": "Cinco de Mayo", "country": "Mexico", "description": "Mexican celebration", "budget_range": "budget-friendly"},
            {"name": "Chelsea Flower Show", "country": "UK", "description": "Premier gardening event in London", "budget_range": "expensive"},
            {"name": "Cannes Film Festival", "country": "France", "description": "International film festival", "budget_range": "expensive"},
            {"name": "Eurovision Song Contest", "country": "Europe", "description": "Annual music competition", "budget_range": "expensive"}
        ]
    },
    "summer": {
        "june": [
            {"name": "Edinburgh Festival", "country": "Scotland", "description": "Arts and culture festival", "budget_range": "expensive"},
            {"name": "Midsummer", "country": "Sweden", "description": "Traditional Swedish celebration", "budget_range": "moderate"},
            {"name": "Wimbledon", "country": "UK", "description": "Tennis championships in London", "budget_range": "expensive"},
            {"name": "White Nights", "country": "Russia", "description": "Cultural festival in St. Petersburg", "budget_range": "moderate"}
        ],
        "july": [
            {"name": "Gion Matsuri", "country": "Japan", "description": "Traditional Japanese festival", "budget_range": "expensive"},
            {"name": "Running of Bulls", "country": "Spain", "description": "Pamplona festival", "budget_range": "moderate"},
            {"name": "Bastille Day", "country": "France", "description": "French national celebration", "budget_range": "moderate"},
            {"name": "Notting Hill Carnival Preparation", "country": "UK", "description": "Caribbean culture in London", "budget_range": "moderate"}
        ],
        "august": [
            {"name": "Edinburgh Fringe", "country": "Scotland", "description": "World's largest arts festival", "budget_range": "expensive"},
            {"name": "Notting Hill Carnival", "country": "UK", "description": "Caribbean street festival in London", "budget_range": "moderate"},
            {"name": "La Tomatina", "country": "Spain", "description": "Tomato throwing festival", "budget_range": "budget-friendly"},
            {"name": "Burning Man", "country": "USA", "description": "Art and music festival in Nevada", "budget_range": "expensive"}
        ]
    },
    "autumn": {
        "september": [
            {"name": "Oktoberfest", "country": "Germany", "description": "Beer festival in Munich", "budget_range": "moderate"},
            {"name": "Mid-Autumn Festival", "country": "China", "description": "Moon cake festival", "budget_range": "budget-friendly"},
            {"name": "London Fashion Week", "country": "UK", "description": "Fashion industry showcase", "budget_range": "expensive"},
            {"name": "Harvest Festival", "country": "Italy", "description": "Wine and food celebrations", "budget_range": "moderate"}
        ],
        "october": [
            {"name": "Diwali", "country": "India", "description": "Festival of Lights", "budget_range": "budget-friendly"},
            {"name": "Day of the Dead", "country": "Mexico", "description": "Colorful Mexican tradition", "budget_range": "budget-friendly"},
            {"name": "Halloween", "country": "Ireland", "description": "Traditional Celtic celebration", "budget_range": "budget-friendly"},
            {"name": "Lord Mayor's Show", "country": "UK", "description": "Historic London parade", "budget_range": "budget-friendly"}
        ],
        "november": [
            {"name": "Loy Krathong", "country": "Thailand", "description": "Floating lantern festival", "budget_range": "budget-friendly"},
            {"name": "Guy Fawkes Night", "country": "UK", "description": "Bonfire night celebrations", "budget_range": "budget-friendly"},
            {"name": "Diwali Celebrations", "country": "UK", "description": "Festival of Lights in London", "budget_range": "budget-friendly"}
        ]
    },
    "winter": {
        "december": [
            {"name": "Christmas Markets", "country": "Germany", "description": "Traditional German markets", "budget_range": "moderate"},
            {"name": "New Year's Eve", "country": "Australia", "description": "Sydney Harbor fireworks", "budget_range": "expensive"},
            {"name": "London Christmas Markets", "country": "UK", "description": "Festive markets across London", "budget_range": "moderate"},
            {"name": "Winter Solstice", "country": "UK", "description": "Stonehenge celebrations", "budget_range": "budget-friendly"}
        ],
        "january": [
            {"name": "Chinese New Year", "country": "Singapore", "description": "Lunar New Year celebrations", "budget_range": "moderate"},
            {"name": "London New Year Parade", "country": "UK", "description": "Street parade through central London", "budget_range": "budget-friendly"},
            {"name": "Burns Night", "country": "Scotland", "description": "Scottish cultural celebration", "budget_range": "moderate"}
        ],
        "february": [
            {"name": "Carnival", "country": "Brazil", "description": "Rio de Janeiro carnival", "budget_range": "expensive"},
            {"name": "Lantern Festival", "country": "Taiwan", "description": "Sky lantern festival", "budget_range": "moderate"},
            {"name": "Valentine's Day", "country": "UK", "description": "Romantic celebrations in London", "budget_range": "moderate"},
            {"name": "Venice Carnival", "country": "Italy", "description": "Masked carnival in Venice", "budget_range": "expensive"}
        ]
    }
}

COUNTRY_SPECIALTIES = {
    "India": ["cultural festivals", "spiritual experiences", "budget-friendly"],
    "Japan": ["traditional culture", "seasonal beauty", "unique experiences"],
    "Germany": ["oktoberfest", "christmas markets", "cultural events"],
    "Thailand": ["water festivals", "floating lanterns", "tropical experiences"],
    "Brazil": ["carnival", "vibrant culture", "beach festivals"],
    "Mexico": ["colorful traditions", "day of dead", "cultural celebrations"],
    "UK": ["royal events", "historic traditions", "premier cultural events"],
    "France": ["art festivals", "culinary experiences", "cultural heritage"],
    "Spain": ["vibrant festivals", "historical celebrations", "passionate culture"],
    "Italy": ["art and culture", "culinary festivals", "historical events"],
    "Ireland": ["celtic traditions", "cultural celebrations", "friendly atmosphere"],
    "Scotland": ["highland culture", "arts festivals", "historic celebrations"],
    "Netherlands": ["flower festivals", "cultural events", "unique experiences"],
    "Greece": ["ancient traditions", "religious festivals", "mediterranean culture"],
    "Sweden": ["nordic traditions", "midsummer celebrations", "natural beauty"],
    "Russia": ["cultural festivals", "classical arts", "winter celebrations"],
    "USA": ["diverse festivals", "music and arts", "modern celebrations"],
    "Australia": ["outdoor celebrations", "new year events", "beach culture"],
    "Singapore": ["multicultural festivals", "modern celebrations", "asian fusion"],
    "Taiwan": ["traditional festivals", "lantern celebrations", "cultural heritage"],
    "China": ["traditional festivals", "cultural heritage", "seasonal celebrations"],
    "Europe": ["diverse cultures", "international events", "historic celebrations"]
}

# City to Country Mapping for intelligent matching
CITY_COUNTRY_MAP = {
    "london": "UK",
    "paris": "France", 
    "madrid": "Spain",
    "barcelona": "Spain",
    "rome": "Italy",
    "venice": "Italy",
    "florence": "Italy",
    "dublin": "Ireland",
    "edinburgh": "Scotland",
    "glasgow": "Scotland",
    "amsterdam": "Netherlands",
    "athens": "Greece",
    "stockholm": "Sweden",
    "moscow": "Russia",
    "st petersburg": "Russia",
    "new york": "USA",
    "los angeles": "USA",
    "las vegas": "USA",
    "sydney": "Australia",
    "melbourne": "Australia",
    "tokyo": "Japan",
    "osaka": "Japan",
    "kyoto": "Japan",
    "mumbai": "India",
    "delhi": "India",
    "bangalore": "India",
    "bangkok": "Thailand",
    "phuket": "Thailand",
    "berlin": "Germany",
    "munich": "Germany",
    "rio": "Brazil",
    "sao paulo": "Brazil",
    "cancun": "Mexico",
    "mexico city": "Mexico"
}

def normalize_country_input(user_input):
    """
    Convert user input to standardized country name
    Handles cities, alternative names, and common variations
    """
    if not user_input:
        return None
    
    user_input = user_input.lower().strip()
    
    # Direct city mapping
    if user_input in CITY_COUNTRY_MAP:
        return CITY_COUNTRY_MAP[user_input]
    
    # Common country name variations
    country_variations = {
        "england": "UK",
        "britain": "UK", 
        "great britain": "UK",
        "united kingdom": "UK",
        "uk": "UK",
        "usa": "USA",
        "united states": "USA",
        "america": "USA",
        "us": "USA",
        "holland": "Netherlands",
        "russia": "Russia",
        "russian federation": "Russia"
    }
    
    if user_input in country_variations:
        return country_variations[user_input]
    
    # Check if it matches any existing country (case insensitive)
    for country in COUNTRY_SPECIALTIES.keys():
        if user_input == country.lower():
            return country
    
    # If no match found, return the original input capitalized
    return user_input.title()

def get_festivals_by_season(season):
    """Get all festivals for a specific season"""
    return SEASONAL_FESTIVALS.get(season.lower(), {})

def get_festivals_by_month(month):
    """Get festivals for a specific month"""
    for season, months in SEASONAL_FESTIVALS.items():
        if month.lower() in months:
            return months[month.lower()]
    return []

def get_festivals_by_country(country):
    """Get all festivals for a specific country"""
    festivals = []
    for season_data in SEASONAL_FESTIVALS.values():
        for month_data in season_data.values():
            for festival in month_data:
                if festival["country"].lower() == country.lower():
                    festivals.append(festival)
    return festivals

def get_budget_friendly_festivals():
    """Get all budget-friendly festivals"""
    budget_festivals = []
    for season_data in SEASONAL_FESTIVALS.values():
        for month_data in season_data.values():
            for festival in month_data:
                if festival["budget_range"] == "budget-friendly":
                    budget_festivals.append(festival)
    return budget_festivals
