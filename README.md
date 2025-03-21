# What is VisionROI?
VisionROI is a powerful data visualization tool designed to help businesses and researchers track projects and gain actionable insights for project success. It provides insightful visual representations of data, enabling better decision-making and strategy optimization.

# Target Users
- Business owners
- Managers
- Researchers
- Startups & enterprises

# Key Benefits
- Clear & Intuitive Insights For Project Success
- Efficiency & ROI Optimization: Helps users make data-driven decisions to maximize their return on investment.
  
VisionROI simplifies data analysis, making it accessible to everyone. Start making smarter decisions today!

# Demo Video
[Watch Quick Demo](https://screenapp.io/app/#/shared/7z_X8TFxsr)
Recorded with ScreenApp -> screenapp.io

# About Azure AD
Once student subscription expires, the azure service will be disabled unless you are in pay as you go subscription. 
Azure AD authentication for localhost is free as long as you’re within the free tier limits.
However, once the offer expires, the Azure AD service will stop working, and your app’s authentication will break unless you upgrade.

The MSAL library supports React 18, not 19. Hence, we uninstalled React 19 and installed React 18 to install MSAL library.

# How to run
 - Make sure node is installed (use node -v in terminal to see)
 - Other installations (dotenv, dash, plotly) -> use 'pip install <insert_tech>' without quotes in terminal
 - Install MSAL library
 - Make sure you are in frontend directory VisionROI\frontend\vision_roi
 - Then open terminal -> enter 'npm run dev' without quotes
 - use Crtl and click on localhost link to open
 - use Crtl+C to terminate session
 - It's recommended to run backend at the same time to see info after login -> cd to backend folder and run app.py

 - Note that this needs sensitive keys from Azure to work.

# To login
- To login with Microsoft, your user and pass needs to be registered in Azure -> Microsoft Entra ID -> VisionROI -> Users
- Once you login, you should be able to view Project Data and have access to visuals and AI features.

# To improve in future
- Implement multifacet sign in -> allow work and school emails.
- Add hierarchies, where based on your role, you are restricted or have access on viewing certain info.
