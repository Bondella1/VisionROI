# VisionROI

# About Azure AD
Once student subscription expires, the azure service will be disabled unless you are in pay as you go subscription. You won't be charged unles you upgrade to a paid plan.
Azure AD authentication for localhost is free as long as you’re within the free tier limits.
However, once the offer expires, the Azure AD service will stop working, and your app’s authentication will break unless you upgrade.

The MSAL library supports React 18, not 19. Hence we uninstalled React 19 and installed React 18 to install MSAL library.

# How to run
 - Make sure node is installed (use node -v in terminal to see)
 - Make sure you are in frontend directory VisionROI\frontend\vision_roi
 - Then open terminal -> enter 'npm run dev' without quotes
 - use Crtl and click on localhost link to open
 - use Crtl+C to terminate session

# To login
- To login with Microsoft, your user and pass needs to be registered in Azure -> Microsoft Entra ID -> VisionROI -> Users
- Once you login, you should be able to view Project Data and have access to visuals and AI features.

# To improve in future
- Implement multifacet sign in -> work and school emails.
- Add hierarchies, where based on your role, you are restricted or have access on viewing certain info.

# Using Plotly-dash to display Data Visualizations
- The code for this is found in app.py 

# Tasks for Tahia
- In Project Data, add styling to Logout button 
- In Home or App component -> Get started button should direct to login page (done)
- If have time, remove home link in Project Data - least important
