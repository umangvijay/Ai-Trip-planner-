# 🌍 AI Trip Planner Prototype

A personalized trip planner prototype with AI-powered recommendations and festival integration.

## ✨ Features (Prototype)

### ✅ Currently Available
- **🎪 Festival Recommendations**: Seasonal and country-wise festival suggestions
- **💰 Budget-Based Planning**: Trip suggestions based on your budget category
- **🌸 Seasonal Highlights**: Weather tips and travel advice for each month
- **🎭 Festival Explorer**: Browse festivals by month or country
- **📱 Interactive Interface**: Simple console-based user interface

### 🚀 Coming Soon
- **🤖 Advanced AI Recommendations**: Machine learning-powered personalization
- **✈️ Real-time Booking**: One-click booking for flights, hotels, activities
- **🌤️ Weather Integration**: Real-time weather-based suggestions
- **📊 Price Optimization**: AI-powered price predictions and deals
- **👥 Social Features**: Travel buddy matching and social recommendations

## 🚀 Quick Start

1. **Navigate to the project folder**:
   ```bash
   cd "ML PROJECTS/Ai trip planner"
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Follow the interactive menu** to:
   - Plan a personalized trip
   - Explore world festivals
   - Get seasonal travel highlights
   - Preview coming soon features

## 💡 How It Works

### Festival Database
- **Seasonal Festivals**: Organized by spring, summer, autumn, winter
- **Country Coverage**: India, Japan, Germany, Thailand, Brazil, Mexico, and more
- **Budget Categories**: Budget-friendly, moderate, and luxury options

### Trip Planning Logic
- Collects user preferences (month, budget, duration, country)
- Matches festivals to user criteria
- Provides cost estimates based on budget category
- Offers seasonal travel tips and weather advice

## 🎯 Example Usage

```
🌍 WELCOME TO AI TRIP PLANNER PROTOTYPE 🌍
Personalized travel recommendations with festival insights!

🎯 MAIN MENU
1. 🎪 Plan Personalized Trip (with Festivals)
2. 🎭 Explore World Festivals
3. 🌸 Seasonal Travel Highlights
4. 🚀 Coming Soon Features
5. ℹ️  About This Prototype
6. 🚪 Exit

Enter your choice: 1

🎪 PERSONALIZED TRIP PLANNER
What month are you planning to travel? March
What's your budget category?
   1. Budget (Under $1,500)
   2. Moderate ($1,500 - $3,500)
   3. Luxury ($3,500+)
Choose (1-3): 1

✨ Here are your top recommendations:
1. Experience Holi Festival in India
   📍 Type: Festival
   📝 Description: Festival of Colors
   🌍 Country: India
   💰 Budget Range: budget-friendly
   💵 Estimated Cost: $672
```

## 🛠️ Technical Details

### File Structure
```
Ai trip planner/
├── main.py              # Main application interface
├── trip_planner.py      # Core trip planning logic
├── festival_data.py     # Festival database and queries
├── requirements.txt     # Dependencies (minimal for prototype)
└── README.md           # This file
```

### Architecture
- **Modular Design**: Separated data, logic, and interface
- **Extensible**: Easy to add new festivals and features
- **Lightweight**: No external dependencies for prototype
- **User-Friendly**: Interactive console interface

## 📊 Festival Data Coverage

### Seasons Covered
- **Spring**: March-May festivals (Holi, Cherry Blossom, Songkran, etc.)
- **Summer**: June-August festivals (Edinburgh, Gion Matsuri, etc.)
- **Autumn**: September-November festivals (Oktoberfest, Diwali, etc.)
- **Winter**: December-February festivals (Christmas Markets, Carnival, etc.)

### Countries Featured
- India (Holi, Diwali)
- Japan (Cherry Blossom, Gion Matsuri)
- Germany (Oktoberfest, Christmas Markets)
- Thailand (Songkran, Loy Krathong)
- Brazil (Carnival)
- Mexico (Cinco de Mayo, Day of the Dead)
- And more...

## 🔮 Future Development

This prototype demonstrates the foundation for a comprehensive AI trip planning platform. Future versions will include:

- **Machine Learning Integration**: Personalized recommendations based on user behavior
- **Real-time API Integration**: Live prices, weather, and availability
- **Advanced Booking System**: Complete trip booking in one platform
- **Web/Mobile Interface**: Modern UI/UX design
- **Social Features**: User reviews, travel buddy matching
- **Extended Database**: Thousands of festivals and destinations worldwide

## 🤝 Contributing

This is a prototype showcasing core functionality. For the full development version:
- Add more festivals to `festival_data.py`
- Enhance AI logic in `trip_planner.py`
- Improve user interface in `main.py`
- Add external API integrations

## 📝 Notes

- **Prototype Status**: This is a working prototype demonstrating core features
- **No External Dependencies**: Runs with standard Python installation
- **Educational Purpose**: Showcases AI trip planning concepts
- **Expandable**: Designed for easy feature additions

---

**Created**: 2025 | **Version**: Prototype v1.0 | **Status**: Working Demo

🌍 Happy Planning! ✈️
