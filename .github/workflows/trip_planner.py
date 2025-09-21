"""
AI Trip Planner - Core Logic
Prototype for personalized trip recommendations with festival integration
"""

import random
from datetime import datetime, timedelta
from festival_data import (
    get_festivals_by_month, 
    get_festivals_by_country, 
    get_budget_friendly_festivals,
    normalize_country_input
)

class TripPlanner:
    def __init__(self):
        self.budget_ranges = {
            "budget": {"min": 500, "max": 1500, "type": "budget-friendly"},
            "moderate": {"min": 1500, "max": 3500, "type": "moderate"}, 
            "luxury": {"min": 3500, "max": 10000, "type": "expensive"}
        }
        
    def get_personalized_recommendations(self, preferences):
        """
        Generate personalized trip recommendations based on user preferences
        This is a prototype - full AI integration coming soon!
        """
        recommendations = []
        
        # Get festival recommendations
        festival_recs = self._get_festival_recommendations(preferences)
        recommendations.extend(festival_recs)
        
        # Add destination recommendations (prototype)
        destination_recs = self._get_destination_recommendations(preferences)
        recommendations.extend(destination_recs)
        
        return recommendations[:3]  # Limit to top 3 for prototype
    
    def _get_festival_recommendations(self, preferences):
        """Get festival recommendations based on preferences"""
        recommendations = []
        
        # Normalize country input if provided
        preferred_country = None
        if preferences.get('preferred_country'):
            preferred_country = normalize_country_input(preferences['preferred_country'])
            print(f"🌍 Searching for festivals in {preferred_country}...")
        
        # Get base festivals list
        all_festivals = []
        if preferences.get('travel_month') and preferred_country:
            # Get festivals for specific month AND country
            month_festivals = get_festivals_by_month(preferences['travel_month'])
            all_festivals = [f for f in month_festivals if f['country'] == preferred_country]
        elif preferences.get('travel_month'):
            all_festivals = get_festivals_by_month(preferences['travel_month'])
        elif preferred_country:
            all_festivals = get_festivals_by_country(preferred_country)
        else:
            all_festivals = get_budget_friendly_festivals()
        
        # Filter by budget type if specified
        budget_type = None
        if preferences.get('budget_category'):
            budget_type = self.budget_ranges[preferences['budget_category']]['type']
            
        filtered_festivals = []
        for festival in all_festivals:
            # Apply budget filter
            if budget_type:
                # Allow budget-friendly for all budget types, and match exact budget types
                if festival['budget_range'] == budget_type or (budget_type in ['moderate', 'expensive'] and festival['budget_range'] == 'budget-friendly'):
                    filtered_festivals.append(festival)
            else:
                filtered_festivals.append(festival)
        
        # If no festivals found for the specific country, provide a message
        if preferred_country and not filtered_festivals:
            # Return a "no festivals found" recommendation
            rec = {
                'type': 'notice',
                'title': f"No festivals found for {preferred_country}",
                'description': f"We don't have festival data for {preferred_country} in our current database. Try exploring our available destinations or check our general recommendations.",
                'country': preferred_country,
                'budget_range': 'N/A',
                'estimated_cost': 0,
                'suggestion': f"Explore general attractions and cultural sites in {preferred_country}"
            }
            recommendations.append(rec)
        
        # Create festival recommendations
        for festival in filtered_festivals[:2]:  # Limit to 2 for prototype
            rec = {
                'type': 'festival',
                'title': f"Experience {festival['name']} in {festival['country']}",
                'description': festival['description'],
                'country': festival['country'],
                'budget_range': festival['budget_range'],
                'estimated_cost': self._estimate_cost(festival['budget_range'], preferences.get('duration', 7))
            }
            recommendations.append(rec)
        
        return recommendations
    
    def _get_destination_recommendations(self, preferences):
        """Get general destination recommendations (prototype)"""
        preferred_country = None
        if preferences.get('preferred_country'):
            preferred_country = normalize_country_input(preferences['preferred_country'])
        
        # All available destinations
        all_destinations = [
            {
                'type': 'destination',
                'title': 'London Cultural Experience',
                'description': 'Explore royal palaces, museums, and historic landmarks in London',
                'countries': ['UK'],
                'country_match': 'UK',
                'budget_range': 'expensive',
                'estimated_cost': self._estimate_cost('expensive', preferences.get('duration', 7))
            },
            {
                'type': 'destination',
                'title': 'UK Heritage Trail',
                'description': 'Discover castles, countryside, and British culture',
                'countries': ['UK'],
                'country_match': 'UK',
                'budget_range': 'moderate',
                'estimated_cost': self._estimate_cost('moderate', preferences.get('duration', 7))
            },
            {
                'type': 'destination',
                'title': 'Paris Art & Romance',
                'description': 'Museums, cafes, and iconic landmarks in the City of Light',
                'countries': ['France'],
                'country_match': 'France',
                'budget_range': 'expensive',
                'estimated_cost': self._estimate_cost('expensive', preferences.get('duration', 7))
            },
            {
                'type': 'destination',
                'title': 'Mediterranean Adventure',
                'description': 'Beaches, history, and culture in Southern Europe',
                'countries': ['Spain', 'Italy', 'Greece'],
                'country_match': 'Spain',
                'budget_range': 'moderate',
                'estimated_cost': self._estimate_cost('moderate', preferences.get('duration', 7))
            },
            {
                'type': 'destination',
                'title': 'Cultural Heritage Tour - Europe',
                'description': 'Explore historical sites and local traditions',
                'countries': ['Italy', 'France', 'Spain'],
                'country_match': None,
                'budget_range': 'moderate',
                'estimated_cost': self._estimate_cost('moderate', preferences.get('duration', 7))
            },
            {
                'type': 'destination', 
                'title': 'Tropical Paradise - Southeast Asia',
                'description': 'Beautiful beaches and exotic culture',
                'countries': ['Thailand', 'Indonesia', 'Philippines'],
                'country_match': 'Thailand',
                'budget_range': 'budget-friendly',
                'estimated_cost': self._estimate_cost('budget-friendly', preferences.get('duration', 7))
            },
            {
                'type': 'destination',
                'title': 'Japanese Cultural Discovery',
                'description': 'Traditional temples, modern cities, and cherry blossoms',
                'countries': ['Japan'],
                'country_match': 'Japan',
                'budget_range': 'expensive',
                'estimated_cost': self._estimate_cost('expensive', preferences.get('duration', 7))
            },
            {
                'type': 'destination',
                'title': 'German Cultural Experience',
                'description': 'Historic cities, castles, and beer culture',
                'countries': ['Germany'],
                'country_match': 'Germany',
                'budget_range': 'moderate',
                'estimated_cost': self._estimate_cost('moderate', preferences.get('duration', 7))
            }
        ]
        
        # Filter by preferred country first
        if preferred_country:
            country_destinations = [d for d in all_destinations if d['country_match'] == preferred_country or preferred_country in d['countries']]
            if country_destinations:
                destinations = country_destinations
            else:
                # If no destinations found for preferred country, return a notice
                return [{
                    'type': 'notice',
                    'title': f"Limited destinations for {preferred_country}",
                    'description': f"We have limited destination packages for {preferred_country}. Consider exploring our festival recommendations or general travel options.",
                    'countries': [preferred_country],
                    'budget_range': 'N/A',
                    'estimated_cost': 0
                }]
        else:
            destinations = all_destinations
        
        # Filter by budget
        budget_type = None
        if preferences.get('budget_category'):
            budget_type = self.budget_ranges[preferences['budget_category']]['type']
            filtered_destinations = []
            for d in destinations:
                if budget_type:
                    # Allow budget-friendly for all budgets, match exact budget types
                    if d['budget_range'] == budget_type or (budget_type in ['moderate', 'expensive'] and d['budget_range'] == 'budget-friendly'):
                        filtered_destinations.append(d)
                else:
                    filtered_destinations.append(d)
            destinations = filtered_destinations
        
        return destinations[:1]  # Return 1 for prototype
    
    def _estimate_cost(self, budget_range, duration_days):
        """Estimate trip cost based on budget range and duration"""
        base_costs = {
            'budget-friendly': 80,
            'moderate': 200,
            'expensive': 500
        }
        
        base_cost = base_costs.get(budget_range, 150)
        total_cost = base_cost * duration_days
        
        # Add some randomness for realism
        variation = random.randint(-20, 20) / 100
        total_cost = int(total_cost * (1 + variation))
        
        return total_cost
    
    def get_seasonal_highlights(self, month):
        """Get seasonal highlights for a specific month"""
        festivals = get_festivals_by_month(month)
        
        highlights = {
            'festivals': festivals,
            'weather_tips': self._get_weather_tips(month),
            'travel_tips': self._get_travel_tips(month)
        }
        
        return highlights
    
    def _get_weather_tips(self, month):
        """Get weather tips for the month (prototype data)"""
        weather_tips = {
            'march': 'Spring weather, pack layers',
            'april': 'Mild temperatures, perfect for sightseeing',
            'may': 'Warm weather begins, light clothing recommended',
            'june': 'Summer begins, hot in many destinations',
            'july': 'Peak summer, very hot in Europe and Asia',
            'august': 'Hot summer continues, monsoon in some regions',
            'september': 'Pleasant weather, great for travel',
            'october': 'Cool temperatures, autumn colors',
            'november': 'Cool weather, fewer crowds',
            'december': 'Winter begins, holiday season',
            'january': 'Cold in northern hemisphere, summer in south',
            'february': 'Still cold in north, good for tropical destinations'
        }
        
        return weather_tips.get(month.lower(), 'Check local weather conditions')
    
    def _get_travel_tips(self, month):
        """Get travel tips for the month"""
        tips = {
            'march': 'Book early for spring festivals',
            'april': 'Cherry blossom season - book accommodations early',
            'may': 'Great weather for outdoor activities',
            'june': 'Peak season begins - expect higher prices',
            'july': 'Peak tourist season - book well in advance',
            'august': 'Very busy season, consider alternative dates',
            'september': 'Shoulder season - good prices and weather',
            'october': 'Excellent time to travel, beautiful autumn',
            'november': 'Low season - great deals available',
            'december': 'Holiday season - book early for festivities',
            'january': 'Low season in most places - good deals',
            'february': 'Still low season - ideal for budget travel'
        }
        
        return tips.get(month.lower(), 'Research local conditions before travel')

# Prototype AI functions (placeholder for advanced AI)
def get_ai_insights(preferences):
    """
    AI-powered insights - Coming Soon!
    Full machine learning integration will include:
    - Real-time price predictions
    - Weather-based recommendations  
    - Crowd density analysis
    - Personalized itinerary optimization
    """
    return {
        'status': 'coming_soon',
        'message': '🤖 Advanced AI insights coming soon!',
        'planned_features': [
            'Real-time price optimization',
            'Weather-based activity suggestions',
            'Crowd density predictions',
            'Personalized itinerary generation'
        ]
    }

def real_time_booking(destination, dates):
    """
    Real-time booking integration - Coming Soon!
    Will include integration with:
    - Flight booking APIs
    - Hotel reservation systems
    - Activity booking platforms  
    - Transport arrangements
    """
    return {
        'status': 'coming_soon',
        'message': '✈️ Seamless booking integration coming soon!',
        'planned_features': [
            'One-click flight booking',
            'Hotel reservations',
            'Activity bookings',
            'Transport arrangements'
        ]
    }
