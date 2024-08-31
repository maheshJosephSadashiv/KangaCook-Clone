## **Kanga Clone: A Recipe Management Application**
Try it out [here](http://kangacook-client.s3-website-us-west-2.amazonaws.com)
Kanga Clone is a full-stack application designed for seamless recipe management, leveraging AWS services for scalability and ease of deployment.
Technologies Used:

    Backend: Django (hosted on EC2 instances)
    Frontend: React
    Database: MongoDB
    Deployment: AWS Elastic Beanstalk

## **Key Features:**

    Recipe Management Endpoints:
        Add Recipes: Create new recipe entries in the MongoDB database.
        List Recipes: Retrieve and display all available recipes.
        Add to Favorites: Mark recipes as favorites for easy access.
        Get All Favorites: Retrieve all recipes marked as favorites.

## **AWS Implementation:**

    AWS Elastic Beanstalk: Utilized to streamline the deployment process, enabling rapid and automated scaling of the application. Elastic Beanstalk abstracts the complexities of infrastructure management, allowing for easy updates and rollbacks while maintaining high availability.

    Django on EC2 Instances: The Django backend is hosted on EC2 instances, providing a robust and flexible environment. EC2 offers fine-grained control over the server configuration, ensuring the application can handle varying loads efficiently.

    MongoDB Integration: The application connects to MongoDB using an ORM, simplifying database interactions and facilitating data migrations. This integration ensures that data operations are consistent, reliable, and scalable.
![kanga drawio](https://github.com/user-attachments/assets/8b7d8256-2c88-4fde-ba62-f3f345378335)


## **API Documentation**

### **Base URL**
` http://django-dev.eba-wpqi3qdy.us-west-2.elasticbeanstalk.com/`

---

### **1. Get All Recipes**

#### **Endpoint:** 
`[GET] /recipes/list`

#### **Description:** 
Retrieves a list of all available recipes.

#### **Response:**

- **Status Code:** `200 OK`
- **Content-Type:** `application/json`

- **Response Body:**
```json
{
    "recipes": [
        {
            "id": 2,
            "title": "Pasta Carbonara",
            "ingredients": [
                "Spaghetti",
                "eggs",
                "bacon",
                "parmesan cheese"
            ],
            "instructions": [
                "Cook pasta.",
                "Fry bacon.",
                "Mix eggs and cheese.",
                "Combine all ingredients."
            ],
            "image_url": "",
            "cuisine": "Italian",
            "is_favorite": false
        },
        {
            "id": 3,
            "title": "Pasta Carbonara",
            "ingredients": [
                "Spaghetti",
                "eggs",
                "bacon",
                "parmesan cheese"
            ],
            "instructions": [
                "Cook pasta.",
                "Fry bacon.",
                "Mix eggs and cheese.",
                "Combine all ingredients."
            ],
            "image_url": "https://www.sweetteaandthyme.com/wp-content/uploads/2023/11/cheesecake-factory-carbonara-overhead-close-500x375.jpg",
            "cuisine": "Italian",
            "is_favorite": false
        }
    ]
}
```

---

### **2. Add a New Recipe**

#### **Endpoint:**
`[POST] /recipes/add`

#### **Description:**
Adds a new recipe to the database.

#### **Request Body:**

- **Content-Type:** `application/json`

- **Example Payload:**
```json
{
    "title": "Pasta Carbonara",
    "ingredients": [
        "Spaghetti",
        "eggs",
        "bacon",
        "parmesan cheese"
    ],
    "instructions": [
        "Cook pasta.",
        "Fry bacon.",
        "Mix eggs and cheese.",
        "Combine all ingredients."
    ],
    "image_url": "https://example.com/image.jpg",
    "cuisine": "Italian"
}
```

#### **Response:**

- **Status Code:** `201 Created`
- **Content-Type:** `application/json`

- **Response Body:**
```json
{
    "message": "Recipe added successfully",
    "recipe_id": 4
}
```

---

### **3. Add Recipe to Favorites**

#### **Endpoint:**
`[POST] /recipes/favorite/{recipe_id}`

#### **Description:**
Marks a specific recipe as a favorite.

#### **Path Parameters:**
- `recipe_id` (integer): The ID of the recipe to mark as a favorite.

#### **Response:**

- **Status Code:** `200 OK`
- **Content-Type:** `application/json`

- **Response Body:**
```json
{
    "message": "Recipe marked as favorite",
    "recipe_id": 3
}
```

---

### **4. Get All Favorite Recipes**

#### **Endpoint:**
`[GET] /recipes/favorites`

#### **Description:**
Retrieves a list of all favorite recipes.

#### **Response:**

- **Status Code:** `200 OK`
- **Content-Type:** `application/json`

- **Response Body:**
```json
{
    "favorites": [
        {
            "id": 3,
            "title": "Pasta Carbonara",
            "ingredients": [
                "Spaghetti",
                "eggs",
                "bacon",
                "parmesan cheese"
            ],
            "instructions": [
                "Cook pasta.",
                "Fry bacon.",
                "Mix eggs and cheese.",
                "Combine all ingredients."
            ],
            "image_url": "https://www.sweetteaandthyme.com/wp-content/uploads/2023/11/cheesecake-factory-carbonara-overhead-close-500x375.jpg",
            "cuisine": "Italian",
            "is_favorite": true
        }
    ]
}
```
