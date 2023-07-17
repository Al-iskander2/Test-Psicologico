# Psychological Test
#### Video Demo:  <https://youtu.be/PjCA7G7hTuA>
#### Description:
The Psychological Test is a specialized application designed to be implemented in rehabilitation clinics with the goal of evaluating individuals' psychological balance. The test is not intended to provide specific personality specifications; I am using the Rorschach inkblot images with a somewhat different purpose than their original intent. In this case, it is for individuals who have used drugs, aiming not to categorize them within their personality but to understand their pains and difficulties in relating to their reality. The purpose of this test is to use it as a tool in therapy for drug addicts, allowing us to understand the psychological struggles they have faced and, through further analysis, provide assistance.

Project Description
The Psychological Test project aims to provide a platform for users to register their personal information and perform a series of visual tests. By analyzing the user's responses to the images, the application evaluates their psychological balance. In total, the user will see 10 images, and for each image, they must select what they see by pressing one of the four buttons. Then, they should press "Next." When they have finished describing what they see in the 10 images, a result will be displayed. The project utilizes Flask, a Python web framework, to create an intuitive and user-friendly web application. Beyond its implementation in a clinical setting, I am confident that this can have many applications. It can be used for social media or for companies. These types of tests are called projective tests in psychology, and they help determine a person's cultural background. Furthermore, with experience, it can be used to easily classify individuals based on their personality.

Design Challenges
One of the main challenges was selecting the categories that people could see in the images. In the end, I chose four categories, although I am aware that individuals may see very different and almost unique figures in each image. The categories I selected were: Animals, Human Beings, Human Bones, and Body Organs. These categories allow for at least one result to be generated. Initially, I wanted to eliminate the "Next" button, but it was impossible to make the option buttons have two simultaneous events. I wanted them to both save the selected variable and change the image. Since achieving both events was impossible, I decided to add the "Next" button to handle the image change.

At one point, I considered an alternative that would provide more specific data. I thought about using libraries as they were used in previous lessons of the course. With libraries, the buttons and their categories could be replaced, and the user would simply write what they see in a label. Then, the label would compare what was written with the library's contents to determine the category of the object the person saw. However, I discarded this approach as it was too elaborate and time-consuming. I aimed to keep the elements more functional, but it is inevitable that the project will evolve over time.

File Structure
The project follows a well-organized file structure, as detailed below:

app.py: This file is the core of the Flask application, handling routing and application logic.
flask_session/: This folder contains the Flask session files, ensuring secure and persistent user sessions.
helpers.py: This file includes several auxiliary functions used throughout the application to streamline processes.
patients.db: This file is an SQLite database responsible for storing and managing patient data. It includes columns for personal information and the 10 images.
requirements.txt: This file lists all the dependencies required for the project to function correctly.
static/: This folder contains static files such as the favicon, sample images, and the CSS file for styles.
templates/: Here, you will find HTML templates defining the structure of the web interface.
index/: This file contains two labels and buttons for users to enter their information.
test/: This file displays the 10 images, and users select what they see in each of them.
result/: This file presents the texts to be shown based on the response sent by the resultado function in app.py.
history/: The history.html file allows users to review the database of patients who have completed the psychological test. This page provides information about each patient's registered data, such as name, age, and drugs used.
Usage
To run the Psychological Test project locally, follow these instructions:

Ensure that you have Python and Flask installed on your system.
Clone this repository to your local machine using your preferred method.
Open a terminal window and navigate to the project directory.
Install the necessary dependencies by running the following command: pip install -r requirements.txt.
Start the application with the command: python app.py.
Open your preferred web browser and visit http://localhost:5000 to access the psychological test.
Contributions
We appreciate contributions from the community to improve the Psychological Test project. If you wish to contribute, please contact Alejandro at dev.alejandro5@gmail.com to discuss your ideas and possible contributions.

License
The Psychological Test project is distributed under a specified license. Please refer to the attached license file for detailed information.

Contact
If you have any questions or comments about this project, please do not hesitate to contact Alejandro at dev.alejandro5@gmail.com. Your feedback is highly appreciated!




