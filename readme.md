This repository contains a Flask application that predicts the gender and age based on the entered name using external APIs.

### Technologies Used:
- **Flask**: Micro web framework for Python.
- **HTML/CSS**: Frontend for user interaction and display.

### Functionality:
1. **Home Page (`index.html`)**:
   - Provides a form to input a name.
   - On submission, it sends a POST request to `/guessGenderAndAge`.

2. **Guess Gender and Age (`guessGenderAndAge` endpoint)**:
   - Receives the name from the form submission.
   - Sends requests to external APIs (`genderize.io` and `agify.io`) to predict gender and age based on the name.
   - Renders a `name.html` template displaying the predicted gender, age, and the entered name.

### How to Run:
1. Install Flask (`pip install Flask`).
2. Run `python app.py` in the terminal.
3. Open `http://localhost:5000` in your web browser.

### Files:
- **`app.py`**: Flask application containing routes and logic.
- **`index.html`**: HTML template for the home page with the input form.
- **`name.html`**: HTML template displaying the predicted data.

### External APIs Used:
- **genderize.io**: Predicts gender based on the name.
- **agify.io**: Predicts age based on the name.

### Additional Notes:
- Ensure internet connectivity as the application depends on external API calls for predictions.
- Debug mode is enabled (`app.run(debug=True)`) for development purposes.

