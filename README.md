# Spotify Custom Playlist Creator
This code provides a way to create a playlist on Spotify using Billboard's top songs for a specific period. It retrieves the top songs from Billboard's website for a given date and uses the Spotify API to create a playlist and add those songs to it.

The Billboard class is responsible for retrieving the top songs from Billboard's website. It uses the requests library to fetch the webpage, parses it using BeautifulSoup, and extracts the song titles. The retrieved song titles are stored in the labels attribute.

The Spotify class handles the interaction with the Spotify API. It takes an instance of the Billboard class as input. The class has methods to obtain an access token from Spotify, create a playlist, and add the songs from Billboard to the playlist. It uses the requests library to make HTTP requests to the Spotify API and the dotenv library to load environment variables containing the Spotify API credentials.

To use the code, you need to have a Spotify developer account and create an application to obtain the client ID and client secret. You also need to set up a redirect URI and obtain a user ID from Spotify. The necessary environment variables are loaded from a file called variables.env using the dotenv library.

1. Install the required dependencies by running the following command:
2. 
    pip install requests beautifulsoup4 python-dotenv
    
2. Create a Spotify developer account and create an application to obtain the client ID and client secret.

3. Set up a redirect URI for your application in the Spotify developer dashboard.

4. Obtain a user ID from Spotify. You can find your user ID by logging in to Spotify's web player, going to your account overview, and clicking on your profile picture. Your user ID will be displayed under your username.

5. Create a file named variables.env in the same directory as the code file (main.py). Add the following lines to the variables.env file, replacing the values with your own:

    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    USER_ID=your_user_id
    
6. Run the main.py file using a Python interpreter:

    python main.py
    
7. Follow the instructions on the console. Enter the date in the format YYYY-MM-DD for the Billboard chart you want to retrieve.

8. The script will retrieve the top songs from Billboard for the specified date and create a playlist on Spotify with those songs. The playlist will be named "Top 100 Hits for [date] period" and will be set to private by default.

# Note: The code provided is a simplified version and may require additional error handling and validation to be production-ready.


