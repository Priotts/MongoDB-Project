
## MongoDB Project
Djongo-Project is a Django project using the Djongo MongoDB.
## Project features
- The platform provides an endpoint to manage user registration and access.

## Installation

- Clone the repository 

```bash
git clone https://github.com/Priotts/MongoDB-project.git
```

- Create a virtual environment and activate it:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

- Install the project dependencies:
```bash
pip install -r requirements.txt
```

- Configure the MongoDB database (you have to create it first) in the settings.py file:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mydatabase',
    }
}
```

- Make database migrations
```bash
py .\manage.py makemigrations
py .\manage.py migrate
```

- Start the development server:
```bash
python manage.py runserver
```

- Access the application from the browser at http://localhost:8000/
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/1a748557-6d48-4f2f-a0ee-f4685409d651)

- It automatically assigns each registered user between 1 and 10 bitcoins.
![code](https://github.com/Priotts/MongoDB-Project/assets/94853311/44886664-e2af-44f7-990d-a7a8476abeba)

- Each user can post one or more orders to sell or buy a certain amount of bitcoin at a certain price.
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/c4c5108a-1e98-48f6-87f3-052071e6f941)

- At the time of publication, if the order's buy price is equal to or higher than any other user's sell price, it registers the transaction and marks both orders as executed.
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/498d15a3-2452-4f64-90d3-6df94f6ea1a1)

- Provide an endpoint to obtain all active buy and sell orders.
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/6055fb8b-6ed0-4f86-8dc7-dc57727ca258)

- Also provide an endpoint to calculate the total profit or loss from each user's transactions.
- you can check your profit/loss in the profile section  ![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/4fd6eab4-79ff-40c1-b7f1-e9dab31db1e4)
