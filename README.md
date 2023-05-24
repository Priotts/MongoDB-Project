
## MongoDB Project
Djongo-Project is a Django project using the Djongo MongoDB.

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

## Project features
- The platform provides an endpoint to manage user registration and access.
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/342f4529-9e49-474a-81f1-599d6d421a6b)

- It automatically assigns each registered user between 1 and 10 bitcoins.
![code](https://github.com/Priotts/MongoDB-Project/assets/94853311/29f5193d-27e3-4b6c-a29f-2cd828afbcbf)

- Each user can post one or more orders to sell or buy a certain amount of bitcoin at a certain price.
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/f5ec779c-3bb2-4c5e-afca-264b815d5397)

- At the time of publication, if the order's buy price is equal to or higher than any other user's sell price, it registers the transaction and marks both orders as executed.
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/429ea54b-1f98-46d3-874f-906f3199a73b)

- Provide an endpoint to obtain all active buy and sell orders.
![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/ec32aae3-75ee-4b82-8a4a-470d378895e3)

- Also provide an endpoint to calculate the total profit or loss from each user's transactions.
- you can check your profit/loss in the profile section  ![image](https://github.com/Priotts/MongoDB-Project/assets/94853311/0ad2e185-b268-4f0f-b0a2-21c716e5bd31)
