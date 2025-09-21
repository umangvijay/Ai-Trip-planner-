"""
AI Trip Planner - Main Application
Personalized Trip Planner Prototype

Features included in this prototype:
✅ Festival recommendations (seasonal/country-wise)
✅ Budget-based trip suggestions  
✅ Seasonal travel highlights

Coming Soon:
🔄 Real-time price optimization
🔄 Advanced AI recommendations
🔄 Seamless booking integration
🔄 Weather-based suggestions
🔄 Crowd density analysis
"""

import sys
from datetime import datetime
from trip_planner import TripPlanner, get_ai_insights, real_time_booking
from festival_data import get_festivals_by_month, get_festivals_by_country

class TripPlannerApp:
    def __init__(self):
        self.planner = TripPlanner()
        self.user_preferences = {}
        
    def run(self):
        """Main application loop"""
        self.show_welcome()
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                self.plan_personalized_trip()
            elif choice == '2':
                self.explore_festivals()
            elif choice == '3':
                self.seasonal_highlights()
            elif choice == '4':
                self.show_available_countries()
            elif choice == '5':
                self.show_coming_soon_features()
            elif choice == '6':
                self.show_about()
            elif choice == '7':
                print("\nThank you for using AI Trip Planner! Safe travels! 🌍✈️")
                break
            else:
                print("\n❌ Invalid choice. Please try again.")
                
            input("\nPress Enter to continue...")
    
    def show_welcome(self):
        """Display welcome message"""
        print("=" * 60)
        print("🌍 WELCOME TO AI TRIP PLANNER PROTOTYPE 🌍")
        print("=" * 60)
        print("Personalized travel recommendations with festival insights!")
        print("This is a working prototype showcasing core features.")
        print()
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "=" * 50)
        print("🎯 MAIN MENU")
        print("=" * 50)
        print("1. 🎪 Plan Personalized Trip (with Festivals)")
        print("2. 🎭 Explore World Festivals")  
        print("3. 🌸 Seasonal Travel Highlights")
        print("4. 🌍 Available Countries & Destinations")
        print("5. 🚀 Coming Soon Features")
        print("6. ℹ️  About This Prototype")
        print("7. 🚪 Exit")
        print("=" * 50)
    
    def plan_personalized_trip(self):
        """Plan a personalized trip with festival recommendations"""
        print("\n🎪 PERSONALIZED TRIP PLANNER")
        print("-" * 40)
        
        # Collect user preferences
        preferences = self.collect_preferences()
        
        print("\n🤖 Generating personalized recommendations...")
        print("(Full AI integration coming soon!)")
        
        # Get recommendations
        recommendations = self.planner.get_personalized_recommendations(preferences)
        
        if recommendations:
            print(f"\n✨ Here are your top {len(recommendations)} recommendations:")
            print("=" * 60)
            
            for i, rec in enumerate(recommendations, 1):
                print(f"\n{i}. {rec['title']}")
                print(f"   📍 Type: {rec['type'].title()}")
                print(f"   📝 Description: {rec['description']}")
                
                if rec['type'] == 'notice':
                    if 'suggestion' in rec:
                        print(f"   💡 Suggestion: {rec['suggestion']}")
                else:
                    if 'country' in rec:
                        print(f"   🌍 Country: {rec['country']}")
                    elif 'countries' in rec:
                        print(f"   🌍 Countries: {', '.join(rec['countries'])}")
                        
                    print(f"   💰 Budget Range: {rec['budget_range']}")
                    if rec['estimated_cost'] > 0:
                        print(f"   💵 Estimated Cost: ${rec['estimated_cost']}")
                print("-" * 50)
        else:
            print("\n❌ No recommendations found for your preferences.")
            print("Try adjusting your budget or travel dates.")
    
    def collect_preferences(self):
        """Collect user travel preferences"""
        preferences = {}
        
        print("\n📝 Let's plan your perfect trip!")
        print("(Answer the questions below - press Enter to skip any)")
        
        # Travel month
        month = input("\n🗓️  What month are you planning to travel? (e.g., March): ").strip()
        if month:
            preferences['travel_month'] = month
        
        # Budget category
        print("\n💰 What's your budget category?")
        print("   1. Budget (Under $1,500)")
        print("   2. Moderate ($1,500 - $3,500)") 
        print("   3. Luxury ($3,500+)")
        
        budget_choice = input("Choose (1-3): ").strip()
        budget_map = {'1': 'budget', '2': 'moderate', '3': 'luxury'}
        if budget_choice in budget_map:
            preferences['budget_category'] = budget_map[budget_choice]
        
        # Duration
        duration = input("\n📅 How many days will you travel? (default: 7): ").strip()
        if duration and duration.isdigit():
            preferences['duration'] = int(duration)
        else:
            preferences['duration'] = 7
        
        # Preferred country (optional)
        print("\n🌍 Any preferred country or city? (optional)")
        print("   Examples: London, Paris, UK, Germany, Japan, Thailand, etc.")
        print("   Type 'list' to see available countries")
        country = input("Enter preference: ").strip()
        
        if country.lower() == 'list':
            self.show_available_countries()
            country = input("\nNow enter your preferred country/city: ").strip()
        
        if country:
            preferences['preferred_country'] = country
        
        return preferences
    
    def explore_festivals(self):
        """Explore festivals by country or month"""
        print("\n🎭 WORLD FESTIVALS EXPLORER")
        print("-" * 40)
        
        print("Explore festivals by:")
        print("1. 🗓️  Month")
        print("2. 🌍 Country")
        
        choice = input("\nChoose (1-2): ").strip()
        
        if choice == '1':
            self.explore_festivals_by_month()
        elif choice == '2':
            self.explore_festivals_by_country()
        else:
            print("❌ Invalid choice.")
    
    def explore_festivals_by_month(self):
        """Show festivals for a specific month"""
        month = input("\n🗓️  Enter month (e.g., March): ").strip()
        
        festivals = get_festivals_by_month(month)
        
        if festivals:
            print(f"\n🎪 Festivals in {month.title()}:")
            print("=" * 50)
            
            for festival in festivals:
                print(f"\n🎭 {festival['name']}")
                print(f"   🌍 Country: {festival['country']}")
                print(f"   📝 Description: {festival['description']}")
                print(f"   💰 Budget: {festival['budget_range']}")
                print("-" * 30)
        else:
            print(f"\n❌ No festivals found for {month}.")
            print("Try: March, April, May, June, July, August, September, October, November, December, January, February")
    
    def explore_festivals_by_country(self):
        """Show festivals for a specific country"""
        country = input("\n🌍 Enter country (e.g., Japan): ").strip()
        
        festivals = get_festivals_by_country(country)
        
        if festivals:
            print(f"\n🎪 Festivals in {country.title()}:")
            print("=" * 50)
            
            for festival in festivals:
                print(f"\n🎭 {festival['name']}")
                print(f"   📝 Description: {festival['description']}")
                print(f"   💰 Budget: {festival['budget_range']}")
                print("-" * 30)
        else:
            print(f"\n❌ No festivals found for {country}.")
            print("Try: India, Japan, Germany, Thailand, Brazil, Mexico, Scotland, etc.")
    
    def seasonal_highlights(self):
        """Show seasonal travel highlights"""
        print("\n🌸 SEASONAL TRAVEL HIGHLIGHTS")
        print("-" * 40)
        
        month = input("🗓️  Enter month for highlights (e.g., April): ").strip()
        
        if not month:
            month = datetime.now().strftime("%B")
            print(f"Using current month: {month}")
        
        highlights = self.planner.get_seasonal_highlights(month)
        
        print(f"\n✨ {month.title()} Travel Highlights:")
        print("=" * 50)
        
        # Show festivals
        if highlights['festivals']:
            print("\n🎪 Featured Festivals:")
            for festival in highlights['festivals'][:3]:  # Show top 3
                print(f"   🎭 {festival['name']} in {festival['country']}")
                print(f"      {festival['description']}")
        else:
            print("\n🎪 No major festivals this month in our database.")
        
        # Weather tips
        print(f"\n🌤️  Weather Tips:")
        print(f"   {highlights['weather_tips']}")
        
        # Travel tips  
        print(f"\n💡 Travel Tips:")
        print(f"   {highlights['travel_tips']}")
    
    def show_available_countries(self):
        """Show all available countries and cities for trip planning"""
        print("\n🌍 AVAILABLE COUNTRIES & DESTINATIONS")
        print("=" * 60)
        
        from festival_data import COUNTRY_SPECIALTIES, CITY_COUNTRY_MAP
        
        print("\n🎪 Countries with Festival Data:")
        print("-" * 40)
        countries_by_type = {}
        for country, specialties in COUNTRY_SPECIALTIES.items():
            budget_types = [s for s in specialties if s in ['budget-friendly', 'moderate', 'expensive']]
            if not budget_types:
                budget_type = 'moderate'  # default
            else:
                budget_type = budget_types[0]
            
            if budget_type not in countries_by_type:
                countries_by_type[budget_type] = []
            countries_by_type[budget_type].append(country)
        
        for budget_type in ['budget-friendly', 'moderate', 'expensive']:
            if budget_type in countries_by_type:
                print(f"\n💰 {budget_type.replace('-', ' ').title()} Options:")
                for country in sorted(countries_by_type[budget_type]):
                    specialties = ', '.join(COUNTRY_SPECIALTIES[country][:2])  # Show first 2 specialties
                    print(f"   🌍 {country}: {specialties}")
        
        print(f"\n🏙️ Major Cities (automatically mapped to countries):")
        print("-" * 40)
        cities_by_country = {}
        for city, country in CITY_COUNTRY_MAP.items():
            if country not in cities_by_country:
                cities_by_country[country] = []
            cities_by_country[country].append(city.title())
        
        for country in sorted(cities_by_country.keys()):
            cities = ', '.join(sorted(cities_by_country[country])[:3])  # Show up to 3 cities
            print(f"   🏙️ {country}: {cities}")
        
        print(f"\n💡 Usage Tips:")
        print("   • You can enter either country names or city names")
        print("   • Examples: 'London' will be mapped to 'UK'")
        print("   • 'Paris' will be mapped to 'France'")
        print("   • Use exact country names for best results")
        print("   • Mix and match with any travel month for personalized results")
    
    def show_coming_soon_features(self):
        """Display upcoming features"""
        print("\n🚀 COMING SOON FEATURES")
        print("=" * 50)
        
        # AI Insights
        ai_insights = get_ai_insights({})
        print(f"\n{ai_insights['message']}")
        print("\nPlanned AI Features:")
        for feature in ai_insights['planned_features']:
            print(f"   🔄 {feature}")
        
        # Booking Integration
        booking_info = real_time_booking({}, {})
        print(f"\n{booking_info['message']}")
        print("\nPlanned Booking Features:")
        for feature in booking_info['planned_features']:
            print(f"   🔄 {feature}")
        
        print(f"\n📊 Additional Features Coming Soon:")
        print("   🔄 Machine Learning trip optimization")
        print("   🔄 Social media integration") 
        print("   🔄 Local insider recommendations")
        print("   🔄 Multi-city route optimization")
        print("   🔄 Travel buddy matching")
        print("   🔄 Real-time currency conversion")
        print("   🔄 Visa requirement checking")
        print("   🔄 Travel insurance suggestions")
    
    def show_about(self):
        """Show information about the prototype"""
        print("\n ℹ️  ABOUT AI TRIP PLANNER PROTOTYPE")
        print("=" * 50)
        print("🎯 Purpose: Demonstrate core AI trip planning features")
        print("🔧 Version: Prototype v1.0")
        print("📅 Created: 2025")
        print()
        print("✅ Current Features:")
        print("   • Festival recommendations (seasonal & country-wise)")
        print("   • Budget-based trip suggestions") 
        print("   • Seasonal travel highlights")
        print("   • Interactive console interface")
        print()
        print("🚀 This prototype showcases the foundation for a full")
        print("   AI-powered trip planning application with real-time")
        print("   booking capabilities and advanced personalization.")
        print()
        print("💡 Future versions will include machine learning,")
        print("   real-time APIs, and seamless booking integration.")

def main():
    """Main entry point"""
    try:
        app = TripPlannerApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Thanks for trying AI Trip Planner!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the application.")

if __name__ == "__main__":
    main()
